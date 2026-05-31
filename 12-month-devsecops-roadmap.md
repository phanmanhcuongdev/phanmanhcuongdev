# 12-Month DevSecOps Roadmap

Owner: Phan Manh Cuong  
Role target: Backend-to-DevSecOps / Platform Engineer  
Operating rule: No new tool collecting. Break -> Measure -> Fix -> Document.

## 0. Hard Constraints

This roadmap is not a motivational checklist. It is an engineering discipline
program. The goal is to turn hands-on homelab work into formally explainable
computer science, networking, operating systems, database, and distributed
systems knowledge.

### Non-Negotiable Rules

1. No new tools unless one of these conditions is met:
   - It is required by CCNA, CKA, or AWS SAA.
   - It replaces an existing tool and the old one is removed.
   - It is approved in writing through an ADR.
2. Every lab must produce evidence:
   - diagram
   - command transcript or summarized commands
   - metrics or packet capture
   - root cause
   - fix
   - postmortem or runbook update
3. Every week must map one practical experiment to one formal concept from:
   - computer networking
   - operating systems
   - database systems
   - distributed systems
   - software architecture
   - information security
4. If you cannot explain it with standard terms, you do not understand it well
   enough yet.
5. If a system works but you cannot prove why, it is not done.
6. If a system fails but you cannot reproduce the failure, it is not learned.

### Core Lab Stack

Use the existing lab only:

- Proxmox
- LXC and Ubuntu Server VMs
- VyOS
- Headscale and Tailscale
- Docker
- Portainer
- Spring Boot app
- FastAPI worker
- RabbitMQ
- MinIO
- SQL Server
- PostgreSQL
- Grafana and InfluxDB
- Ollama where already deployed
- Existing MikroTik/Cisco/router/switch equipment
- Existing Android/ESP32 projects only when they support the main roadmap

Do not add Kubernetes until the CKA phase requires it. Do not add extra
observability, security, service mesh, CI/CD, or cloud tools until the current
quarter allows them.

## 0.1. Calendar Overlay: August-December School-Heavy Mode

This roadmap must respect the real academic load from August to December 2026.
Assume 6-7 university courses, roughly 18-21 credits. That is not a side quest.
It is the main workload for that period.

PTIT semester-7 references for Information Systems commonly include courses
such as:

- Phan tich va thiet ke he thong thong tin
- Xu ly anh
- IOT va ung dung
- Quan ly du an phan mem
- Hoc phan tu chon chuyen nganh, often 6 credits

This is a reference, not a guarantee. The actual timetable wins. When the real
schedule is published, update this section and cut scope immediately.

### School-Heavy Operating Rule

From August 1 to December 31, 2026:

1. University GPA recovery has priority over optional homelab expansion.
2. No AWS SAA preparation unless CCNA and CKA are already passed and school
   grades are stable.
3. Homelab work is capped at 6-8 focused hours per week.
4. Certification work is capped at 4-6 focused hours per week unless an exam is
   already scheduled within 21 days.
5. Each school course must produce at least one artifact that also strengthens
   the DevSecOps roadmap.
6. Failure injection is reduced in frequency, not removed.
7. If a school assignment can be mapped to homelab evidence, do that. Do not
   create two separate workloads.

### Academic Risk Register

From August to December, maintain a weekly academic risk register.

Use this table:

| Course | Current risk | Next deadline | Required output | Roadmap mapping | Action this week |
|---|---|---|---|---|---|

Risk levels:

- Green: on track
- Yellow: unclear requirement, weak understanding, or deadline within 14 days
- Red: deadline within 7 days, missing group dependency, failed quiz/midterm, or
  unclear grading rubric

Rules:

1. If any course is Red, homelab failure injection is banned.
2. If two courses are Yellow, homelab work is documentation-only.
3. If three courses are Yellow, certification work drops to maintenance review.
4. If a group project depends on you, that deliverable outranks any optional
   lab.
5. The goal is not to "balance everything". The goal is to avoid silent
   academic debt.

### Course-to-Roadmap Mapping

Use school as a forcing function for formal language.

