# 12-Month DevSecOps Roadmap

Owner: Phan Manh Cuong  
Role target: Backend-to-DevSecOps / Platform Engineer  
Operating rule: Không sưu tầm tool mới. Break -> Measure -> Fix -> Document.

## 0. Hard Constraints

Roadmap này không phải là một motivational checklist. Đây là một chương trình
kỷ luật kỹ thuật. Mục tiêu là biến công việc homelab thực chiến thành kiến thức
computer science, networking, operating systems, database, và distributed
systems có thể giải thích một cách chính quy.

### Non-Negotiable Rules

1. Không thêm tool mới trừ khi thỏa một trong các điều kiện sau:
   - Tool đó bắt buộc cho CCNA, CKA, hoặc AWS SAA.
   - Tool đó thay thế một tool hiện có và tool cũ được gỡ bỏ.
   - Tool đó được phê duyệt bằng văn bản thông qua một ADR.
2. Mỗi lab phải tạo ra evidence:
   - diagram
   - command transcript hoặc bản tóm tắt commands
   - metrics hoặc packet capture
   - root cause
   - fix
   - postmortem hoặc cập nhật runbook
3. Mỗi tuần phải map một practical experiment với một formal concept từ:
   - computer networking
   - operating systems
   - database systems
   - distributed systems
   - software architecture
   - information security
4. Nếu bạn không thể giải thích bằng thuật ngữ chuẩn, bạn chưa hiểu đủ sâu.
5. Nếu system chạy được nhưng bạn không chứng minh được vì sao, việc đó chưa
   hoàn tất.
6. Nếu system fail nhưng bạn không reproduce được failure, bạn chưa học được gì
   từ nó.

### Core Lab Stack

Chỉ dùng lab hiện có:

- Proxmox
- LXC và Ubuntu Server VMs
- VyOS
- Headscale và Tailscale
- Docker
- Portainer
- Spring Boot app
- FastAPI worker
- RabbitMQ
- MinIO
- SQL Server
- PostgreSQL
- Grafana và InfluxDB
- Ollama ở nơi đã deploy sẵn
- Thiết bị MikroTik/Cisco/router/switch hiện có
- Các dự án Android/ESP32 hiện có chỉ khi chúng hỗ trợ roadmap chính

Không thêm Kubernetes cho đến khi phase CKA yêu cầu. Không thêm observability,
security, service mesh, CI/CD, hoặc cloud tools ngoài phạm vi cho đến khi quý
hiện tại cho phép.

## 0.1. Calendar Overlay: August-December School-Heavy Mode

Roadmap này phải tôn trọng tải học thật từ tháng 8 đến tháng 12 năm 2026. Giả
định 6-7 môn đại học, khoảng 18-21 tín chỉ. Đây không phải side quest. Đây là
workload chính trong giai đoạn đó.

Tham chiếu học kỳ 7 PTIT cho ngành Information Systems thường gồm các môn như:

- Phan tich va thiet ke he thong thong tin
- Xu ly anh
- IOT va ung dung
- Quan ly du an phan mem
- Hoc phan tu chon chuyen nganh, thường 6 tín chỉ

Đây là tham chiếu, không phải cam kết. Thời khóa biểu thực tế là nguồn quyết
định. Khi lịch thật được công bố, cập nhật section này và cắt scope ngay lập
tức.

### School-Heavy Operating Rule

Từ ngày 1 tháng 8 đến ngày 31 tháng 12 năm 2026:

1. Phục hồi GPA đại học có ưu tiên cao hơn mọi homelab expansion tùy chọn.
2. Không chuẩn bị AWS SAA trừ khi CCNA và CKA đã pass và điểm ở trường ổn định.
3. Homelab work bị giới hạn ở 6-8 giờ tập trung mỗi tuần.
4. Certification work bị giới hạn ở 4-6 giờ tập trung mỗi tuần, trừ khi exam đã
   được schedule trong vòng 21 ngày.
5. Mỗi môn học phải tạo ra ít nhất một artifact cũng củng cố DevSecOps roadmap.
6. Failure injection được giảm tần suất, không bị loại bỏ.
7. Nếu một school assignment có thể map vào homelab evidence, hãy làm vậy.
   Không tạo hai workload riêng biệt.

### Academic Risk Register

Từ tháng 8 đến tháng 12, duy trì academic risk register hàng tuần.

Dùng bảng này:

| Course | Current risk | Next deadline | Required output | Roadmap mapping | Action this week |
|---|---|---|---|---|---|

Risk levels:

- Green: đúng tiến độ
- Yellow: requirement chưa rõ, hiểu chưa chắc, hoặc deadline trong vòng 14 ngày
- Red: deadline trong vòng 7 ngày, thiếu group dependency, fail quiz/midterm,
  hoặc grading rubric chưa rõ

