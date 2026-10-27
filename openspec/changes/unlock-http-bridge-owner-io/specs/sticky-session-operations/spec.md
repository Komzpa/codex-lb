## ADDED Requirements

### Requirement: Durable renewal verdicts are generation-bound

A still-current foreign-owner renewal MUST evict only the expected generation and return HTTP 409 `bridge_instance_mismatch`. Established durable identity with a renewal exception or missing row MUST fail with the existing ownership-unavailable HTTP 502, not successful reuse. Deliberately identity-free ordinary sessions MAY retain in-memory fallback; account-neutral recovery without verified durable identity MUST remain fail-closed with recovery eviction. Same-instance epoch adoption MUST require the same process incarnation, durable row, account and still-registered local session and MUST only increase its epoch. Renewal results after local epoch/transport change and reconciliation results after durable identity change or replacement MUST be discarded. Cleanup MUST remain single-flight without removing a successor's aliases, epoch, lease or capacity.

#### Scenario: An ordinary durable renewal is unavailable

- **GIVEN** a local session has an established durable ID and epoch
- **WHEN** renewal raises or its row is missing
- **THEN** the request fails with the ownership-unavailable HTTP 502
- **AND** the unverified socket is not returned for successful reuse

#### Scenario: A late result cannot condemn a successor

- **GIVEN** renewal or reconciliation captured one local durable ID and epoch
- **WHEN** that session is replaced or the same object advances its epoch while I/O is suspended
- **THEN** the old owned, foreign or error result cannot validate or evict the new generation
- **AND** winner aliases, ownership and capacity remain protected during old resource cleanup
