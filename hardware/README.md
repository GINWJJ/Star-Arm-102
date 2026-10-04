# Star Arm 102 hardware resources

For third-party follower setups, see [cross-brand pairing resources](../integrations/README.md).


[Home](../README.md) · [中文](README.zh.md) · [Handoff review](handoff-review.md) · [Changes](CHANGELOG.md)

Choose your exact model: **[102-LD](102-ld/README.md)** · **[102-HD](102-hd/README.md)** · **[102-FL](102-fl/README.md)**.

LD and HD share their main mechanical body. HD additionally has a button base, button cover and UK-01 board, and different servo, cable and fastener selections. Each model has its own downloads so customers do not need to combine a common BOM with a difference list.

<a id="product-specifications"></a>

## Product specifications & datasheets

Compare the three models using the entries below. No standalone product datasheet PDFs have been identified in this repository yet; mechanical drawings are separate resources. Until the datasheets are added, consult the specifications on each official product page.

| Resource | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| Product role | Lightweight leader | Pose-holding leader | Follower for task execution |
| Official product specifications | [View LD specifications](https://fashionstar.com.hk/store/product/star-arm-102-ld/) | [View HD specifications](https://fashionstar.com.hk/store/product/star-arm-102-hd/) | [View FL specifications](https://fashionstar.com.hk/store/product/star-arm-102-fl/) |
| Standalone datasheet PDF | Pending | Pending | Pending |

[Series specifications and joint mapping](../docs/specifications.md) · [Mechanical resource status](#resource-status)

## Directory structure

The LD layout is expanded below. HD and FL use the same resource categories; the additional drawings/images directory shown under LD contains its existing drawing preview. Individual downloads and historical files are omitted.

```text
hardware/
├── README.md
├── README.zh.md
├── CHANGELOG.md
├── 102-ld/
│   ├── README.md
│   ├── README.zh.md
│   ├── step/
│   │   ├── assembly/
│   │   └── parts/
│   ├── printing/
│   │   ├── stl/
│   │   └── 3mf/
│   ├── drawings/
│   │   ├── pdf/
│   │   ├── cad/
│   │   └── images/
│   ├── bom/
│   ├── assembly-guide/
│   │   └── images/
│   └── robot-description/
│       ├── urdf/
│       └── meshes/
├── 102-hd/
├── 102-fl/
├── robot-description/
│   ├── README.md
│   ├── urdf/
│   │   └── star-arm-102.urdf
│   └── meshes/
├── handoff-review.md
├── handoff-review.zh.md
├── handoff-imports.json
├── handoff-inventory.json
└── handoff-step-validation.json
```

`step/assembly/` contains CAD assemblies; `assembly-guide/` is for customer assembly instructions. Model-specific `robot-description/` directories track pending resources, while the shared `hardware/robot-description/` contains the existing ROS model. A directory may currently contain only a README: consult the resource status table before downloading or manufacturing.

## Resource status

As of 2026-10-04. **Available** means the named file set is present. **Partial** means only some resources exist. **Review / Conflict** means reference files are present but cannot yet be treated as a matched production release. **Missing** means no usable model-specific file has been supplied. STEP counts cover the main printed parts named in the handoff BOM; they exclude purchased servos, electronics, accessories and native CAD sources. File availability is not manufacturing or print validation.

| Resource | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| Main printed-part STEP coverage | Available: 11/11 named parts | Available: 13/13, including 2 HD button parts | Available: 11/11 named parts |
| Whole-arm STEP | Shared LD/HD export 2026-07-21; file-set alignment under review | Shared LD/HD export 2026-07-21; file-set alignment under review | Review: FL export 2026-09-27; July 3 reference retained |
| Standalone printing STL | Missing | Missing | Missing |
| 3MF printing project | Review: date/version confirmation | Review: date/version confirmation | Conflict: link1 settings versus BOM |
| Excel BOM | Review: assembled and kit references | Review: handoff reference | Review: overseas-shipment reference |
| PDF / DWG drawings | Review: July 13 reference and older files | Partial: shared LD geometry reference only | Review: July 13 reference |
| Model-specific URDF and meshes | Missing: candidate held for review | Missing | Missing: unlabelled candidate held for review |
| Assembly guide / videos | Partial: [main arm assembly video](102-ld/assembly-guide/README.md) available; revision and wiring coverage under review | Partial: [LD video with HD servo substitution](102-hd/assembly-guide/README.md); HD button instructions pending | Partial: [assembly video](102-fl/assembly-guide/README.md) available; revision and wiring coverage under review |
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
