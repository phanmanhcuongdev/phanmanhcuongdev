# Personal DevSecOps / Platform Engineering Dossier

**Owner:** Phan Manh Cuong  
**Role direction:** Backend developer moving toward DevSecOps / Platform Engineering  
**Document type:** Personal technical dossier, not a marketing brochure  
**Build source:** local roadmap/docs/lab inventory plus public GitHub profile metadata

## 1. Executive Summary

This dossier describes the current technical baseline, evidence system, roadmap, and claim boundaries for a backend-to-DevSecOps / Platform Engineering transition.

The current strongest evidence is backend and full-stack project work around `student-feedback-system`, supported by documentation for Spring Boot, React/TypeScript, SQL Server, Flyway, MinIO, WebSocket notifications, reporting, Docker image builds, and GitHub Actions. There is also evidence of a RabbitMQ translation worker and a local Windows automation/tooling project.

The DevSecOps / Platform direction is intentionally not framed as already complete. It is an evidence-driven transition: build a foundation in networking/OS, then containers/Kubernetes, then database/security/defense-in-depth, then production discipline/cloud mapping/portfolio packaging.

Core operating rule:

> No new tool collecting. Break -> Measure -> Fix -> Document.

## 2. Current Technical Identity

| Area | Status | Claim label | Evidence / boundary |
| --- | --- | --- | --- |
| Backend application engineering | Active baseline | Evidence-backed | `student-feedback-system` README and project structure show Spring Boot, security, JPA, Flyway, SQL Server, reporting, notifications, and operational admin flows. |
| Frontend application engineering | Active baseline | Evidence-backed | React 19, TypeScript, Vite, role-aware navigation, API-driven pages, and operational data views are documented in the project README. |
| DevSecOps / Platform transition | Direction of growth | In progress | Roadmap and tracker define a 12-month operating system for networking, OS, Kubernetes, security, evidence, and portfolio discipline. |
| Homelab / infrastructure thinking | Learning environment | In progress | Roadmap references Proxmox, VyOS, Headscale/Tailscale, Docker, SQL Server/PostgreSQL, RabbitMQ, MinIO, Grafana/InfluxDB as the controlled lab stack. |
| Certification path | Structured plan | Planned/In progress | Q1 CCNA, Q2 CKA, AWS SAA only later if gates are met. |
| Portfolio evidence discipline | Operating system | Evidence-backed | Tracker workbook/report/tutorial and roadmap templates define Daily Log, Evidence Queue, Weekly Review, ADR, postmortem, lab report, and monthly review board. |

The technical identity is therefore not a senior DevSecOps claim. The accurate framing is:

> Backend-focused engineer building a disciplined DevSecOps / Platform Engineering evidence base through homelab, formal networking/OS study, infrastructure documentation, controlled failure experiments, and portfolio-grade case studies.

## 3. Current Engineering Baseline

### 3.1 Backend / Application Systems

**Claim label: Evidence-backed**

The strongest current project evidence is `student-feedback-system`. The local README documents:

* Java 21 and Spring Boot 4 backend.
* Spring MVC, Spring Security, WebSocket/STOMP, Spring Data JPA.
* SQL Server database with Flyway migrations and Hibernate validation.
* JWT bearer authentication.
* MinIO-backed document storage.
* BIRT-based PDF/XLSX reporting.
* Admin, lecturer, and student workflows.
* Survey lifecycle, question bank, templates, recipient tracking, analytics, audit logs, notifications, account/security flows, and operational queues.
* GitHub Actions CI and Docker images for backend/frontend.

This supports a public claim of backend project implementation and system design practice. It does not justify a claim of production SRE ownership unless deployment/incident evidence is added.

### 3.2 Frontend / TypeScript

**Claim label: Evidence-backed**

The same project documents a React 19 / TypeScript / Vite frontend with role-aware navigation, an authenticated app shell, API clients, reusable UI primitives, tables/queues, notification UI, and survey/admin flows.

Public claim allowed:

* Built project frontend features with React/TypeScript and API integration.

Public claim not allowed:

* Do not claim specialized frontend architecture leadership beyond what the project evidence shows.

### 3.3 Data and Integration

**Claim label: Evidence-backed / Current**

The project context supports:

* SQL Server usage.
* Flyway migration workflow.
* Reporting/export boundary.
* RabbitMQ worker integration through `ai-translation-wrapper`.
* MinIO document storage integration.

The `ai-translation-wrapper` README documents a RabbitMQ request/reply contract, exchanges, queues, routing keys, dead-letter queue, bilingual output, compatibility rules, and cache behavior.

### 3.4 Local Tooling

**Claim label: Evidence-backed**

`window_ui` documents a conservative Windows UI/workspace profile switcher implemented with PowerShell and .NET. It emphasizes dry-run, backup, restore, validation, no silent Explorer restart, no silent admin prompts, allowlisted stop-process behavior, and a foreground-only context agent MVP.

This is useful evidence for platform mindset: safety, reversibility, local automation, and operational guardrails.

## 4. Homelab and Infrastructure Context

**Claim label: In progress**

The homelab exists as a learning and evidence environment, not as a claim of enterprise-grade production operation.

Roadmap-defined stack includes:

* Proxmox.
* LXC and Ubuntu Server VMs.
* VyOS.
* Headscale and Tailscale.
* Docker.
* Spring Boot app and FastAPI worker.
* RabbitMQ.
* MinIO.
* SQL Server and PostgreSQL.
* Grafana and InfluxDB.
* Existing router/switch equipment.

The roadmap explicitly says measurement matters more than dashboards for appearance. Monitoring/logging/metrics are the measurement layer for proving behavior, root cause, and fix quality.

Current dossier claim:

* Homelab is the controlled environment for learning packet path, routing, service dependency, identity boundary, failure domain, and evidence discipline.

Boundary:

* Do not claim real production platform operation until there are public runbooks, postmortems, metrics, restore drills, and architecture diagrams that survive review.

## 5. Software Project Context

### 5.1 Primary Project: Student Feedback System

**Claim label: Evidence-backed**

This is the primary software project anchor for the dossier. It provides a real application surface for DevSecOps work:

* backend architecture and security;
* database migrations;
* document storage;
* notification delivery;
* report export;
* role-aware frontend;
* CI/Docker packaging;
* future deployment and observability work.

Potential platform case-study angles:

* request path: frontend -> backend -> database/object storage;
* migration discipline and schema validation;
* authentication/session boundary;
* document upload and storage boundary;
* notification delivery path;
* report rendering boundary;
* CI image build and deployment path.

### 5.2 Translation Worker

**Claim label: Evidence-backed**

The RabbitMQ worker supports bilingual translation request/reply workflows for project integration. This is useful evidence for asynchronous processing, message contracts, compatibility, cache behavior, and dead-letter handling.

### 5.3 Windows Profile Switcher

**Claim label: Evidence-backed**

The local profile switcher demonstrates automation with conservative operational safety. It should be presented as a local tooling project, not as a cloud/platform product.

## 6. DevSecOps / Platform Roadmap

The roadmap is structured across four quarters:

| Phase | Focus | Claim label | Dossier interpretation |
| --- | --- | --- | --- |
| Q1 Network and OS | Packet path, routing, VLAN, ACL, Linux/OS basics, CCNA | In progress | Foundation repair and troubleshooting discipline. |
| Q2 Kubernetes and Runtime | Containers, Kubernetes objects, probes, service discovery, CKA | Planned / near-future | Do not claim Kubernetes proficiency until labs and evidence exist. |
| Q3 Database and Security | DB theory, isolation, indexing, backup/restore, defense in depth | Planned | Convert security/database experiments into formal case studies. |
| Q4 Production and Portfolio | Reliability, cloud mapping, portfolio evidence, public case study | Planned | Package evidence into public artifacts and interview-ready narratives. |

