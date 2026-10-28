# Bridge all gate families R11

## Single completed-log batch and immutable identity

Run 40498949108 metadata was fetched once with `gh api --paginate repos/Komzpa/codex-lb/actions/runs/40498949108/jobs?per_page=100` (exit 0). All 25 jobs fit the one exhausted page. Raw metadata: `bridge-all-gate-families-r11/jobs.json`. Every listed job belongs to published 7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d; no repush or Git mutation. Collector PID 2813425 exited 0; all 15 completed, non-skipped job logs fetched successfully once. Fetch receipts and complete logs are retained in the same directory. Diagnostic IDs 122171582667 and 122171582680 return HTTP 404 on direct job metadata lookup: they are not jobs in this run, not evidence of candidate type/Trivy failures.

## Exhaustive failing families and repair allowlist

- Ruff job 122171582668: one raw `asyncio.wait_for` in session_registry.py:126, timing allowance zero. The real owning scheduler is `scheduler_for(self)`; preserve gather, shielding, timeout, and failure result semantics. Allowlist: registry one-line seam repair; owning bridge unit/integration files only if required for proof; existing OpenSpec context/normative specs and changelog.
- Unit job 122171582730: three failures, all the same raw-timeout cause: test_repository_timing_seams_pass, test_repository_allowances_are_exact, test_repository_report_reproduces_committed_block. No allowance/oracle changes authorized.
- Rust workspace job 122171582675: formatting/clippy/tests/release/native wire probes succeeded; cargo-deny advisories failed. Six actual candidate dependency findings: rustls-webpki 0.103.15 distrusted intermediates; tokio 1.49.0 AsyncFd I/O safety; zstd 0.13.3 context stream leakage; zstd-safe 7.2.4 seekable capacity and legacy uninitialized output; zstd-sys 2.0.16 wasm allocator failure. This is not a Rust type error. Dependency ownership/rewrite decision remains open; no Cargo changes yet.

## Successful / skipped / unresolved families

Candidate Python ty 122171582678 succeeds. Candidate Docker 122171582713 build, SARIF, and high-severity Trivy gate all succeed: no Python dependency refresh warranted. OpenSpec, attribution, detection, SQLite/PostgreSQL migration, package, PostgreSQL tests, e2e, bridge integration and Nix succeed. Frontend type/tests/lint, Helm and other no-step jobs are skipped (see exact metadata). Dashboard smoke 122171582695 and integration-core shards 122171582731/122171582756/122171582905 were in progress at this single observation; remain unproved, no repeated polling.

## Evidence boundary and retrospective

The retained 1385-pass source freeze and clean local dependency-image proof remain historical, not proof for a changed registry hash. Original incident freeze causality remains UNKNOWN; source consumer proof is not installed-runtime proof. Repair the production scheduler seam, not check allowances or exception handling. Preserve this complete batch rather than repairing the first error and discovering other families piecemeal. Exact scoped commands, current hashes and terminal proof will be appended after repair. No shared DB/service/install/public changes are authorized.

### Authorized narrow dependency expansion

Main authorized Cargo.lock and only necessary Cargo manifests for the six observed candidate advisories; no broad refresh, suppression, deny allowance or Python change. Fixed requirements from complete candidate log: RUSTSEC-2026-0382 webpki >=0.103.16,<0.104.0-alpha.1 or >=0.104.0-alpha.8; RUSTSEC-2026-0386 tokio >=1.51.6,<1.52.0 or >=1.53.3; RUSTSEC-2026-0391 zstd >=0.14.3; RUSTSEC-2026-0398 and RUSTSEC-2026-0403 zstd-safe >=8.2.0; RUSTSEC-2026-0410 zstd-sys >=2.1.2. Start with compatible patched versions and minimal resolution; report incompatible constraints instead of bypassing them. Affected complete bridge files, timing oracle, architecture/cancellation/timing, Python type and strict change proof have been launched before dependency mutation; exact PID/exit receipts follow.

## Scoped proof checkpoint and causal follow-through

Runner PID 2842933: initial complete-file PID 2842935 returned 1454 passed / 2 failed in 136.14s. All three bridge owning files passed, including the real shutdown consumer with injected virtual scheduler, pending shielded cleanup and successful subsequent drain. The two remaining timing-oracle failures identify the obsolete `"app/modules/proxy/_service/http_bridge/mixin.py" = { raw-timeout = 1 }` clause in `openspec/specs/proxy-architecture/spec.md:68`: moving and repairing that wait exhausted the allowance. Main explicitly authorized deleting only that clause (1 -> 0); registry remains unlisted with allowance zero. No oracle assertions changed or allowances widened. Initial architecture PID 2898799, cancellation PID 2899192, timing PID 2901782, ty PID 2902007 and strict change PID 2902571 all exited 0. Ruff PID 2902482 found import order in the already moved registry import block; it was repaired by moving only the two type names to Ruff's expected ordering.

