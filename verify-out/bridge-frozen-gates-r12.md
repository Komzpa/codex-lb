# Bridge frozen-gate acceptance R12 — narrow publication handoff

## Disposition

**Local repaired-source/image evidence accepted; publication authority unresolved; parent acceptance remains OPEN.** No product changes, check reruns, external reviewer calls, forge reads/writes, commits, pushes, fetches, merge-tree, installation, service or shared-DB operations were performed in this review. This is an evidence/consumer-wiring review, not a new independent automated code review or runtime acceptance.

Much simpler different way: reuse the frozen R11 consumer and image receipts, distinguish superseded attempts, and hand off only the exact eight-file local delta. Do not restart passed checks or create another branch/PR.

## Exact artifact surface

ROOT: `/home/kom/proj/ai_pr/codex-lb-bridge-owner-main-20261027`.
Observed HEAD: `7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d`. This is the previously published commit, **not** a commit of the R11 repair. Read-only `git status --short`, `git rev-parse HEAD`, `git diff --stat`, and `git diff --name-only` showed eight tracked modified paths, no staged entries, plus untracked `verify-out/`:

```text
CHANGELOG.md
Cargo.lock
Cargo.toml
app/modules/proxy/_service/http_bridge/session_registry.py
openspec/changes/unlock-http-bridge-owner-io/context.md
openspec/changes/unlock-http-bridge-owner-io/specs/sticky-session-operations/spec.md
openspec/specs/proxy-architecture/spec.md
tests/unit/test_proxy_http_bridge.py
```

Exact SHA-256 identities for these eight paths, seven adjacent frozen source/test/dependency inputs, and reviewed receipts are in `bridge-frozen-gates-r12.json`. Final registry `b96a8a5c19cd6e8c9e0e664f825f1309e6edaee301955c2d139ca12e50ee6dc2`; proxy unit `8c2917eb4be7f12b8c94554e3011905a9dfb6ecf8f2b655beabc5d3e9e469965`; Cargo.toml `39ba328c836a78adcfd547bb386d7a2b640317aaa568c2cca4c67081eebb8246`; Cargo.lock `6463b89c9abbc82ceb57edc1dedd60a2dc62c92f99178d90acc13a5d65a512c8` match the final-source receipt. `final-hashes.json` is explicitly a **pre-format** checkpoint: its registry/proxy-unit hashes are not the accepted final identity.

Image: `sha256:66e3d7b29b75ce4cd5b00f74e36222b75c0542c38bfc872f65c11aed6dee0e6a`, tag `codex-lb:bridge-r11-gates`. No new remote-head or lease readback was made here. Retained prior publication tuple: `git@github.com:Komzpa/codex-lb.git`, `refs/heads/fix/http-bridge-owner-io`, old `41111d4364012b21010b395769855b833343c32a`, published `7d1a5d2fddfa5d2786a03f1f78d39d2aed62c31d`, fork PR https://github.com/Komzpa/codex-lb/pull/2. That tuple is historical evidence, not a fresh future push precondition.

## Findings ordered by severity

### Publication gate: exact human authority was not recovered

The canonical parent archive is `/home/kom/.omp/agent/sessions/-Dropbox-Reemxy-tasks-loop/2026-10-26T12-49-13-076Z_01a17841-fd74-73dc-9cde-10b068d3daa0.jsonl`. Extracted all 21 `type=message`, `message.role=user` records, preserving `message.attribution=user`. None expressly authorizes publishing this bridge topic or the expanded eight-file R11 repair. Relevant exact human words:

- `a13b957d`, 2026-10-26T17:37:27.254Z: `[Image #1, 414x331] fix codex-lb too`.
- `d86151fa`, 2026-10-26T17:53:36.344Z: `заработал != починен!!!!`.
- `0c165a54`, 2026-10-26T20:06:02.440Z: `codex-lb keeps dying once in a while...`.
- `e0c45b8b`, 2026-10-27T08:51:34.382Z: `resume, we had power outage`.
- `0a55175e`, 2026-10-27T09:22:03.220Z: `what you need from me?`.

`history://PublishBridgeOwnershipCandidate:5` contains exact fork/ref publication instructions, but this is a **lead-authored worker brief**, not an independently recovered human instruction. `history://PublishBridgeOwnershipCandidateR2-2` claims that this brief was raw authority; that does not establish human provenance. `history://PublishBridgeGateRepairsR6` and R10 prove prior action/receipts, not renewed authority. Equal local/remote OIDs cannot establish permission. Live Hindsight recall returned no grounded source for the requested authority. `history://Main/full` returned only compact history; the physical parent archive was therefore inspected directly. No claim is made that no authority exists anywhere outside these inspected sources.

