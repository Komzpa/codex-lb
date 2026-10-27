# Registry ownership I/O: implementation evidence and retrospective

## Scope and identity

Checkout: `/home/kom/proj/ai_pr/codex-lb-freeze-repro-20261026`.
Fresh initial `git rev-parse HEAD` returned `e0a340190ebb4258e3c9fe8c01bbe975dfba1b84`.
The same command's `git status --short`, `git diff --stat`, and the four bridge modules' `git diff --exit-code e0a340190ebb4258e3c9fe8c01bbe975dfba1b84 -- ...` produced no changes, exit 0. No pre-existing foreign changes were present in that observation. No Git metadata, commit, push, deployment or installation is part of this work. The rejected `fff23edea911a3096a6284507ca1e14b3fa8eadb` timeout patch was not reapplied.

Inputs read: the entire 129-line durable `bridge-lock-handoff-20261027.md` and the complete surviving `history://ReviewCodexStallCandidate` rejection. The first change artifact was `proposal.md`, followed by the small immutable reconciliation identity fence before broad test execution.

## Ownership design and limits

The existing coordinator/repository/session teardown path remains canonical. An immutable renewal snapshot passes into that request-owned await; a typed renewal receipt returns to the registry selection owner. The caller revalidates aliases, slots, inflight identity, reservation and session inputs before applying a verdict or publishing reuse metadata. Both reuse consumers use that handoff. Creation waiters re-enter selection rather than publishing a creator future as an ownership receipt.

Routing resolves one active ring and selects its hash owner through the existing canonical owner helper using that resolved ring. Endpoint reads also run outside the lock. The locked routing phase rejects observations or errors whose session, alias or inflight context changed during suspension. Deliberate identity-free ordinary fallback is distinct from unavailable established durable verification. The narrow same-process, same-row/account epoch adoption exception is preserved.

The actual database proof uses file-backed SQLite through `SessionLocal`, the real coordinator and fenced repository UPDATE/commit, and canonical shielded rollback/close. Execute cancellation is gated after an actual UPDATE with an open transaction; commit cancellation is gated after actual commit (the write outcome is deliberately committed but verification remains unconfirmed); the rollback case raises after an actual UPDATE and cancels during canonical rollback. A held rollback/close gate must coexist with completed unrelated admission and alias unregister before release. This is not evidence about a real PostgreSQL driver's teardown latency, and no new wall-clock cancellation/cleanup guarantee is claimed.

Original incident causality remains **unknown**. The original blocked incident stack and holder are unavailable in the supplied evidence. An independent registry availability defect, DB recovery, backend death and the original readiness-silent incident are separate claims. This patch does not close the incident by itself.

## Observed proof before the complete-file run

All commands below used `.venv/bin/python -m pytest -q` with the listed selectors. Later commands print their actual Python PID before `os.execvp`; the first command printed shell PID 2710115, not an independently recorded Python PID.

| Command selectors | Result | Identity |
|---|---|---|
| Integration `test_v1_responses_http_bridge_reused_unanchored_refresh_reserves_canonical_handoff`, `test_v1_responses_http_bridge_cancellation_during_durable_refresh_releases_reservation`; lifecycle unit `test_fenced_out_renewal_evicts_local_session_and_raises_mismatch`, `test_owned_renewal_keeps_local_session_open`; proxy unit `test_renew_adopts_a_same_instance_epoch_advance_for_the_registered_session` | 5 passed, exit 0, 2.70s | shell PID 2710115 |
| Integration `test_http_bridge_reuse_db_cancellation_leaves_registry_available` (first gate draft) | one case reached pass; command exceeded 120s while fixture close hit the same test gate | shell PID 2710115; no acceptance claim |
| Same cancellation matrix after restricting the gate to the first renewal-owned AsyncSession | 6 passed, exit 0, 3.08s | PID 3764397 |
| Integration `test_http_bridge_delayed_foreign_renewal_rejects_stale_reuse`, `test_http_bridge_late_renewal_preserves_concurrent_replacement`; lifecycle unit `test_ordinary_durable_renewal_unavailable_fails_closed`, `test_reconcile_discards_superseded_foreign_snapshot` | 18 passed, exit 0, 7.28s | PID 3780668 |
| Integration `test_http_bridge_ring_reads_leave_registry_available`, `test_http_bridge_previous_response_alias_retarget_revalidates` | 7 passed, exit 0, 4.07s | PID 3817800 |

