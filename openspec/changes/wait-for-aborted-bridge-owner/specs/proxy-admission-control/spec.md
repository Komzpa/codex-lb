## ADDED Requirements

### Requirement: Aborted HTTP bridge startup owners are observed before retry

The proxy MUST retain an aborted HTTP bridge in-flight marker while its exact
creator task is still running. When a bridge capacity waiter or same-key
in-flight creation waiter reaches its configured admission timeout, it MUST
signal cancellation only to the exact creator recorded on the current
non-handoff marker. The timing-out request MUST wait no longer than one
additional configured admission-wait interval for that exact creator to
terminate; if it terminates, the request MUST retry admission. If it does not
terminate in that interval, the proxy MUST return the existing structured
local-overload HTTP 429.

#### Scenario: Exact owner ends after timeout cancellation

- **WHEN** a capacity or same-key admission waiter times out and its exact
  aborted owner terminates within the additional bounded wait
- **THEN** the waiter retries admission and may complete without a 429
- **AND** no replacement creation begins before the owner terminates

#### Scenario: Exact owner resists cancellation

- **WHEN** a capacity or same-key admission waiter times out and its exact
  aborted owner remains running beyond the additional bounded wait
- **THEN** the waiter returns the existing structured local-overload HTTP 429
- **AND** the owner-held marker remains until that owner finalizes