Rules:

1. Nếu bất kỳ môn nào là Red, homelab failure injection bị cấm.
2. Nếu hai môn là Yellow, homelab work chỉ được phép là documentation.
3. Nếu ba môn là Yellow, certification work giảm xuống mức maintenance review.
4. Nếu group project phụ thuộc vào bạn, deliverable đó cao hơn mọi lab tùy
   chọn.
5. Mục tiêu không phải là "cân bằng mọi thứ". Mục tiêu là tránh academic debt
   âm thầm tích tụ.

### Course-to-Roadmap Mapping

Dùng việc học ở trường như một forcing function để dùng formal language.

| School course | Roadmap artifact | Homelab anchor |
|---|---|---|
| Phan tich va thiet ke he thong thong tin | C4 Context, C4 Container, UML sequence, use-case model | `student-feedback-system` |
| Quan ly du an phan mem | WBS, risk register, milestone plan, retrospective | roadmap này và một repo được chọn |
| IOT va ung dung | lab report, sensor/API flow, threat boundary | ESP32/FaizGear chỉ khi môn học yêu cầu |
| Xu ly anh | formal report về preprocessing/model limits | `identity_number` hoặc ESP32-CAM chỉ khi môn học yêu cầu |
| Distributed systems / cloud / service elective | failure-domain report, service dependency map | RabbitMQ, DB, K8s, Headscale |
| Data science / BI elective | data pipeline hoặc metrics interpretation report | Grafana/InfluxDB, SQL/Postgres |
| Network/security elective | ACL, trust boundary, packet path report | VyOS, Headscale, CrowdSec case |

### School-Heavy Weekly Cadence

Trong giai đoạn tháng 8-tháng 12, thay weekly cadence mặc định bằng lịch này:

- Monday: 45 phút theory mapping từ một bài giảng trên lớp sang một homelab
  concept.
- Tuesday hoặc Wednesday: một lab block 90 phút, chỉ khi school deadlines đang
  được kiểm soát.
- Thursday: document evidence cho school hoặc homelab.
- Friday: không làm việc mới; đóng notes, diagrams, và backlog.
- Saturday: 2-3 giờ certification drill.
- Sunday: review grades, deadlines, và roadmap scope.

Hard rule: nếu có hai school deadlines đến hạn trong vòng 7 ngày, toàn bộ
homelab failure injection tùy chọn tạm dừng. Technical work duy nhất được phép
là documentation trực tiếp hỗ trợ school deliverable.

### Chaos Mode: Midterms, Finals, and Assignment Collisions

Thực tế sẽ phá calendar. Khi PTIT midterms, finals, group projects, hoặc các
bài documentation 20 trang va chạm với roadmap, chuyển sang Chaos Mode ngay lập
tức.

Chaos Mode triggers khi bất kỳ điều kiện nào đúng:

- hai hoặc nhiều university deadlines rơi vào trong vòng 7 ngày
- một exam trong vòng 5 ngày
- ngủ dưới 6 giờ trong hai đêm liên tiếp
- một lab failure chưa được giải quyết sau 2 giờ
- một group assignment phụ thuộc vào phần đóng góp của bạn trong tuần này
- mental fatigue làm việc context switching giữa school, Kubernetes, routing,
  và backend chậm thấy rõ

Chaos Mode rules:

1. Dừng toàn bộ failure injection mới.
2. Dừng toàn bộ infrastructure changes trừ emergency restore.
3. Chỉ giữ ba tasks cho tuần:
   - pass school deadline
   - giữ services ổn định
   - viết một theory mapping note ngắn
4. Thay lab reports bằng "evidence parking":
   - dán commands, screenshots, logs, hoặc notes vào một file tạm
   - formalize chúng sau trong buffer week
5. Certification work chuyển thành maintenance only:
   - 30-45 phút review cards hoặc subnetting drills
   - không học topic CKA/AWS mới trong exam week
6. Chạy bộ lúc 10 PM được phép như một reset, không phải cách kéo dài ngày làm
   việc. Sau khi chạy, chọn sleep hoặc một recovery task 30 phút, không bắt đầu
   debug session mới.

Chỉ exit Chaos Mode khi:

- school deadline gần nhất đã submit
- sleep đã hồi phục
- weekly backlog vừa trên một trang
- không production-like homelab service nào đang ở trạng thái broken

### Work-In-Progress Limit

Tại mọi thời điểm, chỉ các mục này được active:

- một university deliverable
- một certification track
- một homelab experiment hoặc document

Mọi thứ khác đưa vào backlog. Context switching được xem là chi phí thật,
không phải lỗi tính cách.

## 1. Weekly Operating Cadence

### Monday: Theory Mapping

Chọn một formal concept và viết một note một trang:

- definition
- formal terms
- nơi nó xuất hiện trong homelab của bạn
- command nào chứng minh nó
- failure mode nào làm nó lộ ra

Examples:

- VLAN trunking -> IEEE 802.1Q tagging -> VyOS subinterface behavior
- Process scheduling -> CPU contention -> Proxmox VM/LXC resource pressure
- Transaction isolation -> dirty/non-repeatable/phantom reads -> SQL Server lab
- Control plane vs data plane -> Headscale vs WireGuard/Tailscale traffic
- Liveness/readiness -> Kubernetes service routing và failure isolation

### Tuesday-Wednesday: Build or Break

Chạy một controlled experiment. Phải có hypothesis trước khi thực thi.

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

Thu thập evidence:

- Grafana/InfluxDB metrics nếu có
- logs
- packet capture
- route table
- firewall rules
- database state
- application errors
- Kubernetes events trong phase CKA

### Friday: Fix and Document

Fix system và viết:

- incident note
- root cause
- permanent fix
- prevention
- runbook change

### Saturday: Certification Drill

Dùng Saturday cho certification work:

- Q1: CCNA
- Q2: CKA
- Q3: school-heavy mode; AWS SAA bị chặn trừ khi CCNA và CKA đã pass
- Q4: review, exam closure, và portfolio consolidation

### Sunday: Review Gate

Trả lời các câu hỏi này bằng văn bản:

1. Tôi đã break gì?
2. Tôi đã measure gì?
3. Tôi đã map nó với theory nào?
4. Tôi đã tạo evidence gì?
5. Senior engineer sẽ reject điểm nào vì còn hand-wavy?

Nếu câu trả lời cho câu 5 chưa rõ, tuần đó chưa hoàn tất.

## 2. Required Document Types

Tạo và duy trì các documents này dưới `E:\Roadmaps\evidence` hoặc repo folder
phù hợp với project.

### Evidence Quality Ladder

Evidence có nhiều level. Không giả vờ mọi notes đều ngang nhau.

- Level 0: raw command, screenshot, log, hoặc messy note
- Level 1: cleaned observation có timestamp và system context
- Level 2: lab report có hypothesis, measurement, result, và limitation
- Level 3: postmortem hoặc ADR mà một engineer khác có thể đọc được
- Level 4: portfolio-quality case study có diagrams và tradeoffs

Trong school-heavy mode, Level 2 evidence là đủ cho hầu hết các tuần. Level 4
chỉ bắt buộc cho public case study được chọn.

Minimum viable weekly evidence:

- một theory mapping note, hoặc
- một cleaned diagram, hoặc
- một incident/lab note, hoặc
- một phần school deliverable được map sang formal engineering terms

Nếu một tuần tạo ra school documentation chất lượng cao, nó được tính. Không
duplicate nó thành một homelab document riêng trừ khi course rules cấm reuse.

### ADR: Architecture Decision Record

Dùng format này:

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

Dùng format này:

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

Dùng format này:

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

Mỗi quarter phải có diagrams dùng standard notation:

- C4 Context diagram
- C4 Container diagram
- UML sequence diagram
- network topology diagram
- data flow diagram

Diagrams phải dùng terms nhất quán:

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
Theme: Dừng đoán mò packet paths.

Transition rule:

- Tuần cuối của Q1 là buffer week, không phải lab week mới.
- Dùng tuần đó để đóng CCNA notes, clean diagrams, archive unfinished
  experiments, và viết danh sách ngắn "What I still do not understand".
- Không bắt đầu Kubernetes trong cùng tuần với CCNA exam attempt hoặc school
  exam block.

### Focus

Academic focus:

- computer networks
- operating system basics
- Linux process và network stack basics
- routing, switching, subnetting, NAT, ACLs
- control plane vs data plane

Practical focus:

- chứng minh traffic di chuyển như thế nào trong homelab
- document rõ physical, virtual, và overlay network
- làm Headscale/Tailscale/VyOS behavior giải thích được bằng standard
  networking terms

### University Foundations to Repair

- Computer Networks:
  - OSI model và TCP/IP model
  - Ethernet, ARP, ICMP, TCP, UDP
  - subnetting và CIDR
  - routing table lookup
  - VLAN và trunking
  - NAT và firewalling
  - ACL ordering và default deny
- Operating Systems:
  - process, thread, file descriptor
  - sockets
  - memory pressure
  - CPU scheduling basics
  - Linux namespaces ở mức conceptual

### Deliverables

Đến cuối Q1, deliver:

1. `network-ground-truth.md`
   - physical topology
   - Proxmox bridges
   - VyOS interfaces
   - VLANs
   - Headscale/Tailscale nodes
   - route tables
   - DNS path
   - ingress path
2. C4 Context diagram cho homelab services.
3. Network topology diagram với VLANs, gateways, overlay nodes, và trust
   boundaries.
