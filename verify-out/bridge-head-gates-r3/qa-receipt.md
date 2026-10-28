# Bridge head gates R3

Result: FAIL with additional CI pending. Expected and observed head: 41111d4364012b21010b395769855b833343c32a. PR2 OPEN, ready, MERGEABLE/UNSTABLE. No approval waiver. Reviews 0; threads 0; both complete pagination. Check contexts 30, complete pagination. Required query exits 1: no required checks reported; this is not an approval.

CI run 40495930030: lint fails architecture limit (mixin.py 2560 lines > 2436); typecheck fails with 8 diagnostics. Full completed-failure logs retained, with all error lines in all-errors.txt. Pending exact jobs: unit 122161377344; integration-bridge 122161377351; integration-core-1 122161377606; Docker 122161377624; integration-core-2 122161377627; integration-core-3 122161377699; PostgreSQL 122161377702. No polling or CI reruns.

## Original acceptance map (retained review, not re-executed)
- Production entry/wiring: streaming.py:2485–2530 into mixin.py:550; canonical capture 884–892 and previous-response 1303–1309; session_registry.py:769–775 into helpers.py:3203–3225. Await occurs outside registry lock, then locked revalidation.
- Real consumers: independent Astra/high review retained 1385 passing cases, including six actual SQLite execute/commit/rollback cancellation cases across canonical and previous-response consumers; eligibility quarantine/retirement fail-before and pass-after controls. No PostgreSQL latency or incident-cause inference.
- Docs: responses-api-compat lines 3299–3347, sticky-session-operations 900–930, both delta specs and proposal/tasks/context/recovery reviewed. Retained strict specs: 67 passing.
- Narrow publication done: publication owner recorded exact 16-file manifest f2ab015ed9b4a3ede5379f7b150c12ba19d9991e37105e5ddb1e836bd13f1f9e, main base 72630bbfeee9e3b0d9acfb95e2b1e706b8b0188e, exact fork ref and ready PR2 at observed head. No Git metadata accessed in this gate.

## Retro
Simpler different way: one fresh head batch plus completed failed-job logs; no test rerun or repeated head polling. Initial GraphQL required-field query failed because pull-request context was missing; corrected by omitting that field and issuing dedicated required checks. Log collector then incorrectly decoded plain-text logs as JSON; raw logs were already saved, so resumed from saved job metadata only. These collector failures do not erase the real CI failures.

Changed only private evidence files. No source, forge writes, services, shared DB, deployment, fetch, or Git operations. Recorded final collector PID 2173724; earlier collector PID not captured. No process stopped. Remaining: fix two completed CI failures through authorized source owner, obtain completion of seven pending jobs, and retain review/merge acceptance gates. This snapshot does not prove final delivery.
