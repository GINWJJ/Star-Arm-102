# Star Arm 102 硬件资源

第三方从臂搭配请查看 [跨品牌搭配资料](../integrations/README.md)。

[首页](../README.zh.md) · [English](README.md) · [交接审阅](handoff-review.zh.md) · [更新记录](CHANGELOG.md)

请选择准确型号：**[102-LD](102-ld/README.zh.md)** · **[102-HD](102-hd/README.md)** · **[102-FL](102-fl/README.md)**。

LD 和 HD 共用主体机械结构。HD 另外有按钮底座、按钮盖和 UK-01 按键板，舵机、线材及紧固件选型也不同。各型号提供独立下载入口，客户无需自行合并共用 BOM 和差异清单。

<a id="product-specifications"></a>

## 产品规格书

三款产品的规格入口集中列在下方。目前仓库尚未收录可识别的独立产品规格书 PDF；现有机械图纸不作为产品规格书。文件补齐前，可查看对应官方产品页面的规格信息。

| 资料 | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| 产品定位 | 轻量示教主臂 | 姿态保持示教主臂 | 任务执行从臂 |
| 官方产品规格 | [查看 LD 规格](https://fashionstar.com.hk/store/product/star-arm-102-ld/) | [查看 HD 规格](https://fashionstar.com.hk/store/product/star-arm-102-hd/) | [查看 FL 规格](https://fashionstar.com.hk/store/product/star-arm-102-fl/) |
| 独立规格书 PDF | 待补充 | 待补充 | 待补充 |

[系列规格与关节映射](../docs/specifications.md) · [机械资料状态](#resource-status)

## 目录结构

下方展开 LD 的目录。HD 和 FL 采用相同的资源分类；LD 额外列出的 drawings/images 目录存放已有图纸预览。省略具体下载文件及历史资料。

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

`step/assembly/` 存放 CAD 装配模型；`assembly-guide/` 用于客户装配说明。各型号的 `robot-description/` 记录待补资源，共用的 `hardware/robot-description/` 则存放现有 ROS 模型。部分目录目前只有 README，请在下载或制造前核对资源状态表。

<a id="resource-status"></a>

## 资源状态

截至 2026-10-03。**已提供**表示所列文件齐全；**部分提供**表示仅有部分资料；**待核对／冲突**表示已有参考文件，但尚不能视为相互匹配的生产版本；**缺失**表示未提供可用的型号专用文件。STEP 数量仅统计交接 BOM 中列出的主要打印零件，不包括采购舵机、电子件、配件和原生 CAD 源文件。文件齐全不等于通过生产或打印验证。

| 资源 | 102-LD | 102-HD | 102-FL |
| --- | --- | --- | --- |
| 主要打印零件 STEP | 已提供：11/11 个零件 | 已提供：13/13，含 2 个 HD 按钮零件 | 已提供：11/11 个零件 |
| 整机 STEP | 待核对：LD 导出日期 2026-07-21 | 缺失：没有标为 HD 的装配模型 | 待核对：FL 导出日期 2026-07-03 |
| 独立打印 STL | 缺失 | 缺失 | 缺失 |
| 3MF 打印项目 | 待核对：日期／版本 | 待核对：日期／版本 | 冲突：link1 参数与 BOM 不同 |
| Excel BOM | 待核对：整机及套件参考清单 | 待核对：交接参考清单 | 待核对：海外出货参考清单 |
| PDF／DWG 图纸 | 待核对：7 月 13 日参考图及旧文件 | 部分提供：仅共用 LD 几何参考 | 待核对：7 月 13 日参考图 |
| 型号专用 URDF 和网格 | 缺失：候选文件暂缓采用，待核对 | 缺失 | 缺失：无型号标识的候选文件待核对 |
| 装配指南／视频 | 缺失 | 缺失 | 缺失 |
| 已确认生产版本／实物验证 | 待完成 | 待完成 | 待完成 |

## 按用途下载

- 修改几何结构：各型号的 `step/parts/` 和 `step/assembly/`。
- 打印零件：`printing/stl/` 和 `printing/3mf/`。现有 3MF 是待核对的交接参考文件。
- 核对材料及数量：`bom/` 提供 Excel 清单，并说明来源及版本状态。
- 核对尺寸：`drawings/pdf/` 和 `drawings/cad/`。
- 装配：`assembly-guide/` 将提供步骤、照片、视频链接及 Wiki 教程。
- 使用机器人模型：各型号的 `robot-description/` 记录适用性与状态。[现有 ROS 模型](robot-description/README.md) 单独保留，未被未经验证的交接导出文件替换。

## 版本与许可

来源日期、冲突和未采用文件见 [交接审阅](handoff-review.zh.md)。[导入清单](handoff-imports.json) 记录原文件名、目标路径及 SHA-256。原始 Excel、图纸和 3MF 保持原内容及语言；英文索引不代表这些源文件已翻译。

硬件许可仍待明确，见 [许可范围](../LICENSE.md)。复制或重命名文件不授予新的许可。