4. Ít nhất 8 lab reports.
5. Ít nhất 4 postmortems.
6. CCNA study log có weak topics và retest scores.
7. Một formal glossary ít nhất 80 terms.

Quality override:

- Sáu lab reports mạnh tốt hơn tám lab reports yếu.
- Hai postmortems thật có packet evidence tốt hơn bốn postmortems hình thức.
- Không tạo incidents giả chỉ để đủ quota.

### Failure Injection Tasks

Global failure-injection safety rule:

- Mọi failure injection phải có rollback command hoặc restore path trước khi
  bắt đầu.
- Maximum active debug time là 2 giờ.
- Nếu không tìm được root cause trong 2 giờ, dừng lại, restore service, và viết
  partial incident note.
- Partial evidence được chấp nhận. Một tuần học bị phá thì không.
- Không bao giờ chạy destructive failure injection sau 10 PM.
- Không bao giờ chạy destructive failure injection cùng ngày với major school
  deadline.

#### Q1-FI-01: VLAN Trunk Misconfiguration

Break:

- Misconfigure một VLAN tag hoặc trunk path trong controlled window.

Measure:

- ping
- ARP table
- tcpdump trên relevant interfaces
- VyOS interface counters
- Grafana network metrics nếu có

Fix:

- restore trunk hoặc VLAN interface config

Document:

- giải thích access port vs trunk port
- giải thích 802.1Q tagging
- giải thích vì sao packet không đến gateway

Formal concept:

- data link layer segmentation
- broadcast domain
- VLAN tagging

#### Q1-FI-02: Wrong Default Gateway

Break:

- Set một VM/LXC dùng wrong default gateway.

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

- Remove hoặc alter một Headscale/Tailscale tag để một node biến mất khỏi
  expected netmap.

Measure:

- `tailscale status`
- Headscale node list
- ACL file
- ping và SSH behavior

Fix:

- reapply correct tag và policy

Document:

- vì sao identity-based ACL mạnh hơn source-IP-only filtering
- vì sao ZAP/CrowdSec case của bạn quan trọng
- vì sao Tailscale IP là một trust surface riêng so với public ISP IP

Formal concept:

- defense in depth
- identity-based access control
- zero trust network access

#### Q1-FI-04: NAT and Return Path Failure

Break:

- Tạo một case asymmetric routing hoặc missing return route có kiểm soát.

Measure:

- tcpdump trên source, gateway, và target
- NAT table hoặc firewall logs nếu có
- route tables

Fix:

- restore correct route/NAT behavior

Document:

- giải thích request path và response path riêng biệt
- giải thích vì sao ping hoặc TCP handshake fail

Formal concept:

- stateful NAT
- symmetric vs asymmetric routing
- TCP three-way handshake

### Q1 Certification Gate

Bạn được phép schedule CCNA chỉ khi:

- subnetting tự động dưới áp lực thời gian
- bạn có thể giải thích VLAN/trunk/access port không cần analogy
- bạn có thể debug failed route từ route table và packet capture
- bạn consistently score trên target threshold trong practice exams
- bạn có ít nhất 8 written troubleshooting cases

Nếu CCNA trượt lịch:

- Không stack CCNA catch-up và CKA ramp-up trong cùng một tuần.
- Dành một buffer week để đóng CCNA trước khi bắt đầu Kubernetes.
- Nếu school-heavy mode đã bắt đầu, CCNA ưu tiên hơn CKA cho đến khi pass hoặc
  được reschedule chính thức.

## 4. Q2: Kubernetes, Application Runtime, and CKA

Timebox: Months 4-6  
Primary exam target: CKA  
Theme: Dừng xem containers như phép màu.

Transition rule:

- Week 1 của Q2 chỉ là Kubernetes orientation.
- Không migrate real application trong week 1.
- Không break CoreDNS, không RBAC hardening, không queue backlog drill trong
  week 1.
- Mục tiêu là hiểu cluster objects và command workflow, không phải chứng minh
  production readiness.

### Focus

Academic focus:

- operating systems
- distributed systems basics
- service discovery
- scheduling
- health checking
- storage và state
- RBAC và least privilege

Practical focus:

- deploy một phiên bản rút gọn của real application stack trên Kubernetes
- debug failures bằng events, logs, probes, DNS, service selectors, và network
  paths
- giữ cluster nhỏ, observable, và explainable

Scope ladder:

1. Stage 0: local `kubectl` fluency, pods, deployments, services, logs,
   describe, events.
2. Stage 1: một stateless demo workload.
3. Stage 2: một Spring Boot service với config và probes.
4. Stage 3: thêm một dependency duy nhất, ưu tiên RabbitMQ hoặc PostgreSQL.
5. Stage 4: thêm ingress và RBAC.
6. Stage 5: chỉ khi đó mới chạy failure injection.