The process-local raw-timeout negative control (PID 2877688) restored only the original `asyncio.wait_for` in memory. The same real shutdown consumer failed at its one-second completion guard after virtual time advanced; its shielded cleanup then completed after release. Exit 1 as expected, 1 failed. Initial incorrect invocation `.venv/bin/python -m runpy verify-out/bridge-negative-control-r11.py` exited 1 before execution; corrected command was `.venv/bin/python -c 'import runpy; runpy.run_path("verify-out/bridge-negative-control-r11.py", run_name="__main__")'`. No checkout mutation by the negative control.

### Minimal Cargo resolution

Only Cargo.toml's exact Tokio pin needed a manifest change, 1.49.0 -> 1.51.6. Existing async-compression 0.4.43 permits codec 0.4.40; cached release metadata shows 0.4.38/39 require zstd ^0.13.1/safe ^7, whereas 0.4.40 is the first release requiring zstd ^0.14.0/safe ^8. Selective commands (all exit 0): `cargo update -p tokio --precise 1.51.6`, `cargo update -p rustls-webpki --precise 0.103.16`, `cargo update -p compression-codecs --precise 0.4.40`, `cargo update -p zstd --precise 0.14.3`, `cargo update -p zstd-safe --precise 8.2.0`, `cargo update -p zstd-sys --precise 2.1.2`. Necessary companion resolutions: tokio-macros 2.6.1 -> 2.7.2 and compression-core 0.4.32 -> 0.4.34. Python manifest/lock are untouched. Exact published/current dependency graph delta and final gate receipts are retained alongside logs.

### Non-gating completed-log diagnostics

The successful published integration-bridge job additionally reports aiosqlite worker-thread `Event loop is closed` warnings from `tests/integration/test_proxy_websocket_responses.py`, outside the changed bridge owning file. They are retained in the complete log, not suppressed or misreported as gate failures. No unrelated test/DB repair is authorized by this batch.

## Terminal repaired-gate batch

Final gate runner PID 2920622 completed. Exact arguments/PIDs/exits are in `bridge-all-gate-families-r11/final-receipt.json`; all families passed except two formatter diagnostics subsequently repaired (registry trailing blank, existing multiline AsyncMock fixture). No semantic/test-oracle change was made for those diagnostics.

| Actual command / consumer | PID | Exit / observed result |
|---|---:|---|
| `cargo deny --all-features check` | 2920756 | 0; advisories/bans/licenses/sources all OK; all six findings cleared |
| `cargo clippy --workspace --all-targets --all-features --locked -- -D warnings` | 2920885 | 0 |
| `cargo test --workspace --all-targets --locked` | 2925581 | 0 |
| `cargo build --locked -p codex-lb-egress-worker --bin codex-lb-native-egress` | 2930272 | 0 |
| Full native routed/SSE/websocket/usage integration files (exact four in receipt) | 2930285 | 0; 11 passed, 350 skipped because TEST_BINARY absent; not native wire proof. Corrected actual-consumer run follows separately. |
| Full bridge integration/lifecycle/proxy unit + timing-seam unit files (`pytest -q --tb=short --timeout=120 -n 8 --dist=load`) | 2931252 | 0; 1456 passed, 8 existing deprecation warnings, 120.09s |
| architecture / cancellation / timing scripts | 2969382 / 2969514 / 2970722 | all 0 |
| `ty check` | 2970918 | 0 |
| scoped `ruff check` | 2971178 | 0 |
| scoped `ruff format --check` | 2971223 | 1; two exact formatting hunks repaired; final source-identity proof in flight |
| `openspec validate --specs --strict` / `openspec validate unlock-http-bridge-owner-io --strict` | 2971268 / 2971380 | both 0 |

The native release build passed on the published head before dependency repair; the fresh lock's debug build and real native consumers pass above. A fresh Docker build/unchanged Trivy HIGH,CRITICAL gate is chained after the final formatted-source proof, because Cargo.lock is copied into the native build stage. This is an isolated verification image, not an install or service mutation.

### Final source identities after measured formatting

