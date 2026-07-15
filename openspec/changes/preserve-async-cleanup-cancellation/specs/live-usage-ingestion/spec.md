## ADDED Requirements

### Requirement: Live ingestion shutdown settles all owned tasks

`LiveUsageIngestor.stop()` MUST cancel and settle both its consumer task and any pending trailing cache-invalidation task before it returns. Cancellation raised by those child tasks as part of shutdown MUST be consumed, while non-cancellation child failures MUST remain observable after every owned task settles. If the caller of `stop()` is cancelled during shutdown, that caller cancellation MUST remain pending, MUST NOT abandon settlement of either child task, and MUST be propagated after both tasks settle in preference to child failures.

#### Scenario: Normal shutdown consumes owned-task cancellation

- **GIVEN** the consumer and trailing cache-invalidation tasks are active
- **WHEN** `LiveUsageIngestor.stop()` cancels them
- **THEN** it waits for both tasks to settle
- **AND** cancellation raised by either child as part of shutdown does not escape from `stop()`

#### Scenario: Child failure remains observable after complete settlement

- **GIVEN** both owned tasks are being stopped
- **WHEN** one child raises a non-cancellation exception
- **THEN** `stop()` still settles the other child
- **AND** the child failure is raised after both tasks settle unless caller cancellation takes precedence

#### Scenario: Caller cancellation waits for complete shutdown

- **GIVEN** at least one owned task is still unwinding
- **WHEN** the caller of `stop()` is cancelled
- **THEN** `stop()` continues settling every owned task
- **AND** it propagates the caller cancellation only after all owned tasks settle