Không skip stages. Nếu một stage mất lâu hơn dự kiến, giảm final deliverables
thay vì nén stages.

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
  - leader/follower như một concept
  - retries và backoff
  - partial failure
  - health checks
  - eventual consistency như một concept
- Software Engineering:
  - deployment architecture
  - dependency boundaries
  - interface contracts

### Deliverables

Đến cuối Q2, deliver:

1. Minimal Kubernetes deployment cho một real system:
   - Spring Boot backend
   - frontend hoặc test client
   - RabbitMQ
   - PostgreSQL hoặc SQL Server nếu practical
   - MinIO nếu cần
2. `cka-troubleshooting-runbook.md`.
3. C4 Container diagram cho Kubernetes deployment.
4. UML sequence diagram cho một request path:
   - client -> ingress/service -> backend -> queue -> worker -> database/object
     storage
5. Ít nhất 10 Kubernetes failure reports.
6. Ít nhất 2 RBAC/least-privilege ADRs.
7. CKA exam attempt hoặc scheduled exam.

Quality override:

- Năm CKA-style failure reports có commands, events, root cause, và restore
  steps tốt hơn mười notes hời hợt.
- Nếu CKA exam preparation đang active, ưu tiên timed troubleshooting hơn
  polished writing.

Minimum viable Q2 nếu school pressure hoặc CCNA delay xảy ra:

1. Một stateless app được deployed và debugged.
2. Một Spring Boot service deployed với ConfigMap/Secret và probes.
3. Một dependency được integrated.
4. Năm Kubernetes failure reports, không phải mười.
5. `cka-troubleshooting-runbook.md` với command recipes chất lượng cao.
6. Chỉ schedule CKA nếu practice results đủ cơ sở.

### Failure Injection Tasks

Global Kubernetes failure-injection safety rule:

- Chỉ chạy failure injection sau khi cluster có known-good baseline.
- Save baseline YAML hoặc command state trước khi thay đổi bất cứ thứ gì.
- Một failure mỗi session.
- Maximum active debug time là 2 giờ.
- Nếu failure không được resolve trong 2 giờ, restore baseline và viết một
  "failed investigation" note. Failed investigations vẫn được tính nếu evidence
  trung thực.
- CoreDNS và cluster-wide failures bị cấm trong school-heavy weeks.

#### Q2-FI-01: Broken Service Selector

Break:

- Change một Service selector để nó không point tới pod nào.

Measure:

- `kubectl get endpoints`
- `kubectl describe svc`
- app error behavior
- ingress response

Fix:

- restore selector

Document:

- giải thích Kubernetes Service map stable virtual IP sang pod endpoints như
  thế nào

Formal concept:

- service discovery
- indirection
- control plane reconciliation

#### Q2-FI-02: Readiness Probe Failure

Break:

- Làm readiness probe fail trong khi process vẫn đang chạy.

Measure:

- `kubectl describe pod`
- events
- endpoint changes
- app availability

Fix:

- sửa probe path, port, hoặc app readiness logic

Document:

- khác biệt giữa liveness và readiness
- vì sao traffic không nên được route tới unready pods

Formal concept:

- health checking
- failure detection

#### Q2-FI-03: CoreDNS Failure

Break:

- Tạo một DNS failure có kiểm soát bên trong cluster.

Measure:

- pod DNS lookup
- CoreDNS logs
- service name resolution

Fix:

- restore CoreDNS configuration

Document:

- giải thích DNS resolution path bên trong Kubernetes

Formal concept:

- name resolution
- distributed service discovery

Scope guard:

- Chỉ chạy việc này trong disposable cluster hoặc sau khi export toàn bộ
  relevant manifests.
- Không chạy việc này trong bất kỳ tuần nào có university deadlines.
- Nếu bạn không thể giải thích cách restore CoreDNS trước khi break nó, bạn
  không được phép chạy experiment.

#### Q2-FI-04: Resource Starvation

Break:

- Set CPU/memory limits phi thực tế cho một service.

Measure:

- pod restarts
- OOMKilled events
- CPU throttling
- Grafana metrics nếu integrated

Fix:

- set requests và limits hợp lý

Document:

- giải thích requests vs limits
- giải thích cgroups và resource isolation

Formal concept:

- OS resource management
- scheduling
- isolation

Scope guard:

- Bắt đầu với một non-critical pod.
- Không starve database hoặc queue services trong school-heavy weeks.
- Mục tiêu là observe cgroups và scheduling behavior, không phải tạo
  multi-service outage.

#### Q2-FI-05: Queue Backlog

Break:

- Làm chậm hoặc stop translation worker trong khi messages tiếp tục đi vào
  RabbitMQ.

Measure:

- queue depth
- backend response behavior
- worker logs
- latency

