# Master Plan

## Source Of Truth

This handbook implements `E:\Roadmaps\phanmanhcuongdev\12-month-devsecops-roadmap.md`.

The parent roadmap wins over this repository whenever there is a conflict. This repo explains how to execute the roadmap; it must not invent a parallel roadmap.

## Operating Principles

- Everything as Code, from Backend Logic to Operated Infrastructure.
- Learn foundations before platforms: networking, OS, packet path, routing, VLAN, NAT, ACL, Linux process/filesystem/systemd/logs, then Kubernetes and cloud mapping.
- No new tool collecting. Add a tool only when it is required by CCNA/CKA/AWS SAA, replaces an existing tool, or is approved by ADR.
- Security is not a final gate. It is a property of disciplined system design: identity, least privilege, logging, recovery, and threat boundaries from the start.
- Monitoring is a measurement layer across every lab, not a separate dashboard hobby.
- CCNA and CKA are learning milestones. AWS SAA is a bonus after school, CCNA, CKA, and fundamentals are controlled.

## Learning Loop

Use this loop for every meaningful task:

1. Break: define one controlled failure, limitation, or unknown behavior.
2. Measure: collect packets, metrics, logs, route tables, DB state, Kubernetes events, or application output.
3. Fix: restore the system using a known rollback path or permanent correction.
4. Document: write the formal concept, root cause, evidence, limitation, and runbook/postmortem update.

## Definition Of Done For A Lab

A lab is done only when it has:

- a written hypothesis and expected behavior
- a rollback plan before destructive changes
- commands or summarized commands
- measurement evidence: logs, metrics, packet capture, DB output, service status, config diff, or screenshots
- formal concept mapping
- result and limitation
- fix or restore path
- postmortem, lab report, runbook update, or ADR
- review checklist answers
- one portfolio note if the lab may become public evidence

If a system works but the behavior cannot be proven, the lab is not done. If a system fails but the failure cannot be reproduced, the lesson is incomplete.

## Evidence Rules

| Level | Meaning | Minimum contents |
| --- | --- | --- |
| 0 | Raw capture | Commands, screenshot, log, notes |
| 1 | Clean observation | Timestamp, system context, cleaned output |
| 2 | Lab report | Hypothesis, measurement, result, limitation |
| 3 | Engineering document | Postmortem or ADR readable by another engineer |
| 4 | Portfolio case study | Diagrams, tradeoffs, failure evidence, remaining risk |

Minimum weekly evidence is one of:

- theory mapping note
- cleaned diagram
- lab report or incident note
- school deliverable section mapped to formal engineering terms

## Anti-Tool-Sprawl Rules

Before adding a tool, answer in an ADR:

1. Which source-roadmap gate allows this now?
2. Which existing tool or manual process does it replace?
3. What failure or evidence gap does it solve?
4. What operational cost does it add?
5. How will it be removed if it becomes distraction?

If the answer is only "it is useful" or "it is DevSecOps", reject it.

## Mapping Homelab Work To Formal Concepts

Every lab must map one practical behavior to one formal concept:

| Practical observation | Formal concept |
| --- | --- |
| VLAN tag missing, gateway unreachable | L2 segmentation, broadcast domain, 802.1Q |
| Wrong route or return path | routing table lookup, longest prefix match, stateful NAT |
| Tailscale ACL denies SSH | identity-based access control, zero trust network access |
| Process restarts under memory pressure | cgroups, resource isolation, scheduling |
| Service selector has no endpoints | service discovery, indirection, reconciliation |
| Queue depth rises when worker stops | producer-consumer model, backpressure |
| Dirty/non-repeatable read appears | ACID, isolation levels, concurrency control |
| Public ban but private admin path works | defense in depth, trust boundary, break-glass access |

## Weekly Operating Cadence

| Day | Action | Output |
| --- | --- | --- |
| Monday | Theory mapping | One-page note connecting a formal concept to homelab evidence |
| Tuesday-Wednesday | Build or break | Controlled experiment with hypothesis and rollback plan |
| Thursday | Measure | Logs, metrics, packet capture, route table, DB state, Kubernetes events, or app errors |
| Friday | Fix and document | Incident note, root cause, permanent fix, runbook update |
| Saturday | Certification drill | CCNA in Q1, CKA in Q2, maintenance during school-heavy mode |
| Sunday | Review gate | Written answers to the five review questions |

Sunday Review Gate:

1. What did I break?
2. What did I measure?
3. What theory did I map it to?
4. What evidence did I produce?
5. What would a senior engineer reject as hand-wavy?

## How To Stop

Stop a lab when:

- the evidence proves or disproves the hypothesis
- the system is restored or the permanent fix is applied
- the root cause or current unknown is written down
- the review checklist is complete
- a portfolio note exists if the artifact may be reused publicly

Do not continue debugging past 2 focused hours without restoring service and writing a partial investigation note.

## Phase Sequence

| Phase | Focus | Primary outcome | Exit criteria |
| --- | --- | --- | --- |
| 1 | Network and OS foundations | Ground-truth packet paths and Linux/network behavior | `network-ground-truth.md`, diagrams, CCNA readiness evidence |
| 2 | Containers, Kubernetes, runtime | Small, explainable Kubernetes deployment | `cka-troubleshooting-runbook.md`, failure reports, CKA readiness evidence |
| 3 | Database, security, defense in depth | Formal trust-boundary and database evidence | Defense-in-depth case study, DB lab report, threat model |
| 4 | Production discipline and portfolio | Senior-review-ready evidence | Whitepaper, case study, ADR/postmortem index, cloud mapping |

## Required Document Types

Use `resources/templates.md` for:

- theory mapping note
- lab report
- evidence index
- postmortem
- ADR
- risk register
- senior review checklist
- portfolio case study
- homelab-to-cloud mapping

## School-Heavy Overlay

From August 1 to December 31, 2026:

- Keep only one university deliverable, one certification track, and one homelab experiment or document active.
- If any course is Red, ban new failure injection.
- If two courses are Yellow, documentation-only homelab work.
- If three courses are Yellow, certification drops to maintenance review.
- Prefer school-integrated artifacts over duplicate homelab work.
- AWS SAA stays suspended unless CCNA and CKA are passed and no course is at risk.

## Monthly Review Board

At the end of each month, score 1-5:

- formal explanation quality
- evidence quality
- debugging discipline
- diagram quality
- postmortem quality
- certification progress
- restraint from tool collecting

Also archive or kill at least one distraction: unused service, duplicate document, abandoned lab, unclear script, half-written roadmap, or tool kept only because it is interesting.

## Senior Engineer Questions

Every major artifact should answer:

1. What does this system do?
2. What are its trust boundaries?
3. What are its failure domains?
4. How do you know it is healthy?
5. How do you know it is secure enough for its purpose?
6. How do you restore it?
7. What fails first under load?
8. What assumption has not been tested?
