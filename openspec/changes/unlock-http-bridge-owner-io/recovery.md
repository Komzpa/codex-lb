# Power-outage recovery checkpoint

Recovered implementation without source mutation. HEAD is e0a340190ebb4258e3c9fe8c01bbe975dfba1b84; absolute Git common directory is /home/kom/proj/ai_pr/codex-lb-freeze-repro-20261026/.git. No fetch, Git mutation, publication, installation or live mutation performed.

Recovered changed tracked paths: CHANGELOG.md; four http_bridge modules helpers.py, mixin.py, protocol.py, session_registry.py; responses-api-compat and sticky-session-operations normative specs; integration/test_http_responses_bridge.py; unit/test_bridge_ring_lifecycle.py; unit/test_proxy_http_bridge.py. Existing untracked OpenSpec change directory preserved.

SHA-256 at recovery:

```
5a45118c85f6588d76bfe35abc3ee696763c0d49e58af75dcccb9c5cfb1ff674 helpers.py
d85d69f7e51d91e36e6eab1e9417edf8655d2a103bbb0bd08dbbfeca9107909c mixin.py
769508c799e5213372e79be284db46cfca58f49b29bcc74c9719db214b92e846 protocol.py
de7429a099946d456716f99091cbdf4d55efb45c8f3af6e6fb75d51d2023e9df session_registry.py
6b8e430bc15c0e08f921772075760d396ca7d7a85614520ffc3ec011a0268216 test_http_responses_bridge.py
c26a69080d0986f218c0c04421fad24e99a5846e524f333fe6babfd4e01d6135 test_bridge_ring_lifecycle.py
423657fc6191f6398220b8ff75bd9868f99a22f103498be6d1bac75b0e1a57e0 test_proxy_http_bridge.py
```

Prior owner history recovered from ImplementBridgeRegistryHandoff.jsonl, not inferred from a summary. Its combined unfiltered three-file run PID 3840834 / bg_97 had reached 54% with four failure markers at its last recorded inspection. Final output is not yet recovered. Six real transaction-cancellation cases, eighteen renewal/replacement/reconciliation cases, and seven routing/alias cases have recorded passing targeted receipts; full-file acceptance remains open. Prior strict OpenSpec validation passed. Temporary negative-control script is absent from /tmp after reboot.

Retro: partial test progress is not a full-file receipt; preserve saved source and inspect durable runner output before repeating proof. No original incident-causality claim follows from this lock-boundary repair.

## Recovered terminal output and causal repairs

The predecessor's custom async-result message `d6436628` in `ImplementBridgeRegistryHandoff.jsonl` records the combined three-file PID 3840834 run ending after 3600 seconds, status failed, at 54% with four failure markers. There were not three successful full-file outputs to reuse: the surviving evidence is one incomplete combined owning-file run. Its terminal receipt was recovered before a missing full proof was started.

The first resumed owning-file run, PID 184833, used `-n 8 --dist=loadscope -v --tb=short --timeout=60` on all three owning files. It exposed completed-future fixture publication and retained routing snapshots that reset intentional fork selections. Once the causal fork repair was made and its targeted test passed, this obsolete loaded-source run and only its observed children were stopped with `kill 184833 185048 185052 185055 185059 185062 185065 185068 185075` (exit 0). Its terminal receipt is `artifact://4406`, exit 143; it is not passing acceptance evidence.

The next unfiltered run, PID 273124, used `-n 8 --dist=load -q --tb=short --timeout=30` on all three files. `artifact://4536` records **12 failed, 1453 passed**, exit 1. A read-only stack capture, `sudo -n /home/kom/.local/bin/py-spy dump --pid 273757` (exit 0), proved one worker looping through selection snapshot comparison in `test_get_or_create_http_bridge_session_preserves_verified_replay_kind_for_local_model_transition[previous_response_only]`. Only that worker was stopped with `kill 273757` (exit 0), allowing the controller to return the complete failure list; the reported worker crash was deliberately induced, not an unexplained process death. Unprivileged `py-spy dump --pid 273757` returned permission denied, exit 1.

