# Contributing

Use [GitHub Issues](https://github.com/servodevelop/Star-Arm-102/issues/new/choose) for a reproducible problem or documentation correction. Include your arm models, software versions, selected plugin generation, command, and full error text. Remove tokens and personal information from logs.

## Documentation

English is the default for customer-facing entry pages and executable instructions. Chinese supplementary material is welcome through [README.zh.md](README.zh.md). Keep one current command sequence per integration; link to it rather than maintaining conflicting copies. Label historical material clearly.

Preserve existing package names, source directory paths, and model release links unless a migration is explicitly documented. Do not put model weights, local datasets, calibration files, or virtual environments into Git.

## Check a change

From the repository root in a Python environment:

```bash
python -m pip install -r tools/requirements-docs.txt -r Python_SDK/requirements.txt
python tools/check_docs.py
python -m unittest discover -s tests -v
```

For hardware-affecting changes, record the actual arm, firmware, environment, calibration, and observed behavior. Software checks do not establish physical correctness. See the [validation checklist](docs/validation.md).

Follow the existing [license scope](LICENSE.md); do not replace component licenses during a documentation edit.
