from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(r"E:\Roadmaps\phanmanhcuongdev\personal-dossier-builder")
NOTES = ROOT / "working-notes"
OUT = ROOT / "output"
TEMPLATES = ROOT / "templates"
EXTRACTED = ROOT / "extracted"
NOTES.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
TEMPLATES.mkdir(parents=True, exist_ok=True)

MD = OUT / "personal-devsecops-platform-engineering-dossier.md"
DOCX = OUT / "personal-devsecops-platform-engineering-dossier.docx"
OUTLINE = OUT / "personal-devsecops-platform-engineering-dossier-outline.md"


def load_sources() -> list[dict]:
    return json.loads((EXTRACTED / "sources.json").read_text(encoding="utf-8"))


def source_index(sources: list[dict]) -> str:
    selected = [s for s in sources if s["use_in_final"].startswith("Yes")]
    lines = ["| Source | Use |", "| --- | --- |"]
    for s in selected[:28]:
        lines.append(f"| `{s['path']}` | {s['relevance']} |")
    return "\n".join(lines)


def write_context_notes() -> None:
    context = """# Personal Technical Context

## 1. Verified / Evidence-backed

* `student-feedback-system` exists locally with README evidence for a Java 21 / Spring Boot 4 backend, React 19 / TypeScript / Vite frontend, SQL Server, Flyway migrations, JWT authentication, MinIO document storage, BIRT PDF/XLSX reporting, WebSocket/STOMP notifications, GitHub Actions CI, and Docker image builds.
* `ai-translation-wrapper` exists locally with README evidence for a RabbitMQ worker that consumes translation tasks and returns bilingual Vietnamese/English content.
* `window_ui` exists locally with README evidence for a Windows profile/workspace switcher using PowerShell and .NET, with dry-run, backup, validation, and conservative safety behavior.
* The roadmap and handbook documents exist under `E:\\Roadmaps` and define the 12-month DevSecOps transition, operating rules, phase plans, templates, evidence ladder, and anti-tool-sprawl constraints.
* The tracker workbook/report/tutorial exist under `trackers` and define a daily/weekly/monthly evidence system.
* Public GitHub profile metadata shows `phanmanhcuongdev` and visible public repositories including `student-feedback-system`, `sqlserver-replication-lab`, `distributed-systems-lab`, and `headscale-infra`.

## 2. Current / Already Practiced

* Backend application development with Spring Boot, Spring Security, Spring Data JPA, Flyway, SQL Server, JWT, REST APIs, report export, and role-based workflows.
* React/TypeScript frontend work with Vite, role-aware navigation, API clients, reusable operational table/queue components, and authenticated user flows.
* Database-backed application design using SQL Server and migration discipline through Flyway.
* Message-driven integration through RabbitMQ for translation worker workflows.
* Local automation/tooling through a Windows profile switcher built with PowerShell and .NET.
* Documentation discipline: README, tracker report/tutorial, roadmap handbooks, templates, and operating rules.

## 3. Learning / In Progress

* DevSecOps / Platform transition from backend foundation toward network, OS, homelab, evidence, and operating discipline.
* Q1 focus: networking, OS foundations, packet path, routing, VLANs, ACLs, CCNA-aligned troubleshooting.
* Evidence-first lab practice: hypothesis, measurement, rollback, root cause, fix, document.

## 4. Planned / Roadmap

* Q2: containers, Kubernetes runtime, and CKA-oriented troubleshooting.
* Q3: database/security/defense-in-depth case study and selected database/security failure reports.
* Q4: production discipline, cloud mapping, portfolio case study, and public artifact polish.

## 5. Optional Later

* AWS SAA is explicitly optional/blocked until CCNA, CKA, and school load are under control.
* Advanced enterprise DevSecOps tooling is later-stage only unless required by a roadmap gate or ADR.

## 6. Sensitive / Exclude

* Any `.env`, token, API key, private endpoint, credential, private config, seed password, MinIO key, JWT secret, Resend API key, database password, or social/private profile details.
* README environment variable examples are source context only; do not reproduce credential-looking values in the dossier.
"""
    (NOTES / "personal-technical-context.md").write_text(context, encoding="utf-8")