Repairs after those receipts:

- Discard routing receipts on intentional fork/recovery key changes and when entering renewal. Otherwise the request's own selection transition looks like a concurrent mutation and can reset to the original key indefinitely.
- Previous-response renewal resumes the original consumer selection key, rather than accidentally converting the accepted previous-response candidate into canonical admission with different eligibility policy. Its alias/session snapshot is still revalidated before publication; delayed alias retarget and superseding epochs retain their consumer tests.
- The synthetic creator fixture now publishes its session and removes its inflight marker before completing the future, matching production publication. The owner callback accepts/asserts the canonical resolved ring. Account test doubles include the plan field consumed on reselection.
- Shutdown waiter proof waits for actual registry waiting instead of a single scheduling yield. Retained-owner tests account for the routing-snapshot pass while still rejecting spinning. Ring-gate tests await their request task even on negative-control failure.

Scoped candidate commands use `.venv/bin/python -m pytest -q --timeout=30 --tb=short`:

- PID 256231: forwarded prompt-cache fork (2 cases), published inflight recreation, ordinary unavailable durable reuse (4 cases): **7 passed**, exit 0.
- PID 381788: repaired previous-response/replay/waiter/fixture neighbors: **11 passed, 3 failed**, exit 1; remaining were previous-response consumer reselection, final canceled-marker pass count and an over-short idle-reader test timeout.
- PID 412248: stale previous-response recovery, canceled-marker waiter, previous-response alias retarget, all 6 real transaction cancellation cases and all 12 delayed receipt/replacement cases: **21 passed**, exit 0.

The idle-reader consumer has an existing approximately 60-second path. Diagnostic candidate PID 410958 with `--timeout=0` passed in **61.09 seconds**, exit 0 (`artifact://4595`). A diagnostic async-task dump through Python 3.14 `sys.remote_exec` inspected only that owned test process; it showed the replacement reader awaiting its fake transport, not a registry lock or database holder. Baseline PID 422521 with the restored baseline loader and `--timeout=30` also failed the test-runner deadline (exit 1), so the 30-second full-run failure is not evidence of a new production timeout defect. Final full-file proof uses a 120-second test-runner diagnostic deadline, not any production ownership deadline.

## Fail-before and negative controls

Controls are process-local import/monkeypatch changes; no source or Git metadata is switched. The baseline loader reads the four bridge modules with `git show e0a340190ebb4258e3c9fe8c01bbe975dfba1b84:<path>`. The temporary script SHA-256 after adding the ring control was `30268cbc7518f4103bafaf4946f34da0bf4eee21ccc7a620ac1fbe45bb0aeeef`.

Commands below start with `.venv/bin/python /tmp/codex_lb_bridge_controls_20261027.py`, followed by mode and selector, with `--tb=short`; the script invokes pytest with `-q --timeout=30`:

| PID | Mode and exact selector | Result |
|---|---|---|
| 232364 | `baseline tests/integration/test_http_responses_bridge.py::test_v1_responses_http_bridge_reused_unanchored_refresh_reserves_canonical_handoff` | exit 1, but NOT behavioral fail-before: the candidate mock expects the new snapshot interface and base passed a session. Rejected as proof. |
| 235281 | `baseline tests/integration/test_http_responses_bridge.py::test_http_bridge_reuse_db_cancellation_leaves_registry_available[execute-canonical]` | exit 1 at unrelated registry progress while real rollback cleanup remained gated. This is the causal base failure. |
| 235282 | `fail-open tests/unit/test_bridge_ring_lifecycle.py::test_ordinary_durable_renewal_unavailable_fails_closed` | 2 passed, exit 0; NOT a valid negative control because the test imported a direct function reference before replacement. Replaced by the real consumer control below. |
| 249420 | `locked-renewal tests/integration/test_http_responses_bridge.py::test_http_bridge_reuse_db_cancellation_leaves_registry_available[execute-canonical]` | exit 1 at pre-release unrelated-progress assertion, restoring only the lock-around-renewal defect. |
| 249424 | `fail-open tests/integration/test_http_responses_bridge.py::test_http_bridge_durable_reuse_unavailable_fails_closed` | 4 expected failures, exit 1: both consumers incorrectly return on exception/missing receipt when fail-open behavior is restored. |
| 261760 | `locked-ring tests/integration/test_http_responses_bridge.py::test_http_bridge_ring_reads_leave_registry_available[session-membership]` | exit 1 at pre-release unrelated-progress assertion when membership observation holds the registry lock. |