School-heavy mode from August to December protects GPA and limits optional homelab expansion. This is not a pause in engineering development; it is scope control.

## 7. Stack and Knowledge Map

| Layer | Current | Next to learn | Optional later |
| --- | --- | --- | --- |
| Application backend | Spring Boot, REST, security, JPA, Flyway | stronger operational boundaries and failure evidence | advanced platform APIs |
| Frontend | React, TypeScript, Vite | production build/deployment flow | advanced frontend platform concerns |
| Database | SQL Server, migrations | isolation, indexing, backup/restore evidence | replication/failover depth |
| Messaging | RabbitMQ worker contract | backlog, retry, DLQ, backpressure evidence | distributed workflow orchestration |
| Containers | Docker images documented | runtime debugging, resource limits | advanced image/security pipeline |
| Kubernetes | not claimed as completed | Q2 CKA-style labs | multi-cluster/service mesh later only if justified |
| Networking | roadmap/homelab focus | packet path, VLAN, routing, ACL evidence | advanced network automation later |
| Security | app auth plus roadmap security cases | threat model, ZAP/CrowdSec/Tailscale case study | enterprise security tooling later |
| Observability | measurement layer planned | logs/metrics tied to failures | dashboard polish only after evidence |
| Cloud | mapping planned | map homelab concepts to AWS | AWS SAA only after gates |

## 8. Evidence and Operating System

**Claim label: Evidence-backed**

The operating system for learning is documented through:

* Daily Log.
* Evidence Queue.
* Weekly Review.
* WIP Limit.
* Chaos Mode.
* Habit & Energy.
* Certification tracking.
* School Risk.
* Monthly Review.
* Templates for lab reports, postmortems, ADRs, risk registers, evidence indexes, and portfolio case studies.

Evidence ladder:

| Level | Meaning | Use |
| --- | --- | --- |
| Level 0 | Raw command, screenshot, log, or messy note | Do not lose the facts. |
| Level 1 | Cleaned observation | Useful for weekly review. |
| Level 2 | Lab report | Minimum strong lab artifact. |
| Level 3 | Postmortem or ADR | Readable by another engineer. |
| Level 4 | Portfolio case study | Public/interview-ready artifact. |

Operating rule:

* If the system works but cannot be proven, it is not done.
* If the system fails but cannot be reproduced, it is not learned.

## 9. Portfolio Case Study Plan

| Candidate | Status | Why it matters | Required evidence before public claim |
| --- | --- | --- | --- |
| `student-feedback-system` platform case study | Current project, not fully packaged | Real application with backend, frontend, database, storage, notifications, reporting | architecture diagram, request path, deployment notes, CI evidence, failure/postmortem, security boundary |
| Headscale/Tailscale/VyOS defense-in-depth case | Planned from roadmap/public repo context | Strong platform/security/networking story | topology, ACL policy, packet path, ZAP/CrowdSec event evidence, risk analysis |
| SQL Server replication/database lab | Public repo visible / roadmap aligned | Good database/platform reliability story | lab report, failure mode, measurement, restore or replication evidence |
| RabbitMQ translation worker | Current project evidence | Shows async integration and contract discipline | queue topology, failure handling, DLQ/retry/backpressure evidence |
| Windows profile switcher | Current local tooling | Shows operational safety and automation | README, dry-run output, backup/restore validation, design rationale |

## 10. Interview Readiness Map

| Interview topic | Current answer quality | Improvement path |
| --- | --- | --- |
| Backend project design | Good project-level evidence | Prepare concise architecture narrative and tradeoffs. |
| Database migrations | Evidence-backed | Add migration failure/rollback case. |
| Auth and security boundaries | Current at app level | Add threat model and defense-in-depth case. |
| Networking fundamentals | In progress | Produce packet-path lab reports. |
| Kubernetes troubleshooting | Planned | Build CKA-style failure reports before claiming. |
| Incident/postmortem writing | Operating system exists | Add real postmortems with evidence. |
| Observability | Planned measurement layer | Tie metrics/logs to specific failure investigations. |
| Cloud architecture | Planned/Q4 | Map homelab concepts to AWS only after local fundamentals are stable. |

