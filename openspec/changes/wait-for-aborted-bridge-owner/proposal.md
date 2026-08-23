## Why

An HTTP bridge admission waiter can time out while the exact creator that owns
the shared marker is still running. The existing code signals cancellation but
immediately returns a local-overload 429, even when that owner terminates a
moment later and capacity is otherwise available.

## What Changes

- After a bridge capacity or same-key inflight timeout aborts its exact owner,
  wait boundedly for that owner task to terminate and retry admission.
- Keep the aborted marker until its owner finalizes; do not create a
  replacement while that marker is still owner-held.
- Preserve the existing structured local-overload 429 when the owner does not
  terminate within the additional bounded wait.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `proxy-admission-control`: HTTP bridge startup timeout recovery waits for the
  aborted owner before retrying admission.

## Impact

- `app/modules/proxy/_service/http_bridge/mixin.py`
- `tests/unit/test_proxy_http_bridge.py`
