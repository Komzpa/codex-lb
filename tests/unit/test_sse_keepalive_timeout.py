from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from typing import Any

import pytest
from starlette.requests import ClientDisconnect
from starlette.responses import StreamingResponse

from app.core.utils.sse import SSE_KEEPALIVE_FRAME, inject_sse_keepalives

pytestmark = [pytest.mark.unit, pytest.mark.asyncio]


@pytest.mark.parametrize("after_heartbeat", [False, True])
async def test_keepalive_propagates_source_timeout(after_heartbeat: bool) -> None:
    release = asyncio.Event()
    failed = asyncio.Event()
    closed = asyncio.Event()
    failure = TimeoutError("provider budget expired")

    async def source() -> AsyncIterator[str]:
        try:
            yield "data: first\n\n"
            if after_heartbeat:
                await release.wait()
            raise failure
        finally:
            failed.set()
            closed.set()

    stream = inject_sse_keepalives(source(), 0.01 if after_heartbeat else 30)
    try:
        assert await anext(stream) == "data: first\n\n"
        if after_heartbeat:
            assert await anext(stream) == SSE_KEEPALIVE_FRAME
            release.set()
            await failed.wait()
        with pytest.raises(TimeoutError) as caught:
            await anext(stream)
        assert caught.value is failure
        assert closed.is_set()
    finally:
        await stream.aclose()


@pytest.mark.parametrize("spec_version", ["2.3", "2.4"])
async def test_streaming_response_does_not_flood_heartbeats_after_source_timeout(spec_version: str) -> None:
    bodies: list[bytes] = []
    closed = asyncio.Event()

    async def source() -> AsyncIterator[str]:
        try:
            yield "data: first\n\n"
            raise TimeoutError("provider budget expired")
        finally:
            closed.set()

    async def send(message: Any) -> None:
        if message["type"] == "http.response.body":
            bodies.append(message["body"])
            # A finite assertion catches the pre-fix busy loop without hanging
            # this test's event loop or depending on an in-loop timeout.
            assert len(bodies) <= 3, "source timeout became an endless heartbeat stream"

    async def receive() -> Any:
        await asyncio.Event().wait()

    response = StreamingResponse(inject_sse_keepalives(source(), 30), media_type="text/event-stream")
    # ASGI 2.4 interprets OSError (including TimeoutError) as a disconnect.
    expected = ClientDisconnect if spec_version == "2.4" else TimeoutError
    with pytest.raises(expected):
        await response({"type": "http", "asgi": {"spec_version": spec_version}}, receive, send)
    assert bodies == [b"data: first\n\n"]
    assert closed.is_set()
