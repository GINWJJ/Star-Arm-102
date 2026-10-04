# Star Arm 102 规格与硬件资源

[首页](../README.zh.md) · [English](README.md) · [更新记录](CHANGELOG.md)

对比 LD、HD、FL 的产品规格，按型号获取 STEP 模型、打印文件、BOM、图纸和装配视频。

[🔧 规格](#product-specifications) · [📂 目录结构](#directory-structure) · [📋 资源状态](#resource-status)

按型号查看详情：**[102-LD](102-ld/README.zh.md)** · **[102-HD](102-hd/README.md)** · **[102-FL](102-fl/README.md)**。

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

下方展开 LD 的目录。HD 和 FL 暂时保留原有布局，包括独立 BOM 目录。省略具体下载文件及历史资料。

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

`step/assembly/` 存放 CAD 装配模型；`assembly-guide/` 用于客户装配说明。LD 和 HD 的 `robot-description/` 提供通用 URDF 模型 ZIP；FL 资料待补，共用的 `hardware/robot-description/` 则存放现有 ROS 模型。部分目录目前只有 README，请在下载或制造前核对资源状态表。

<a id="resource-status"></a>

## 资源状态

截至 2026-10-04。**已提供**表示所列文件齐全；**部分提供**表示仅有部分资料；**待核对／冲突**表示已有参考文件，但尚不能视为相互匹配的生产版本；**缺失**表示未提供可用的型号专用文件。STEP 数量仅统计交接 BOM 中列出的主要打印零件，不包括采购舵机、电子件、配件和原生 CAD 源文件。文件齐全不等于通过生产或打印验证。

| 资源 | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| 主要打印零件 STEP | 已提供：11/11 个零件 | 已提供：13/13，含 2 个 HD 按钮零件 | 已提供：11/11 个零件 |
| 整机 STEP | 已提供 LD/HD 共用模型，导出日期 2026-07-21；配套文件待核对 | 已提供 LD/HD 共用模型，导出日期 2026-07-21；配套文件待核对 | 待核对：FL 导出日期 2026-09-27；保留 7 月 3 日参考文件 |
| 独立打印 STL | 缺失 | 缺失 | 缺失 |
| 3MF 打印项目 | 已提供 11 个独立零件及整套项目；切片检查通过，实物打印待验证 | 待核对：日期／版本 | 冲突：link1 参数与 BOM 不同 |
| 物料清单 | [LD 表格](102-ld/README.zh.md#bill-of-materials)；28 项装机物料 | 待核对：交接参考清单 | 待核对：海外出货参考清单 |
| PDF／DWG 图纸 | 待核对：7 月 13 日参考图 | 部分提供：仅共用 LD 几何参考 | 待核对：7 月 13 日参考图 |
| 型号专用 URDF 和网格 | LD/HD 通用 ZIP（ROS 1）；RViz 配置待补；限位及运行待验证 | LD/HD 通用 ZIP（ROS 1）；RViz 配置待补；限位及运行待验证 | 缺失：无型号标识的候选文件待核对 |
| 装配指南／视频 | 部分提供：[主体机械臂装配视频](102-ld/assembly-guide/README.zh.md)已提供；版本及接线覆盖范围待核对 | 部分提供：[参考 LD 视频并替换 HD 舵机](102-hd/assembly-guide/README.zh.md)；HD 按钮安装说明待补充 | 部分提供：[装配视频](102-fl/assembly-guide/README.zh.md)已提供；版本及接线覆盖范围待核对 |
| 已确认生产版本／实物验证 | 待完成 | 待完成 | 待完成 |

## 版本与许可

来源日期、冲突和未采用文件见 [交接审阅](handoff-review.zh.md)。[导入清单](handoff-imports.json) 记录原文件名、目标路径及 SHA-256。原始 Excel、图纸和 3MF 保持原内容及语言；英文索引不代表这些源文件已翻译。

硬件许可仍待明确，见 [许可范围](../LICENSE.md)。复制或重命名文件不授予新的许可。
