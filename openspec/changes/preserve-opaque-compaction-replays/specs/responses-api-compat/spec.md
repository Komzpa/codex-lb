## ADDED Requirements

### Requirement: Compaction replay sanitization preserves opaque encrypted state

When a standard or compact Responses request replays a historical compaction item, the proxy MUST preserve that item unchanged whenever it already carries string `encrypted_content`. The proxy MUST NOT infer local plaintext provenance from ciphertext prefix or length heuristics, and MUST NOT replace such an item with synthetic assistant text solely because the encrypted payload shape is unfamiliar.

When the replayed compaction item instead carries plaintext `summary`, `text`, or text-bearing `content` without string `encrypted_content`, the proxy MAY rewrite it into assistant context for upstream compatibility. Any assistant replacement synthesized during request serialization MUST use the canonical assistant content schema (`output_text` content parts), not a raw string `content` field.

#### Scenario: compact replay keeps opaque encrypted content

- **WHEN** `/backend-api/codex/responses/compact` receives a replayed `compaction` item whose `encrypted_content` is a non-empty opaque string
- **THEN** the forwarded upstream payload preserves that compaction item unchanged
- **AND** its `id`, `status`, and `encrypted_content` remain intact

#### Scenario: plaintext compact summary rewrites to canonical assistant content

- **WHEN** a replayed compact request contains a historical `compaction` item with plaintext `summary` and no string `encrypted_content`
- **THEN** the proxy rewrites it to an assistant item with `content` as an `output_text` array
- **AND** the synthesized text begins with the compact-state prefix used for local plaintext summaries
