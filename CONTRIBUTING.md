# Contributing

Use [GitHub Issues](https://github.com/servodevelop/Star-Arm-102/issues/new/choose) for a reproducible problem or documentation correction. Include your arm models, software versions, selected plugin generation, command, and full error text. Remove tokens and personal information from logs.

## Documentation

English is the default for customer-facing entry pages and executable instructions. Chinese supplementary material is welcome through [README.zh.md](README.zh.md). Keep one current command sequence per integration; link to it rather than maintaining conflicting copies. Label historical material clearly.

Preserve existing package names, source directory paths, and model release links unless a migration is explicitly documented. Do not put model weights, local datasets, calibration files, or virtual environments into Git.

## Cross-brand pairing documentation

Keep customer pairing guides in `integrations/`, Python implementations in `python-sdk/`, and LeRobot plugins in `lerobot/` or their upstream repositories. Link to one authoritative command sequence. Use exact brand/model names and record LD, HD button, teleoperation, recording, and inference evidence separately. Do not label a virtual-model preview as real-follower support. See the [evidence requirements](integrations/compatibility.md).

## Naming

Use lowercase words separated by hyphens (`kebab-case`) for new repository names, resource directories, descriptive filenames, and branch names. Examples: `hardware/`, `102-ld/`, `camera-mount.step`, and `codex/phase-one-english`. Use lowercase file extensions for exported assets.

Keep conventional filenames such as `README.md`, `README.zh.md`, `LICENSE`, and `CHANGELOG.md`. Follow language and tool requirements for Python modules, ROS packages, and other integration identifiers. Migrate existing paths deliberately and update their references; check exact letter case for Linux and GitHub compatibility. Do not rename the GitHub repository or existing branches as part of a resource-file cleanup.

## Check a change

From the repository root in a Python environment:

```bash
python -m pip install -r scripts/requirements-docs.txt -r python-sdk/requirements.txt
python scripts/check_docs.py
python -m unittest discover -s tests -v
```

For hardware-affecting changes, record the actual arm, firmware, environment, calibration, and observed behavior. Software checks do not establish physical correctness. See the [validation checklist](docs/validation.md).

Follow the existing [license scope](LICENSE.md); do not replace component licenses during a documentation edit.