| School course | Roadmap artifact | Homelab anchor |
|---|---|---|
| Phan tich va thiet ke he thong thong tin | C4 Context, C4 Container, UML sequence, use-case model | `student-feedback-system` |
| Quan ly du an phan mem | WBS, risk register, milestone plan, retrospective | this roadmap and one selected repo |
| IOT va ung dung | lab report, sensor/API flow, threat boundary | ESP32/FaizGear only if required by course |
| Xu ly anh | formal report on preprocessing/model limits | `identity_number` or ESP32-CAM only if required |
| Distributed systems / cloud / service elective | failure-domain report, service dependency map | RabbitMQ, DB, K8s, Headscale |
| Data science / BI elective | data pipeline or metrics interpretation report | Grafana/InfluxDB, SQL/Postgres |
| Network/security elective | ACL, trust boundary, packet path report | VyOS, Headscale, CrowdSec case |

### School-Heavy Weekly Cadence

During August-December, replace the default weekly cadence with this:

- Monday: 45-minute theory mapping from one school lecture to one homelab
  concept.
- Tuesday or Wednesday: one 90-minute lab block, only if school deadlines are
  under control.
- Thursday: document evidence for either school or homelab.
- Friday: no new work; close notes, diagrams, and backlog.
- Saturday: 2-3 hours certification drill.
- Sunday: review grades, deadlines, and roadmap scope.

Hard rule: if two school deadlines are due within 7 days, all optional homelab
failure injection pauses. The only allowed technical work is documentation that
directly supports a school deliverable.

### Chaos Mode: Midterms, Finals, and Assignment Collisions

Reality will break the calendar. When PTIT midterms, finals, group projects, or
20-page documentation assignments collide with the roadmap, switch to Chaos
Mode immediately.

Chaos Mode triggers when any condition is true:

- two or more university deadlines fall within 7 days
- one exam is within 5 days
- sleep drops below 6 hours for two consecutive nights
- a lab failure remains unresolved after 2 hours
- a group assignment depends on your contribution this week
- mental fatigue makes context switching between school, Kubernetes, routing,
  and backend work visibly slow

Chaos Mode rules:

1. Stop all new failure injection.
2. Stop all infrastructure changes except emergency restore.
3. Keep only three tasks for the week:
   - pass the school deadline
   - keep services stable
   - write one short theory mapping note
4. Replace lab reports with "evidence parking":
   - paste commands, screenshots, logs, or notes into a temporary file
   - formalize them later during a buffer week
5. Certification work becomes maintenance only:
   - 30-45 minutes of review cards or subnetting drills
   - no new CKA/AWS topic during exam week
6. A 10 PM run is allowed as reset, not as a way to extend the workday. After
   the run, choose either sleep or one 30-minute recovery task, not a new debug
   session.

Exit Chaos Mode only when:

- the nearest school deadline is submitted
- sleep has recovered
- the weekly backlog fits on one page
- no production-like homelab service is in a broken state

### Work-In-Progress Limit

At any time, only these can be active:

- one university deliverable
- one certification track
- one homelab experiment or document

Everything else goes to backlog. Context switching is treated as a real cost,
not as a personality flaw.

## 1. Weekly Operating Cadence

### Monday: Theory Mapping

Pick one formal concept and write a one-page note:

- definition
- formal terms
- where it appears in your homelab
- what command proves it
- what failure mode exposes it

Examples:

- VLAN trunking -> IEEE 802.1Q tagging -> VyOS subinterface behavior
- Process scheduling -> CPU contention -> Proxmox VM/LXC resource pressure
- Transaction isolation -> dirty/non-repeatable/phantom reads -> SQL Server lab
- Control plane vs data plane -> Headscale vs WireGuard/Tailscale traffic
- Liveness/readiness -> Kubernetes service routing and failure isolation

### Tuesday-Wednesday: Build or Break

Run one controlled experiment. It must have a hypothesis before execution.

Template:

```text
Hypothesis:
Expected behavior:
Failure injected:
Metrics to observe:
Commands to run:
Rollback plan:
```

### Thursday: Measure

Collect evidence:

- Grafana/InfluxDB metrics where available
- logs
- packet capture
- route table
- firewall rules
- database state
- application errors
- Kubernetes events during CKA phase

### Friday: Fix and Document

Fix the system and write:

- incident note
- root cause
- permanent fix
- prevention
- runbook change

### Saturday: Certification Drill

Use Saturday for certification work:

- Q1: CCNA
- Q2: CKA
- Q3: school-heavy mode; AWS SAA is blocked unless CCNA and CKA are already
  passed
- Q4: review, exam closure, and portfolio consolidation

