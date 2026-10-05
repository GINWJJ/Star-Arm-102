# Star Arm 102 规格与硬件资源

[← 首页](../README.zh.md)　|　🌐 [English](README.md) / **简体中文**

**本页导航：**

- [🔧 规格](#product-specifications)
- [📂 目录结构](#directory-structure)

按型号查看详情：**[102-LD](102-ld/)** · **[102-HD](102-hd/)** · **[102-FL](102-fl/)**。

配件：**[摄像头模组](camera-module/)** · **[柔性夹爪](flexible-gripper/)**。

<a id="product-specifications"></a>

## 规格

| 规格 | Star Arm 102-LD | Star Arm 102-HD | Star Arm 102-FL |
| --- | --- | --- | --- |
| 产品类型 | 示教主臂（Leader Arm） | 姿态保持主臂（Leader Arm） | 执行从臂（Follower Arm） |
| 电源规格 | 12V@3A | 12V@5A | 12V@8A |
| 臂展 | 420mm | 420mm | 420mm |
| 自由度 | 6+1 | 6+1 | 6+1 |
| 负载 | — | — | 500g（建议在 70% 臂展处使用） |
| 重复定位精度／编码器 | 12-bit 磁编码器 | 12-bit 磁编码器 | 2mm |
| 关节运动范围 | 关节 1: ±110°<br>关节 2: 0°–180°<br>关节 3: 0°–270°<br>关节 4: ±90°<br>关节 5: ±65°<br>关节 6: ±150°<br>手柄: 0°–90° | 关节 1: ±110°<br>关节 2: 0°–180°<br>关节 3: 0°–270°<br>关节 4: ±90°<br>关节 5: ±65°<br>关节 6: ±150°<br>手柄: 0°–90° | 关节 1: ±110°<br>关节 2: 0°–180°<br>关节 3: 0°–270°<br>关节 4: ±90°<br>关节 5: ±65°<br>关节 6: ±150°<br>夹爪: 0°–90° |
| 舵机配置 | RA8-U01H-M × 4<br>RA8-U02H-M × 1<br>RA8-U03H-M × 2 | RP8-U45H-M × 4<br>RP8-U45H-M-C029 × 1<br>RP8-U45H-M-C028 × 2 | RA8-U35H-M × 3<br>RX8-U50H-M × 2<br>RA8-U27H-M-C005 × 1<br>RA8-U35H-M-C047 × 1 |
| 本机重量 | 721g | 883g | 791g |
| 通信方式 | UART / UC-01 | UART / UC-01 | UART / UC-01 |
| 工作温度 | 0–40°C | 0–40°C | 0–40°C |

<a id="directory-structure"></a>

## 目录结构

下方展开 LD 的目录。HD 和 FL 使用相同资源分类，各自提供型号对应文件和页内 BOM。省略具体文件。

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

`step/assembly/` 存放 CAD 装配模型；`assembly-guide/` 用于客户装配说明。LD 和 HD 的 `robot-description/` 提供通用 URDF 模型 ZIP；FL 资料待补，共用的 `hardware/robot-description/` 则存放现有 ROS 模型。

## 许可

硬件许可仍待明确，见 [许可范围](../LICENSE.md)。复制或重命名文件不授予新的许可。