The full unfiltered owning run is `.venv/bin/python -m pytest -q --timeout=60 tests/integration/test_http_responses_bridge.py tests/unit/test_bridge_ring_lifecycle.py tests/unit/test_proxy_http_bridge.py`, PID 3840834. Its `--timeout` is a test-runner deadlock diagnostic, not a production renewal timeout. Acceptance remains open until that run and the targeted fail-before/negative controls are recorded below.

`openspec validate --specs --strict && openspec validate unlock-http-bridge-owner-io --strict`: exit 0; 68 specs passed and this change is valid.

## Retrospective promoted into the repair

1. The rejected five-second timeout bounded cancellation initiation, not shielded transaction teardown. The causal repair moves the complete owned await chain out of the registry critical section. The discriminating assertion requires unrelated work to complete **while cleanup is still held**, not after gate release.
2. An exception, missing row or incomplete commit acknowledgement is not ownership evidence. Established durable verification now fails closed; legitimate identity-free fallback remains separately covered. Foreign verdicts only condemn their captured generation.
3. Releasing a lock without immutable generation and alias/inflight revalidation would trade availability for stale serving or successor eviction. The receipt/application split, replacement/epoch/alias consumers and immutable reconciliation ID/epoch fence encode that lesson on the main path.
4. Test gates need their own ownership: the first cancellation test draft also gated fixture release and stalled. Restricting it to the renewal-owned session preserves real cleanup without blocking a later legitimate release. Every test-owned task is released and awaited.
5. CF2 stays tied to a real reuse consumer, CF26 to the exact clean base plus final source identity, and CF67 to an actual fail-before consumer receipt. Green helpers or restored service availability alone cannot substitute for those proofs.

## Final recovered acceptance

The power-outage continuation recovered the predecessor's actual incomplete 3600-second owning run before rerunning missing proof. Full causal recovery, failed intermediate receipts, exact commands, process ownership and final SHA-256 identities are recorded in [recovery.md](recovery.md).

Final frozen source/test proof: PID 437887, `.venv/bin/python -m pytest -n 8 --dist=load -q --tb=short --timeout=120 --junitxml=/home/kom/Dropbox/Reemxy/tasks-loop/local/bridge-lock-full-owning-20261027.xml tests/integration/test_http_responses_bridge.py tests/unit/test_bridge_ring_lifecycle.py tests/unit/test_proxy_http_bridge.py`: **1465 passed, 8 warnings in 126.22s**, exit 0. All files were unfiltered: 229 integration, 89 lifecycle-unit and 1147 proxy-unit cases. The 120-second option is exclusively a test-runner diagnostic; no production deadline was introduced.

Final exact-input negative controls: restoring locked renewal (PID 483775) and locked membership (PID 483773) each fails the pre-release unrelated-registry-progress assertion; restoring fail-open application (PID 483774) fails all four ordinary durable error/missing-row consumer cases. Each control exits 1 as expected and exists only in its own process. The baseline real transaction consumer fails the same progress assertion on e0a340190ebb4258e3c9fe8c01bbe975dfba1b84 (PID 235281). Candidate success and negative-control failures jointly establish the scoped defect, not incident causality.

Strict normative validation returned exit 0: 68 specs passed and `unlock-http-bridge-owner-io` is valid. No publication, installation, live service mutation or Git metadata change was performed. Original incident causality and real PostgreSQL driver teardown behavior remain unproved; no claim closes those separate questions.

## Selection revalidation follow-up

An accepted renewal does not authorize a session that is pruned or no longer eligible on the resumed selection pass. Discard that receipt and reselect; check the existing request deadline after ownership I/O and between retries, releasing only the original request's reservation before reporting budget exhaustion.

The anchored idle-TTL crossing and repeated snapshot churn are exercised through the selection consumer with real durable renewals. Process-local negative controls remove the respective safeguards and fail those same consumer cases; they do not modify the checkout.

