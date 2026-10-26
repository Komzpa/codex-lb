# Propagate source timeouts through SSE keepalives

## Why
An upstream TimeoutError is mistaken for the keepalive timer expiring. Rewaiting on the already-failed chunk task emits heartbeats without suspension and can freeze the entire proxy event loop.

## What Changes
Distinguish expiry of the injector's own timer from an exception raised by the source. Preserve idle heartbeats, cancellation and source closure.

## Impact
- Affected specs: responses-api-compat
- Affected code: app/core/utils/sse.py
