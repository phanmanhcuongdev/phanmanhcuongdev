# Phase 3: Database, Security, and Defense in Depth

## 1. Purpose

Turn database behavior, public exposure, identity, secrets, ACLs, application security, logs, and recovery into formally explained security evidence. This phase proves that security is a property of system design, not a scanner report at the end.

## 2. Mapping To Source-Of-Truth Roadmap

- Source quarter: Q3, Database, Security, and Defense in Depth.
- Secondary exam target: AWS SAA only if CCNA and CKA are complete or firmly controlled.
- Theme: Stop calling scanners security.
- School-heavy default: reduced but stricter deliverables, no AWS SAA unless gates are met.

## 3. Why This Phase Exists

After the network and runtime are understood, the next risk is bad assumptions about data, identity, public exposure, secret handling, and operational recovery. A system is not secure because ZAP, Trivy, CrowdSec, Tailscale, or a firewall exists. It is secure enough only when the trust boundaries, controls, logs, restore paths, and remaining risks are explicit.

## 4. Theory To Learn

Database reliability:

- relational model and normalization
- indexing, selectivity, query plan, table scan, index scan
- transaction, ACID, isolation levels, locks
- backup, restore, RTO, RPO, durability
- replication/failover as concepts where feasible

Security:

- CIA triad
- authentication vs authorization
- least privilege
- credential lifecycle and secret rotation
- public exposure minimization
- threat modeling and data flow diagrams
- defense in depth
- trust boundary and break-glass access
- audit log integrity and incident response
- vulnerability management as a process, not tool output

## 5. Practical Labs

### Lab 1: Data And Trust Boundary Model

Choose the default real path:

`public client -> reverse proxy -> Spring Boot backend -> RabbitMQ -> FastAPI worker -> database/object storage`

Also model the admin path:

`admin workstation -> Tailscale/Headscale -> SSH/API -> service or host`

Document:

```text
Assets:
Actors:
Entry points:
Public ports:
Private/admin paths:
Trust boundaries:
Authentication points:
Authorization points:
Secrets involved:
Logs produced:
Data stores:
Backup/restore owner:
Failure domains:
Break-glass path:
```

### Lab 2: Database Exposure And Least Privilege

For SQL Server or PostgreSQL, prove:

- which interface/port the DB listens on
- which network paths can reach it
- which users/roles exist
- what grants each app user has
- whether admin credentials are separated from app credentials
- whether backup/restore can be performed without over-privileging the app

Evidence examples:

```text
ss -lntup
nmap -sV -p <db-port> <target>
psql privilege queries or SQL Server role/grant queries
firewall/ACL excerpts
application connection failure/success logs
```

### Lab 3: Backup And Restore Drill

Run a real restore test for one database or object store dataset. Measure:

- backup command/output
- restore command/output
- RTO
- RPO
- row/object count before and after
- application behavior after restore
- missing dependency or permission issue

### Lab 4: Web App Security Baseline

Run a controlled OWASP ZAP scan against a test environment. Treat the report as evidence, not truth by itself. Correlate findings with:

- application logs
- reverse proxy logs
- rate-limit or ban behavior
- authentication/authorization boundary
- false positives and accepted risks

### Lab 5: CrowdSec And Public Exposure Case

Use the ZAP/CrowdSec/Tailscale case to explain layered controls:

- public scan or abusive behavior
- CrowdSec decision or ban event
- whether public access is blocked
- whether Tailscale/Headscale admin path still works
- why that is both useful and risky
- policy recommendation for public vs private access

### Lab 6: Secret Handling Drill

Use a fake secret only. Prove:

- how it would be detected if a scanner already exists
- why removal is not enough
- what rotation means
- how to prevent recurrence with review, config structure, and least privilege

Trivy may be used as pipeline or filesystem evidence if already available or justified, but it is not the learning objective.

## 6. Evidence Required

Each Phase 3 lab must include:

- data flow or trust boundary diagram where relevant
- config excerpt with secrets redacted
- logs or scan output
- DB grants/roles or query plan where relevant
- backup/restore transcript where relevant
- public exposure proof such as `nmap` or firewall/ACL output
- root cause or risk analysis
- remediation plan
- formal concept mapping

