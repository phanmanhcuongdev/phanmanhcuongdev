# Everything as Code, from Backend Logic to Operated Infrastructure

<p align="left">
  <img src="https://komarev.com/ghpvc/?username=phanmanhcuongdev&label=Profile%20Views&color=0f172a&style=for-the-badge" alt="Profile views" />
  <img src="https://img.shields.io/badge/Focus-Backend%20to%20DevSecOps-0f172a?style=for-the-badge" alt="Focus" />
  <img src="https://img.shields.io/badge/Mindset-System%20First-1d4ed8?style=for-the-badge" alt="Mindset" />
  <img src="https://img.shields.io/badge/PTIT-Information%20Systems-e11d48?style=for-the-badge" alt="PTIT" />
</p>

<p align="left">
  <a href="mailto:phanmanhcuong2411@gmail.com">
    <img src="https://img.shields.io/badge/Email-0f172a?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.facebook.com/cuong.phanmanh.77312">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook" />
  </a>
  <a href="https://www.instagram.com/phanmanhcuongdev">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="https://github.com/phanmanhcuongdev">
    <img src="https://img.shields.io/badge/GitHub-111827?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

## About Me

I am **Phan Manh Cuong**, a **3rd-year Information Systems student at PTIT** and a **Backend Intern** working across **.NET** and **Java**.

I do not see software as isolated source code. I see it as a system that has to be designed, deployed, secured, observed, recovered, and improved over time.

My direction is clear:

> **From backend development to DevSecOps — not by theory alone, but by operating real systems.**

I care about what happens after the code leaves the IDE: how services are deployed, how traffic reaches them, how logs and metrics expose problems, how failures are recovered, and how security decisions shape the entire architecture.

Outside engineering, I am also a **regular apheresis donor**. That long-term habit shapes the way I work: steady, consistent, and committed to building value that lasts.

## What I Actually Operate

My homelab is my personal engineering ground. It is not only a collection of machines, but a small environment where I practice infrastructure, networking, observability, and security under real constraints.

### Core Infrastructure

My homelab runs on a **Dual Xeon E5-2676 v3 platform (24 Cores / 48 Threads)** with 64GB RAM and a GTX 1050Ti, combining both physical networking gear and hypervisor infrastructure. This environment is where I test real problems before bringing solutions to production mindsets.

The environment includes:

* **Hybrid Networking & Routing:** Operating physical switches and routers (Cisco, Mikrotik RB450G, RB2011) alongside virtualized **VyOS** instances for deep packet routing, VLAN segmentation, and access control.
* **Secure Access & Overlay Networks:** Managing a self-hosted VPN mesh network using **Headscale & Tailscale** (with custom domain routing via `headscale.cuongdso.id.vn`) and enforcing strict **WireGuard** policies across device cohorts.
* **Proxmox Virtualization:** Orchestrating multiple VMs and LXC containers (Ubuntu Server, Kali Linux) for strict service isolation, security testing, and self-hosted workflows (RabbitMQ, MinIO, databases).
* **Full-Stack Observability:** Instrumenting the entire infrastructure with **Prometheus, InfluxDB, Loki, and Grafana** to capture metrics, aggregate logs, and monitor system health in real-time.

This is where theory becomes operational skill, debugging deep into how packets travel and how systems recover.

## Engineering Mindset

Many developers stop when the feature works.

I want to understand the full path around that feature:

* How the request enters the system.
* How traffic moves across Layer 2 and Layer 3.
* How services are isolated and exposed.
* How logs, metrics, and alerts help during failure.
* How access is controlled.
* How recovery works when SSH, VPN, or routing breaks.
* How documentation prevents the system from becoming tribal knowledge.

That is the kind of engineering I am building toward: backend logic with infrastructure awareness, security thinking, and operational maturity.

## Operational Lessons I Care About

My homelab has taught me that infrastructure is not only about tools. It is about discipline.

Some principles I try to follow:

* **Always keep a recovery path.** VPN, SSH, and reverse proxy are useful, but console access can save the system when networking fails.
* **Expose less by default.** Private mesh access is often better than public exposure.
* **Monitor for understanding, not decoration.** Dashboards should help explain system behavior during incidents.
* **Document the network.** If the topology only exists in your head, it will eventually become a problem.
* **Treat security as part of design.** Hardening, access control, and logs should not be added only at the end.
* **Respect physical constraints.** Power, heat, and cost are also architecture concerns.

## Featured Work

