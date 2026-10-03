# Changelog

## Unreleased — English-first customer entry

- Audit coverage against previous main, restore nested ignore rules and the refactored LeRobot checkpoint evaluation entry, and record migration validation and remaining gaps in `docs/main-migration-review.md`.

- Align all eight existing bilingual README pairs; archive older Chinese guides, remove the redundant root README_zh.md redirect, and add bilingual maintenance rules and structural CI checks.

- Add cross-brand pairing navigation for Galaxea A1, Lumos Touch, YAM, and Seeed reBot; separate documented upstream paths from pending setup and validation records. Move the reBot guide into `integrations/` while preserving its old documentation link.

- Add a Wiki-linked robot and servo tool directory with a web interface preview; move repository documentation checks to `scripts/` and update workflow commands.

- Add an English homepage with setup selection, a prominent ACT model entry, demo, and official product links.
- Add first-use, wiring, compatibility, troubleshooting, and joint-mapping guides.
- Provide English Python, LeRobot, ACT inference, ROS 2, and hardware navigation; preserve Chinese supplementary material.
- Separate the release-compatible ACT plugins from the refactored HD/FL environment.
- Add explicit serial-port options and a ping-only communication check to the Python examples.
- Correct HD button examples, plugin import names, conflicting dataset paths, and unsafe stopping descriptions. Use regular plugin installation so LeRobot 0.4.1 can discover device types.
- Add issue templates and automated documentation/CLI checks. Record physical verification separately.

- Standardize top-level resource and workspace paths as `hardware/`, `media/`, `lerobot/`, `python-sdk/`, and `ros2-humble/`; update documentation, tests, and workflow commands to match.

Python module names, ROS package identifiers, model assets, and release URLs are retained. Existing external links to renamed directories need updating. License scope still requires maintainer clarification for resources without a complete license declaration.
