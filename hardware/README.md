# Star Arm 102 Specifications & Hardware Resources

[← Home](../README.md)　|　🌐 **English** / [简体中文](README.zh.md)

**On this page:**

- [🔧 Specifications](#product-specifications)
- [📂 Directory Structure](#directory-structure)

Explore your model: **[102-LD](102-ld/)** · **[102-HD](102-hd/)** · **[102-FL](102-fl/)**.

Accessories: **[Camera Module](camera-module/)** · **[Flexible Gripper](flexible-gripper/)**.

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

The LD layout is expanded below. HD and FL use the same resource categories, with model-specific files and inline BOMs. Individual files are omitted.

```text
hardware/
├── README.md
├── README.zh.md
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
├── camera-module/
├── flexible-gripper/
└── robot-description/
    ├── README.md
    ├── urdf/
    │   └── star-arm-102.urdf
    └── meshes/
```

`step/assembly/` contains CAD assemblies; `assembly-guide/` is for customer assembly instructions. LD and HD `robot-description/` directories provide the shared URDF model ZIP; FL resources remain pending, while the shared `hardware/robot-description/` contains the existing ROS model.

## Licensing

Hardware licensing remains unresolved; see [license scope](../LICENSE.md). No new license is granted by copying or renaming files.
