## Implementation

- [x] Split canonical and previous-response renewal into locked selection, unlocked request-owned I/O and locked revalidation/publication.
- [x] Move membership and endpoint reads outside the registry lock and derive the owner from one resolved ring.
- [x] Fail established durable renewal unavailable closed and fence reconciliation by immutable durable identity.
- [x] Preserve narrowly scoped same-process epoch adoption and generation-owned cleanup.

## Acceptance

- [x] Execute full owning integration and unit test files without filtering.
- [x] Prove actual execute/commit/rollback cancellation allows unrelated registry work before cleanup release on both reuse consumers.
- [x] Prove delayed foreign ownership, replacement/epoch/alias/inflight races and stale endpoint failure handling.
- [x] Run fail-before consumer and targeted ownership negative controls, restoring the candidate afterward.
- [x] Validate normative specs strictly and record exact source identity and retrospective evidence in context.md.