## Prepared-main recut — 2026-10-27

The sections above and recovery.md describe the saved candidate, not current-main acceptance. PortBridgeContractOnMain recut only that candidate's staged ownership hunks into `/home/kom/proj/ai_pr/codex-lb-bridge-owner-main-20261027`, based on `72630bbfeee9e3b0d9acfb95e2b1e706b8b0188e`. The saved source `/home/kom/proj/ai_pr/codex-lb-freeze-repro-20261026` remains read-only at `e0a340190ebb4258e3c9fe8c01bbe975dfba1b84`.

Before the first write, absolute Git common-directory readbacks identified distinct ROOT/.git and SOURCE/.git directories. No index, branch, commit, push, deployment, updater or live-service mutation was performed. The first changed artifact was this saved OpenSpec change, applied before implementation. CHANGELOG.md was intentionally untouched, following AGENTS.md.

### Reconciliation findings and repair

- The saved implementation patch applied except two mixin hunks, one registry-import hunk, and five assertion hunks belonging to tests removed by intervening main. The expected `git apply --reject --verbose` exit was 1; its applicable hunks were retained and every generated reject was removed after reconciliation.
- Restored only the missing snapshot/receipt imports and the accepted-renewal post-prune invalidation. Main had removed an unused `requested_key`; selection revalidation now needs that immutable original key, so its local capture was restored without reviving main's removed affinity helpers or creation-owner machinery.
- The five obsolete retained-owner test assertion hunks were intentionally omitted: their test functions no longer exist on prepared main. No deleted tests, old synthesized-turn-state behavior or retired inflight architecture were resurrected. All surviving consumers and direct renewal tests use the new explicit receipt contract.
- Accepted renewal still requires the selected, registered and eligible session. TTL expiry discards the receipt and reselects. The original request deadline is checked between completed renewal, membership, owner-selection and endpoint operations and between reselections. Deadline/cancellation cleanup releases only the original request/session reservation. Database transaction teardown remains request-owned and awaited; no timeout worker or detached renewal was added.

### Fresh frozen-main evidence

All paths below are under `/home/kom/Dropbox/Reemxy/tasks-loop/local/` and use prefix `bridge-owner-main-20261027-`. Each log records the exact command, actual child PID and terminal exit. JSON receipts contain exact argument arrays, log paths and SHA-256 values. No source or test changed during or after the complete owning-file run.

| Proof | Actual PID | Terminal result | Full log suffix |
|---|---:|---|---|
| Prepared-main baseline, actual execute cancellation with held teardown | 1659009 | exit 1: unrelated admission/alias removal cannot finish before gate release | baseline-lock.log |
| Prepared-main baseline, ordinary durable error/missing row, both consumers | 1663646 | exit 1: four `DID NOT RAISE ProxyResponseError` failures | baseline-fail-open.log |
| Remove accepted-renewal eligibility/prune safeguards process-locally | 1645164 | exit 1: anchored TTL consumer reaches stale routing assertion | ttl.log |
| Remove original-deadline checks process-locally | 1645975 | exit 1: repeated churn exceeds the consumer's two-second test guard | deadline.log |
| Put only renewal back under the registry lock process-locally | 1647222 | exit 1: pre-release unrelated-progress wait fails | locked-renewal.log |
| Restore fail-open receipt application process-locally | 1648797 | exit 1: four ordinary durable consumer failures | fail-open.log |
| Complete unfiltered owning integration and both unit files | 1648728 | exit 0: **1382 passed, 8 warnings in 111.24 seconds** | full.log; full.xml |
| `openspec validate --specs --strict` | 1675048 | exit 0: **67 passed, 0 failed** | specs.log |
| `openspec validate unlock-http-bridge-owner-io --strict` | 1675108 | exit 0: change valid | change.log |