Required Phase 3 artifacts:

1. `defense-in-depth-case-study.md`
2. Database lab report: transaction isolation, indexing, backup/restore, or replication/failover where feasible
3. Threat model for `student-feedback-system`
4. Data flow diagram with trust boundaries
5. Security ADRs: secret handling, admin access path, network ACL policy, audit logging policy
6. Up to 6 security failure reports if school load allows
7. AWS SAA decision checkpoint only after CCNA and CKA are complete or nearly complete

School-heavy reduced deliverables:

1. Polished `defense-in-depth-case-study.md`
2. One database lab report, not four
3. One school-integrated architecture package: C4 Context, C4 Container, UML sequence, written course mapping
4. Maximum two failure reports, both high quality
5. One software project risk register
6. No AWS SAA unless CCNA and CKA are passed, no course is at risk, and weekly school backlog is empty

## 7. Failure Scenarios To Trigger Or Analyze

### Q3-FI-01: ZAP Scan And Layered Defense

Run a controlled scan against a test environment until rate limiting or ban logic triggers. Measure ZAP report, app logs, reverse proxy logs, CrowdSec decisions, source IP classification, and Tailscale source identity. Explain defense in depth, trust boundary, fail-safe/fail-open, and break-glass access.

### Q3-FI-02: Database Isolation Anomaly

Create concurrent transactions that demonstrate one anomaly. Measure SQL output, timing, lock behavior, and transaction settings. Explain ACID, isolation level, and concurrency control.

### Q3-FI-03: Missing Index Under Load

Remove or avoid a useful index in a test query path. Measure query plan, latency, CPU/disk impact, and available metrics. Add the index back and compare. Explain selectivity, scan type, and cost.

### Q3-FI-04: Secret Exposure Drill

Place a fake secret in a controlled local file or branch. Measure detection if tooling already exists, review process, blast radius, removal, fake rotation, and prevention. Explain credential lifecycle and incident response.

### Q3-FI-05: Backup Restore Failure

Simulate backup corruption or missing restore dependency. Measure restore logs, RTO, RPO, and consistency. Fix the procedure and document why backup is not real until restore is tested.

### Q3-FI-06: DB Public Exposure Regression

Intentionally expose a test DB port to the wrong network segment, then prove reachability with `nmap` and connection attempts. Restore the firewall/ACL and prove denial. Explain least privilege and public exposure policy.

### Q3-FI-07: Tailscale/Headscale ACL Regression

Over-permit one test identity in ACL. Prove which resource becomes reachable, restore policy, and add verification commands. Explain identity source and overlay trust surface.

## 8. Review Checklist

- Did I define assets, actors, trust boundaries, and data stores?
- Did I prove which ports are public and which are private?
- Did I separate authentication from authorization?
- Did I show least privilege with DB grants, ACLs, or service identity evidence?
- Did I treat ZAP/Trivy/CrowdSec output as evidence instead of final truth?
- Did I prove backup by restoring?
- Did I document break-glass access intentionally?
- Did I preserve logs that distinguish public attacker behavior from private admin access?

## 9. Portfolio Artifact

Create `defense-in-depth-case-study.md` with:

- system context and data flow diagram
- public path and private/admin path
- ZAP/CrowdSec/Tailscale evidence
- DB exposure and least-privilege evidence
- backup/restore evidence
- security ADR links
- remediation plan
- remaining risks

This should become one of the strongest Q4 portfolio candidates.

## 10. Exit Criteria

Phase 3 is complete when a reviewer can answer:

- what the protected asset is
- where trust boundaries are
- which layer owns each control
- how public access differs from private overlay access
- what database behavior was proven
- what evidence proves the control worked
- what risk remains

## 11. Anti-Tool-Sprawl Guardrails

- Do not turn Phase 3 into a CI/CD product rollout.
- ZAP, Trivy, CrowdSec, Tailscale, and Headscale are evidence sources only when they answer a specific question.
- Do not add Vault, SIEM, SAST, SCA, or new scanners unless the source roadmap gate or ADR approves it.
- Prefer one polished trust-boundary case study over six shallow scanner reports.
