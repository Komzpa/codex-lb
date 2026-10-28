# Bridge publication receipt — 2026-10-27

## Publication tuple
- Remote: `git@github.com:Komzpa/codex-lb.git`
- Destination: `refs/heads/fix/http-bridge-owner-io`
- Observed prior OID: `41111d4364012b21010b395769855b833343c32a`
- Local branch: `fix/http-bridge-owner-io`
- Published OID: `7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d`
- Author and committer: Darafei Praliaskouski <me@komzpa.net> (configured identity).
- Lease push succeeded; exact-ref readback and PR head read back the published OID.

## Published files and content hashes
- `app/modules/proxy/_service/http_bridge/mixin.py` — `409c6b4698351c8417fcfcf3dd8f0dce110774f7a3a9ab306448ac0fffc26f4c`
- `app/modules/proxy/_service/http_bridge/session_registry.py` — `6a158366bde29519c693d89a5a68c7989bf3e31afbb194c9c68e58752e6bd8f7`
- `tests/integration/test_http_responses_bridge.py` — `609cfa05bb072d90acaef3d0a72b7e28a663b2a3e231b67492b85453eeaec701`
- `tests/unit/test_proxy_http_bridge.py` — `6869717bcfd7a8b03b000a979bfd7637f41aa5ace109c4032029ef72325fdae9`
- `openspec/changes/unlock-http-bridge-owner-io/context.md` — `74858e6e8f63e47415748628c8676f85a196f26d57376662d48f80b927a7a136`
- `pyproject.toml` — `0080ee5d8b4c3d7ad3b42aa58f1f558c83759213dd7d0246d3f350a4725d5487`
- `uv.lock` — `0e583a911223eb451f915399a111cdc34160f20da37d46ecea5e6865afeeaa03`

## Current-head CI evidence
Source: captured run `40498949108` for the published head; no polling performed here.
- Failed: `Lint (ruff)` job `122171582668`; retained log `verify-out/bridge-head-gates-r4/logs-122171582668.stdout`. Root cause: `scripts/check_proxy_timing_seams.py` flags raw `asyncio.wait_for` at `app/modules/proxy/_service/http_bridge/session_registry.py:126`, allowance zero. Replace with `scheduler_for(owner).wait_for`/`wait`/`fail_after` or pass scheduler to `wait_on_shared_future`; determine intended owner scheduler and preserve timeout semantics.
- Failures in the new-head snapshot recorded in the user-provided prior transcript: Ruff timing-seam check (`122171582668`, detailed above); Rust type check (`122171582667`, exact diagnostic unavailable); Docker Trivy high-severity gate (`122171582680`, exact findings unavailable in the candidate snapshot). Other check statuses stated successful in that snapshot: docs/release/simplicity/OpenSpec/package/Docker build/migration/e2e. Unit and integration shards, dashboard smoke, Rust workspace, Nix were pending at snapshot; frontend and Helm checks were skipped. Exact pending job IDs are not preserved in the read evidence, so remain unresolved; no polling performed.

## Acceptance and evidence boundary
- Prior source evidence: 1,385 tests passed and Trivy was clean on the frozen dependency candidate; these are not runtime acceptance for this PR head.
- Reviews/threads: previous captured snapshot reported no submitted reviews or review threads; acceptance remains pending.
- No source/Git/forge mutations or tests performed for this receipt. No unrelated state altered.
- Rollback: `git push --force-with-lease=refs/heads/fix/http-bridge-owner-io:7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d git@github.com:Komzpa/codex-lb.git 41111d4364012b21010b395769855b833343c32a:refs/heads/fix/http-bridge-owner-io`.
- Baseline old-head failure: architecture budget 2,560 > 2,436 and eight type diagnostics per retained repair receipt. Candidate failure: raw `asyncio.wait_for` at line 126 per candidate log. Causal comparison: baseline errors differ from candidate Ruff failure; no basis to claim same cause.
- Product conflicts: none reported.
