## ADDED Requirements

### Requirement: HTTP bridge ownership I/O leaves the registry available

Canonical and previous-response reuse MUST select and reserve under the registry lock, perform ownership I/O outside it, and revalidate immutable session generation, durable identity, account/transport, aliases, inflight bindings and server-scoped reservations before publishing successful-use metadata or returning. Creation waiters MUST re-enter selection. Renewal MUST remain request-owned through execute, commit, owner-read, rollback and close, without a detached renewal worker or new arbitrary deadline. Membership and endpoint I/O MUST remain outside the lock, use one resolved ring for owner selection, and discard stale results or errors before forwarding, detachment or admission. Live local reuse MUST NOT read the ring; missing endpoints MUST NOT override durable fencing of live DRAINING owners.

#### Scenario: Actual transaction cancellation retains unrelated progress

- **GIVEN** canonical or previous-response reuse has entered actual execute, commit or rollback
- **AND** request-owned transaction teardown remains gated
- **WHEN** the caller is cancelled repeatedly
- **THEN** unrelated soft admission and alias removal finish before the gate opens
- **AND** cancellation and original-reservation cleanup finish after release without an unfenced compensating release

#### Scenario: A local winner supersedes held routing I/O

- **GIVEN** membership or endpoint I/O is held
- **WHEN** a local session, alias or inflight binding changes
- **THEN** the stale result or endpoint error is discarded
- **AND** current selection is independently verified before reuse or routing

#### Scenario: Previous-response eligibility changes during renewal

- **GIVEN** previous-response reuse is awaiting durable renewal
- **WHEN** its selected session becomes quarantined or marked to retire after drain
- **THEN** reselection MUST NOT renew or publish that ineligible session for reuse
- **AND** a still-eligible session remains available for independently renewed continuity
