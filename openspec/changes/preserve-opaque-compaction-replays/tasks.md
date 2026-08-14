## 1. Spec

- [x] 1.1 Add a `responses-api-compat` delta for compact replay sanitization requirements.

## 2. Implementation

- [x] 2.1 Preserve opaque encrypted compaction items instead of inferring ciphertext provenance from prefix shape.
- [x] 2.2 Normalize synthesized plaintext compact-state assistant replacements to canonical `output_text` content arrays.

## 3. Verification

- [x] 3.1 Run focused unit/integration pytest coverage for compact replay handling.
- [x] 3.2 Run `ruff check` and `ruff format --check` on touched files.
