# Frozen bridge CI-contract repair

Result: local owning proof passed; external acceptance remains blocked. No Git metadata, forge writes, services, shared DB, updater, dependency manifest or lock mutation.

## Changes and identity

- app/modules/proxy/_service/http_bridge/mixin.py: 409c6b4698351c8417fcfcf3dd8f0dce110774f7a3a9ab306448ac0fffc26f4c
- app/modules/proxy/_service/http_bridge/session_registry.py: 6a158366bde29519c693d89a5a68c7989bf3e31afbb194c9c68e58752e6bd8f7
- tests/integration/test_http_responses_bridge.py: 609cfa05bb072d90acaef3d0a72b7e28a663b2a3e231b67492b85453eeaec701
- tests/unit/test_proxy_http_bridge.py: 6869717bcfd7a8b03b000a979bfd7637f41aa5ace109c4032029ef72325fdae9
- openspec/changes/unlock-http-bridge-owner-io/context.md: 74858e6e8f63e47415748628c8676f85a196f26d57376662d48f80b927a7a136

Moved cleanup scheduling/draining, inflight failure/eviction and idle pruning unchanged into existing registry mixin; annotated self with existing protocol. Mixin is 2428 lines against unchanged 2436 limit. No exported names, protocol contract or consumer callsites changed; no LSP export change was required or performed. Typed DurableBridgeLookup replaces the incorrect namespace fixture; explicit presence assertions narrow optional rows and mock await arguments. No casts or suppression added. Existing change context records repair/Retro; normative behavior is intentionally unchanged.

## Baseline and all failures

Existing published head 41111d4364012b21010b395769855b833343c32a failed architecture at 2560 > 2436 and eight ty diagnostics: wrong lookup fixture, six optional-row attributes, optional await_args. Full original logs/errors remain in ../bridge-head-gates-r3/. User-reported failures were not rerun as baseline.

One fresh read-only head/jobs/reviews batch is retained in this directory receipt.json, head-reviews.stdout, jobs.stdout, logs-122161377624.stdout, all-errors.txt and vulnerability-findings.txt. Integration-bridge and PostgreSQL succeeded on that prior published head, not the extracted candidate. New Docker failure: Trivy five findings, HIGH 3/CRITICAL 2, aiohttp 3.14.3 -> 3.14.4 (CVE-2026-111064, CVE-2026-111066, GHSA-2g87-pp6c-29x5), brotli 1.2.0 -> 1.2.1 (GHSA-9v8h-qqgm-4m35), certifi 2026.7.22 -> 2026.10.18 (GHSA-6q48-6c7w-9gw2). Four jobs remained in progress; no polling.

## Once-only frozen proof

Runner PID 2240751, proc bg_236. Commands executed sequentially after all source edits, all exit 0:

1. uv run python scripts/check_proxy_architecture.py
2. uv run ty check
3. uv run python -m pytest -q --tb=short --timeout=120 tests/integration/test_http_responses_bridge.py tests/unit/test_bridge_ring_lifecycle.py tests/unit/test_proxy_http_bridge.py

Actual result: 1385 passed, one existing Starlette BlockingPortal deprecation warning, 291.02 seconds. Whole command 297.63 seconds. No process stopped; child PIDs were not separately captured. Full owning files include both real reuse consumers, six SQLite execute/commit/rollback cancellation cases, continuity, quarantine/retirement, alias/epoch replacement, original deadline and request-owned reservation cleanup. Neighboring negative controls (ordinary owned reuse, eligible transition, unchanged alias/epoch paths) pass in the same unfiltered run. No new process-mutated fail-before controls were run; earlier actual fail-before controls remain retained historical evidence. Historical 67-spec result is retained, not rerun or represented as new approval.

Independent read-only ReviewNativeExecContractR2 review matched all five frozen hashes and returned no actionable findings. Receipt local://bridge-ci-contract-r4-readonly-review.md. It inspected concrete MRO/wiring and ownership/revalidation guards, but did not independently establish pre-move byte identity or execute tests. Forge review count and threads remain zero at the single fresh snapshot; no external approval waiver.

## Sequential dependency-owner handoff

Minimal authorized next allowlist: pyproject.toml and uv.lock only; this lane did not edit either. pyproject.toml direct floors are aiohttp>=3.13.4 (37), brotli>=1.2.0 (44), certifi>=2026.4.22 (45). Raise these to >=3.14.4, >=1.2.1, >=2026.10.18; regenerate uv.lock with uv's selective --upgrade-package aiohttp --upgrade-package brotli --upgrade-package certifi, preserving unrelated graph unless solver necessity is evidenced. Current lock blocks begin at 19,329,357; project metadata requirements at 558,566,567 must stay consistent with the manifest. Do not hand-edit artifact hashes.

Oracle: uv lock --check; frozen production sync matching Dockerfile line42 (uv sync --frozen --no-dev --no-install-project --extra metrics --extra tracing) in isolated verification environment; inspect installed versions and dependency delta; build the same Docker target/image then run unchanged .github/workflows/ci.yml lines725–732 Trivy CRITICAL,HIGH gate with ignore-unfixed=true and exit-code=1. Dependency availability and vulnerability clearance are not yet proved. No scan suppression, workflow change or Dockerfile change is needed by the observed evidence.

Protected Git-owner handoff: publish only the five frozen owned paths above as repair to the existing authorized bridge candidate, preserving the existing 16-file manifest/history and user acceptance. Do not include verify-out artifacts, environment state, dependency files, other lanes, commit/push/deploy from this coder role. Subsequent dependency work and external CI/review remain separate gates.

## Retro

Much simpler different way: move lifecycle operations to the existing registry helper boundary, not raise architecture budgets or add a new abstraction. Typed fixtures and explicit narrowing repair the actual contracts rather than suppress diagnostics. Fresh local 1385-test proof is distinct from retained prior 1385/67 evidence, published-head integration/PG successes, Docker findings and external approval; original incident causality and PostgreSQL-driver cancellation latency remain unproved.
