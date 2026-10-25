from __future__ import annotations

import asyncio
import time
from pathlib import Path
from typing import Any

import pytest
from sqlalchemy import event, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.models import Base
from app.db.session import _create_main_engine, close_session
from app.modules.proxy.durable_bridge_coordinator import DurableBridgeSessionCoordinator
from app.modules.proxy.http_bridge_event_batcher import HttpBridgeOperationEventBatcher


@pytest.mark.asyncio
async def test_file_sqlite_writer_control(tmp_path: Path) -> None:
    """The production engine really rejects a peer while a transaction is open."""
    engine = _create_main_engine(f"sqlite+aiosqlite:///{tmp_path}/control.db")
    factory = async_sessionmaker(engine, expire_on_commit=False)
    holder = factory()
    try:
        async with engine.begin() as connection:
            await connection.execute(text("CREATE TABLE writer_probe (value INTEGER)"))
        await holder.execute(text("INSERT INTO writer_probe VALUES (1)"))
        with pytest.raises(OperationalError, match="database is locked"):
            async with factory() as peer:
                await peer.execute(text("INSERT INTO writer_probe VALUES (2)"))
                await peer.commit()
        await close_session(holder)
        async with factory() as peer:
            await peer.execute(text("INSERT INTO writer_probe VALUES (3)"))
            await peer.commit()
    finally:
        await close_session(holder)
        await engine.dispose()


@pytest.mark.asyncio
@pytest.mark.parametrize("spool_format", ["rows_v1", "chunks_v2"])
@pytest.mark.parametrize("queued", [False, True], ids=["terminal", "queued-drain"])
async def test_terminal_timeout_releases_sqlite_writer(
    tmp_path: Path, spool_format: str, queued: bool, monkeypatch: pytest.MonkeyPatch
) -> None:
    engine = _create_main_engine(f"sqlite+aiosqlite:///{tmp_path}/terminal.db")
    factory = async_sessionmaker(engine, expire_on_commit=False)
    coordinator = DurableBridgeSessionCoordinator(factory)
    batcher = HttpBridgeOperationEventBatcher(
        coordinator, max_bytes=4096, spool_format=spool_format, flush_interval_seconds=60.0
    )
    entered = asyncio.Event()
    release = asyncio.Event()

    def pause_write_completion(connection: Any, record: Any) -> None:
        driver = connection.driver_connection
        execute = driver._execute

        async def delayed(function: Any, *args: Any, **kwargs: Any) -> Any:
            result = await execute(function, *args, **kwargs)
            if (
                not entered.is_set()
                and args
                and isinstance(args[0], str)
                and args[0].lstrip().upper().startswith(("INSERT ", "UPDATE "))
            ):
                # SQLite has executed the real write and returned its cursor,
                # but SQLAlchemy has not consumed that result. Cancel here,
                # inside the DBAPI await, rather than mocking the repository.
                entered.set()
                await release.wait()
            return result

        driver._execute = delayed

    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
            await connection.execute(text("CREATE TABLE writer_probe (value INTEGER)"))
        owner = await coordinator.claim_live_session(
            session_key_kind="session_header",
            session_key_value="owner",
            api_key_id=None,
            instance_id="instance",
            owner_process_epoch="process",
            lease_ttl_seconds=120,
            account_id=None,
            model="model",
            service_tier=None,
            latest_turn_state=None,
            latest_response_id=None,
            allow_takeover=True,
        )
        operation = await coordinator.record_operation(
            operation_id="operation",
            session_id=owner.session_id,
            instance_id="instance",
            owner_epoch=owner.owner_epoch,
            request_fingerprint="fingerprint",
            account_id=None,
            model="model",
            parent_response_id=None,
        )
        assert operation is not None
        if queued:
            monkeypatch.setattr(batcher, "_ensure_task", lambda: None)
            await batcher.enqueue(
                operation_id="operation",
                session_id=owner.session_id,
                instance_id="instance",
                owner_epoch=owner.owner_epoch,
                event_text="queued",
            )
        event.listen(engine.sync_engine, "connect", pause_write_completion)
        started = time.monotonic()
        call = asyncio.create_task(
            batcher.append_terminal_event(
                operation_id="operation",
                session_id=owner.session_id,
                instance_id="instance",
                owner_epoch=owner.owner_epoch,
                event_text="terminal",
                max_bytes=4096,
                state="completed",
                response_id="response",
            )
        )
        await asyncio.wait_for(entered.wait(), timeout=5)
        result = await asyncio.wait_for(call, timeout=3)
        assert time.monotonic() - started < 2
        assert not result.persisted
        assert result.settlement_required
        assert not release.is_set()
        # Completing the simulated DB await must suffice: no restart, forced
        # connection release, or garbage collection is allowed to repair it.
        release.set()
        async with factory() as peer:
            await peer.execute(text("INSERT INTO writer_probe VALUES (1)"))
            await peer.commit()
        await batcher.close()
        persisted = await coordinator.get_operation(operation_id="operation")
        assert persisted is not None
        assert not persisted.event_spool_complete
        assert not batcher._terminal_append_tasks
    finally:
        release.set()
        await batcher.close()
        await engine.dispose()