- registry `b96a8a5c19cd6e8c9e0e664f825f1309e6edaee301955c2d139ca12e50ee6dc2`
- proxy unit `8c2917eb4be7f12b8c94554e3011905a9dfb6ecf8f2b655beabc5d3e9e469965`
- Cargo.toml `39ba328c836a78adcfd547bb386d7a2b640317aaa568c2cca4c67081eebb8246`; Cargo.lock `6463b89c9abbc82ceb57edc1dedd60a2dc62c92f99178d90acc13a5d65a512c8`
- canonical architecture spec `6810fea41d985389a90c27e50aa112756d36f444d11f73aa2993b4db42a1dc04`
- Python manifest `0080ee5d8b4c3d7ad3b42aa58f1f558c83759213dd7d0246d3f350a4725d5487`; uv.lock `0e583a911223eb451f915399a111cdc34160f20da37d46ecea5e6865afeeaa03` (unchanged)

Still-unproved criteria: cloud dashboard + three core shards at the single captured snapshot; remote gates/review/approval for this unpublished local repair; installed-runtime behavior; original incident freeze cause; real PostgreSQL-driver cancellation latency. None is closed by source tests, local image scan or historical 1385 passes. No new acceptance rows or publication authority are inferred.

### Actual native consumer proof after explicit binary binding

The first exit-zero native pytest attempt was not wire proof: 350 cases skipped without CODEX_LB_NATIVE_EGRESS_TEST_BINARY. Corrected invocation sets `CODEX_LB_NATIVE_EGRESS_TEST_BINARY=/home/kom/proj/ai_pr/codex-lb-bridge-owner-main-20261027/target/debug/codex-lb-native-egress` and runs `.venv/bin/python -m pytest -q -ra tests/integration/test_native_routed_egress.py tests/integration/test_native_sse_egress.py tests/integration/test_native_websocket_events.py tests/integration/test_native_usage_egress.py`. Actual exec PID 3019340: **361 passed, 1 existing deprecation warning in 13.26s**, exit 0. This proves the rebuilt native helper through the real routed/SSE/websocket/usage consumers, not direct helper invocation or skipped coverage.

## Final terminal result — all affected local families pass

The final formatted source identity passed the complete four-file run again: PID **2979145**, **1456 passed**, 8 existing deprecation warnings in 127.34s, exit 0. The subsequent exact scoped Ruff check and format check, architecture/cancellation/timing scripts and ty check all exited 0. Exact arguments and final source hashes: `bridge-all-gate-families-r11/final-source-receipt.json`. Earlier `final-hashes.json` is the pre-format checkpoint, not the final source identity.

Fresh image runner PID 3045993 completed normally. `docker build --progress=plain -t codex-lb:bridge-r11-gates .` PID 3045997 exit 0; this builds the actual Docker native release target from the repaired lock. `trivy image --scanners vuln --ignore-unfixed --severity CRITICAL,HIGH --exit-code 1 --format json --output <ROOT>/verify-out/bridge-all-gate-families-r11/trivy-image.json codex-lb:bridge-r11-gates` PID 3055658 exit 0. Image inspect PID 3056319 exit 0, identity **sha256:66e3d7b29b75ce4cd5b00f74e36222b75c0542c38bfc872f65c11aed6dee0e6a**. Actual JSON has zero selected vulnerabilities for Debian and Python. This scanner output has no Rust-package result; Rust advisories are separately proved clear by the actual cargo-deny gate, not inferred from Trivy. Full image logs and exact commands/exits are in `image-receipt.json`, `image-*.log`, and `trivy-image.json`.

Changed production/documentation paths: registry; existing proxy bridge unit file; Cargo.toml; Cargo.lock; canonical proxy-architecture spec (one exhausted allowance deletion); existing change's sticky-session normative delta and context; CHANGELOG.md (explicitly requested). No other production paths, Python dependencies, native fork refs, feature set or deny configuration changed. All temporary collector/control/runner scripts were removed after completion; raw evidence remains. Every launched finite process completed; no PID was killed and no service was started. No Git metadata, push, installation, live/shared DB or service mutation occurred.

Acceptance mapping: registry-drain production entry -> owner scheduler -> real close-all shutdown consumer with virtual deadline and retained close ownership, plus raw-wait negative control; source ownership-I/O behavior -> complete three bridge files, including actual SQLite teardown-gated availability and generation/reselection controls; dependency repair -> exact eight-package delta -> actual cargo-deny, clippy/workspace tests, rebuilt helper real native consumers and Docker release build; image security -> exact new image and unchanged high/critical gate. All affected local families now pass. The explicit still-unproved criteria listed above remain open, including the unpublished local tree's remote CI/review and installed/runtime/original-incident claims.

Retro completion: moving a method requires migrating its scheduler seam and retiring only the exhausted allowance; green command exit must not hide skipped consumer coverage; completed job IDs must be checked against the exact published head before refreshing dependencies. These lessons are embodied in the owner seam, zero-allowance tightening, virtual shutdown consumer, bound-binary actual native proof and all-family immutable log inventory, not only this retrospective text.
