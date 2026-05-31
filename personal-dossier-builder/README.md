# Personal Dossier Builder

Build project for the personal DevSecOps / Platform Engineering dossier.

## Outputs

- `output/personal-devsecops-platform-engineering-dossier.md`
- `output/personal-devsecops-platform-engineering-dossier.docx`

## Workflow

```powershell
python scripts/extract_sources.py
python scripts/build_dossier.py
python scripts/verify_dossier.py
```

The builder reads from:

- `E:\Roadmaps`
- `E:\Lap`
- public GitHub profile metadata for `phanmanhcuongdev`

It must not include secrets, tokens, private credentials, `.env` values, or unsupported claims.
