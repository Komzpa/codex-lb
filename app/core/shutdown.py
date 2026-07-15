from __future__ import annotations

import asyncio
import math
import time

DEFAULT_INTERNAL_DRAIN_TTL_SECONDS = 30.0

_draining: bool = False
_bridge_drain_active: bool = False
_in_flight: int = 0
_internal_drain_expires_at: float | None = None
_internal_drain_ttl_seconds: float | None = None


def reset() -> None:
    global _draining, _bridge_drain_active, _in_flight
    global _internal_drain_expires_at, _internal_drain_ttl_seconds
    _draining = False
    _bridge_drain_active = False
    _in_flight = 0
    _internal_drain_expires_at = None
    _internal_drain_ttl_seconds = None


def set_draining(val: bool = True) -> None:
    global _draining, _internal_drain_expires_at, _internal_drain_ttl_seconds
    _draining = val
    _internal_drain_expires_at = None
    _internal_drain_ttl_seconds = None


def is_draining() -> bool:
    _expire_internal_drain_lease_if_needed()
    return _draining


def set_bridge_drain_active(val: bool = True) -> None:
    global _bridge_drain_active
    _bridge_drain_active = val


def is_bridge_drain_active() -> bool:
    _expire_internal_drain_lease_if_needed()
    return _bridge_drain_active


def start_internal_drain_lease(ttl_seconds: float = DEFAULT_INTERNAL_DRAIN_TTL_SECONDS) -> float:
    if not math.isfinite(ttl_seconds) or ttl_seconds <= 0:
        raise ValueError("internal drain TTL must be a positive finite number")

    global _draining, _bridge_drain_active
    global _internal_drain_expires_at, _internal_drain_ttl_seconds
    _draining = True
    _bridge_drain_active = True
    _internal_drain_ttl_seconds = ttl_seconds
    _internal_drain_expires_at = time.monotonic() + ttl_seconds
    return _internal_drain_expires_at


def clear_internal_drain_lease() -> None:
    global _draining, _bridge_drain_active
    global _internal_drain_expires_at, _internal_drain_ttl_seconds
    _draining = False
    _bridge_drain_active = False
    _internal_drain_expires_at = None
    _internal_drain_ttl_seconds = None


def get_internal_drain_status() -> tuple[bool, bool, float | None, float | None]:
    _expire_internal_drain_lease_if_needed()
    return _draining, _bridge_drain_active, _internal_drain_ttl_seconds, _internal_drain_expires_at


def _expire_internal_drain_lease_if_needed() -> None:
    if _internal_drain_expires_at is not None and time.monotonic() >= _internal_drain_expires_at:
        clear_internal_drain_lease()


def increment_in_flight() -> None:
    global _in_flight
    _in_flight += 1


def decrement_in_flight() -> None:
    global _in_flight
    _in_flight = max(0, _in_flight - 1)


def get_in_flight() -> int:
    return _in_flight


async def wait_for_in_flight_drain(timeout_seconds: float, poll_interval_seconds: float = 0.1) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while get_in_flight() > 0 and time.monotonic() < deadline:
        await asyncio.sleep(poll_interval_seconds)
    return get_in_flight() == 0
