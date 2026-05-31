# Personal DevSecOps Tutorial Handbook

This repository is the concrete tutorial companion for the source-of-truth roadmap:

`E:\Roadmaps\phanmanhcuongdev\12-month-devsecops-roadmap.md`

The parent roadmap is the moment of truth. It defines the strategy, order, scope, gates, school-heavy constraints, and final standard. This repository only turns that strategy into executable labs, checklists, templates, evidence rules, and portfolio artifacts.

## Operating Rule

Everything as Code, from Backend Logic to Operated Infrastructure.

No new tool collecting. Break -> Measure -> Fix -> Document.

A task is not complete because a service starts. It is complete only when the evidence explains what happened with standard engineering terms.

## Repository Layout

```text
.
|-- core-roadmap/
|   `-- master-plan.md
|-- phases/
|   |-- 01-infra-network/
|   |   `-- master-plan.md
|   |-- 02-k8s-orchestration/
|   |   `-- master-plan.md
|   |-- 03-db-security-defense/
|   |   `-- master-plan.md
|   `-- 04-production-portfolio/
|       `-- master-plan.md
`-- resources/
    |-- links.md
    `-- templates.md
```

## How To Use This Repo

1. Read `E:\Roadmaps\phanmanhcuongdev\12-month-devsecops-roadmap.md` first.
2. Use `core-roadmap/master-plan.md` as the execution handbook.
3. Work through phases in order unless school-heavy mode forces scope reduction.
4. For every lab, write the hypothesis, expected behavior, measurement plan, and rollback path before touching the system.
5. Capture commands, logs, packet traces, metrics, screenshots, diagrams, and config excerpts as evidence.
6. Use `resources/templates.md` for theory notes, lab reports, postmortems, ADRs, risk registers, evidence indexes, cloud mapping, and portfolio case studies.
7. End each week by answering the Sunday Review Gate from the source roadmap.

## What This Repo Is Not

- It is not a second roadmap.
- It is not a DevSecOps tool shopping list.
- It is not a replacement for CCNA, CKA, school, or the parent roadmap.
- It is not a promise to deploy every interesting security, CI/CD, SIEM, service mesh, or cloud tool.

## Core Lab Stack

Use the existing lab first:

- Proxmox, LXC, Ubuntu Server VMs
- VyOS and existing MikroTik/Cisco/router/switch equipment
- Headscale and Tailscale
- Docker and Portainer
- Spring Boot app and FastAPI worker
- RabbitMQ, MinIO
- SQL Server and PostgreSQL
- Grafana and InfluxDB
- Ollama where already deployed
- Existing Android/ESP32 projects only when they support the main roadmap or school work

Kubernetes appears only in Phase 2 because the CKA phase requires it. Cloud/AWS appears only as mapping after local fundamentals are defensible. Extra CI/CD, SIEM, policy, registry, or security tools are optional later work and require the source roadmap gate or an ADR.

## Measurement Layer

Monitoring, logging, metrics, traces, packet captures, and database/application logs are a measurement layer across all phases. They are not a standalone dashboard-collection phase.

Use them to answer:

- What changed?
- Where did the request or packet stop?
- Which metric moved?
- Which log line proves the failure?
- Which control allowed or denied the action?
- What is still an assumption?

## Evidence Standard

Each meaningful lab should produce at least Level 2 evidence:

- formal concept
- system context
- hypothesis
- commands or summarized commands
- metrics, logs, packet capture, DB output, app output, or config excerpt
- result and limitation
- root cause where a failure was involved
- fix or rollback
- mapping to the source roadmap

Portfolio-quality work should reach Level 4: diagrams, tradeoffs, risks, failure evidence, and remaining assumptions.

## School-Heavy Mode

From August 1 to December 31, 2026, this repo obeys the source roadmap's school-heavy rule:

- GPA recovery outranks optional homelab expansion.
- Homelab work is capped at 6-8 focused hours per week.
- Certification work is capped at 4-6 focused hours per week unless an exam is scheduled within 21 days.
- If any course is Red, failure injection is banned.
- If two courses are Yellow, homelab work is documentation-only.
- AWS SAA is blocked unless CCNA and CKA are passed and school is stable.

School deliverables count as roadmap artifacts when they use formal engineering language and course rules allow reuse.

## Phase Map

| Phase | Source roadmap quarter | Focus | Main gate |
| --- | --- | --- | --- |
| 01 | Q1 | Network and OS foundations, packet path, CCNA | Packet paths are proven, not guessed |
| 02 | Q2 | Containers, Kubernetes runtime, CKA | Failures are debugged with events, logs, probes, DNS, endpoints, and RBAC |
| 03 | Q3 | Database, security, defense in depth | Trust boundaries, DB behavior, and controls are backed by evidence |
| 04 | Q4 | Production discipline, portfolio, cloud mapping | Evidence is packaged for senior review |

## Final Standard

At the end of the year, the work should support these statements without hiding behind tool names:

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
