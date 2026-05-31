# Human Review Checklist

This checklist is for manual review before using the dossier publicly or for job applications.

Input files reviewed:

* `output/personal-devsecops-platform-engineering-dossier.md`
* `working-notes/source-inventory.md`
* `working-notes/personal-technical-context.md`
* `working-notes/evidence-map.md`
* `working-notes/final-verification.md`

The automated verification passed, but regex checks cannot prove whether a claim is professionally appropriate. Use this file to decide what to keep, revise, remove, or support with stronger evidence.

## 1. Claims To Check Manually

| Claim / Phrase | Current label | Why to check | Decision |
| --- | --- | --- | --- |
| `student-feedback-system` is the strongest current evidence. | Evidence-backed | Confirm the repo is clean, runnable, and representative enough to be the anchor project. | Keep / Revise / Remove / Need evidence |
| Backend work includes Spring Boot, Spring Security, JPA, Flyway, SQL Server, JWT, reporting, notifications, Docker, and GitHub Actions. | Evidence-backed | Verify these are implemented, not just configured or planned. | Keep / Revise / Remove / Need evidence |
| React/TypeScript frontend work includes role-aware navigation, API clients, reusable UI primitives, operational tables/queues, notifications, and survey/admin flows. | Evidence-backed | Confirm frontend features exist in code and screenshots/demo, not only README text. | Keep / Revise / Remove / Need evidence |
| RabbitMQ worker supports bilingual translation request/reply workflows. | Evidence-backed | Confirm worker is runnable and integrated with `student-feedback-system`, or revise to "documented worker contract". | Keep / Revise / Remove / Need evidence |
| `window_ui` demonstrates safety-first automation and platform mindset. | Evidence-backed | Verify whether it should be public-facing or kept as local/private tooling evidence. | Keep / Revise / Remove / Need evidence |
| Homelab is a controlled environment for packet path, routing, identity boundary, failure domain, and evidence discipline. | In progress | Confirm what has actually been built versus what is roadmap intent. | Keep / Revise / Remove / Need evidence |
| Q1 networking/OS/CCNA is in progress. | In progress | Check whether this reflects current status today, not just roadmap status. | Keep / Revise / Remove / Need evidence |
| Evidence system is documented through tracker workbook/report/tutorial/templates. | Evidence-backed | Verify it has actually been used beyond sample data before presenting strongly. | Keep / Revise / Remove / Need evidence |
| `student-feedback-system` can become a platform case study. | Current project, not fully packaged | Safe as a plan, but needs architecture diagrams, deployment notes, and failure evidence before public case-study claim. | Keep / Revise / Remove / Need evidence |
| SQL Server replication/database lab is a public repo visible / roadmap aligned. | Public repo visible / roadmap aligned | Verify repo exists, has meaningful README/evidence, and is yours/public. | Keep / Revise / Remove / Need evidence |
| Headscale/Tailscale/VyOS defense-in-depth case is planned from roadmap/public repo context. | Planned | Verify public `headscale-infra` repo contents before mentioning it outside private docs. | Keep / Revise / Remove / Need evidence |

## 2. GitHub Repositories Mentioned And Why To Verify

| Repository | Where it appears | Why verify | Decision |
| --- | --- | --- | --- |
| `phanmanhcuongdev/student-feedback-system` | Dossier, source inventory, public profile metadata | Primary anchor project. It must be clean, public-safe, documented, and not contain secrets or broken setup instructions. | Keep / Revise / Remove / Need evidence |
| `phanmanhcuongdev/sqlserver-replication-lab` | Public GitHub profile metadata, portfolio case-study plan | Dossier implies database/platform reliability potential. Verify README, lab evidence, and whether it supports the claim. | Keep / Revise / Remove / Need evidence |
| `phanmanhcuongdev/distributed-systems-lab` | Public GitHub profile metadata / context | Name suggests distributed systems capability. Verify whether it is mature enough to mention or should remain appendix-only. | Keep / Revise / Remove / Need evidence |
| `phanmanhcuongdev/headscale-infra` | Public GitHub profile metadata, networking/security case plan | Could expose infrastructure detail. Verify no private endpoints, keys, domains, IPs, or operationally sensitive config. | Keep / Revise / Remove / Need evidence |
| `phanmanhcuongdev/hotel-management-system` | Public GitHub profile metadata | Not central to DevSecOps dossier. Mention only if needed for backend baseline; otherwise omit. | Keep / Revise / Remove / Need evidence |
| `phanmanhcuongdev/TRR-PTIT` | Public GitHub profile metadata | Likely school/algorithm context, not central to Platform Engineering. Avoid unless it supports foundation narrative. | Keep / Revise / Remove / Need evidence |

