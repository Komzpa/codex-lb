## Why

Durable renewal, ring membership and endpoint reads currently retain the global HTTP bridge registry lock. Database transaction teardown can outlive cancellation, so a timeout around renewal cannot guarantee registry progress. Ordinary renewal errors also currently permit reuse without ownership evidence.

## What Changes

- Select and reserve under the registry lock, perform request-owned ownership I/O outside it, then revalidate immutable session generation, aliases, reservations and routing inputs before publication.
- Fail established durable reuse closed when ownership verification is unavailable; retain intentional identity-free in-memory fallback and the narrow same-process epoch adoption rule.
- Reject stale renewal and reconciliation results without mutating replacement generations.
- Keep execute, commit and rollback cleanup owned by the request and preserve unrelated registry progress while cleanup is held. Add no renewal timeout or detached renewal worker.

## Capabilities

### Modified Capabilities

- `responses-api-compat`: lock-free ownership I/O with generation-checked reuse and routing.
- `sticky-session-operations`: fenced renewal verdicts and immutable reconciliation snapshots.

## Evidence limit

This independently fixes a registry-lock defect. The original readiness-silent incident's blocked stack and causal holder are unknown; this change alone cannot establish incident resolution.
