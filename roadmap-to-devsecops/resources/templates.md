# Execution Templates

Use these templates to turn roadmap work into evidence. Keep them short during school-heavy weeks, but do not remove sections that prove behavior.

## Theory Note

```text
# Theory Note: <formal concept>

Date:
Phase:
Source roadmap mapping:
System touched:

## Definition

## Formal Terms

## Where It Appears In The Homelab

## Evidence That Proves It

Commands, logs, packet capture, metrics, DB output, config excerpt, or diagram path.

## Failure Mode That Exposes It

## What I Still Cannot Explain Cleanly

## Next Small Experiment
```

## Lab Report

```text
# Lab Report: <title>

Date:
Phase:
Evidence level:
Source roadmap mapping:

## Formal Concept

## Practical System

## Hypothesis

## Expected Behavior

## Experiment Design

## Rollback Plan

## Commands

## Observations

## Measurement Evidence

Logs, metrics, packet capture, route table, DB state, Kubernetes events, application output, config diff, or screenshots.

## Result

## Root Cause Or Confirmed Non-Cause

## Fix Or Restore Path

## What This Proves

## What This Does Not Prove

## Runbook Or Postmortem Update

## Portfolio Note
```

## Evidence Index

```text
# Evidence Index

| Artifact | Type | Phase | Formal concept | System touched | Evidence level | Reviewer concern | Path | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | Theory note / Lab report / Postmortem / ADR / Diagram / Runbook / Case study | | | | 0-4 | | | |
```

## Postmortem

```text
# Postmortem: <incident title>

Date:
Severity:
Duration:
Affected systems:
Source roadmap mapping:

## Impact

## Timeline

## Detection

How was the issue found? Include logs, alerts, packet traces, metrics, user-facing error, or manual command.

## Root Cause

## Trigger

## Resolution

## What Went Well

## What Went Wrong

## Preventive Actions

## Evidence

## Runbook Changes

## What This Does Not Prove
```

## Architecture Decision Record

```text
# ADR-NNN: <title>

Status: Proposed | Accepted | Rejected | Superseded
Date:
Phase:
Source roadmap mapping:

## Context

## Decision

## Alternatives Considered

## Consequences

## Verification

What command, log, metric, test, or review proves the decision works?

## Review Or Expiry Date
```

## Risk Register

Use this weekly during August-December school-heavy mode.

| Course / Workstream | Current risk | Next deadline | Required output | Roadmap mapping | Action this week |
| --- | --- | --- | --- | --- | --- |
| | Green / Yellow / Red | | | | |

Rules:

- Red: deadline within 7 days, failed quiz/midterm, unclear rubric, missing group dependency, or broken production-like service.
- Yellow: unclear requirement, weak understanding, or deadline within 14 days.
- Green: on track.
- If any course is Red, homelab failure injection is banned.
- If two courses are Yellow, homelab work becomes documentation-only.
- If three courses are Yellow, certification work drops to maintenance review.

## Senior Review Checklist

```text
# Senior Review Checklist: <system or artifact>

Reviewer date:
Artifact path:

1. What does this system do?
2. What are its trust boundaries?
3. What are its failure domains?
4. How do you know it is healthy?
5. How do you know it is secure enough for its purpose?
6. How do you restore it?
7. What fails first under load?
8. What assumption has not been tested?
9. What evidence would be rejected as hand-wavy?
10. What is the next smallest improvement?
```

## Portfolio Case Study

```text
# Case Study: <title>

## Summary

What system was built, operated, broken, measured, fixed, and documented?

## Source Roadmap Mapping

Q1 / Q2 / Q3 / Q4 mapping and formal concepts.

## System Context

## Architecture Diagram

## Request Or Packet Path

## Trust Boundaries

## Failure Or Experiment

## Evidence

Commands, logs, metrics, packet captures, DB output, Kubernetes events, scan reports, config excerpts, diagrams.

## Root Cause Or Key Lesson

## Fix Or Design Decision

## Tradeoffs

## Remaining Risks

## Links To ADRs / Postmortems / Runbooks

## What A Senior Reviewer Might Challenge
```

## Homelab-To-Cloud Mapping

```text
# Homelab-To-Cloud Mapping

Date:
Prerequisites: CCNA passed? CKA passed? School load stable?

| Homelab concept | Local evidence path | AWS equivalent | Similarity | Difference | Risk of false analogy | Next study action |
| --- | --- | --- | --- | --- | --- | --- |
| VLAN/subnet | | VPC subnet | | | | |
| firewall/ACL | | Security Group/NACL | | | | |
| MinIO | | S3 | | | | |
| SQL Server/PostgreSQL | | RDS | | | | |
| reverse proxy/ingress | | ALB/NLB | | | | |
| Tailscale/Headscale | | private connectivity / identity-aware access | | | | |
| Grafana/InfluxDB | | CloudWatch / managed observability | | | | |
```

