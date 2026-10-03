# Star Arm 102 hardware resources

For third-party follower setups, see [cross-brand pairing resources](../integrations/README.md).


[Home](../README.md) · [中文](README.zh.md) · [Handoff review](handoff-review.md) · [Changes](CHANGELOG.md)

Choose your exact model: **[102-LD](102-ld/README.md)** · **[102-HD](102-hd/README.md)** · **[102-FL](102-fl/README.md)**.

LD and HD share their main mechanical body. HD additionally has a button base, button cover and UK-01 board, and different servo, cable and fastener selections. Each model has its own downloads so customers do not need to combine a common BOM with a difference list.

## Resource status

As of 2026-10-03. **Available** means the named file set is present. **Partial** means only some resources exist. **Review / Conflict** means reference files are present but cannot yet be treated as a matched production release. **Missing** means no usable model-specific file has been supplied. STEP counts cover the main printed parts named in the handoff BOM; they exclude purchased servos, electronics, accessories and native CAD sources. File availability is not manufacturing or print validation.

| Resource | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| Main printed-part STEP coverage | Available: 11/11 named parts | Available: 13/13, including 2 HD button parts | Available: 11/11 named parts |
| Whole-arm STEP | Review: LD export 2026-07-21 | Missing: no HD-labelled assembly | Review: FL export 2026-07-03 |
| Standalone printing STL | Missing | Missing | Missing |
| 3MF printing project | Review: date/version confirmation | Review: date/version confirmation | Conflict: link1 settings versus BOM |
| Excel BOM | Review: assembled and kit references | Review: handoff reference | Review: overseas-shipment reference |
| PDF / DWG drawings | Review: July 13 reference and older files | Partial: shared LD geometry reference only | Review: July 13 reference |
| Model-specific URDF and meshes | Missing: candidate held for review | Missing | Missing: unlabelled candidate held for review |
| Assembly guide / videos | Missing | Missing | Missing |
| Confirmed production revision / physical validation | Pending | Pending | Pending |

## Download by purpose

- Edit geometry: each model's `step/parts/` and `step/assembly/`.
- Print parts: `printing/stl/` and `printing/3mf/`. Current 3MF files are handoff references requiring review.
- Check materials and quantities: `bom/` provides Excel workbooks, with source/revision status.
- Check dimensions: `drawings/pdf/` and `drawings/cad/`.
- Assemble: `assembly-guide/` will provide steps, photos, video links and Wiki tutorials.
- Use a robot model: each model's `robot-description/` records applicability and status. The [existing ROS model](robot-description/README.md) remains separate and has not been replaced by unverified handoff exports.

## Versions and licensing

Source dates, conflicts and excluded files are documented in the [handoff review](handoff-review.md). The [import manifest](handoff-imports.json) maps original filenames to destinations and SHA-256 hashes. Original workbooks, drawings and 3MF files retain their content and language; English indexes do not imply those source files have been translated.

Hardware licensing remains unresolved; see [license scope](../LICENSE.md). No new license is granted by copying or renaming files.
