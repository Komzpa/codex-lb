## 1. Exact-owner timeout recovery

- [x] 1.1 After capacity and same-key timeout aborts, wait boundedly for the exact owner and retry only after it terminates.
- [x] 1.2 Preserve the existing structured 429 when the exact owner outlives that bounded wait.

## 2. Regression coverage and verification

- [x] 2.1 Cover both timeout paths for successful post-cancellation admission and cancellation-resistant 429 behavior, including no duplicate creation before owner termination.
- [x] 2.2 Run focused bridge tests, requested bridge suite, lint/format/diff, and strict OpenSpec validation.