The locked-renewal control wraps the existing refresh call in `async with self._http_bridge_lock`. The fail-open control returns the renewal snapshot on missing lookup/error in the actual consumer's verdict-application function. The locked-ring control uses a task-local ContextVar to identify the real lookup service and holds its registry lock around the canonical membership call. No control changes production files.

## Frozen final proof

PID 437887 / bg_43 executed exactly:

```
.venv/bin/python -m pytest -n 8 --dist=load -q --tb=short --timeout=120 --junitxml=/home/kom/Dropbox/Reemxy/tasks-loop/local/bridge-lock-full-owning-20261027.xml tests/integration/test_http_responses_bridge.py tests/unit/test_bridge_ring_lifecycle.py tests/unit/test_proxy_http_bridge.py
```

Terminal receipt: **1465 passed, 8 warnings in 126.22 seconds; exit 0**, wall time 129.56 seconds. No source/test edits occurred during this run. JUnit contains **229** integration cases, **89** lifecycle-unit cases and **1147** proxy-unit cases, with zero failures and errors. JUnit SHA-256: `93cc94ae3223ae420b945c1c487b42ebbb38a800e21ccdc09563053ac83be87e`. `openspec validate --specs --strict && openspec validate unlock-http-bridge-owner-io --strict` returned exit 0: 68 specs passed and this change is valid.

Final exact-input controls repeated after source freeze: locked renewal PID **483775** and locked ring PID **483773** each exit 1 at the required progress assertion before gate release. Fail-open PID **483774** exits 1 with four `DID NOT RAISE ProxyResponseError` consumer failures. The deliberately locked-renewal run additionally emitted an aiosqlite worker warning during teardown of the injected failure; the passing full candidate run had only the eight reported Starlette deprecation warnings. Controls never changed checkout source. All four owned temporary control/diagnostic scripts were removed after their results were recorded. All lane-owned test processes have returned terminal receipts or were stopped by the exact PID commands recorded above; no lane-owned service was started.

## Final frozen input SHA-256

Paths below are relative to ROOT, except the named external JUnit artifact above. HEAD remains the read-only observed base **e0a340190ebb4258e3c9fe8c01bbe975dfba1b84**; the implementation is intentionally uncommitted and is identified by these exact file bytes, not misrepresented as that base commit.

```
5a45118c85f6588d76bfe35abc3ee696763c0d49e58af75dcccb9c5cfb1ff674 app/modules/proxy/_service/http_bridge/helpers.py
f698e021d37a654ff38371846760af2584f8624aca15a3de29a2edf069780ff6 app/modules/proxy/_service/http_bridge/mixin.py
769508c799e5213372e79be284db46cfca58f49b29bcc74c9719db214b92e846 app/modules/proxy/_service/http_bridge/protocol.py
de7429a099946d456716f99091cbdf4d55efb45c8f3af6e6fb75d51d2023e9df app/modules/proxy/_service/http_bridge/session_registry.py
753ffd7a9af80c5067b9f46c516ef492015853f9f29e0eed6dcd2293e131b4ba tests/integration/test_http_responses_bridge.py
c26a69080d0986f218c0c04421fad24e99a5846e524f333fe6babfd4e01d6135 tests/unit/test_bridge_ring_lifecycle.py
1a810bbf3bd72d5364f33a114da7df2173f6dbc148f7eb0cdc2a914a5e2e064a tests/unit/test_proxy_http_bridge.py
cfc850c6c93b194ff267b50c35081650cf674a7e5670ee0d554d1189eef89f2e openspec/specs/responses-api-compat/spec.md
3befa65d98ff540f654804137f561c1a11dd82a123d067057cf6adb47918ff26 openspec/specs/sticky-session-operations/spec.md
b4cbd874806bbd8b34c2e6e0ad44d47f7c6f8209771402367b59bc47427c33b5 CHANGELOG.md
```