### Sunday: Review Gate

Answer these questions in writing:

1. What did I break?
2. What did I measure?
3. What theory did I map it to?
4. What evidence did I produce?
5. What would a senior engineer reject as hand-wavy?

If the answer to question 5 is unclear, the week is not complete.

## 2. Required Document Types

Create and maintain these documents under `E:\Roadmaps\evidence` or a repo
folder that fits the project.

### Evidence Quality Ladder

Evidence has levels. Do not pretend all notes are equal.

- Level 0: raw command, screenshot, log, or messy note
- Level 1: cleaned observation with timestamp and system context
- Level 2: lab report with hypothesis, measurement, result, and limitation
- Level 3: postmortem or ADR that can be read by another engineer
- Level 4: portfolio-quality case study with diagrams and tradeoffs

During school-heavy mode, Level 2 evidence is enough for most weeks. Level 4 is
required only for the selected public case study.

Minimum viable weekly evidence:

- one theory mapping note, or
- one cleaned diagram, or
- one incident/lab note, or
- one school deliverable section mapped to formal engineering terms

If a week produces high-quality school documentation, it counts. Do not
duplicate it in a separate homelab document unless the reuse is forbidden by
course rules.

### ADR: Architecture Decision Record

Use this format:

```text
# ADR-NNN: Title

Status: Proposed | Accepted | Rejected | Superseded
Date:

## Context
## Decision
## Alternatives Considered
## Consequences
## Verification
```

### Postmortem

Use this format:

```text
# Postmortem: Incident Title

Date:
Severity:
Duration:
Affected systems:

## Impact
## Timeline
## Detection
## Root Cause
## Trigger
## Resolution
## What Went Well
## What Went Wrong
## Preventive Actions
## Evidence
```

### Lab Report

Use this format:

```text
# Lab Report: Title

## Formal Concept
## Practical System
## Hypothesis
## Experiment Design
## Commands
## Observations
## Metrics
## Packet/Log Evidence
## Result
## What This Proves
## What This Does Not Prove
```

### Diagram Requirements

Every quarter must include diagrams using standard notation:

- C4 Context diagram
- C4 Container diagram
- UML sequence diagram
- network topology diagram
- data flow diagram

Diagrams must use consistent terms:

- client
- reverse proxy
- control plane
- data plane
- gateway
- router
- subnet
- VLAN
- workload
- queue
- database
- object storage
- identity
- policy
- trust boundary

## 3. Q1: Network and OS Foundations

Timebox: Months 1-3  
Primary exam target: CCNA  
Theme: Stop guessing packet paths.

Transition rule:

- The last week of Q1 is a buffer week, not a new lab week.
- Use it to close CCNA notes, clean diagrams, archive unfinished experiments,
  and write a short "What I still do not understand" list.
- Do not start Kubernetes in the same week as a CCNA exam attempt or a school
  exam block.

### Focus

Academic focus:

- computer networks
- operating system basics
- Linux process and network stack basics
- routing, switching, subnetting, NAT, ACLs
- control plane vs data plane

Practical focus:

- prove how traffic moves through your homelab
- cleanly document the physical, virtual, and overlay network
- make Headscale/Tailscale/VyOS behavior explainable with standard networking
  terms

### University Foundations to Repair

- Computer Networks:
  - OSI model and TCP/IP model
  - Ethernet, ARP, ICMP, TCP, UDP
  - subnetting and CIDR
  - routing table lookup
  - VLAN and trunking
  - NAT and firewalling
  - ACL ordering and default deny
- Operating Systems:
  - process, thread, file descriptor
  - sockets
  - memory pressure
  - CPU scheduling basics
  - Linux namespaces at a conceptual level

### Deliverables

By the end of Q1, deliver:

1. `network-ground-truth.md`
   - physical topology
   - Proxmox bridges
   - VyOS interfaces
   - VLANs
   - Headscale/Tailscale nodes
   - route tables
   - DNS path
   - ingress path
2. C4 Context diagram for homelab services.
3. Network topology diagram with VLANs, gateways, overlay nodes, and trust
   boundaries.
4. At least 8 lab reports.
5. At least 4 postmortems.
6. CCNA study log with weak topics and retest scores.
7. A formal glossary of at least 80 terms.

Quality override:

- Six strong lab reports beat eight weak ones.
- Two real postmortems with packet evidence beat four cosmetic postmortems.
- Do not manufacture incidents for quota.

### Failure Injection Tasks

Global failure-injection safety rule:

- Every failure injection must have a rollback command or restore path before
  it starts.
- Maximum active debug time is 2 hours.
- If root cause is not found within 2 hours, stop, restore service, and write a
  partial incident note.
- Partial evidence is acceptable. A broken school week is not.
- Never run destructive failure injection after 10 PM.
- Never run destructive failure injection on the same day as a major school
  deadline.

#### Q1-FI-01: VLAN Trunk Misconfiguration

Break:

- Misconfigure one VLAN tag or trunk path in a controlled window.

Measure:

- ping
- ARP table
- tcpdump on relevant interfaces
- VyOS interface counters
- Grafana network metrics if available

Fix:

- restore trunk or VLAN interface config

Document:

- explain access port vs trunk port
- explain 802.1Q tagging
- explain why the packet did not reach the gateway

Formal concept:

- data link layer segmentation
- broadcast domain
- VLAN tagging

#### Q1-FI-02: Wrong Default Gateway

Break:

- Set one VM/LXC to use a wrong default gateway.

Measure:

- `ip route`
- `traceroute`
- ARP behavior
- packet capture

Fix:

- restore correct gateway

Document:

- route selection
- longest prefix match
- default route behavior

Formal concept:

- routing table lookup
- L3 forwarding

#### Q1-FI-03: ACL Deny by Identity

Break:

- Remove or alter a Headscale/Tailscale tag so a node disappears from the
  expected netmap.

Measure:

- `tailscale status`
- Headscale node list
- ACL file
- ping and SSH behavior

Fix:

- reapply correct tag and policy

Document:

- why identity-based ACL is stronger than source-IP-only filtering
- why your ZAP/CrowdSec case matters
- why Tailscale IP is a separate trust surface from public ISP IP

Formal concept:

- defense in depth
- identity-based access control
- zero trust network access

#### Q1-FI-04: NAT and Return Path Failure

Break:

- Create a controlled asymmetric routing or missing return route case.

Measure:

- tcpdump on source, gateway, and target
- NAT table or firewall logs where available
- route tables

Fix:

- restore correct route/NAT behavior

Document:

- explain request path and response path separately
- explain why ping or TCP handshake fails

Formal concept:

- stateful NAT
- symmetric vs asymmetric routing
- TCP three-way handshake

### Q1 Certification Gate

You are allowed to schedule CCNA only when:

- subnetting is automatic under time pressure
- you can explain VLAN/trunk/access port without analogy
- you can debug a failed route from route table and packet capture
- you score consistently above your target threshold on practice exams
- you have at least 8 written troubleshooting cases

If CCNA slips:

- Do not stack CCNA catch-up and CKA ramp-up in the same week.
- Spend one buffer week closing CCNA before starting Kubernetes.
- If school-heavy mode has already started, CCNA takes priority over CKA until
  it is passed or formally rescheduled.

## 4. Q2: Kubernetes, Application Runtime, and CKA

Timebox: Months 4-6  
Primary exam target: CKA  
Theme: Stop treating containers as magic.

Transition rule:

- Week 1 of Q2 is Kubernetes orientation only.
- No real application migration in week 1.
- No CoreDNS breaking, no RBAC hardening, no queue backlog drill in week 1.
- The goal is to understand cluster objects and command workflow, not to prove
  production readiness.

### Focus

Academic focus:

- operating systems
- distributed systems basics
- service discovery
- scheduling
- health checking
- storage and state
- RBAC and least privilege

Practical focus:

- deploy a reduced version of your real application stack on Kubernetes
- debug failures using events, logs, probes, DNS, service selectors, and network
  paths
- keep the cluster small, observable, and explainable

Scope ladder:

1. Stage 0: local `kubectl` fluency, pods, deployments, services, logs,
   describe, events.
2. Stage 1: one stateless demo workload.
3. Stage 2: one Spring Boot service with config and probes.
4. Stage 3: add one dependency only, preferably RabbitMQ or PostgreSQL.
5. Stage 4: add ingress and RBAC.
6. Stage 5: only then run failure injection.

Do not skip stages. If a stage takes longer than planned, reduce the final
deliverables instead of compressing the stages.

### University Foundations to Repair

