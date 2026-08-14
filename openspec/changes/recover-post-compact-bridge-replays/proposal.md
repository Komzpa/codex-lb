# Recover post-compact HTTP bridge replays

## Why

Post-compaction Codex turns can carry a compact context item, completed
tool-search call/output side effects, and a fresh user message. When the HTTP
bridge treats a session-level compact-anchor trim as a generically safe fresh
replay, later recovery may drop the durable context or tool-search side effects
that make the follow-up self-contained. If the original owner account is also
silent or unavailable, the retry path can keep requiring that owner and stall at
the `response.created` gate instead of completing on another eligible account.

## What Changes

- Treat completed `compaction` items with encrypted content as self-contained
  account-neutral replay context.
- Preserve completed `tool_search_call` / `tool_search_output` pairs when
  projecting a compacted fresh replay payload.
- Preserve compact context when projecting a fresh replay payload, while removing
  response-owned ids.
- Keep session-level compact-anchor trim safety separate from durable full-resend
  proof; trimming a stored prefix does not automatically make an unanchored
  replay safe.
- Let account-neutral recovery switch away from an excluded or silent owner
  account, while still failing closed for requests that explicitly require the
  previous owner.
- Retire stale response-create gate holders with evidence about whether upstream
  response events were already observed, so wedged bridge sessions take the
  existing recovery/quarantine path.

## Impact

Post-compaction follow-up turns recover with the compact context preserved and
do not loop on an owner account that cannot acknowledge `response.create`.
