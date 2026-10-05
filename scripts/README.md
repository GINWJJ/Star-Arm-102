# Repository Maintenance Scripts

[← Home](../README.md)　|　🌐 **English**

These scripts are for repository contributors. For customer-facing robot and servo tools, see the [tool directory](../tools/README.md).

- `check_docs.py`: check local file and image links in Markdown. Remote URLs and heading fragments are not checked.
- `check_readme_sync.py`: check section structure, table dimensions, images, code blocks, and link targets across existing English/Chinese README pairs. Translation meaning still requires human review.
- `requirements-docs.txt`: Python dependencies for the documentation check.

Run from the repository root with Python 3.10 or newer:

```bash
python -m pip install -r scripts/requirements-docs.txt
python scripts/check_docs.py
python scripts/check_readme_sync.py
```

The GitHub documentation workflow runs this check automatically. See [Contributing](../CONTRIBUTING.md) for the complete checks.