## 11. Risk Management

Key risks:

* Tool sprawl: learning too many tools without evidence.
* Overclaiming: presenting roadmap items as completed skills.
* Academic overload: school-heavy period can silently damage execution quality.
* Evidence debt: doing work without preserving command/log/metric/config proof.
* Late-night debugging: poor-quality decisions when sleep is low.

Controls:

* WIP limit: one university deliverable, one certification track, one homelab experiment/document.
* Chaos Mode: reduce scope during deadline/exam/sleep/lab-failure collision.
* Weekly review gate: answer what broke, what was measured, what theory was mapped, what evidence was produced, and what a senior engineer would reject.
* Monthly review board: score evidence quality, debugging discipline, diagram quality, postmortem quality, certification progress, and restraint from tool collecting.

## 12. Public Claim Boundaries

Allowed public claims:

* Backend/full-stack project work with Spring Boot, React/TypeScript, SQL Server, Flyway, MinIO, WebSocket notifications, reporting, Docker image builds, and GitHub Actions, based on the `student-feedback-system` evidence.
* RabbitMQ worker integration and message-contract documentation, based on `ai-translation-wrapper`.
* Local automation/tooling with safety-first PowerShell/.NET workflow, based on `window_ui`.
* Structured transition toward DevSecOps / Platform Engineering, based on the roadmap and tracker.
* Evidence-first learning system with lab report/postmortem/ADR templates and tracker.

Claims to avoid until stronger evidence exists:

* Kubernetes specialist / CKA-ready.
* AWS/cloud architect.
* Production platform engineer.
* Security engineer with mature detection/response program.
* SRE owning production reliability.
* Fully completed networking.

Use safer wording:

* "In progress", "roadmap phase", "homelab evidence target", "case-study candidate", "currently building evidence".

## 13. Appendix Index

| Source | Use |
| --- | --- |
| `E:\Lap\IOT_Va_Ung_Dung\RoadmapForMe\README.md` | School / adjacent project context |
| `E:\Lap\IOT_Va_Ung_Dung\RoadmapForMe\roadmap.md` | School / adjacent project context |
| `E:\Lap\TTCS\ai-translation-wrapper\.github\workflows\docker-image.yml` | Worker / RabbitMQ integration evidence |
| `E:\Lap\TTCS\ai-translation-wrapper\deploy\k8s\ai-worker-deployment.yaml` | Worker / RabbitMQ integration evidence |
| `E:\Lap\TTCS\ai-translation-wrapper\docker-compose.yml` | Worker / RabbitMQ integration evidence |
| `E:\Lap\TTCS\ai-translation-wrapper\README.md` | Worker / RabbitMQ integration evidence |
| `E:\Lap\TTCS\ai-translation-wrapper\requirements.txt` | Worker / RabbitMQ integration evidence |
| `E:\Lap\TTCS\student-feedback-system\.github\workflows\ci.yml` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\API_CONTRACT.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\backend\pom.xml` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\backend\README.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\backend\src\main\resources\application.yaml` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\database\README.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docker-compose.yml` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\backend-architecture.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\feature-tech-mapping-plan.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\final-recommended-expansion-scope.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\implementation-expansion-plan.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\lecturer-and-recruiter-expansion-review.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\next-product-expansion-strategy.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\product-hard-review-and-evolution-roadmap.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\reporting-architecture.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\survey-ai-summary-feature.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\technical-roadmap-evaluation.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\docs\technical-roadmap.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\embedding-service\README.md` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\embedding-service\requirements.txt` | Primary software project evidence |
| `E:\Lap\TTCS\student-feedback-system\frontend\package-lock.json` | Primary software project evidence |

## Closing Standard

This dossier should be updated only when evidence improves. The goal is not to look broader than reality. The goal is to become easier to evaluate: what exists, what is practiced, what is planned, what is excluded, and what evidence supports each claim.