The full command was `.venv/bin/python -m pytest -q --tb=short --timeout=120 -n 8 --dist=load --junitxml=/home/kom/Dropbox/Reemxy/tasks-loop/local/bridge-owner-main-20261027-full.xml tests/integration/test_http_responses_bridge.py tests/unit/test_bridge_ring_lifecycle.py tests/unit/test_proxy_http_bridge.py`. JUnit records 229 integration, 89 lifecycle-unit and 1064 proxy-unit cases, zero failures and errors. These are current-main counts, not the historical candidate's 1467 tests or 68 specs. The eight warnings are the existing Starlette BlockingPortal deprecation. The 120-second option is only the test runner's diagnostic deadline.

Before freeze, the targeted TTL, churn, ordinary unavailable and six transaction-cancellation consumers passed together: 12 passed, 217 deselected, exit 0. The full run also supplies their pass-after and neighboring owned-reuse, no-ring, epoch/process/account, creation, teardown, alias and live-DRAINING negative-control coverage. Baseline loading used `git show 72630bbfeee9e3b0d9acfb95e2b1e706b8b0188e:<path>` for the four bridge owners in memory; negative controls altered only the test process. Injected lock-failure logs include canonical SQLite teardown warning output, not warnings from the passing full run. All owned children returned terminal results; none required stopping.

Receipts: baseline-receipt.json, controls-receipt.json, full-receipt.json and spec-receipt.json. The complete full log SHA-256 is `9905e30deea76d7c7892a4431a9e76e59e10d7dc841d83af6291f346eaebdad5`.

### Own retrospective and narrow handoff

The earlier refusal confused an already requested ownership contract with an unauthorized new public design change. This recut had explicit authorization for the saved 409/502 contract; it did not invent a different contract. The earlier applicability failure was evidence to reconcile individual hunks, not permission to copy merged historical files. Preserving main's deleted tests and architecture required dropping their now-inapplicable test hunks, while restoring only the original-key capture actually needed by the new selection loop. Those lessons are embodied in the narrow patch, the distinct-root check, the behavioral baseline controls and fresh complete-main proof rather than a historical green count.

Authorized Git handoff is limited to four bridge modules, the three owning test files, the two normative specs and the seven existing files beneath `openspec/changes/unlock-http-bridge-owner-io/`. Do not include CHANGELOG.md, test environments, proof logs, temporary scripts, other topics or anything from SOURCE's Git metadata. This lane does not authorize push, publication, deployment or updater execution. Independent review/publication remain the lead's boundary. Real PostgreSQL-driver teardown latency and original incident causality remain unproved; no new wall-clock cancellation guarantee is claimed.

### Previous-response eligibility review repair

The independent review identified a gap in the prepared-main candidate: a fresh snapshot after a held renewal could still select a session newly quarantined or marked to retire after drain. The canonical lookup guard did not cover previous-response selection when its key differed from the requested key. Previous-response selection now uses the existing quarantine registry and request-reusability primitive while retaining its distinct continuity policy.

The real previous-response selection consumer held its first durable renewal while each transition was applied. Before the repair both ineligible cases failed with `DID NOT RAISE`; the still-eligible snapshot-churn control passed. After the repair those three cases and the neighboring alias-retarget continuity case passed (4 passed). The subsequent unfiltered three-file run passed 1385 tests, with eight existing deprecation warnings, and strict validation passed all 67 specs and the change. Test databases were disposable SQLite, not production. These observations do not establish incident causality or PostgreSQL cancellation latency.

Retro: snapshot freshness is not itself eligibility. Review every distinct consumer's reselection and publication guard, and distinguish an actually observed reviewer model from a requested model. The earlier automated review banner showed `gpt-6.1-sol` despite a requested Astra configuration; it is not evidence of an Astra review.

### Published-head CI repair

Registry cleanup, inflight failure/eviction and idle pruning now live in the existing session-registry mixin; inherited method names and the ownership receipt protocol are unchanged. This keeps the mixin within its existing architecture budget without raising limits or changing selection, cancellation, quarantine, retirement, alias-generation or original-deadline behavior.

The blocked-renewal fixture uses the real typed durable lookup, and optional database rows and mock await records are asserted present before inspection. Retro: use the existing responsibility boundary, not an architecture-limit increase or type suppression; retained 1385-test/67-spec evidence is historical identity, not renewed approval.

