# Resources

This page collects references for the tutorial handbook. Prefer official documentation, standards, and certification references. Do not treat this page as permission to add tools outside the source-of-truth roadmap.

## Source Of Truth

- Parent roadmap: `E:\Roadmaps\phanmanhcuongdev\12-month-devsecops-roadmap.md`
- Vietnamese companion: `E:\Roadmaps\phanmanhcuongdev\12-month-devsecops-roadmap_vi.md`

## Core Learning

Networking and OS foundations:

- Cisco CCNA overview: https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html
- Linux iproute2 manual pages: https://man7.org/linux/man-pages/man8/ip.8.html
- ss manual: https://man7.org/linux/man-pages/man8/ss.8.html
- tcpdump manual: https://www.tcpdump.org/manpages/tcpdump.1.html
- systemd documentation: https://www.freedesktop.org/wiki/Software/systemd/
- Wireshark Display Filters: https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html

Containers and Kubernetes:

- Kubernetes Documentation: https://kubernetes.io/docs/
- Kubernetes Concepts: https://kubernetes.io/docs/concepts/
- Kubernetes Tasks: https://kubernetes.io/docs/tasks/
- CKA Certification: https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
- K3s Documentation: https://docs.k3s.io/

Database and security fundamentals:

- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Microsoft SQL Server Documentation: https://learn.microsoft.com/sql/sql-server/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- NIST SP 800-61 Incident Response Guide: https://csrc.nist.gov/pubs/sp/800/61/r2/final
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

Architecture and documentation:

- C4 Model: https://c4model.com/
- arc42 Architecture Template: https://arc42.org/
- Mermaid Documentation: https://mermaid.js.org/
- ADR GitHub Organization: https://adr.github.io/

## Official Homelab Docs

Use these as references for existing lab components, not as reasons to expand scope:

- Proxmox VE Documentation: https://pve.proxmox.com/pve-docs/
- VyOS Documentation: https://docs.vyos.io/
- Tailscale ACLs: https://tailscale.com/kb/1018/acls
- Headscale Documentation: https://headscale.net/

## Certification References

- CCNA: use only as Q1 learning validation for networking foundations.
- CKA: use only as Q2 learning validation for Kubernetes troubleshooting.
- AWS SAA: optional in Q4 or later only after CCNA, CKA, school load, and local fundamentals are stable.
- AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- AWS VPC User Guide: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- AWS IAM User Guide: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
- AWS S3 User Guide: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- AWS RDS User Guide: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
- AWS Elastic Load Balancing User Guide: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html
- AWS CloudWatch User Guide: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

## Optional Later Tools

These are optional references, not phase requirements. Add one only when the parent roadmap gate allows it or an ADR proves the need.

- OpenTofu: https://opentofu.org/docs/
- Ansible: https://docs.ansible.com/
- Trivy: https://aquasecurity.github.io/trivy/
- SonarQube: https://docs.sonarsource.com/sonarqube/
- Vault: https://developer.hashicorp.com/vault/docs
- Wazuh: https://documentation.wazuh.com/
- Falco: https://falco.org/docs/

## Personal References To Maintain

- local IP plan
- VLAN ID table
- route and firewall inventory
- Headscale/Tailscale ACL notes
- backup and restore runbooks
- postmortem index
- ADR index
- evidence index
- monthly scorecards
- portfolio case study index
