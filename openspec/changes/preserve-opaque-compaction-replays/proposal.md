## Why

PR #1720 rewrites plaintext compaction replays before forwarding them upstream, but the current branch still treats only one ciphertext shape as provider-authored. Any other non-empty `encrypted_content` string is rewritten into synthetic assistant text, which drops the authoritative compact item identity and ciphertext even though the proxy's own compaction output normalizer preserves opaque encrypted strings unchanged.

The branch also synthesizes assistant replacements after request validation, so compact replays forwarded as plaintext summaries can bypass the canonical assistant-content normalization path and still reach upstream with raw string `content`.

## What Changes

- Preserve any compaction item that already carries string `encrypted_content`; only rewrite plaintext summary/text/content shapes that lack encrypted payload.
- Emit rewritten plaintext compact-state summaries in canonical assistant `output_text` form so both standard and compact Responses payloads stay upstream-compatible.
- Document the replay-sanitization contract under `responses-api-compat`.

## Impact

- Prevents compact replay continuity loss for opaque provider envelopes.
- Keeps plaintext local summaries replay-safe without relying on post-validation string content.
- Aligns PR #1720's behavior change with the repository's OpenSpec-first merge gate.