## 3. Areas With Overclaim Risk Even Though Regex Passed

| Area | Risk | Safer wording | Decision |
| --- | --- | --- | --- |
| "Backend/full-stack project work" | Could sound broader than one main project. | "Backend/full-stack project work primarily demonstrated through `student-feedback-system`." | Keep / Revise / Remove / Need evidence |
| "System design practice" | Could sound like professional system design experience. | "Project-level system design practice." | Keep / Revise / Remove / Need evidence |
| "Platform mindset" for `window_ui` | Could sound too abstract or inflated. | "Safety-first local automation practice." | Keep / Revise / Remove / Need evidence |
| "Homelab and infrastructure context" | Could be read as mature infra operation. | "Homelab learning environment and evidence target." | Keep / Revise / Remove / Need evidence |
| "Security boundary" and "defense-in-depth" | Security terms carry high credibility burden. | "Security learning track / planned defense-in-depth case study." | Keep / Revise / Remove / Need evidence |
| "CI/CD" | GitHub Actions workflow does not automatically mean mature CI/CD. | "CI exposure through GitHub Actions workflow." | Keep / Revise / Remove / Need evidence |
| "Docker image builds" | Dockerfiles/images may exist but deployment may not. | "Docker packaging/image build evidence." | Keep / Revise / Remove / Need evidence |
| "Observability" | Roadmap/tracker references measurement, but concrete dashboards may be missing. | "Measurement layer planned; concrete observability evidence pending." | Keep / Revise / Remove / Need evidence |
| "Interview readiness" | Could imply ready now. | "Interview readiness map / improvement plan." | Keep / Revise / Remove / Need evidence |
| "Public portfolio presence" | GitHub profile exists but repo quality varies. | "Public GitHub profile with selected repositories requiring review." | Keep / Revise / Remove / Need evidence |

## 4. Parts That May Lack Evidence

| Topic | Current evidence strength | What evidence would make it stronger | Decision |
| --- | --- | --- | --- |
| Proxmox / VyOS / Headscale / Tailscale homelab | Roadmap and public repo context, not fully verified in dossier | Network topology, sanitized config snippets, packet path notes, lab reports. | Keep / Revise / Remove / Need evidence |
| VLAN / routing / ACL troubleshooting | Roadmap and tracker sample data | Real lab report with commands: `ip route`, `traceroute`, `tcpdump`, config diff, result. | Keep / Revise / Remove / Need evidence |
| Grafana / Prometheus / Loki / InfluxDB measurement | Roadmap/tracker concept | Screenshot-free metric notes, alert/runbook, metric tied to a failure. | Keep / Revise / Remove / Need evidence |
| CrowdSec / ZAP / defense-in-depth | Roadmap personal context | Sanitized incident note, logs, trust-boundary diagram, remediation ADR. | Keep / Revise / Remove / Need evidence |
| Kubernetes / CKA | Planned only | CKA-style failure reports, manifests, events/logs, restore steps. | Keep / Revise / Remove / Need evidence |
| Cloud / AWS mapping | Planned/Q4 only | Homelab-to-AWS mapping document and AWS SAA study evidence. | Keep / Revise / Remove / Need evidence |
| Production discipline | Planned/Q4 and evidence system | Postmortems, runbooks, restore drills, uptime/health checks, capacity notes. | Keep / Revise / Remove / Need evidence |
| SQL Server replication lab | Public repo mentioned | README, topology, scripts, replication failure/restore report. | Keep / Revise / Remove / Need evidence |
| `student-feedback-system` deployment path | Project docs mention Docker/CI | Deployment diagram, compose/k8s proof, environment boundary, rollback notes. | Keep / Revise / Remove / Need evidence |
| Portfolio case studies | Planned | Level 4 case study documents with diagrams/tradeoffs/evidence links. | Keep / Revise / Remove / Need evidence |

