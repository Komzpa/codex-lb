## Why

Async cleanup is part of the service's cancellation contract. A caller can be cancelled while a database session is rolling back or closing, and `LiveUsageIngestor.stop()` can itself be cancelled while its consumer or trailing cache-invalidation task is still unwinding. Cleanup must finish without erasing the cancellation that asked the caller to stop, and shutdown must not return while an owned task remains unsettled.

## What Changes

- Shielded database rollback and close run to settlement after caller cancellation. The first caller cancellation is propagated after cleanup, even when cleanup raises, cancels itself, or the caller receives additional cancellation requests.
- `LiveUsageIngestor.stop()` cancels and settles both owned tasks, consumes only their shutdown cancellation, preserves child failures, and propagates caller cancellation after all owned tasks settle.
- Regression coverage exercises successful, failing, internally cancelled, and repeatedly cancelled cleanup, plus live-ingestor shutdown cancellation.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `database-backends`: database session finalization preserves caller cancellation while rollback and close settle.
- `live-usage-ingestion`: ingestor shutdown settles every owned task before returning or propagating caller cancellation.

## Impact

- Code: `app/db/session.py`, `app/modules/usage/live_ingest.py`
- Tests: `tests/unit/test_db_session.py`, `tests/unit/test_live_usage_ingest.py`, `tests/integration/test_live_usage_ingest.py`
- Specs: `openspec/specs/database-backends/spec.md`, `openspec/specs/live-usage-ingestion/spec.md`