## Acceptance mapping and residual

| Contract | Production entry and wiring | Behavioral proof |
|---|---|---|
| Both durable reuse consumers; immutable identity/alias/reservation; foreign fail closed | `mixin.py::_get_or_create_http_bridge_session` selects/snapshots, awaits the registry mixin's refresh outside the lock, then applies the typed helper receipt under locked selection. Previous-response acceptance resumes its original consumer. | Both reuse paths in foreign-owner, ordinary error/missing, alias retarget, same-object epoch and replacement matrices; all executed by the full integration file. Existing unit adoption/process/account controls passed in the full proxy file. |
| Membership/endpoint I/O outside global lock and stale routing discarded | Unlocked routing resolves one ring, derives owner from that ring, and resolves endpoint before locked snapshot comparison. Intentional fork/recovery transitions invalidate their obsolete receipt. | Six membership/endpoint × session/alias/inflight races complete unrelated admission and alias unregister before release, including stale endpoint failure; full unit file preserves no-ring local reuse, hard-continuity failure and live-DRAINING authority. Locked-ring control fails the pre-release assertion. |
| Cancellation-safe execute/commit/rollback; unrelated progress; owned reservation and cleanup | Immutable refresh inputs flow into the unchanged coordinator, independent AsyncSession, fenced repository transaction and canonical close-session teardown. Reservation cleanup uses cancellation-deferring original-session/request ownership; no renewal task is detached. | Six real file-backed SQLite cases cancel repeatedly while actual rollback/close is held; unrelated admission and alias unregister finish first; reservation clears and DB commit/noncommit outcomes are asserted after release. Base and locked-renewal control fail before release. |
| Reconciliation and resource ownership preserve successors | Helper sweep snapshots durable ID/epoch before I/O and checks both before expected-session detach; existing generation close owners retain capacity and resource ownership. | Old foreign sweep after epoch/replacement, late owned/foreign/error receipts, predecessor repeated close with successor durable epoch/aliases intact, and full lifecycle/proxy closure/capacity suites passed. |

Residual: original incident causality remains unknown; this is a separately proved registry-availability/ownership defect. Real PostgreSQL driver teardown timing is not exercised; the passing transaction matrix uses real file-backed SQLite. No new wall-clock cancellation guarantee is claimed. No Git publication, upstream action, installation, live mutation or manifest change occurred. Independent code review/publication/live incident acceptance remain outside this local assignment.

## Retro

- **Trigger:** implementation survived the outage, but the predecessor never obtained a complete owning-file receipt. Recovery found an actual failed 3600-second run, not inherited green proof.
- **Mistake corrected:** retaining routing snapshots across the request's own fork/recovery transition undid that transition; treating a previous-response candidate as a canonical selection changed its consuming policy. Both are fixed on the main selection path, not with deadlines or fallback success.
- **Evidence:** base and locked-renewal/ring controls fail while cleanup/membership remains held; fail-open controls fail both ordinary durable consumers. Final frozen full-file proof passes all 1465 cases. Mock-interface mismatch and an unintercepted helper reference were explicitly rejected as proof.
- **Operational repair:** inspect task/CPU ownership before stopping exact owned PIDs; distinguish the existing 60-second consumer path from an over-short test deadline. Partial progress, timeout markers and green targeted helpers are not full acceptance.
- **Carry-forward:** CF56 lost-owner recovery, CF59 exact-input gate, CF70 durable receipts/hashes and CF114 Retro are recorded here. The original readiness-silent incident remains separately unproved.
