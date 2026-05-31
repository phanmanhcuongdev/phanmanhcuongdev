# Phase 1: Network and OS Foundations

## 1. Purpose

Build a defensible ground truth for packet paths and Linux host behavior before adding higher-level platforms. This phase turns the homelab into a controlled environment for proving how traffic moves, where it is filtered, how services listen, and how failures appear in packets, routes, processes, systemd, and logs.

## 2. Mapping To Source-Of-Truth Roadmap

- Source quarter: Q1, Network and OS Foundations.
- Primary milestone: CCNA readiness through real troubleshooting evidence.
- Theme: Stop guessing packet paths.
- Gate before Phase 2: do not start Kubernetes in the same week as a CCNA attempt or school exam block; do not move on while basic routing/VLAN/NAT/ACL behavior is still hand-wavy.

## 3. Why This Phase Exists

Every later system depends on correct assumptions about L2, L3, DNS, firewalling, processes, ports, and logs. If packet paths are guessed in Q1, Kubernetes, security, observability, and cloud mapping will become tool rituals instead of engineering knowledge.

Proxmox, VyOS, Tailscale, Headscale, MikroTik, Cisco, Ubuntu, and Docker are examples in this phase. The real subject is not a vendor; it is the path from source to destination and the evidence that proves it.

## 4. Theory To Learn

Networking:

- OSI and TCP/IP models
- Ethernet, MAC address, ARP, broadcast domain
- IPv4 subnetting, CIDR, gateway, route table lookup, longest prefix match
- VLAN access port, trunk port, 802.1Q tag
- ICMP, TCP three-way handshake, UDP
- DNS resolution path and failure modes
- NAT, stateful firewalling, ACL ordering, default deny
- control plane vs data plane
- overlay network vs underlay network

Operating systems:

- process, thread, PID, file descriptor
- socket, listening port, ephemeral port
- Linux network namespace at conceptual level
- filesystem path, mount, permissions
- systemd unit, service state, journal logs
- CPU and memory pressure at a practical level

CCNA mapping:

- subnetting speed and accuracy
- VLAN/trunk/access behavior
- routing and default gateway behavior
- ACL order and implicit deny
- NAT and return-path reasoning
- troubleshooting from symptoms, not from hope

## 5. Practical Labs

### Lab 1: Network Ground Truth Inventory

Create `network-ground-truth.md` with:

- physical topology
- switch/router ports and VLAN IDs
- Proxmox bridges and VM/LXC network attachment
- VyOS interfaces, subinterfaces, routes, NAT, firewall rules
- Headscale/Tailscale nodes, tags, ACL excerpts
- DNS resolver path
- ingress/reverse proxy path
- management access path

Commands/evidence to collect where applicable:

```text
ip addr
ip route
ip neigh
ss -tulpn
systemctl status <service>
journalctl -u <service> --since "1 hour ago"
traceroute <target>
ping <gateway>
curl -vk <url>
tcpdump -ni <interface> <filter>
nft list ruleset
iptables -S
ufw status verbose
tailscale status
headscale nodes list
show interfaces
show configuration commands
```

Also capture Proxmox network config and relevant VyOS/Tailscale/Headscale config excerpts. Redact secrets; keep policy shape visible.

### Lab 2: One Request, One Packet Path

Pick one real service path and prove each hop:

```text
Client:
DNS result:
Client route:
Client egress interface:
Gateway:
Firewall/ACL decision:
NAT behavior if any:
Server ingress interface:
Listening process:
Application response:
Logs created:
Metric or packet that moved:
```

### Lab 3: DNS Failure And Recovery

Change only one DNS variable in a controlled way: resolver, host record, search domain, or service name. Prove the difference between DNS failure, TCP failure, TLS failure, and application failure.

### Lab 4: Linux Service And Port Ownership

For one service, map:

- systemd unit -> process -> PID -> socket -> port -> firewall rule -> log line

Evidence commands:

```text
systemctl status <service>
systemctl cat <service>
ps -fp <pid>
ss -lntup
journalctl -u <service>
curl -v <service-url>
```

### Lab 5: CCNA Troubleshooting Drill

Each week, write one troubleshooting case with:

- symptom
- suspected layer
- command used
- evidence found
- root cause
- fix
- CCNA topic mapping

## 6. Evidence Required

Each Phase 1 lab must include at least:

- diagram or topology excerpt
- command transcript or summarized commands
- route table or interface state
- packet capture or logs
- firewall/ACL/NAT evidence where relevant
- systemd/log/process evidence where relevant
- root cause or confirmed non-cause
- fix or rollback
- formal concept mapping

Required Phase 1 artifacts:

1. `network-ground-truth.md`
2. C4 Context diagram for homelab services
3. Network topology diagram with VLANs, gateways, overlay nodes, and trust boundaries
4. At least 8 troubleshooting/lab reports, or 6 strong reports with better evidence
5. At least 4 postmortems, or 2 real postmortems with packet evidence
6. CCNA study log with weak topics and retest scores
7. Formal glossary with at least 80 terms

## 7. Failure Scenarios To Trigger Or Analyze

Run one failure per session. Write rollback first. Stop after 2 hours if unresolved.

### Q1-FI-01: VLAN Trunk Misconfiguration

Break one VLAN tag or trunk path. Measure ping, ARP, tcpdump, interface counters, route tables, and firewall logs. Document access vs trunk, 802.1Q tagging, broadcast domain, and why the packet did not reach the gateway.

### Q1-FI-02: Wrong Default Gateway

Set one VM/LXC to the wrong default gateway. Measure `ip route`, `traceroute`, ARP, and packet capture. Document route selection, longest prefix match, and default route behavior.

### Q1-FI-03: ACL Deny By Identity

Alter one Headscale/Tailscale tag or ACL entry so a node loses access. Measure `tailscale status`, Headscale node list, ACL excerpt, ping, SSH, and logs. Document identity-based access control and why overlay IP is a separate trust surface.

### Q1-FI-04: NAT And Return Path Failure

Create a controlled missing return route or NAT mismatch. Measure tcpdump on source/gateway/target, NAT/firewall rules, route tables, and TCP handshake behavior. Document request path and response path separately.

### Q1-FI-05: DNS Wrong Answer

Point one test hostname to the wrong IP or resolver. Measure `dig`/`nslookup`, `curl -v`, tcpdump port 53 where appropriate, and application logs. Document name resolution vs transport reachability.

### Q1-FI-06: Service Listening On Wrong Interface

Bind a test service to localhost or the wrong interface. Measure `ss -lntup`, firewall rules, curl from local and remote, and journal logs. Document socket binding and exposure scope.

## 8. Review Checklist

- Can I draw the packet path without skipping DNS, route, firewall, NAT, and process ownership?
- Can I explain the failure using standard L2/L3/L4 terms?
- Did I prove the path with commands, not memory?
- Did I capture packet/log/metric evidence before and after the fix?
- Did I separate public path, management path, and overlay path?
- Did I document what the evidence does not prove?
- Would this help me solve a similar CCNA troubleshooting question faster?

## 9. Portfolio Artifact

Create a private or public-ready artifact titled `network-ground-truth.md` or `homelab-packet-path-case-study.md` containing:

- topology diagram
- one successful request path
- one failed request path
- packet/log evidence
- root cause and fix
- trust boundary notes
- remaining risks

This can later feed the Q4 homelab architecture case study.

## 10. Exit Criteria

Do not exit Phase 1 until:

- subnetting is automatic under time pressure
- VLAN, trunk, access port, gateway, route, NAT, and ACL behavior can be explained without analogy
- at least one service path is proven end to end with packet/log/process evidence
- failed routes can be debugged from route table and packet capture
- CCNA practice scores are consistently above target threshold
- at least 8 written troubleshooting cases exist

## 11. Anti-Tool-Sprawl Guardrails

- Do not add OpenTofu, Ansible, SIEM, service mesh, or new observability tools as Phase 1 requirements.
- Use Grafana/InfluxDB only where already deployed as measurement evidence.
- Prefer `ip`, `ss`, `tcpdump`, `curl`, systemd, route tables, firewall rules, and config excerpts over new dashboards.
- Vendor-specific commands are evidence sources, not the learning objective.
