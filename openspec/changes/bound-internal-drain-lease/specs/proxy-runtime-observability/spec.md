# Proxy runtime observability delta

## ADDED Requirements

### Requirement: Internal deployment drain is bounded

An internal deployment drain MUST use a default bounded lease measured with a
monotonic clock. Starting drain MUST create or renew the lease and report its
TTL and expiry. Stopping drain MUST clear both finite-request and HTTP-bridge
drain state. Once the lease expires, the next drain-state observation MUST
clear both states and admit ordinary requests again. Process shutdown MAY still
set unbounded drain state independently of the internal deployment lease.

#### Scenario: Drain caller exits before stop

- **GIVEN** the internal drain endpoint started a bounded lease
- **AND** the caller exits without stopping drain
- **WHEN** the lease expires and another request checks drain state
- **THEN** finite-request and HTTP-bridge drain state are both cleared
- **AND** the request is admitted normally

#### Scenario: Repeated drain start renews the lease

- **GIVEN** an internal drain lease is active
- **WHEN** the internal drain endpoint is called again
- **THEN** the lease expiry advances by the default TTL
- **AND** the response reports the renewed TTL and expiry
