# Star Arm 102 Specifications & Hardware Resources

[Home](../README.md) · [中文](README.zh.md) · [Changes](CHANGELOG.md)

Compare LD, HD, and FL specifications, then find STEP models, printing files, BOMs, drawings, and assembly videos for your model.

[🔧 Specifications](#product-specifications) · [📂 Directory Structure](#directory-structure) · [📋 Resource Status](#resource-status)

Explore your model: **[102-LD](102-ld/README.md)** · **[102-HD](102-hd/README.md)** · **[102-FL](102-fl/README.md)**.

<a id="product-specifications"></a>

## Specifications

| Specification | Star Arm 102-LD | Star Arm 102-HD | Star Arm 102-FL |
| --- | --- | --- | --- |
| Arm type | Leader Arm | Pose-holding Leader Arm | Follower Arm |
| Power | 12V@3A | 12V@5A | 12V@8A |
| Reach | 420mm | 420mm | 420mm |
| DoF | 6+1 | 6+1 | 6+1 |
| Payload | — | — | 500g (70% reach recommended) |
| Repeatability / Encoder | 12-bit magnetic encoder | 12-bit magnetic encoder | 2mm |
| Joint Motion Range | Joint 1: ±110°<br>Joint 2: 0°–180°<br>Joint 3: 0°–270°<br>Joint 4: ±90°<br>Joint 5: ±65°<br>Joint 6: ±150°<br>Handle: 0°–90° | Joint 1: ±110°<br>Joint 2: 0°–180°<br>Joint 3: 0°–270°<br>Joint 4: ±90°<br>Joint 5: ±65°<br>Joint 6: ±150°<br>Handle: 0°–90° | Joint 1: ±110°<br>Joint 2: 0°–180°<br>Joint 3: 0°–270°<br>Joint 4: ±90°<br>Joint 5: ±65°<br>Joint 6: ±150°<br>Gripper: 0°–90° |
| Servos | RA8-U01H-M × 4<br>RA8-U02H-M × 1<br>RA8-U03H-M × 2 | RP8-U45H-M × 4<br>RP8-U45H-M-C029 × 1<br>RP8-U45H-M-C028 × 2 | RA8-U35H-M × 3<br>RX8-U50H-M × 2<br>RA8-U27H-M-C005 × 1<br>RA8-U35H-M-C047 × 1 |
| Arm weight | 721g | 883g | 791g |
| Communication | UART / UC-01 | UART / UC-01 | UART / UC-01 |
| Operating Temperature | 0–40°C | 0–40°C | 0–40°C |

<a id="directory-structure"></a>

## Directory structure

The LD layout is expanded below. HD and FL retain their existing layouts, including separate BOM directories. Individual downloads and historical files are omitted.

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
│   ├── images/
│   ├── assembly-guide/
│   │   └── images/
│   └── robot-description/
│       └── star-arm-102-ld-hd-urdf.zip
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

`step/assembly/` contains CAD assemblies; `assembly-guide/` is for customer assembly instructions. LD and HD `robot-description/` directories provide the shared URDF model ZIP; FL resources remain pending, while the shared `hardware/robot-description/` contains the existing ROS model. A directory may currently contain only a README: consult the resource status table before downloading or manufacturing.

<a id="resource-status"></a>

## Resource status

As of 2026-10-04. **Available** means the named file set is present. **Partial** means only some resources exist. **Review / Conflict** means reference files are present but cannot yet be treated as a matched production release. **Missing** means no usable model-specific file has been supplied. STEP counts cover the main printed parts named in the handoff BOM; they exclude purchased servos, electronics, accessories and native CAD sources. File availability is not manufacturing or print validation.

| Resource | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| Main printed-part STEP coverage | Available: 11/11 named parts | Available: 13/13, including 2 HD button parts | Available: 11/11 named parts |
| Whole-arm STEP | Shared LD/HD export 2026-07-21; file-set alignment under review | Shared LD/HD export 2026-07-21; file-set alignment under review | Review: FL export 2026-09-27; July 3 reference retained |
| Standalone printing STL | Missing | Missing | Missing |
| 3MF printing project | Review: date/version confirmation | Review: date/version confirmation | Conflict: link1 settings versus BOM |
| BOM | [LD table](102-ld/README.md#bill-of-materials); 28 assembly items | Review: handoff reference | Review: overseas-shipment reference |
| PDF / DWG drawings | Review: July 13 reference | Partial: shared LD geometry reference only | Review: July 13 reference |
| Model-specific URDF and meshes | Shared LD/HD ZIP (ROS 1); RViz configuration incomplete; limits and runtime validation pending | Shared LD/HD ZIP (ROS 1); RViz configuration incomplete; limits and runtime validation pending | Missing: unlabelled candidate held for review |
| Assembly guide / videos | Partial: [main arm assembly video](102-ld/assembly-guide/README.md) available; revision and wiring coverage under review | Partial: [LD video with HD servo substitution](102-hd/assembly-guide/README.md); HD button instructions pending | Partial: [assembly video](102-fl/assembly-guide/README.md) available; revision and wiring coverage under review |
| Confirmed production revision / physical validation | Pending | Pending | Pending |

## Versions and licensing

Source dates, conflicts and excluded files are documented in the [handoff review](handoff-review.md). The [import manifest](handoff-imports.json) maps original filenames to destinations and SHA-256 hashes. Original workbooks, drawings and 3MF files retain their content and language; English indexes do not imply those source files have been translated.

Hardware licensing remains unresolved; see [license scope](../LICENSE.md). No new license is granted by copying or renaming files.