Fix:

- restart worker hoặc scale replicas
- thêm backpressure hoặc retry policy khi phù hợp

Document:

- giải thích asynchronous processing và backpressure

Formal concept:

- producer-consumer model
- queueing
- backpressure

Scope guard:

- Dùng test queue hoặc test namespace.
- Cap message volume trước experiment.
- Experiment kết thúc khi queue depth behavior được chứng minh, không phải khi
  system đã "fully tuned".

### Q2 Certification Gate

Bạn được phép thi CKA chỉ khi:

- bạn có thể debug failed pods mà không xóa sạch mọi thứ
- bạn biết nên nhìn đâu trước: events, describe, logs, endpoints, DNS, RBAC
- bạn có thể rebuild một small deployment từ YAML dưới áp lực thời gian
- bạn có thể giải thích vì sao failure xảy ra bằng Kubernetes control plane
  terms

## 5. Q3: Database, Security, and Defense in Depth

Timebox: Months 7-9  
Secondary exam target: AWS SAA chỉ khi CCNA và CKA đã xong hoặc được kiểm soát
chắc chắn.  
Theme: Dừng gọi scanners là security.

School-heavy override:

- Nếu Q3 overlap tháng 8-tháng 12, Q3 không phải maximal lab quarter.
- Xem Q3 là quarter cho documentation, database, security, và school
  integration.
- Minimum viable Q3 tốt hơn một kế hoạch anh hùng làm hỏng GPA.
- AWS SAA mặc định bị suspend trong giai đoạn này.

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

- biến ZAP/CrowdSec/Tailscale case thành một formal defense-in-depth case study
- harden một application path end to end
- chứng minh identity, network, app auth, logs, và rate limits tương tác như
  thế nào
- chuyển school assignments thành formal engineering documents thay vì xem
  chúng là academic burden tách biệt

### University Foundations to Repair

- Database Systems:
  - relational model
  - normalization
  - indexing
  - transactions
  - ACID
  - isolation levels
  - replication
  - backup và restore
- Information Security:
  - CIA triad
  - authentication vs authorization
  - least privilege
  - threat modeling
  - defense in depth
  - audit log integrity
  - vulnerability management

### Deliverables

Đến cuối Q3, deliver:

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
   - replication/failover analysis nếu feasible
3. Threat model cho `student-feedback-system`.
4. Data flow diagram với trust boundaries.
5. Security ADRs:
   - secret handling
   - admin access path
   - network ACL policy
   - audit logging policy
6. Ít nhất 6 security failure reports.
7. AWS SAA decision checkpoint:
   - chỉ bắt đầu nếu CCNA và CKA hoàn tất hoặc gần hoàn tất

Quality override:

- Defense-in-depth case study là artifact chính của Q3.
- Không chạy sáu security experiments nếu một trust-boundary case được document
  tốt đã dạy được core lesson.

Nếu Q3 overlap tháng 8-tháng 12, dùng reduced nhưng stricter deliverable set
này:

1. `defense-in-depth-case-study.md` hoàn tất và polished.
2. Một database lab report, không phải bốn:
   - chọn transaction isolation, indexing, backup/restore, hoặc
     replication/failover
   - bao gồm formal theory và measured evidence
3. Một school-integrated architecture package:
   - C4 Context diagram
   - C4 Container diagram
   - một UML sequence diagram
   - written mapping tới "Phan tich va thiet ke he thong thong tin"
4. Tối đa hai failure reports, nhưng cả hai phải chất lượng cao.
5. Một risk register dùng software project management language:
   - scope
   - schedule
   - technical risk
   - operational risk
   - mitigation
6. Không AWS SAA trừ khi:
   - CCNA passed
   - CKA passed
   - không school course nào at risk
   - weekly school backlog trống

### Failure Injection Tasks

#### Q3-FI-01: ZAP Scan and Layered Defense

Break:

- Chạy controlled scan against test environment cho đến khi rate limiting hoặc
  ban logic trigger.

Measure:

- application logs
- reverse proxy logs
- CrowdSec logs
- source IP classification
- Tailscale source identity

Fix:

- define policies riêng cho public IP access và overlay network access
- tránh trust Tailscale IP đơn thuần
- document emergency admin path riêng

Document:

- giải thích vì sao có thể SSH qua Tailscale sau public ban vừa hữu ích vừa
  nguy hiểm
- define layer nào sở hữu control nào

Formal concept:

- defense in depth
- trust boundary
- fail-safe vs fail-open
- break-glass access

School-heavy version:

- Không chạy aggressive scans trong exam hoặc assignment weeks.
- Dùng evidence ZAP/CrowdSec/Tailscale trước đó nếu đủ.
- Dành thời gian viết trust-boundary analysis cho đúng.

#### Q3-FI-02: Database Isolation Anomaly

