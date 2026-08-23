from __future__ import annotations

import asyncio
import logging
from typing import Any

from app.core.clients.proxy import ProxyResponseError
from app.core.resilience.overload import local_overload_error
from app.modules.proxy._service.http_bridge.helpers import (
    _HTTP_BRIDGE_BACKGROUND_CLOSE_TIMEOUT_SECONDS,
    _abort_http_bridge_inflight_creation_by_future_locked,
    _abort_http_bridge_inflight_creation_locked,
    _close_http_bridge_session_bounded,
    _http_bridge_capacity_generation_count,
    _http_bridge_pending_count_nowait,
    _http_bridge_pending_state_is_stale,
    _http_bridge_request_counts_against_queue,
    _log_http_bridge_event,
    _raise_http_bridge_incompatible_admission_handoff,
    _record_http_bridge_unanchored_handoff_recovery,
    http_bridge_activity_snapshot_nowait,
)
from app.modules.proxy._service.http_bridge.protocol import _HTTPBridgeServiceProtocol
from app.modules.proxy._service.observability import _hash_identifier
from app.modules.proxy._service.support import (
    _http_bridge_session_supports_service_tier,
    _HTTPBridgeSession,
    _HTTPBridgeSessionKey,
)
from app.modules.proxy.affinity import _extract_model_class

logger = logging.getLogger("app.modules.proxy.service")
_HTTP_BRIDGE_BACKGROUND_CLEANUP_WARN_THRESHOLD = 100


