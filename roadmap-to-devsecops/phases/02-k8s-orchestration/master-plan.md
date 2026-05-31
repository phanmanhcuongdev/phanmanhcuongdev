# Phase 2: Containers, Kubernetes Runtime, and CKA

## 1. Purpose

Move from Linux process/network fundamentals into containers and Kubernetes without treating either as magic. Build a small, explainable deployment path and debug failures using runtime, Kubernetes, and distributed-systems terms.

## 2. Mapping To Source-Of-Truth Roadmap

- Source quarter: Q2, Kubernetes, Application Runtime, and CKA.
- Primary milestone: CKA readiness through timed troubleshooting and written failure reports.
- Theme: Stop treating containers as magic.
- Entry condition: Phase 1 packet path, routing, DNS, firewall, and Linux service evidence exists.

## 3. Why This Phase Exists

Kubernetes hides Linux, networking, and scheduling behind API objects. This phase exists to connect Pod/Service/Ingress behavior back to processes, cgroups, namespaces, DNS, endpoints, logs, and health checks. The target is a small cluster that can be explained under pressure, not a large platform full of optional add-ons.

## 4. Theory To Learn

Container/runtime foundations:

- image vs container
- registry concept without requiring a new registry product
- process isolation, namespaces, cgroups
- bind mount, volume, filesystem layers
- environment variables and secret material
- container network path and port mapping
- logs/stdout/stderr and restart behavior

Kubernetes:

- Pod, ReplicaSet, Deployment
- Service, selector, Endpoints/EndpointSlice
- Ingress as an entry path concept
- ConfigMap, Secret
- Volume and persistent data risks
- readiness vs liveness
- requests, limits, scheduling, eviction
- namespace and RBAC
- events, describe, logs, rollout history

CKA mapping:

- object inspection
- YAML editing under time pressure
- failed rollout debug
- service connectivity debug
- DNS debug
- RBAC and namespace scoping
- resource pressure and probe failure

## 5. Practical Labs

### Lab 1: Container Before Kubernetes

Run one simple container and prove:

```text
image used:
process inside container:
port exposed:
mounts:
environment variables:
logs:
network path from host:
resource limit if any:
cleanup command:
```

Use Docker/Portainer only if already present. The learning target is runtime behavior.

### Lab 2: Kubectl Object Inspection

For Pod, Deployment, Service, and Events, capture desired and observed state:

```text
kubectl get pods -o wide
kubectl describe pod <name>
kubectl logs <pod>
kubectl get events --sort-by=.lastTimestamp
kubectl get deploy,rs,pod,svc,endpoints,endpointslice
kubectl explain deployment.spec.template.spec.containers
```

Write what each command proves and what it does not prove.

### Lab 3: Stateless Workload

Deploy one stateless app. Evidence must show:

- scheduling result
- Service selector
- endpoints created
- DNS name resolution inside cluster
- logs
- internal connectivity
- rollback/deletion path

### Lab 4: One Real Service

Deploy a reduced Spring Boot service with:

- ConfigMap for non-secret config
- Secret for sensitive test config
- readiness probe
- liveness probe
- requests and limits
- logs linked to one request

### Lab 5: One Dependency Only

Add only one dependency first: RabbitMQ, PostgreSQL, or SQL Server where practical. Document:

- connection string source
- Secret/ConfigMap split
- network path
- logs on success and failure
- backup/restore concern if stateful

### Lab 6: RBAC And Namespace Boundary

Create one non-admin identity or service account and prove what it can and cannot do. Evidence must include commands that fail as expected.

## 6. Evidence Required

Each Phase 2 lab must include:

- YAML or command summary
- `kubectl get/describe/logs/events` evidence
- endpoint or DNS evidence where networking is involved
- resource/probe status where runtime health is involved
- application log tied to one request where possible
- metric/log/packet evidence if already available
- rollback command or baseline manifest
- formal concept mapping

Required Phase 2 artifacts:

1. Minimal Kubernetes deployment for one real system path
2. `cka-troubleshooting-runbook.md`
3. C4 Container diagram for the Kubernetes deployment
4. UML sequence diagram: client -> ingress/service -> backend -> queue -> worker -> database/object storage
5. At least 10 Kubernetes failure reports, or 5 strong CKA-style reports
6. At least 2 RBAC/least-privilege ADRs
7. CKA attempt or scheduled exam only when practice results justify it

## 7. Failure Scenarios To Trigger Or Analyze

Run only after a known-good baseline. Save manifests first. One failure per session.

### Q2-FI-01: Broken Service Selector

Change a Service selector so it points to no pods. Measure endpoints, service description, ingress response, and application errors. Explain service discovery, indirection, and reconciliation.

### Q2-FI-02: Readiness Probe Failure

Make readiness fail while the process still runs. Measure pod events, endpoint removal, and user-facing availability. Explain readiness vs liveness and traffic routing.

### Q2-FI-03: CoreDNS Failure

Only in a disposable cluster or after exporting manifests. Measure pod DNS lookup, CoreDNS logs, service name resolution, and restore path. Do not run during school-heavy weeks with deadlines.

### Q2-FI-04: Resource Pressure

Set unrealistic CPU/memory limits for a non-critical workload. Measure OOMKilled, restart count, CPU throttling, events, and available Grafana/InfluxDB metrics. Explain cgroups, scheduling, requests, and limits.

### Q2-FI-05: Queue Backlog

Stop or slow the translation worker while messages enter RabbitMQ. Measure queue depth, backend behavior, worker logs, and latency. Explain producer-consumer model and backpressure.

### Q2-FI-06: Bad Image Or Bad Env

Deploy a wrong image tag or bad environment variable. Measure ImagePullBackOff, CrashLoopBackOff, logs, events, and rollout status. Explain image resolution, container startup, and configuration failure.

### Q2-FI-07: Failed Rollout And Rollback

Deploy a broken version and recover with rollout history. Measure before/after availability and explain Deployment revision behavior.

## 8. Review Checklist

- Did I prove container runtime behavior before Kubernetes behavior?
- Can I connect Pod behavior to process, namespace, cgroup, filesystem, and network concepts?
- Can I debug from events, describe, logs, endpoints, DNS, and RBAC without deleting everything?
- Did I save a known-good baseline before failure injection?
- Did I avoid adding Harbor, Kyverno, Falco, service mesh, or extra platform tools as requirements?
- Did the lab produce CKA-style command evidence?
- Can I rebuild the object from YAML under time pressure?

## 9. Portfolio Artifact

Create `cka-troubleshooting-runbook.md` and one compact case study:

- baseline architecture
- one broken service path
- events/logs/endpoints evidence
- root cause
- restore command
- formal concept mapping

This artifact should show that Kubernetes failures are understandable through runtime and distributed-system behavior.

## 10. Exit Criteria

Take CKA only when:

- failed pods can be debugged without deleting everything
- first inspection points are clear: events, describe, logs, endpoints, DNS, RBAC
- a small deployment can be rebuilt from YAML under time pressure
- failures can be explained with Kubernetes control-plane terms
- at least 5 strong CKA-style failure reports exist

## 11. Anti-Tool-Sprawl Guardrails

- Week 1 is Kubernetes orientation only.
- Do not migrate the full real application in week 1.
- Do not require Harbor, Kyverno, Falco, service mesh, or SIEM in this phase.
- Use K3s/Kubernetes because CKA requires Kubernetes, not because a bigger platform looks better.
- If CCNA slips, close CCNA before ramping CKA in the same week.
