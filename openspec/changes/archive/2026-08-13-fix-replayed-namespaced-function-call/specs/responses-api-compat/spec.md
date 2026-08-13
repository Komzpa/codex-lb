## ADDED Requirements

### Requirement: Replayed tool-call namespace metadata survives live Responses egress

For standard live Responses requests, including WebSocket `response.create` and configured Responses model-source egress, the proxy MUST preserve `namespace` on replayed `input` items whose `type` is `function_call`, `custom_tool_call`, or `apply_patch_call`. Tool namespaces are part of the live tool-routing identity. Compact Responses egress MAY omit those namespaces only as part of the compact-specific upstream compatibility serializer. The proxy MUST preserve all other fields on each tool-call item and MUST NOT alter client-provided top-level tool entries as part of this normalization.

Historical response.create slimming MUST preserve outputs for namespaced agent-control calls, including `collaboration` and `multi_agent_v1` calls, even when those outputs are large. Such outputs carry the completed spawn/wait state needed by the next model turn and MUST NOT be replaced with a generic historical tool-output omission notice. Unrelated historical tool outputs MAY still be slimmed under the normal payload-budget policy.

#### Scenario: Standard Responses replay preserves tool-call namespaces upstream

- **WHEN** a standard Responses request replays `function_call` and `custom_tool_call` input items with `namespace`
- **THEN** the upstream payload preserves those items' `namespace`
- **AND** preserves their remaining call fields
- **AND** the local request input retains the namespace metadata

#### Scenario: Compact Responses replay omits tool-call namespace upstream

- **WHEN** `/v1/responses/compact` replays a recognized tool-call input item with a namespace
- **THEN** its upstream payload omits the input item's `namespace`
- **AND** preserves the remaining tool-call fields

#### Scenario: WebSocket response.create preserves tool-call namespaces upstream

- **WHEN** a Responses WebSocket request replays namespaced `function_call` and `custom_tool_call` input items
- **THEN** the upstream `response.create` frame preserves those items' `namespace`
- **AND** preserves their remaining call fields

#### Scenario: Configured Responses model source preserves tool-call namespaces upstream

- **WHEN** `/v1/responses` routes a replayed namespaced tool call to a configured OpenAI-compatible Responses model source
- **THEN** the source payload preserves the call item's `namespace`
- **AND** preserves source-compatible request fields that the Codex upstream path does not support

#### Scenario: Account-neutral replay classification retains namespace identity

- **WHEN** an HTTP bridge evaluates a namespaced tool-call history for cross-account replay safety
- **THEN** the classifier input retains the namespace metadata
- **AND** the request fails closed rather than becoming account-neutral because of wire normalization

#### Scenario: Malformed replay item type does not fail serialization

- **WHEN** a permissively parsed input item has a non-string `type` and a `namespace`
- **THEN** outbound serialization does not raise an internal type error
- **AND** does not treat the item as a recognized replayed tool call

#### Scenario: Top-level namespace tool remains byte-preserved

- **WHEN** the client includes a top-level tool entry whose `type` is `namespace`
- **THEN** standard Responses serialization forwards that tool entry byte-identically

#### Scenario: Historical agent wait output remains visible after slimming

- **WHEN** a response.create payload contains a historical `multi_agent_v1.wait_agent` call with a large matching output
- **AND** also contains an unrelated large historical shell output
- **THEN** the agent wait output remains byte-preserved in the upstream input
- **AND** the unrelated shell output MAY be replaced with the historical tool-output omission notice