**Remaining gate:** lead must bind an actual raw human authorization to this final artifact and publication scope before dispatching a publisher. Current assignment itself prohibits publication. The candidate stays intact; no source rollback or approval request was issued by this lane.

### Publication scope: CHANGELOG and newly expanded paths need explicit reconciliation

`AGENTS.md:Documentation & Release Notes` forbids direct CHANGELOG edits; the original worker publication brief also excluded CHANGELOG. R11's lead brief explicitly requested a changelog update, and current CHANGELOG includes a new Unreleased section. This review preserves that edit and does not decide that a worker instruction supplies human public authority. Cargo.toml/Cargo.lock and the architecture allowance deletion are also outside the original sixteen-file publication surface. A publisher must use the final eight-path manifest only after authority/scope reconciliation; do not silently omit those paths, use a historical seven/sixteen-path manifest, include `verify-out/`, or treat a no-findings historical review as approval of this new delta.

## Accepted retained proof; no reruns

| Surface | Exact retained evidence | Conclusion and limit |
|---|---|---|
| Final formatted bridge source | `final-source-receipt.json`, source-test PID 2979145; actual terminal tool-result `2d0cc4fa` in R11 raw transcript | **1456 passed**, 8 warnings, 127.34s, exit 0 across complete integration/lifecycle/proxy-unit/timing-oracle files; following Ruff check/format, architecture, cancellation, timing and ty outputs all green. This supersedes the pre-format result. |
| Real native consumers | `final-source-receipt.json`, native PID 3019340, explicit absolute CODEX_LB_NATIVE_EGRESS_TEST_BINARY; raw async-result `d45de1cd`, R11 transcript line 292 | **361 passed**, 1 warning, 13.26s, completed. Earlier PID 2930285 (`final-4.log`: 11 passed/350 skipped) is NOT native wire proof; the actual bound-binary run replaces it. |
| Six RustSec findings | `dependency-diff.json`, `final-receipt.json`, `final-0.log` ending `advisories ok, bans ok, licenses ok, sources ok`; cargo-deny PID 2920756 exit 0 | RUSTSEC-2026-0382/-0386/-0391/-0398/-0403/-0410 cleared. Eight package versions changed: webpki .103.15→.103.16; Tokio 1.49.0→1.51.6; macros 2.6.1→2.7.2; codecs .4.38→.4.40; core .4.32→.4.34; zstd .13.3→.14.3; safe 7.2.4→8.2.0; sys 2.0.16→2.1.2. Clippy PID 2920885, workspace tests 2925581, rebuilt helper 2930272 all exit 0. Python manifest/lock remain frozen. |
| Actual Docker/security gate | `image-receipt.json`, `image-0.log` final export, `image-1.log`, `image-2.log`, actual `trivy-image.json` | Docker native release build PID 3045997 exit 0; unchanged HIGH/CRITICAL, ignore-unfixed Trivy PID 3055658 exit 0; inspect PID 3056319 same image. Zero selected Debian/Python findings. **No Rust-package scan result**: Rust clearance comes from cargo-deny, not Trivy. No container-runtime test implied. |
| Normative proof and negative control | `final-receipt.json`, `final-12.log` (67 passed), `final-13.log`; raw-wait control PID 2877688 in final-source receipt | Strict specs/change exit 0. Restoring raw asyncio.wait_for process-locally fails the same real close-all consumer at its completion guard; original source was untouched. This is a diagnostic negative control, not a new production deadline. |

R11 raw transcript: `/home/kom/.omp/agent/sessions/-Dropbox-Reemxy-tasks-loop/2026-10-26T12-49-13-076Z_01a17841-fd74-73dc-9cde-10b068d3daa0/RepairBridgePublishedGateFamiliesR11.jsonl`. Relevant actual native/final-source terminal records are also copied into the durable JSON receipt so they do not depend on a short chat summary.

## Production entry → wiring → consumer clause map