- Operating Systems:
  - process isolation
  - namespaces
  - cgroups
  - filesystem mounts
  - signals
  - resource limits
- Distributed Systems:
  - service discovery
  - leader/follower as a concept
  - retries and backoff
  - partial failure
  - health checks
  - eventual consistency as a concept
- Software Engineering:
  - deployment architecture
  - dependency boundaries
  - interface contracts

### Deliverables

By the end of Q2, deliver:

1. Minimal Kubernetes deployment for one real system:
   - Spring Boot backend
   - frontend or test client
   - RabbitMQ
   - PostgreSQL or SQL Server where practical
   - MinIO if needed
2. `cka-troubleshooting-runbook.md`.
3. C4 Container diagram for the Kubernetes deployment.
4. UML sequence diagram for one request path:
   - client -> ingress/service -> backend -> queue -> worker -> database/object
     storage
5. At least 10 Kubernetes failure reports.
6. At least 2 RBAC/least-privilege ADRs.
7. CKA exam attempt or scheduled exam.

Quality override:

- Five CKA-style failure reports with commands, events, root cause, and restore
  steps are better than ten shallow notes.
- If CKA exam preparation is active, prioritize timed troubleshooting over
  polished writing.

Minimum viable Q2 if school pressure or CCNA delay hits:

1. One stateless app deployed and debugged.
2. One Spring Boot service deployed with ConfigMap/Secret and probes.
3. One dependency integrated.
4. Five Kubernetes failure reports, not ten.
5. `cka-troubleshooting-runbook.md` with high-quality command recipes.
6. CKA scheduled only if practice results justify it.

### Failure Injection Tasks

Global Kubernetes failure-injection safety rule:

- Run failure injection only after the cluster has a known-good baseline.
- Save the baseline YAML or command state before changing anything.
- One failure per session.
- Maximum active debug time is 2 hours.
- If the failure is not resolved within 2 hours, restore the baseline and write
  a "failed investigation" note. Failed investigations still count if the
  evidence is honest.
- CoreDNS and cluster-wide failures are forbidden during school-heavy weeks.

#### Q2-FI-01: Broken Service Selector

Break:

- Change a Service selector so it points to no pods.

Measure:

- `kubectl get endpoints`
- `kubectl describe svc`
- app error behavior
- ingress response

Fix:

- restore selector

Document:

- explain how Kubernetes Service maps stable virtual IP to pod endpoints

Formal concept:

- service discovery
- indirection
- control plane reconciliation

#### Q2-FI-02: Readiness Probe Failure

Break:

- Make readiness probe fail while process is still running.

Measure:

- `kubectl describe pod`
- events
- endpoint changes
- app availability

Fix:

- correct probe path, port, or app readiness logic

Document:

- difference between liveness and readiness
- why traffic should not be routed to unready pods

Formal concept:

- health checking
- failure detection

#### Q2-FI-03: CoreDNS Failure

Break:

- Introduce a controlled DNS failure inside the cluster.

Measure:

- pod DNS lookup
- CoreDNS logs
- service name resolution

Fix:

- restore CoreDNS configuration

Document:

- explain DNS resolution path inside Kubernetes

Formal concept:

- name resolution
- distributed service discovery

Scope guard:

- Run this only in a disposable cluster or after exporting all relevant
  manifests.
- Do not run this during any week with university deadlines.
- If you cannot explain how to restore CoreDNS before breaking it, you are not
  allowed to run the experiment.

#### Q2-FI-04: Resource Starvation

Break:

- Set unrealistic CPU/memory limits for one service.

Measure:

- pod restarts
- OOMKilled events
- CPU throttling
- Grafana metrics if integrated

Fix:

- set sane requests and limits

Document:

- explain requests vs limits
- explain cgroups and resource isolation

Formal concept:

- OS resource management
- scheduling
- isolation

Scope guard:

- Start with one non-critical pod.
- Do not starve database or queue services during school-heavy weeks.
- The goal is to observe cgroups and scheduling behavior, not to create a
  multi-service outage.

#### Q2-FI-05: Queue Backlog

Break:

- Slow down or stop the translation worker while messages continue to enter
  RabbitMQ.

Measure:

- queue depth
- backend response behavior
- worker logs
- latency

Fix:

- restart worker or scale replicas
- add backpressure or retry policy where appropriate

Document:

- explain asynchronous processing and backpressure

Formal concept:

- producer-consumer model
- queueing
- backpressure

Scope guard:

- Use a test queue or test namespace.
- Cap message volume before the experiment.
- The experiment ends when queue depth behavior is proven, not when the system
  is "fully tuned".

### Q2 Certification Gate

You are allowed to take CKA only when:

- you can debug failed pods without deleting everything
- you know where to look first: events, describe, logs, endpoints, DNS, RBAC
- you can rebuild a small deployment from YAML under time pressure
- you can explain why the failure happened using Kubernetes control plane terms

## 5. Q3: Database, Security, and Defense in Depth

Timebox: Months 7-9  
Secondary exam target: AWS SAA only if CCNA and CKA are done or firmly under
control.  
Theme: Stop calling scanners security.

School-heavy override:

- If Q3 overlaps August-December, Q3 is not a maximal lab quarter.
- Treat Q3 as a documentation, database, security, and school-integration
  quarter.
- Minimum viable Q3 is better than a heroic plan that damages GPA.
- AWS SAA is suspended by default during this period.

### Focus

Academic focus:

- database systems
- transaction theory
- replication concepts
- information security
- threat modeling
- access control
- auditability

Practical focus:

- turn the ZAP/CrowdSec/Tailscale case into a formal defense-in-depth case
  study
- harden one application path end to end
- prove how identity, network, app auth, logs, and rate limits interact
- convert school assignments into formal engineering documents instead of
  treating them as unrelated academic burden

### University Foundations to Repair

- Database Systems:
  - relational model
  - normalization
  - indexing
  - transactions
  - ACID
  - isolation levels
  - replication
  - backup and restore
- Information Security:
  - CIA triad
  - authentication vs authorization
  - least privilege
  - threat modeling
  - defense in depth
  - audit log integrity
  - vulnerability management

### Deliverables

By the end of Q3, deliver:

1. `defense-in-depth-case-study.md`
   - ZAP scan
   - ban event
   - Tailscale SSH bypass path
   - CrowdSec trust boundary issue
   - remediation plan
   - policy recommendation
2. Database lab report:
   - transaction isolation experiments
   - indexing experiment
   - backup/restore drill
   - replication/failover analysis where feasible
3. Threat model for `student-feedback-system`.
4. Data flow diagram with trust boundaries.
5. Security ADRs:
   - secret handling
   - admin access path
   - network ACL policy
   - audit logging policy
6. At least 6 security failure reports.
7. AWS SAA decision checkpoint:
   - start only if CCNA and CKA are complete or nearly complete

Quality override:

- The defense-in-depth case study is the main Q3 artifact.
- Do not run six security experiments if one well-documented trust-boundary
  case already teaches the core lesson.

If Q3 overlaps August-December, use this reduced but stricter deliverable set:

1. `defense-in-depth-case-study.md` completed and polished.
2. One database lab report, not four:
   - choose either transaction isolation, indexing, backup/restore, or
     replication/failover
   - include formal theory and measured evidence
3. One school-integrated architecture package:
   - C4 Context diagram
   - C4 Container diagram
   - one UML sequence diagram
   - written mapping to "Phan tich va thiet ke he thong thong tin"
4. Two failure reports maximum, but both must be high quality.
5. One risk register using software project management language:
   - scope
   - schedule
   - technical risk
   - operational risk
   - mitigation
6. No AWS SAA unless:
   - CCNA passed
   - CKA passed
   - no school course is at risk
   - weekly school backlog is empty

### Failure Injection Tasks

#### Q3-FI-01: ZAP Scan and Layered Defense

Break:

- Run a controlled scan against a test environment until rate limiting or ban
  logic triggers.

Measure:

- application logs
- reverse proxy logs
- CrowdSec logs
- source IP classification
- Tailscale source identity

Fix:

- define separate policies for public IP access and overlay network access
- avoid trusting Tailscale IP alone
- document emergency admin path separately

Document:

- explain why being able to SSH through Tailscale after a public ban is both
  useful and dangerous
- define which layer owns which control

Formal concept:

- defense in depth
- trust boundary
- fail-safe vs fail-open
- break-glass access

School-heavy version:

- Do not run aggressive scans during exam or assignment weeks.
- Use prior ZAP/CrowdSec/Tailscale evidence if it is enough.
- Spend the time writing the trust-boundary analysis properly.

#### Q3-FI-02: Database Isolation Anomaly

