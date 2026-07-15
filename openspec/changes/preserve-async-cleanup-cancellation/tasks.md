## 1. Database cleanup cancellation

- [x] 1.1 Keep rollback and close cleanup alive until settlement after caller cancellation, preserving the first caller cancellation over cleanup success, failure, or internal cancellation.
- [x] 1.2 Cover cleanup success, cleanup failure, repeated caller cancellation, and internally cancelled cleanup with unit regressions.

## 2. Live ingestion shutdown

- [x] 2.1 Make `LiveUsageIngestor.stop()` cancel and settle both owned tasks, consume child-task cancellation, preserve child failures, and re-raise caller cancellation after settlement.
- [x] 2.2 Cover cancelled consumer cleanup, repeated child cancellation, and cancellation of the stop caller with unit regressions; ensure integration shutdown waits for cache invalidation.

## 3. OpenSpec

- [x] 3.1 Add normative deltas to `database-backends` and `live-usage-ingestion`.
- [x] 3.2 Validate the change and canonical specs in strict mode.