| Authored clause | Actual production wiring inspected | Consumer/negative control and evidence boundary |
|---|---|---|
| Registry available through request-owned execute/commit/rollback/close; no detached renewal/new deadline | `streaming.py:2485,2785` → `_HTTPBridgeMixin._get_or_create_http_bridge_session`; `mixin.py:444-505` does renewal/membership/endpoint I/O before lookup lock at 549; `helpers.py:3203-3224` returns typed renewal receipt | Integration `test_http_bridge_reuse_db_cancellation_leaves_registry_available` at 13014 exercises both canonical/previous-response and execute/commit/rollback. Real fenced UPDATE/commit plus held rollback/close; unrelated admission/alias removal finish **before** release (13120-13143). Included in final 1456. SQLite proves availability/ownership, not PostgreSQL latency or original incident cause. Historical controls in existing context are retained, not newly rerun. |
| Immutable generation/account/transport/alias/inflight/reservation revalidation; stale routing ignored; creation waiter reselects | `mixin.py:549-582` context comparison and verdict application; `704-743` prune/eligibility invalidation; previous-response capture at 1206-1210; `helpers.py:3227-3286` immutable match and fenced verdict; reconciliation at 3289-3350 checks row/epoch/session | Integration delayed foreign renewal 12649 (409, single close, durable successor preserved); late replacement 12691; previous-response eligibility 12760 (quarantine/retire rejected; eligible churn remains usable); alias retarget 12803; held membership/endpoint matrix 12908 (session/alias/inflight, pre-release unrelated progress, stale endpoint error loses to current winner). Final whole-file pass covers these real selection consumers. |
| 409 foreign-generation fence; ordinary durable error/missing row 502; identity-free fallback distinct; recovery fail-closed; same-process epoch adoption; reconciliation stale snapshots ignored | `helpers.py:3231-3271` matches immutable snapshot, registered identity, deliberate missing identity, error/missing-row, row/account/process/epoch predicates; snapshot class 2056; reconciliation capture/apply 3300-3332 | Lifecycle tests at 4500 (foreign), 4541 (owned), 4571 (recovery outage), 4607 (ordinary error/missing), 4628 (superseded reconciliation), neighboring epoch/cleanup tests in full final file. No measured PG-driver cancellation budget follows from these assertions. |
| Drain uses owner scheduler and retains shielded closes after timeout | `app/main.py:295-300` → `ProxyService` (`service.py:919-932`) → `_HTTPBridgeMixin` (`mixin.py:238-240`) → registry `close_all_http_bridge_sessions:284-328` → drain `113-139`, `scheduler_for(self).wait_for` at 126. `clock.py:135` is real asyncio.wait_for alias | Unit `test_close_all_http_bridge_sessions_reports_background_cleanup_timeout:23101-23129` injects VirtualScheduler, advances existing timeout, asserts shutdown False and close still owned/pending, releases/awaits close, then drains successfully. Raw-wait control fails this same consumer. Final 1456 includes it. No ownership-I/O deadline or exception suppression added. |

The existing normative deltas in responses-api-compat and sticky-session-operations, their context, the current production seam, exhausted allowance removal and actual bound-binary proof embody the required retrospective. This lane added evidence only, not another product repair.

## Remaining acceptance and safe publication continuation

1. **Authority/scope:** raw human publication authorization for this final expanded artifact is unresolved; changelog policy/scope requires lead reconciliation. No commit of R11 exists. This blocks publication, not retention of local proof.
2. **Cloud:** retained run 40498949108 belongs to old published HEAD, not the unpublished repair. Dashboard 122171582695 and core shards 122171582731/122171582756/122171582905 were in progress at that single snapshot. Frontend type/tests/lint/build and Helm gates were skipped, not passes. R11 final head's remote CI/review/approval, actionable current-head CodeRabbit threads and mergeability remain unobserved. No current-head approval/merge claim.
3. **Runtime:** installed binary/container/service identity, actual request-path behavior after installation, deployment/rollback and live availability remain unproved. Source consumer and image build/security proof do not close these.
4. **Incident:** original readiness-silent freeze holder/stack and causal relationship remain UNKNOWN. Preserve the human correction `заработал != починен!!!!`; historical 1385 passes and this local 1456/361/image proof cannot close that incident.
5. **Database:** real PostgreSQL-driver cancellation and shielded teardown latency remain unmeasured. Published PostgreSQL suite success is not that latency experiment. No wall-clock transaction-cleanup guarantee is claimed.

After authority and scope are resolved, the existing publication owner can bind the final manifest, preserve identity/history, obtain a **fresh exact fork URL/full-ref lease**, publish only the reviewed named delta (never evidence), read back new remote/PR identity and reconcile that head's cloud/review gates. Do not push from this lane, reuse a stale lease, duplicate the PR, merge, deploy or close the parent on local greens.

## Process ownership / retrospective

Review ran only short read-only identity/diff/hash commands; recorded diff shell PID 73796 and hash PID 3145804. No owned jobs remain and no process was killed. R11's recorded PIDs completed; no stopping action was needed. The durable JSON creation records its own PID separately.

Retrospective: retain actual final terminal stdout when zero exit could hide skips; freeze post-format rather than pre-format identities; audit actual candidate job IDs before dependency refresh; trace production entry and concrete consumer, not only a helper; recover **human** provenance rather than promoting a worker brief or equal OIDs into public authority. These are preserved as explicit publication gates rather than premature parent closure.