def write_evidence_map() -> None:
    rows = [
        ("Backend / Spring Boot", "student-feedback-system README; backend architecture notes", "High", "Yes", "Claim concrete backend project work, not senior mastery."),
        ("React / TypeScript", "student-feedback-system frontend README/project structure", "High", "Yes", "Claim project implementation with React/Vite/TypeScript."),
        ("Database", "student-feedback-system SQL Server/Flyway; roadmap DB phase", "High", "Yes", "SQL Server/Flyway current; advanced DB experiments planned."),
        ("Homelab / Proxmox", "roadmap core lab stack", "Medium", "Careful", "Roadmap and homelab context mention; avoid claiming production operation without public evidence."),
        ("Linux / OS", "roadmap Q1/Q2; lab stack", "Medium", "Careful", "Foundation focus and learning path."),
        ("Networking / routing / VLAN / ACL / Tailscale", "roadmap Q1; GitHub visible headscale/distributed-system repos", "Medium", "Careful", "Can claim learning/homelab focus; specific completed labs require evidence links."),
        ("Docker / container", "student-feedback-system Docker images; roadmap Q2", "Medium", "Yes", "Docker image build evidence; Kubernetes remains planned/in progress."),
        ("Monitoring / Grafana / Prometheus / Loki", "roadmap/tracker measurement layer", "Low-Medium", "Careful", "Mention as roadmap measurement layer unless concrete dashboard evidence is added."),
        ("Security / CrowdSec / ZAP / ACL / defense in depth", "roadmap personal context and Q3 plan", "Medium", "Careful", "Use as case-study target; do not overstate mature security program."),
        ("CI/CD", "student-feedback-system GitHub Actions workflow reference", "Medium", "Yes", "Claim CI exposure for project workflows."),
        ("Kubernetes", "roadmap Q2", "Low for current", "No as completed", "Mark Planned/In progress only."),
        ("Cloud mapping", "roadmap Q4 / AWS SAA gate", "Low for current", "No as completed", "Mark Planned/Q4."),
        ("Documentation / ADR / postmortem / evidence system", "roadmap templates; tracker report/tutorial/workbook", "High", "Yes", "Strong claim around operating system for evidence, with continued execution needed."),
    ]
    lines = [
        "# Evidence Map",
        "",
        "| Capability | Evidence Source | Confidence | Public Claim Allowed? | Notes |",
        "| ---------- | --------------- | ---------- | --------------------- | ----- |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    (NOTES / "evidence-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_outline() -> None:
    outline = """# Personal DevSecOps / Platform Engineering Dossier

## 1. Executive Summary

## 2. Current Technical Identity

## 3. Current Engineering Baseline

## 4. Homelab and Infrastructure Context

## 5. Software Project Context

## 6. DevSecOps / Platform Roadmap

## 7. Stack and Knowledge Map

## 8. Evidence and Operating System

## 9. Portfolio Case Study Plan

## 10. Interview Readiness Map

## 11. Risk Management

## 12. Public Claim Boundaries

## 13. Appendix Index

## Self-review

* Length: designed as a structured dossier, not a giant file dump.
* Roadmap duplication: summarizes roadmap and references appendices instead of copying source documents.
* Claim control: major claims are labeled Evidence-backed, Current, In progress, Planned, or Optional later.
* Current-state coverage: includes backend/project baseline, homelab context, evidence system, and gaps.
* Roadmap/evidence coverage: includes phase map, evidence ladder, portfolio plan, and public claim boundaries.
"""
    OUTLINE.write_text(outline, encoding="utf-8")


def dossier_text(sources: list[dict]) -> str:
    appendix = source_index(sources)
    return f"""# Personal DevSecOps / Platform Engineering Dossier

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

{appendix}

## Closing Standard

This dossier should be updated only when evidence improves. The goal is not to look broader than reality. The goal is to become easier to evaluate: what exists, what is practiced, what is planned, what is excluded, and what evidence supports each claim.
"""


def build_docx() -> None:
    subprocess.run(["pandoc", str(MD), "-o", str(DOCX)], check=True)


def main() -> None:
    sources = load_sources()
    write_context_notes()
    write_evidence_map()
    write_outline()
    MD.write_text(dossier_text(sources), encoding="utf-8", newline="\n")
    build_docx()
    print(NOTES / "personal-technical-context.md")
    print(NOTES / "evidence-map.md")
    print(OUTLINE)
    print(MD)
    print(DOCX)


if __name__ == "__main__":
    main()