## 5. Sections To Read Carefully Before Public Use / Applying

| Section | Why read carefully | Decision |
| --- | --- | --- |
| `## 1. Executive Summary` | Sets the first impression. Make sure it sounds accurate and not inflated. | Keep / Revise / Remove / Need evidence |
| `## 2. Current Technical Identity` | Contains identity-level claims; these must match how you want recruiters/interviewers to perceive you. | Keep / Revise / Remove / Need evidence |
| `## 3. Current Engineering Baseline` | Lists concrete technologies. Verify every technology is truly implemented or used. | Keep / Revise / Remove / Need evidence |
| `## 4. Homelab and Infrastructure Context` | Homelab claims are easy to overread as production experience. Keep boundaries clear. | Keep / Revise / Remove / Need evidence |
| `## 6. DevSecOps / Platform Roadmap` | Make sure planned phases are not mistaken for current skills. | Keep / Revise / Remove / Need evidence |
| `## 7. Stack and Knowledge Map` | Current/next/optional classifications must be accurate. | Keep / Revise / Remove / Need evidence |
| `## 9. Portfolio Case Study Plan` | Case-study candidates need evidence before being used as public claims. | Keep / Revise / Remove / Need evidence |
| `## 10. Interview Readiness Map` | Useful internally, but may be too self-critical or too raw for public sharing. | Keep / Revise / Remove / Need evidence |
| `## 12. Public Claim Boundaries` | This is the most important section before using the dossier publicly. | Keep / Revise / Remove / Need evidence |
| `## 13. Appendix Index` | Check that listed sources do not expose private paths you do not want to share. | Keep / Revise / Remove / Need evidence |

## 6. Decision Checklist

Use this table as the final manual gate.

| Item | Keep | Revise | Remove | Need evidence | Notes |
| --- | --- | --- | --- | --- | --- |
| Executive summary accurately describes current state. | [ ] | [ ] | [ ] | [ ] | |
| `student-feedback-system` claims are supported by code/docs and safe for public use. | [ ] | [ ] | [ ] | [ ] | |
| Spring Boot / React / SQL Server / Flyway / MinIO / WebSocket / reporting / Docker / GitHub Actions list is accurate. | [ ] | [ ] | [ ] | [ ] | |
| RabbitMQ worker claim is supported by working code or clear docs. | [ ] | [ ] | [ ] | [ ] | |
| `window_ui` should be included in public dossier. | [ ] | [ ] | [ ] | [ ] | |
| Homelab language is clearly "in progress" and not production experience. | [ ] | [ ] | [ ] | [ ] | |
| Networking/VLAN/ACL/Tailscale statements have enough evidence or are marked planned/in progress. | [ ] | [ ] | [ ] | [ ] | |
| Kubernetes is not claimed as completed/current proficiency. | [ ] | [ ] | [ ] | [ ] | |
| Cloud/AWS is not claimed beyond planned mapping. | [ ] | [ ] | [ ] | [ ] | |
| Security/CrowdSec/ZAP/defense-in-depth language is not too strong. | [ ] | [ ] | [ ] | [ ] | |
| CI/CD wording is limited to project workflow exposure unless more evidence exists. | [ ] | [ ] | [ ] | [ ] | |
| Appendix does not reveal private/local paths you do not want public. | [ ] | [ ] | [ ] | [ ] | |
| No `.env`, token, key, password, seed credential, private endpoint, or private config appears in public version. | [ ] | [ ] | [ ] | [ ] | |
| Dossier tone is technical and factual, not marketing. | [ ] | [ ] | [ ] | [ ] | |
| Final public/apply version is shorter if needed for the audience. | [ ] | [ ] | [ ] | [ ] | |

## 7. Recommended Review Order

1. Verify the primary public repos first: `student-feedback-system`, `sqlserver-replication-lab`, `distributed-systems-lab`, `headscale-infra`.
2. Review `Public Claim Boundaries`.
3. Review `Current Engineering Baseline`.
4. Review `Portfolio Case Study Plan`.
5. Decide whether local Windows paths in Appendix are acceptable for the target audience.
6. Create a revised public version only after the checklist above is complete.
