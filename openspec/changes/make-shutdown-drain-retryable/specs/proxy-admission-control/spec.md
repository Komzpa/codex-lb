## ADDED Requirements

### Requirement: Shutdown drain rejection is explicitly retryable

When a replica rejects new finite HTTP work because shutdown drain is active, it MUST return HTTP 503 with an OpenAI-style error envelope whose code is `server_draining`, and it MUST include a `Retry-After` header.

#### Scenario: Codex Responses request arrives during shutdown drain

- **WHEN** shutdown drain is active and a client posts to `/backend-api/codex/responses`
- **THEN** the response status is 503
- **AND** `error.code` is `server_draining`
- **AND** `Retry-After` provides a positive delay in seconds