Break:

- Tạo concurrent transactions để demonstrate một isolation anomaly.

Measure:

- transaction logs nếu có
- SQL output
- lock behavior

Fix:

- chọn isolation level hoặc transaction design phù hợp

Document:

- giải thích anomaly bằng formal terms

Formal concept:

- ACID
- isolation level
- concurrency control

School-heavy version:

- Đây là Q3 database experiment ưu tiên vì nó map gọn với database theory và có
  thể document thành report ngắn.

#### Q3-FI-03: Missing Index Under Load

Break:

- Remove hoặc tránh dùng một useful index trong test query path.

Measure:

- query plan
- latency
- CPU/disk impact
- Grafana metrics nếu có

Fix:

- add index và compare execution plan

Document:

- giải thích selectivity, index scan, table scan, và cost

Formal concept:

- database indexing
- query optimization

#### Q3-FI-04: Secret Exposure Drill

Break:

- Đặt fake secret vào một controlled branch hoặc local test file.

Measure:

- secret scan result nếu có
- review process

Fix:

- remove secret
- rotate fake credential
- document prevention

Document:

- giải thích vì sao secret rotation quan trọng kể cả sau khi removal

Formal concept:

- credential lifecycle
- least privilege
- incident response

#### Q3-FI-05: Backup Restore Failure

Break:

- Simulate backup corruption hoặc missing restore dependency.

Measure:

- restore logs
- RTO
- RPO
- data consistency

Fix:

- repair backup procedure
- add restore verification

Document:

- giải thích backup không thật cho đến khi restore được test

Formal concept:

- disaster recovery
- RTO/RPO
- durability

School-heavy version:

- Chỉ chạy nếu database course workload nhẹ. Nếu không, giữ việc này cho Q4.

## 6. Q4: Production Discipline, Cloud Mapping, and Portfolio

Timebox: Months 10-12  
Optional exam target: AWS SAA  
Theme: Trở nên đáng tin trên giấy tờ, không chỉ trong terminal.

School-heavy override:

- Nếu Q4 overlap tháng 8-tháng 12, Q4 là consolidation quarter, không phải
  expansion quarter.
- Việc chính là pass school đúng nghĩa, đóng CCNA/CKA nếu còn pending, và
  chuyển existing work thành readable evidence.
- AWS SAA là bonus chỉ sau khi semester được kiểm soát.

### Focus

Academic focus:

- software architecture
- distributed systems
- cloud architecture
- reliability engineering
- cost và capacity planning

Practical focus:

- consolidate evidence thành professional portfolio
- chuyển homelab architecture thành standard diagrams và written explanations
- map on-prem concepts sang AWS SAA concepts chỉ sau khi local fundamentals ổn
  định
- chuyển school project reports thành portfolio-quality documentation nơi
  course rules cho phép

### University Foundations to Repair

- Software Architecture:
  - modularity
  - coupling và cohesion
  - ports and adapters
  - C4 model
  - UML sequence và component diagrams
- Distributed Systems:
  - partial failure
  - timeout và retry
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

Đến cuối Q4, deliver:

1. Public portfolio update:
   - profile README cleaned
   - top 5 repos documented với evidence
   - diagrams và postmortems linked
2. `homelab-architecture-whitepaper.md`
   - business goal
   - constraints
   - architecture
   - tradeoffs
   - risks
   - security controls
   - observability
   - recovery plan
3. Ít nhất 12 postmortems tổng cộng trong năm.
4. Ít nhất 20 lab reports tổng cộng trong năm.
5. Ít nhất 12 ADRs tổng cộng trong năm.
6. Một polished case study:
   - `student-feedback-system` end-to-end
   - hoặc Headscale/Tailscale/VyOS defense-in-depth networking case
7. AWS SAA attempt chỉ khi Q1-Q3 gates được satisfy.

Quality override:

- Một case study sống sót qua senior review là win condition.
- Portfolio polish không được lấy thời gian khỏi final exams.

Nếu Q4 overlap tháng 8-tháng 12, dùng reduced deliverable set này:

1. Hoàn tất toàn bộ school deliverables với formal diagrams và terminology.
2. Hoàn thành một polished public case study, không phải ba.
3. Đưa total yearly evidence lên ít nhất:
   - 8 postmortems
   - 12 lab reports
   - 8 ADRs
4. Chỉ update top 3 repos, không phải top 5.
5. Nếu CCNA hoặc CKA còn unfinished, hoàn tất việc đó trước AWS SAA.
6. AWS SAA chỉ được vào active study sau major school deadline cuối cùng.

### Failure Injection Tasks

#### Q4-FI-01: Full Request Path Failure

Break:

- Introduce một failure ở từng layer qua các test runs riêng biệt:
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
- packet path nếu relevant

Fix:

- restore từng layer
- update runbook

Document:

- giải thích blast radius và detection path

Formal concept:

- dependency graph
- failure domain
- observability

School-heavy version:

- Chỉ chạy một full request path failure mỗi tháng.
- Ưu tiên failures hỗ trợ school report hoặc portfolio case study.

#### Q4-FI-02: Capacity Pressure

Break:

- Generate controlled load cho đến khi một bottleneck xuất hiện.

Measure:

- CPU
- memory
- disk I/O
- database latency
- queue depth
- application latency

Fix:

- tune resource allocation hoặc reduce bottleneck

Document:

- giải thích bottleneck và capacity limit

Formal concept:

- performance modeling
- utilization
- saturation

School-heavy version:

- Giữ việc này thành một weekend experiment duy nhất sau khi midterm/final
  pressure thấp.
- Không dành cả semester để build load-testing platform.

#### Q4-FI-03: Access Control Regression

Break:

- Vô tình over-permit một non-admin identity trong test ACL/RBAC policy.

Measure:

- resource nào trở nên reachable
- logs
- policy diff

Fix:

- restore least privilege
- add verification checklist

Document:

- giải thích vì sao policy tests là bắt buộc

Formal concept:

- least privilege
- access control model
- regression testing

### AWS SAA Gate

Chỉ bắt đầu AWS SAA nếu:

- CCNA đã pass
- CKA đã pass, không chỉ là "planned"
- Q1-Q3 deliverables tồn tại
- school load tháng 8-tháng 12 ổn định và không môn nào at risk
- bạn có thể map homelab concepts sang AWS:
  - VLAN/subnet -> VPC subnet
  - firewall/ACL -> Security Group/NACL
  - MinIO -> S3
  - SQL Server/Postgres -> RDS concept
  - reverse proxy/ingress -> ALB/NLB concept
  - Tailscale/Headscale -> private connectivity và identity-aware access
  - Grafana/InfluxDB -> CloudWatch/managed observability concept

## 7. Monthly Review Board

Cuối mỗi tháng, chạy một personal review board. Viết câu trả lời ra, không nghĩ
thầm.

Trong tháng 8-tháng 12, chạy một weekly academic review ngắn trước monthly
review:

1. Môn nào gần Red nhất?
2. School deliverable nào có thể trở thành roadmap artifact?
3. Roadmap task nào phải bị cắt trong tuần này?
4. Certification còn thực tế trong tuần này, hay chỉ maintenance?
5. Tôi có ngủ đủ để debug an toàn không?

### Scorecard

Rate mỗi mục từ 1 đến 5:

- formal explanation quality
- evidence quality
- debugging discipline
- diagram quality
- postmortem quality
- certification progress
- restraint from tool collecting

### Kill List

Mỗi tháng, kill hoặc archive ít nhất một distraction:

- unused service
- duplicated document
- abandoned lab
- unclear script
- half-written roadmap
- tool chỉ tồn tại vì nó thú vị

### Senior Engineer Questions

Answer:

1. System này làm gì?
2. Trust boundaries của nó là gì?
3. Failure domains của nó là gì?
4. Làm sao biết nó healthy?
5. Làm sao biết nó đủ secure cho mục đích của nó?
6. Làm sao restore nó?
7. Dưới load, thứ gì sẽ fail trước?
8. Assumption nào chưa được test?

## 8. Corrected Personal Context

Internship ezCloud của bạn kéo dài 1 năm, không phải 6 tháng. Hãy xem đó là
industry exposure có ý nghĩa, nhưng đừng overvalue nó nếu môi trường không phù
hợp cho intern growth. Bài học không phải là "industry vô dụng". Bài học là
bây giờ bạn cần filters mạnh hơn khi chọn môi trường:

- Team có review code nghiêm túc không?
- Có production incidents để học không?
- Intern có được trao ownership cùng guardrails không?
- Architecture decisions có được giải thích không?
- Có feedback loop không?

ZAP/CrowdSec/Tailscale case của bạn là một security lesson thực tế mạnh. Bài
học đúng không phải là "tôi bypass được ban". Bài học đúng là:

- controls phải được layered
- identity source matters
- overlay networks là các trust surfaces riêng
- admin break-glass paths phải intentional
- public protection và private access policy phải được modeled riêng
- logs phải giữ đủ context để phân biệt public attacker behavior với private
  administrative access

## 9. Final Standard

Sau 12 tháng, bạn phải có thể ngồi trước một senior panel và defend system của
mình mà không núp sau tool names.

Bạn phải có thể nói:

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

Nếu bạn làm được điều đó một cách consistent, GPA sẽ bớt gây hại vì engineering
evidence của bạn mạnh hơn transcript. Nếu bạn không làm được, homelab chỉ là
tiếng ồn đắt tiền.