Break:

- Create concurrent transactions that demonstrate one isolation anomaly.

Measure:

- transaction logs where available
- SQL output
- lock behavior

Fix:

- choose appropriate isolation level or transaction design

Document:

- explain the anomaly formally

Formal concept:

- ACID
- isolation level
- concurrency control

School-heavy version:

- This is the preferred Q3 database experiment because it maps cleanly to
  database theory and can be documented in a compact report.

#### Q3-FI-03: Missing Index Under Load

Break:

- Remove or avoid a useful index in a test query path.

Measure:

- query plan
- latency
- CPU/disk impact
- Grafana metrics where available

Fix:

- add index and compare execution plan

Document:

- explain selectivity, index scan, table scan, and cost

Formal concept:

- database indexing
- query optimization

#### Q3-FI-04: Secret Exposure Drill

Break:

- Place a fake secret in a controlled branch or local test file.

Measure:

- secret scan result if available
- review process

Fix:

- remove secret
- rotate fake credential
- document prevention

Document:

- explain why secret rotation matters even after removal

Formal concept:

- credential lifecycle
- least privilege
- incident response

#### Q3-FI-05: Backup Restore Failure

Break:

- Simulate backup corruption or missing restore dependency.

Measure:

- restore logs
- RTO
- RPO
- data consistency

Fix:

- repair backup procedure
- add restore verification

Document:

- explain backup is not real until restore is tested

Formal concept:

- disaster recovery
- RTO/RPO
- durability

School-heavy version:

- Run only if the database course workload is light. Otherwise keep this as a
  Q4 task.

## 6. Q4: Production Discipline, Cloud Mapping, and Portfolio

Timebox: Months 10-12  
Optional exam target: AWS SAA  
Theme: Become credible on paper, not just in the terminal.

School-heavy override:

- If Q4 overlaps August-December, Q4 is a consolidation quarter, not an
  expansion quarter.
- The main job is to pass school properly, close CCNA/CKA if still pending, and
  convert existing work into readable evidence.
- AWS SAA is a bonus only after the semester is under control.

### Focus

Academic focus:

- software architecture
- distributed systems
- cloud architecture
- reliability engineering
- cost and capacity planning

Practical focus:

- consolidate evidence into a professional portfolio
- convert homelab architecture into standard diagrams and written explanations
- map on-prem concepts to AWS SAA concepts only after the local fundamentals are
  stable
- turn school project reports into portfolio-quality documentation where
  allowed by course rules

### University Foundations to Repair

- Software Architecture:
  - modularity
  - coupling and cohesion
  - ports and adapters
  - C4 model
  - UML sequence and component diagrams
- Distributed Systems:
  - partial failure
  - timeout and retry
  - idempotency
  - consistency
  - observability
- Cloud Computing:
  - VPC/subnet/security group/NACL
  - IAM
  - load balancer
  - managed database
  - object storage
  - autoscaling
  - monitoring

### Deliverables

By the end of Q4, deliver:

1. Public portfolio update:
   - profile README cleaned
   - top 5 repos documented with evidence
   - diagrams and postmortems linked
2. `homelab-architecture-whitepaper.md`
   - business goal
   - constraints
   - architecture
   - tradeoffs
   - risks
   - security controls
   - observability
   - recovery plan
3. At least 12 postmortems total across the year.
4. At least 20 lab reports total across the year.
5. At least 12 ADRs total across the year.
6. One polished case study:
   - `student-feedback-system` end-to-end
   - or Headscale/Tailscale/VyOS defense-in-depth networking case
7. AWS SAA attempt only if Q1-Q3 gates are satisfied.

Quality override:

- One case study that survives senior review is the win condition.
- Portfolio polish must not steal time from final exams.

If Q4 overlaps August-December, use this reduced deliverable set:

1. Finish all school deliverables with formal diagrams and terminology.
2. Complete one polished public case study, not three.
3. Bring total yearly evidence to at least:
   - 8 postmortems
   - 12 lab reports
   - 8 ADRs
4. Update only the top 3 repos, not the top 5.
5. If CCNA or CKA is still unfinished, finish that before AWS SAA.
6. AWS SAA may only enter active study after the last major school deadline.

### Failure Injection Tasks

#### Q4-FI-01: Full Request Path Failure

Break:

