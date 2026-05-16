## ADDED Requirements

### Requirement: Opportunistic Proxy Traffic Burns Only Safe Quota

When a proxy request is authenticated by an API key whose `traffic_class` is `opportunistic`, the proxy SHALL admit the request only if at least one eligible account can serve opportunistic traffic without crossing the burn policy floors.

Burn-first and normal accounts MAY be drained to zero only when another usable foreground account remains. The last usable normal account SHALL keep an emergency reserve. Preserve accounts SHALL require fresh usage data and SHALL remain above dynamic weekly and 5h floors.

#### Scenario: Closed burn window returns OpenAI rate limit
- **WHEN** an opportunistic API key calls a protected Codex-compatible route and no account is currently burnable
- **THEN** the proxy returns HTTP `429`
- **AND** the response uses an OpenAI-style error with code `rate_limit_exceeded`
- **AND** the message begins with `opportunistic burn window closed:`
- **AND** the response includes `Retry-After`

#### Scenario: Preflight admission mirrors routing
- **WHEN** an opportunistic API key calls `/backend-api/codex/opportunistic/admission`
- **THEN** the proxy returns `200` only when the same traffic class could select an account for a real request
- **AND** otherwise returns the same OpenAI-style `429` denial shape