class _HTTPBridgeActivityMixin:
    _http_bridge_pending_state_is_stale = staticmethod(_http_bridge_pending_state_is_stale)

    def _recover_http_bridge_incompatible_admission_handoff(
        self: Any,
        key: Any,
        existing: Any,
        force_durable_takeover: bool,
        original_request_unanchored: bool,
        request_model: str | None,
        api_key: Any,
        incoming_turn_state: str | None,
        previous_response_id: str | None,
        preferred_account_id: str | None,
        require_preferred_account: bool,
        request_service_tier: str | None,
    ) -> tuple[Any, bool]:
        if original_request_unanchored and existing is not None:
            detached = self._detach_http_bridge_session_locked(key, expected_session=existing)
            if detached is not None:
                force_durable_takeover = True
                _record_http_bridge_unanchored_handoff_recovery(reason="closed_admission_handoff")
                _log_http_bridge_event(
                    "unanchored_handoff_recovery",
                    key,
                    account_id=detached.account.id,
                    model=request_model,
                    detail="outcome=retired_closed_admission_handoff",
                    cache_key_family=key.affinity_kind,
                    model_class=_extract_model_class(request_model) if request_model else None,
                    owner_check_applied=False,
                )
                self._schedule_http_bridge_session_closes([detached], reason="unanchored_handoff_recovery")
            return None, force_durable_takeover

        _raise_http_bridge_incompatible_admission_handoff(
            session=existing,
            key=key,
            api_key=api_key,
            incoming_turn_state=incoming_turn_state,
            previous_response_id=previous_response_id,
            preferred_account_id=preferred_account_id,
            require_preferred_account=require_preferred_account,
            request_service_tier=request_service_tier,
            service_tier_supported=_http_bridge_session_supports_service_tier(
                existing,
                request_model=request_model,
                request_service_tier=request_service_tier,
            ),
        )
        raise AssertionError("incompatible admission handoff must raise")

    async def _close_http_bridge_session_bounded(
        self: Any,
        session: _HTTPBridgeSession,
        *,
        reason: str,
    ) -> None:
        await _close_http_bridge_session_bounded(self, session, reason=reason)

    def _schedule_http_bridge_session_closes(
        self,
        sessions: list[_HTTPBridgeSession],
        *,
        reason: str,
    ) -> None:
        for session in sessions:
            if len(self._background_cleanup_tasks) >= _HTTP_BRIDGE_BACKGROUND_CLEANUP_WARN_THRESHOLD:
                logger.warning(
                    "http_bridge_background_cleanup_backlog action=session_close count=%d threshold=%d reason=%s",
                    len(self._background_cleanup_tasks),
                    _HTTP_BRIDGE_BACKGROUND_CLEANUP_WARN_THRESHOLD,
                    reason,
                )
            self._schedule_cancel_safe_cleanup(
                self._close_http_bridge_session_bounded(session, reason=reason),
                action="http_bridge_session_close",
                request_id=_hash_identifier(session.key.affinity_key),
            )

    async def _drain_http_bridge_background_cleanup_tasks(self, *, reason: str) -> None:
        tasks = [
            task
            for task in self._background_cleanup_tasks
            if not task.done()
            and (
                task.get_name().startswith("proxy-http_bridge_session_close-")
                or task.get_name().startswith("http-bridge-close-")
                or task.get_name().startswith("cancelled-task-cleanup-")
            )
        ]
        if not tasks:
            return
        try:
            await asyncio.wait_for(
                asyncio.gather(*(asyncio.shield(task) for task in tasks), return_exceptions=True),
                timeout=_HTTP_BRIDGE_BACKGROUND_CLOSE_TIMEOUT_SECONDS,
            )
        except TimeoutError:
            logger.warning(
                "http_bridge_background_cleanup_drain_timeout reason=%s count=%d timeout_seconds=%.1f",
                reason,
                len(tasks),
                _HTTP_BRIDGE_BACKGROUND_CLOSE_TIMEOUT_SECONDS,
            )

    async def _fail_http_bridge_inflight_session_creation(
        self,
        key: _HTTPBridgeSessionKey,
        inflight_future: asyncio.Future[_HTTPBridgeSession] | None,
        exc: BaseException,
    ) -> bool:
        if inflight_future is None:
            return False
        async with self._http_bridge_lock:
            return _abort_http_bridge_inflight_creation_locked(self, key, inflight_future, exc)

    async def _evict_http_bridge_inflight_waiter(
        self,
        inflight_future: asyncio.Future[_HTTPBridgeSession],
        exc: BaseException,
    ) -> _HTTPBridgeSessionKey | None:
        async with self._http_bridge_lock:
            return _abort_http_bridge_inflight_creation_by_future_locked(self, inflight_future, exc)

    def _http_bridge_active_capacity_error(
        self: _HTTPBridgeServiceProtocol,
        *,
        key: _HTTPBridgeSessionKey,
        request_model: str | None,
    ) -> ProxyResponseError:
        _log_http_bridge_event(
            "capacity_exhausted_active_sessions",
            key,
            account_id=None,
            model=request_model,
            pending_count=_http_bridge_capacity_generation_count(self),
            cache_key_family=key.affinity_kind,
            model_class=_extract_model_class(request_model) if request_model else None,
        )
        return ProxyResponseError(
            429,
            local_overload_error(
                "HTTP responses session bridge has no idle capacity",
                code="capacity_exhausted_active_sessions",
            ),
        )

    def _http_bridge_forced_close_must_finish_before_create(
        self: _HTTPBridgeServiceProtocol,
        forced_replacement: bool,
        max_sessions: int,
    ) -> bool:
        # Detachment retains capacity. A forced replacement at the cap must
        # finish closing its idle predecessor before enforcing the same cap.
        return forced_replacement and _http_bridge_capacity_generation_count(self) >= max_sessions

    async def _enforce_http_bridge_capacity_after_planned_closes(
        self: _HTTPBridgeServiceProtocol,
        *,
        key: _HTTPBridgeSessionKey,
        inflight_future: asyncio.Future[_HTTPBridgeSession] | None,
        max_sessions: int,
        request_model: str | None,
    ) -> None:
        assert inflight_future is not None
        async with self._http_bridge_lock:
            if (
                self._http_bridge_inflight_sessions.get(key) is not inflight_future
                or _http_bridge_capacity_generation_count(self) <= max_sessions
            ):
                return
            # Planned evictions are discounted only to reserve this creation
            # slot. A bounded close may return on timeout while the detached
            # socket and leases remain live, so registry ownership wins here.
            _log_http_bridge_event(
                "capacity_exhausted_after_lru_close",
                key,
                account_id=None,
                model=request_model,
                pending_count=_http_bridge_capacity_generation_count(self),
                cache_key_family=key.affinity_kind,
                model_class=_extract_model_class(request_model) if request_model else None,
            )
            capacity_error = ProxyResponseError(
                429,
                local_overload_error(
                    "HTTP responses session bridge has no idle capacity",
                    code="capacity_exhausted_active_sessions",
                ),
            )
        await self._fail_http_bridge_inflight_session_creation(key, inflight_future, capacity_error)
        raise capacity_error

    async def _http_bridge_pending_count(
        self: _HTTPBridgeServiceProtocol,
        session: _HTTPBridgeSession,
    ) -> int:
        async with session.pending_lock:
            visible_pending_count = sum(
                1
                for request_state in session.pending_requests
                if _http_bridge_request_counts_against_queue(request_state)
            )
            return max(visible_pending_count, session.queued_request_count)

    def http_bridge_activity_snapshot_nowait(self: _HTTPBridgeServiceProtocol) -> dict[str, int | bool]:
        return http_bridge_activity_snapshot_nowait(self)

    def _http_bridge_pending_count_nowait(
        self: _HTTPBridgeServiceProtocol,
        session: _HTTPBridgeSession,
        *,
        context: str,
    ) -> int | None:
        return _http_bridge_pending_count_nowait(session, context=context)
