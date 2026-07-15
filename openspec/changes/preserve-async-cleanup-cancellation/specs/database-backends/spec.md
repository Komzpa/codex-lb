## ADDED Requirements

### Requirement: Database session cleanup preserves caller cancellation

Once asynchronous session rollback or close cleanup starts, it MUST run to settlement even if its caller is cancelled. When caller cancellation arrives while cleanup is pending, the first caller cancellation MUST be propagated after cleanup settles and MUST take precedence over cleanup success, a cleanup exception, or cancellation raised by the cleanup task itself. Additional cancellation requests to the caller MUST NOT interrupt the cleanup task or replace the first pending caller cancellation.

#### Scenario: Cleanup failure does not erase caller cancellation

- **GIVEN** session rollback or close is still pending
- **WHEN** the caller is cancelled and the cleanup later succeeds or raises a non-cancellation exception
- **THEN** cleanup reaches settlement
- **AND** awaiting the caller raises its original cancellation rather than returning or raising the cleanup result

#### Scenario: Repeated and internal cancellation preserve the first caller cancellation

- **GIVEN** session rollback or close is still pending
- **AND** the caller has already received a cancellation request
- **WHEN** the caller receives another cancellation request or the cleanup task cancels itself
- **THEN** the cleanup task is allowed to settle without interruption from the repeated caller cancellation
- **AND** the first caller cancellation is propagated instead of a later or cleanup-owned cancellation