| Project / System | What it represents |
| --- | --- |
| [**CoreAuth**](https://github.com/phanmanhcuongdev/CoreAuth) | 🔐 **NEW** Android FIDO2/U2F Security Key framework (Rust daemon + Kotlin/Compose UI). Implements Legacy U2F over USB HID with transactional lifecycle, independent biometric modes (Fingerprint, Face, NFC), and zero-trust protocol isolation. Security Key does not invoke Android BiometricPrompt—it's a hardware-grade authenticator in your pocket. |
| [**roadmap-to-devsecops**](https://github.com/phanmanhcuongdev/roadmap-to-devsecops) | My personalized learning journey, homelab notes, and system hardening guides as I move from backend toward DevSecOps. Evidence-based labs with formal methodology for each phase. |
| [**student-feedback-system**](https://github.com/phanmanhcuongdev/student-feedback-system) | An enterprise-style academic project: Java 21 + Spring Boot 4 backend with Hexagonal Architecture, Reactor async patterns, and modular API design—how backend architecture should feel at scale. |
| [**translation-ai-worker**](https://github.com/phanmanhcuongdev/translation-ai-worker) | A backend worker service consuming RabbitMQ translation requests, generating bilingual (Vietnamese/English) content using FastAPI, and demonstrating async patterns in a real-world integration. |
| [**FaizGear**](https://github.com/phanmanhcuongdev/FaizGear) | 🤖 **NEW** A Faiz Phone (Kamen Rider 555) simulator built with **Jetpack Compose** and Kotlin. Acts as a Zero-Trust IoT remote controller for Proxmox homelab—blending mobile UI, hardware control, and security in one experimental package. |
| **Homelab Mesh Infrastructure** | A private network environment using Headscale/Tailscale, Proxmox, VyOS, Prometheus/Grafana stack, and security layers including network segmentation and access control. The operational ground where backend meets infrastructure. |
| [**headscale-infra**](https://github.com/phanmanhcuongdev/headscale-infra) | Documentation and configuration for self-hosted Headscale + Nginx overlay network infrastructure. Includes architecture decisions, failure recovery, and real-world ConfigFS/UDC management. |
| [**distributed-systems-lab**](https://github.com/phanmanhcuongdev/distributed-systems-lab) | SQL Server replication lab combining Publisher–Distributor–Subscriber topology with Headscale mesh networking for geographic distribution testing. |
| [**sqlserver-replication-lab**](https://github.com/phanmanhcuongdev/sqlserver-replication-lab) | Docker Compose setup for SQL Server replication testing—how data moves, where it breaks, and how to recover. |
| [**IOT-v-ng-d-ng**](https://github.com/phanmanhcuongdev/IOT-v-ng-d-ng) | IoT / embedded systems experimentation ground—extending the security-key and device-controller paradigm into real-world hardware challenges. |

## Tech Stack

### Backend Engineering

<p align="left">
  <img src="https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" alt=".NET" />
  <img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/Java-EA580C?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/Spring%20Boot-3FA34D?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/REST%20API-0F172A?style=for-the-badge&logo=swagger&logoColor=white" alt="REST API" />
  <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
</p>

### Mobile & Systems Programming

<p align="left">
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Jetpack%20Compose-3FA34D?style=for-the-badge&logo=android&logoColor=white" alt="Jetpack Compose" />
  <img src="https://img.shields.io/badge/Rust-CE422B?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

### Infrastructure, Networking & Operations

<p align="left">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox" />
  <img src="https://img.shields.io/badge/VyOS-1E293B?style=for-the-badge" alt="VyOS" />
  <img src="https://img.shields.io/badge/Ubuntu%20Server-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu Server" />
  <img src="https://img.shields.io/badge/Windows%20Server-2563EB?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Server" />
  <img src="https://img.shields.io/badge/Tailscale-0F172A?style=for-the-badge&logo=tailscale&logoColor=white" alt="Tailscale" />
  <img src="https://img.shields.io/badge/Headscale-1F2937?style=for-the-badge&logo=tailscale&logoColor=white" alt="Headscale" />
  <img src="https://img.shields.io/badge/NetBox-2563EB?style=for-the-badge" alt="NetBox" />
</p>

### Networking & Security Infrastructure

<p align="left">
  <img src="https://img.shields.io/badge/Cisco-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white" alt="Cisco" />
  <img src="https://img.shields.io/badge/MikroTik-282A36?style=for-the-badge&logo=mikrotik&logoColor=white" alt="MikroTik" />
  <img src="https://img.shields.io/badge/VyOS-1E293B?style=for-the-badge&logo=letsencrypt&logoColor=white" alt="VyOS" />
  <img src="https://img.shields.io/badge/WireGuard-88171A?style=for-the-badge&logo=wireguard&logoColor=white" alt="WireGuard" />
  <img src="https://img.shields.io/badge/Tailscale-0F172A?style=for-the-badge&logo=tailscale&logoColor=white" alt="Tailscale" />
  <img src="https://img.shields.io/badge/Headscale-1F2937?style=for-the-badge&logo=tailscale&logoColor=white" alt="Headscale" />
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
</p>

### Containers, Delivery & Observability

<p align="left">
  <img src="https://img.shields.io/badge/Docker-0EA5E9?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Portainer-13BEF9?style=for-the-badge&logo=portainer&logoColor=white" alt="Portainer" />
  <img src="https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white" alt="MinIO" />
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-0F172A?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
  <img src="https://img.shields.io/badge/Loki-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Loki" />
</p>

### Observability & Data

<p align="left">
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
  <img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white" alt="InfluxDB" />
  <img src="https://img.shields.io/badge/Loki-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Loki" />
  <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>

## Engineering Map

```mermaid
flowchart LR
    A[Backend Engineering]
    B[Infrastructure]
    C[Networking]
    D[Security]
    E[Observability]
    F[Homelab Cyber Range]
    G[DevSecOps Direction]

    A --> F
    B --> F
    C --> F
    D --> F
    E --> F
    F --> G

    A <--> B
    B <--> C
    C <--> D
    D <--> E
    E <--> A

    style F fill:#dcfce7,stroke:#15803d,stroke-width:2px,color:#0f172a
    style G fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#0f172a
    style A fill:#dbeafe,stroke:#1d4ed8,color:#0f172a
    style B fill:#f8fafc,stroke:#475569,color:#0f172a
    style C fill:#f8fafc,stroke:#475569,color:#0f172a
    style D fill:#f8fafc,stroke:#475569,color:#0f172a
    style E fill:#f8fafc,stroke:#475569,color:#0f172a
```

## Current Direction

I am currently focusing on:

1. **Backend architecture**
   Building maintainable services with clear boundaries, practical API design, and database-aware thinking. Currently implementing enterprise patterns: Hexagonal Architecture, Ports & Adapters, JWT/OAuth flows, and async message processing.

2. **Infrastructure as Code**
   Reducing manual drift and making environments reproducible. Exploring OpenTofu and Ansible for infrastructure provisioning, and Kubernetes orchestration with K3s for production-mindedness.

3. **Private networking and secure access**
   Using mesh VPN patterns (Headscale, Tailscale) and network segmentation to reduce unnecessary public exposure. Implementing zero-trust principles and strict VPN ACLs.

4. **CI/CD and security in delivery**
   Moving security checks closer to the development workflow instead of treating them as a final gate. Exploring SonarQube, Trivy scanning, and container image validation.

5. **Observability and incident readiness**
   Building systems that can explain themselves when something goes wrong. Instrumenting with Prometheus, Grafana, Loki for metrics, logs, and visibility. Creating operational dashboards for understanding system behavior during failures.

6. **Security-first system design**
   Recently diving into FIDO2/U2F protocol implementation (**CoreAuth**), understanding hardware-grade authentication, and exploring how security decisions cascade through architecture—from daemon privilege boundaries to USB gadget lifecycle management.

## Contribution & Stats

### 📊 On GitHub

<p align="center">
  <a href="https://github.com/phanmanhcuongdev">
    <img src="https://img.shields.io/badge/GitHub%20Profile-phanmanhcuongdev-0f172a?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/followers/phanmanhcuongdev?style=for-the-badge&label=Followers&color=1d4ed8&logo=github&logoColor=white" alt="GitHub Followers" />
  <img src="https://img.shields.io/badge/Total%20Repos-14+-475569?style=for-the-badge&logo=github&logoColor=white" alt="Total Repositories" />
</p>

### 🛠️ Main Technology Languages

<p align="center">
  <img src="https://img.shields.io/badge/Java-20%25-EA580C?style=flat-square&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/C%23/.NET-18%25-239120?style=flat-square&logo=csharp&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/Python-15%25-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Kotlin-12%25-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Rust-8%25-CE422B?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/TypeScript-7%25-3178c6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Other-20%25-666666?style=flat-square" alt="Other" />
</p>

### 🎯 Key Metrics

<p align="center">
  <img src="https://img.shields.io/badge/Pinned%20Repos-6-3FA34D?style=for-the-badge&logo=github&logoColor=white" alt="Pinned Repos" />
  <img src="https://img.shields.io/badge/Public%20Contributions-Active-15803d?style=for-the-badge&logo=github&logoColor=white" alt="Public Contributions" />
</p>

## Closing Note

I am building toward a version of engineering where backend, infrastructure, networking, observability, and security are not separate tracks.

They are one system.

> "Security is not a gate at the end. It is a property of systems designed with discipline from the start."