- Introduce one failure in each layer across separate test runs:
  - DNS
  - ingress/reverse proxy
  - service routing
  - backend config
  - queue
  - database
  - object storage

Measure:

- user-facing error
- logs
- metrics
- packet path where relevant

Fix:

- restore each layer
- update runbook

Document:

- explain blast radius and detection path

Formal concept:

- dependency graph
- failure domain
- observability

School-heavy version:

- Run only one full request path failure per month.
- Prefer failures that support a school report or portfolio case study.

#### Q4-FI-02: Capacity Pressure

Break:

- Generate controlled load until one bottleneck appears.

Measure:

- CPU
- memory
- disk I/O
- database latency
- queue depth
- application latency

Fix:

- tune resource allocation or reduce bottleneck

Document:

- explain bottleneck and capacity limit

Formal concept:

- performance modeling
- utilization
- saturation

School-heavy version:

- Keep this as a single weekend experiment after midterm/final pressure is low.
- Do not spend the semester building a load-testing platform.

#### Q4-FI-03: Access Control Regression

Break:

- Accidentally over-permit a non-admin identity in a test ACL/RBAC policy.

Measure:

- what resource becomes reachable
- logs
- policy diff

Fix:

- restore least privilege
- add verification checklist

Document:

- explain why policy tests are required

Formal concept:

- least privilege
- access control model
- regression testing

### AWS SAA Gate

Only start AWS SAA if:

- CCNA is passed
- CKA is passed, not merely "planned"
- Q1-Q3 deliverables exist
- August-December school load is stable and no course is at risk
- you can map your homelab concepts to AWS:
  - VLAN/subnet -> VPC subnet
  - firewall/ACL -> Security Group/NACL
  - MinIO -> S3
  - SQL Server/Postgres -> RDS concept
  - reverse proxy/ingress -> ALB/NLB concept
  - Tailscale/Headscale -> private connectivity and identity-aware access
  - Grafana/InfluxDB -> CloudWatch/managed observability concept

## 7. Monthly Review Board

At the end of each month, run a personal review board. Write answers, do not
think them silently.

During August-December, run a shorter weekly academic review before the monthly
review:

1. Which course is closest to Red?
2. Which school deliverable can become a roadmap artifact?
3. Which roadmap task must be cut this week?
4. Is certification still realistic this week, or only maintenance?
5. Did I sleep enough to do debugging safely?

### Scorecard

Rate each from 1 to 5:

- formal explanation quality
- evidence quality
- debugging discipline
- diagram quality
- postmortem quality
- certification progress
- restraint from tool collecting

### Kill List

Every month, kill or archive at least one distraction:

- unused service
- duplicated document
- abandoned lab
- unclear script
- half-written roadmap
- tool that exists only because it was interesting

### Senior Engineer Questions

Answer:

1. What does this system do?
2. What are its trust boundaries?
3. What are its failure domains?
4. How do you know it is healthy?
5. How do you know it is secure enough for its purpose?
6. How do you restore it?
7. What would fail first under load?
8. What assumption has not been tested?

## 8. Corrected Personal Context

Your ezCloud internship lasted 1 year, not 6 months. Treat that as meaningful
industry exposure, but do not overvalue it if the environment was not suitable
for intern growth. The lesson is not "industry is useless". The lesson is that
you now need stronger filters for choosing environments:

- Does the team review code seriously?
- Are there production incidents to learn from?
- Are interns given ownership with guardrails?
- Are architecture decisions explained?
- Is there a feedback loop?

Your ZAP/CrowdSec/Tailscale case is a strong real-world security lesson. The
correct lesson is not "I bypassed a ban". The correct lesson is:

- controls must be layered
- identity source matters
- overlay networks are separate trust surfaces
- admin break-glass paths must be intentional
- public protection and private access policy must be modeled separately
- logs must preserve enough context to distinguish public attacker behavior
  from private administrative access

## 9. Final Standard

At the end of 12 months, you should be able to sit in front of a senior panel
and defend your system without hiding behind tool names.

You should be able to say:

- here is the architecture
- here are the tradeoffs
- here is the packet path
- here is the trust boundary
- here is the failure I injected
- here is the metric that moved
- here is the root cause
- here is the fix
- here is the formal concept
- here is the remaining risk

If you can do that consistently, your GPA becomes less damaging because your
engineering evidence is stronger than your transcript. If you cannot do that,
the homelab is just expensive noise.
