## ADDED Requirements

### Requirement: Codex usage exposes pooled quota in response headers

The authenticated `/api/codex/usage` endpoint SHALL include the existing pooled rate-limit headers when upstream quota visibility permits it. Its JSON body SHALL retain the caller-specific quota contract.

#### Scenario: Key allowance differs from pool capacity

- **WHEN** an API key has consumed 5 percent of its primary allowance and the pool has consumed 85 percent
- **THEN** the JSON primary window reports 5 percent
- **AND** `x-codex-primary-used-percent` reports 85 percent

#### Scenario: Quota privacy is enabled

- **WHEN** an API-key caller requests usage with upstream quota visibility disabled
- **THEN** the JSON still reports that key's allowance
- **AND** pooled quota headers are omitted

#### Scenario: ChatGPT caller observes the pool

- **WHEN** an authenticated ChatGPT caller requests usage
- **THEN** the existing pooled JSON payload is preserved
- **AND** the response includes primary, secondary, and credit headers from the canonical pool provider
