# Phase 4: Production Discipline, Cloud Mapping, and Portfolio

## 1. Purpose

Package the year's evidence into credible engineering artifacts: case studies, architecture decisions, postmortems, runbooks, cloud mapping, GitHub/profile updates, and final review material. The goal is to become defensible on paper, not only capable in the terminal.

## 2. Mapping To Source-Of-Truth Roadmap

- Source quarter: Q4, Production Discipline, Cloud Mapping, and Portfolio.
- Optional exam target: AWS SAA.
- Theme: Become credible on paper, not just in the terminal.
- School-heavy default: consolidation, not expansion.

## 3. Why This Phase Exists

Good homelab work can still fail a senior review if evidence is scattered, diagrams are vague, postmortems are missing, and cloud mapping is just vocabulary. This phase turns raw work into readable proof: architecture, tradeoffs, packet paths, trust boundaries, failures, metrics, root causes, fixes, formal concepts, and remaining risks.

## 4. Theory To Learn

Production discipline:

- incident management
- postmortem quality
- runbook clarity
- recovery planning
- capacity and saturation
- change risk
- operational ownership

Software architecture:

- modularity
- coupling and cohesion
- ports and adapters
- C4 model
- UML sequence and component diagrams
- ADR discipline

Distributed systems and reliability:

- partial failure
- timeout and retry
- idempotency
- consistency
- dependency graph
- failure domain
- observability as evidence

Cloud mapping:

- VPC, subnet, security group, NACL
- IAM
- load balancer
- managed database
- object storage
- autoscaling
- monitoring
- cost and capacity tradeoffs

## 5. Practical Labs

### Lab 1: Evidence Index

Create a yearly evidence index:

```text
Artifact:
Type:
Phase:
Formal concept:
System touched:
Evidence level:
Reviewer concern:
Path:
Next action:
```

Use it to find weak or duplicate work before polishing.

### Lab 2: Architecture Whitepaper

Create `homelab-architecture-whitepaper.md` with:

- learning/business goal
- constraints
- physical and logical architecture
- packet/request paths
- trust boundaries
- security controls
- observability and evidence sources
- recovery plan
- tradeoffs
- remaining assumptions

### Lab 3: Case Study Packaging

Choose one primary public case study:

- hybrid homelab architecture case study
- secure deployment case study
- Headscale/Tailscale/VyOS defense-in-depth case
- `student-feedback-system` end-to-end case

Do not attempt three case studies during school-heavy mode.

### Lab 4: Incident/Postmortem Write-Up

Select one real incident or failure injection. Rewrite it to Level 3 or Level 4 quality with timeline, impact, detection, root cause, resolution, prevention, evidence, and runbook change.

### Lab 5: ADR Collection

Clean at least the important ADRs:

- admin access path
- secret handling
- network ACL policy
- audit logging policy
- backup/restore policy
- public exposure policy
- Kubernetes RBAC policy if Phase 2 completed

### Lab 6: Homelab-To-Cloud Mapping

Map local concepts to AWS only after local evidence exists:

| Homelab concept | AWS concept | Required local proof first |
| --- | --- | --- |
| VLAN/subnet | VPC subnet | route/subnet/VLAN diagram and packet path |
| firewall/ACL | Security Group/NACL | allow/deny evidence and ACL rule order |
| MinIO | S3 concept | object storage path and access policy |
| SQL Server/PostgreSQL | RDS concept | backup/restore and least privilege evidence |
| reverse proxy/ingress | ALB/NLB concept | request path and health behavior |
| Tailscale/Headscale | private connectivity and identity-aware access | ACL and identity evidence |
| Grafana/InfluxDB | CloudWatch/managed observability concept | metric/log evidence used in a real investigation |

### Lab 7: GitHub/Profile Polish

Update only evidence-backed claims:

- profile README
- top 3-5 repos depending on school-heavy mode
- diagrams linked from repos
- postmortems or case studies linked where safe
- claims tied to artifacts, not tool badges

## 6. Evidence Required

Each Phase 4 artifact must include:

- source evidence links or paths
- diagrams where useful
- tradeoffs
- risks
- operational notes
- remaining assumptions
- reviewer questions answered

Full Phase 4 deliverables:

1. Public portfolio update
2. `homelab-architecture-whitepaper.md`
3. At least 12 postmortems total across the year
4. At least 20 lab reports total across the year
5. At least 12 ADRs total across the year
6. One polished case study
7. AWS SAA attempt only if Q1-Q3 gates are satisfied

Reduced school-heavy deliverables:

1. Finish school deliverables with formal diagrams and terminology
2. Complete one polished public case study, not three
3. Bring yearly evidence to at least 8 postmortems, 12 lab reports, 8 ADRs
4. Update only top 3 repos, not top 5
5. Finish CCNA or CKA before AWS SAA if either is unfinished
6. AWS SAA may enter active study only after the last major school deadline

## 7. Failure Scenarios To Trigger Or Analyze

### Q4-FI-01: Full Request Path Failure

Introduce one failure in each layer across separate test runs: DNS, ingress/reverse proxy, service routing, backend config, queue, database, object storage. Measure user-facing error, logs, metrics, packet path, and restore steps. Document blast radius and detection path.

### Q4-FI-02: Capacity Pressure

Generate controlled load until one bottleneck appears. Measure CPU, memory, disk I/O, database latency, queue depth, and application latency. Explain utilization, saturation, and capacity limit. Do not spend the semester building a load-testing platform.

### Q4-FI-03: Access Control Regression

Over-permit a non-admin identity in a test ACL/RBAC policy. Measure what becomes reachable, logs, and policy diff. Restore least privilege and add verification checklist.

### Q4-FI-04: Restore Under Pressure

Restore one service or dataset from documented runbook. Measure time to detect, time to restore, missing steps, and data consistency. Update runbook.

## 8. Review Checklist

- Can a reviewer follow evidence from claim to file/path/log/diagram?
- Does each case study include architecture, tradeoffs, failure, metric, root cause, fix, and remaining risk?
- Are tool names secondary to system behavior?
- Are postmortems honest about what was not proven?
- Are ADRs tied to real decisions, not invented ceremony?
- Does cloud mapping depend on local proof first?
- Does GitHub/profile wording avoid claims that are not backed by artifacts?

## 9. Portfolio Artifact

Create or polish these concrete outputs:

- hybrid homelab architecture case study
- secure deployment or defense-in-depth case study
- one incident/postmortem write-up
- ADR collection
- `homelab-to-cloud-mapping.md`
- `homelab-architecture-whitepaper.md`
- GitHub profile/repo README updates backed by evidence

## 10. Exit Criteria

Phase 4 is complete when the portfolio can support a senior panel discussion without relying on tool names. The answer must show:

- architecture
- tradeoffs
- packet/request path
- trust boundary
- injected or analyzed failure
- metric/log/packet evidence
- root cause
- fix
- formal concept
- remaining risk

AWS SAA starts only if:

- CCNA is passed
- CKA is passed, not merely planned
- Q1-Q3 deliverables exist
- August-December school load is stable and no course is at risk
- homelab concepts can be mapped to AWS without hand-waving

## 11. Anti-Tool-Sprawl Guardrails

- Q4 is consolidation first, expansion second.
- Do not add AWS work to compensate for weak local fundamentals.
- Do not polish portfolio at the cost of final exams.
- Do not add new observability or SIEM tooling just to look production-like; use existing evidence unless a specific gap is documented by ADR.
- One case study that survives senior review beats many shallow repo updates.
