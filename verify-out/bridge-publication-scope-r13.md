# Bridge publication scope R13

## Disposition

**Scope reconciled; accepted local evidence preserved; publication authority unresolved; parent OPEN.** Approval-ready target: `git@github.com:Komzpa/codex-lb.git` → `refs/heads/fix/http-bridge-owner-io` (existing fork PR https://github.com/Komzpa/codex-lb/pull/2). This is not permission to publish. Historical HEAD `7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d` is not a fresh lease or a commit of the retained repair.

Much simpler different way: remove only the conflicting release-note addition and reuse R12's accepted proof; do not change production, tests, Cargo or specs and do not rerun gates.

## Policy and surgical correction

Actual repository rule, `AGENTS.md:37-40`, Documentation & Release Notes:

> **Do not edit `CHANGELOG.md` directly.** Leave changelog updates to the release process; record change notes in OpenSpec artifacts instead.

OpenSpec is the repository's SSOT for feature/behavior documentation. Existing change context and normative spec deltas satisfy the documentation requirement and remain unchanged. R11's generic changelog request conflicted with this policy and the original publication exclusion; it did not override either.

Before editing, `git diff --no-ext-diff -- CHANGELOG.md` showed exactly one addition: the seven-line Unreleased/Bug Fixes block containing the proxy scheduler and native dependency notes. Removed only those read, anchored lines 3–9 with the edit tool; no whole-file reset or replacement. The necessary post-edit baseline comparison proves CHANGELOG equals `git show HEAD:CHANGELOG.md` byte-for-byte (SHA-256 `2cfcfbf984d658ad3d5568262105820b6cd4798db0438cc264c3028bdaa3e57a`). Thus no preexisting changelog content or another owner's delta was removed.

## Exact seven-path candidate

The machine manifest is `verify-out/bridge-publication-scope-r13.json`. The tracked modified path set equals these seven paths exactly; CHANGELOG and all `verify-out/` evidence are excluded from publication.

| Path | SHA-256 |
|---|---|
| `Cargo.lock` | `6463b89c9abbc82ceb57edc1dedd60a2dc62c92f99178d90acc13a5d65a512c8` |
| `Cargo.toml` | `39ba328c836a78adcfd547bb386d7a2b640317aaa568c2cca4c67081eebb8246` |
| `app/modules/proxy/_service/http_bridge/session_registry.py` | `b96a8a5c19cd6e8c9e0e664f825f1309e6edaee301955c2d139ca12e50ee6dc2` |
| `openspec/changes/unlock-http-bridge-owner-io/context.md` | `8c2100734cf16c0078696cdeff018f5a063ec18e7a0d4c83bc8a4c02b870215a` |
| `openspec/changes/unlock-http-bridge-owner-io/specs/sticky-session-operations/spec.md` | `5f08b49fc98c46c80b9a26c5ade341b34cdddaed06bc20d4a79f50862db5537f` |
| `openspec/specs/proxy-architecture/spec.md` | `6810fea41d985389a90c27e50aa112756d36f444d11f73aa2993b4db42a1dc04` |
| `tests/unit/test_proxy_http_bridge.py` | `8c2917eb4be7f12b8c94554e3011905a9dfb6ecf8f2b655beabc5d3e9e469965` |

All seven hashes match `bridge-frozen-gates-r12.json`. Seven adjacent frozen inputs also match: mixin.py, helpers.py, protocol.py, integration HTTP responses bridge tests, ring lifecycle tests, pyproject.toml and uv.lock. All 14 comparisons passed. Accepted final formatted source is used, not the superseded pre-format `final-hashes.json` checkpoint.

## Retained behavior and negative-control evidence — no reruns

The full production-entry → wiring → consumer map remains in `bridge-frozen-gates-r12.md:61-70`: streaming → mixin ownership I/O outside registry lock and immutable revalidation; fenced helper verdicts/reconciliation; application shutdown → service → mixin → registry drain → owning scheduler. This scope-only correction changes none of that wiring or consumer proof.

| Accepted proof | Retained result |
|---|---|
| Final formatted production/test consumers | 1456 passed, 8 warnings, 127.34s, source PID 2979145, exit 0; final-source receipt and actual terminal record `2d0cc4fa` |
| Real bound native consumers | 361 passed, 1 warning, 13.26s, PID 3019340, actual terminal record `d45de1cd`; earlier 11 passed/350 skipped is not native proof |
| Cargo advisories | Six RUSTSEC-2026-0382/-0386/-0391/-0398/-0403/-0410 cleared; cargo-deny PID 2920756 exit 0; Clippy/workspace/helper rebuild retained, not rerun |
| Docker / Trivy | Image `sha256:66e3d7b29b75ce4cd5b00f74e36222b75c0542c38bfc872f65c11aed6dee0e6a`; Docker build PID 3045997 and unchanged HIGH/CRITICAL ignore-unfixed Trivy PID 3055658 exit 0; zero selected Debian/Python findings. Rust clearance is cargo-deny, not a Trivy Rust-package scan; no runtime claim |
| Specs / negative control | Existing strict spec/change results exit 0. Process-local raw asyncio.wait_for control PID 2877688 failed the same real close-all consumer completion guard; original source untouched. Preserved, not rerun |

All original accepted receipts remain intact. No test, build, lint, format, security or negative-control reruns occurred.

## Remaining gates — not waived

1. **Human authority and publication:** R12 recovered no raw human publication authority in the 21 inspected parent human-message records. No search was repeated. Lead-authored publication briefs, prior actions and equal OIDs do not supply human permission. Bind actual authorization to this final seven-path artifact before publisher dispatch. Scope policy is now reconciled; publication authority is not.
2. **Cloud/current head:** retained run 40498949108 belongs to the old published head, not this unpublished repair. Dashboard job 122171582695 and core shards 122171582731/122171582756/122171582905 were in progress at the retained snapshot; frontend type/tests/lint/build and Helm were skipped. Repair-head CI, review/approval, current actionable CodeRabbit threads and mergeability remain unobserved.
3. **Runtime:** installed binary/container/service identity, post-install request-path behavior, deployment/rollback and live availability remain unproved. Local source consumers and image build/security cannot close these.
4. **Incident:** original readiness-silent freeze holder/stack and causal relation remain UNKNOWN. Preserve `заработал != починен!!!!`; local 1456/361/image proof does not close the incident.
5. **PostgreSQL latency:** real PostgreSQL-driver cancellation and shielded teardown latency remain unmeasured; no wall-clock transaction-cleanup guarantee follows from SQLite or previously published PostgreSQL suite passes.

After human authority is bound, the existing authorized publication owner must preserve identity/history, obtain a fresh exact fork URL/full-ref lease, publish only the seven-path candidate, read back the new remote/PR identity, and reconcile that head's cloud/review gates. Do not reuse historical HEAD as a lease, duplicate the PR, merge, deploy or close the parent from local greens.

## Commands, process ownership and retrospective

- `printf 'PID=%s\n' "$$"; git diff --no-ext-diff -- CHANGELOG.md` — exit 0; shell reported PID 73796. Baseline diff showed only R11's seven-line addition.
- `python3 -c` read-only hash/baseline proof — exit 0, PID 3223000. It read the R12 JSON, SHA-256 hashed the 14 frozen inputs, called `git diff --no-ext-diff --name-only` and `git show HEAD:CHANGELOG.md`, and asserted all hashes match, exact seven-path modified set, and baseline changelog equality. This is necessary file/hash proof, not a test rerun.
- Surgical edit: CHANGELOG lines 3–9 only. New evidence: this markdown and sibling JSON. No commit, push, fetch, Git metadata mutation, install, service, database or forge action. No process was killed; no owned long-running job remains.

Retrospective: generic docs instructions must yield to the actual repository release policy. Preserve accepted final-byte identities and completed consumer proof while repairing only the offending publication delta; keep scope reconciliation separate from unresolved human authority and runtime/incident acceptance.
