from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(r"E:\Roadmaps\phanmanhcuongdev\personal-dossier-builder")
NOTES = ROOT / "working-notes"
OUT = ROOT / "output"
MD = OUT / "personal-devsecops-platform-engineering-dossier.md"
DOCX = OUT / "personal-devsecops-platform-engineering-dossier.docx"
VERIFY = NOTES / "final-verification.md"

REQUIRED_SECTIONS = [
    "# Personal DevSecOps / Platform Engineering Dossier",
    "## 1. Executive Summary",
    "## 2. Current Technical Identity",
    "## 3. Current Engineering Baseline",
    "## 4. Homelab and Infrastructure Context",
    "## 5. Software Project Context",
    "## 6. DevSecOps / Platform Roadmap",
    "## 7. Stack and Knowledge Map",
    "## 8. Evidence and Operating System",
    "## 9. Portfolio Case Study Plan",
    "## 10. Interview Readiness Map",
    "## 11. Risk Management",
    "## 12. Public Claim Boundaries",
    "## 13. Appendix Index",
]
SENSITIVE = [
    r"password\s*=",
    r"token\s*=",
    r"api_key",
    r"secret\s*=",
    r"private key",
    r"BEGIN RSA PRIVATE KEY",
    r"\.env",
]
OVERCLAIM = [r"\bexpert\b", r"\bmastered\b", r"\bproduction-grade\b"]


def docx_to_md() -> str:
    result = subprocess.run(
        ["pandoc", str(DOCX), "-t", "markdown", "--wrap=none"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout


def main() -> None:
    errors = []
    md_exists = MD.exists()
    docx_exists = DOCX.exists()
    if not md_exists:
        errors.append("Markdown dossier missing")
        md_text = ""
    else:
        md_text = MD.read_text(encoding="utf-8", errors="replace")
    if not docx_exists:
        errors.append("DOCX dossier missing")
        docx_text = ""
    else:
        docx_text = docx_to_md()

    for section in REQUIRED_SECTIONS:
        if section not in md_text:
            errors.append(f"Missing section in Markdown: {section}")
        if section not in docx_text:
            errors.append(f"Missing section in DOCX readback: {section}")

    combined = md_text + "\n" + docx_text
    sensitive_hits = []
    for pattern in SENSITIVE:
        if re.search(pattern, combined, re.IGNORECASE):
            sensitive_hits.append(pattern)
    if sensitive_hits:
        errors.append("Sensitive pattern hits: " + ", ".join(sensitive_hits))

    overclaim_hits = []
    for pattern in OVERCLAIM:
        if re.search(pattern, combined, re.IGNORECASE):
            overclaim_hits.append(pattern)
    if overclaim_hits:
        errors.append("Overclaim pattern hits: " + ", ".join(overclaim_hits))

    headings = [line for line in docx_text.splitlines() if line.startswith("#")]
    lines = [
        "# Final Verification",
        "",
        f"* Markdown exists: {'yes' if md_exists else 'no'}",
        f"* DOCX exists: {'yes' if docx_exists else 'no'}",
        f"* Markdown path: `{MD}`",
        f"* DOCX path: `{DOCX}`",
        "",
        "## Heading Structure",
        "",
        *[f"* {h}" for h in headings[:80]],
        "",
        "## Checks",
        "",
        f"* Required sections present: {'yes' if not any('Missing section' in e for e in errors) else 'no'}",
        f"* Sensitive pattern check: {'pass' if not sensitive_hits else 'fail'}",
        f"* Overclaim check: {'pass' if not overclaim_hits else 'fail'}",
        f"* Appendix index present: {'yes' if '## 13. Appendix Index' in md_text else 'no'}",
        "",
        "## Result",
        "",
        "PASS" if not errors else "FAIL",
    ]
    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"* {e}" for e in errors)
    VERIFY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(VERIFY)
    print("VERIFY " + ("PASS" if not errors else "FAIL"))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
