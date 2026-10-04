<h1 align="center">🦾 Star Arm 102</h1>

<p align="center">
  <strong>面向 LeRobot 的开源 6+1 自由度机械臂</strong><br>
  遥操作、示范学习，运行你的第一个 AI 任务。
</p>

<p align="center">
  <a href="docs/specifications.md"><img src="https://img.shields.io/badge/DOF-6%2B1-16A085?style=flat-square" alt="6 arm joints plus 1 gripper"></a>
  <a href="lerobot/README.md"><img src="https://img.shields.io/badge/LeRobot-Integration-FFD21E?style=flat-square&amp;logo=huggingface&amp;logoColor=FFD21E" alt="LeRobot integration"></a>
  <a href="python-sdk/README.md"><img src="https://img.shields.io/badge/Python-SDK-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python SDK"></a>
  <a href="ros2-humble/README.zh.md"><img src="https://img.shields.io/badge/ROS_2-Humble-22314E?style=flat-square&amp;logo=ros&amp;logoColor=white" alt="ROS 2 Humble"></a>
  <a href="lerobot/examples/act_pick/README.zh.md"><img src="https://img.shields.io/badge/ACT-Pretrained_Model-8B5CF6?style=flat-square" alt="ACT pretrained model"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-8B5CF6?style=flat-square" alt="English"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/语言-简体中文-64748B?style=flat-square" alt="简体中文"></a>
</p>

<p align="center">
  <a href="docs/getting-started.md"><strong>🚀 开始使用</strong></a> ·
  <a href="integrations/README.md"><strong>🌐 跨品牌搭配</strong></a> ·
  <a href="#try-your-first-ai-task"><strong>🤖 体验第一个 AI 任务</strong></a> ·
  <a href="integrations/butterfly/README.zh-CN.md"><strong>💬 自然语言控制</strong></a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/">🌐 官方网站</a> ·
  <a href="https://fashionstar.com.hk/robot-arm/star-arm-102">🦾 系列介绍</a> ·
  <a href="#where-to-buy">🛒 购买入口</a> ·
  <a href="https://fashionstar.com.hk/support/">💬 支持</a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/store/collections/robot-arm/star-arm-102/">
    <img src="media/images/11.png" alt="Fashion Star Star Arm 102 leader and follower arm family" width="880">
  </a>
</p>

<p align="center"><strong>六个机械臂关节 + 一个夹爪 · LD／HD 主臂 + FL 从臂 · 遥操作与模仿学习</strong></p>

Star Arm 102 由 **[Fashion Star](https://fashionstar.com.hk/)** 开发。连接机械臂，使用 Python 和 LeRobot，或体验已发布的 ACT 积木放置策略。本仓库汇集首次安装及后续开发所需的代码、硬件资源与指南。

| 🦾 6+1 自由度 | 🎮 通过示范学习 | 🤖 体验预训练策略 |
| :---: | :---: | :---: |
| 六个机械臂关节及一个夹爪控制通道 | 使用 LD 或 HD 主臂遥操作 | 从提供的 ACT 积木放置模型开始 |
| [了解硬件](docs/specifications.md) | [配置遥操作](python-sdk/README.md) | [打开模型指南](lerobot/examples/act_pick/README.zh.md) |

📑 **导航：** [购买](#where-to-buy) · [AI 任务](#try-your-first-ai-task) · [选择配置](#choose-your-setup) · [工具](#control-and-configuration-tools) · [跨品牌搭配](#cross-brand-pairings) · [伙伴项目](integrations/README.md#partner-applications) · [开发](#development-paths) · [文档索引](#documentation-index)

---

<a id="where-to-buy"></a>

## 🛒 购买入口

对比 [Star Arm 102 系列](https://fashionstar.com.hk/store/collections/robot-arm/star-arm-102/)。三款均采用 6+1 自由度、420 mm 臂展；主臂用于示范，从臂用于执行任务。产品页面提供整机和 DIY 套件选项。

**国际商城：**

| 购买 | 产品简介 |
| --- | --- |
| **[购买&nbsp;102&#8209;LD&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-ld/)** | **轻量示教主臂**：关节在扭矩关闭时可自由手动引导，用于示教、遥操作和示范数据采集 |
| **[购买&nbsp;102&#8209;HD&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-hd/)** | **姿态保持主臂（Pose-holding）**：采用高扭矩空心杯总线舵机，用于稳定示范和长时间数据采集 |
| **[购买&nbsp;102&#8209;FL&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-fl/)** | **任务执行从臂**：配备两个高扭矩无刷总线舵机关节，用于遥操作和策略执行，标称工作负载 500g |

**中文购买入口：** [淘宝购买](https://item.taobao.com/item.htm?id=1045277992605&skuId=6239416958433)。请在商品页面选择所需型号及整机／套件选项。

<a id="cross-brand-pairings"></a>

## 🌐 一个主臂，多种机器人平台

已有其他品牌的从臂？按从臂型号查看 Star Arm 102-LD／HD 的搭配资料，再选择对应的 Python 或 LeRobot 路径。

| 从臂 | 搭配资料 | 当前状态 |
| --- | --- | --- |
| **Seeed reBot B601** | [打开 reBot 搭配指南](integrations/seeed-rebot/README.md) | 已有 B601-DM 上游 LeRobot 指南 |
| **YAM** | [查看 YAM 搭配](integrations/yam/README.md) | 具体型号和安装指南待确认 |
| **Galaxea A1** | [查看 A1 搭配](integrations/galaxea-a1/README.md) | 安装指南和验证记录待补充 |
| **Lumos Touch** | [查看 Touch 搭配](integrations/lumos-touch/README.md) | 安装指南和验证记录待补充 |

**[查找搭配方案 →](integrations/README.md)** · **[核对能力与验证依据 →](integrations/compatibility.md)**

支持范围取决于具体从臂、主臂版本及软件路径。LD 兼容性、HD 按键行为、遥操作和学习流程分别记录。待完善的文档不代表已验证的兼容性。

<a id="try-your-first-ai-task"></a>

## 🤖 体验第一个 AI 任务

先观看下方 ACT 积木放置演示，再按照指南在自己的机械臂上运行预训练模型。你也可以了解支持自然语言控制的伙伴应用。

| 🤖 体验 ACT 预训练任务 | 💬 用自然语言控制 Star Arm 102 |
| --- | --- |
| 运行提供的积木放置策略。 | 在 Butterfly Community 的网页界面中描述抓放任务。 |
| **Fashion Star 示例** · 使用 102-FL 及指定双相机配置。 | **社区／伙伴集成** · 上游报告使用 StarArm-102 + RealSense D415；具体 102 型号兼容性待确认。 |
| 准备文档指定的环境、校准和匹配场景。 | 准备上游应用、深度相机、校准及兼容的 AI 模型服务。我们的端到端验证待完成。 |
| **[打开 ACT 指南 →](lerobot/examples/act_pick/README.zh.md)** | **[了解伙伴集成 →](integrations/butterfly/README.zh-CN.md)** |

### ACT 积木放置：先看演示，再动手体验

**提供的 ACT 演示无需重新训练。** 完成环境、校准和双相机配置后，可在 Star Arm 102-FL 上运行已发布的积木放置策略。场景匹配很重要：这是针对特定任务的策略，不是通用抓取模型。

<p align="center">
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7">
    <img src="lerobot/examples/act_pick/docs/images/setup-side.jpg" alt="Star Arm 102 ACT 工作区侧视图，点击观看积木放置演示" width="640">
  </a><br>
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7"><strong>▶ 观看 ACT 积木放置演示</strong></a>
</p>

- [运行预训练模型](lerobot/examples/act_pick/inference.md)：下载、相机配置、校准及首次运行。
- [模型发布版本与原始视频](https://github.com/servodevelop/Star-Arm-102/releases/tag/act-pick-v1.0.0)。
- [训练自己的任务](lerobot/examples/act_pick/training.md)：后续步骤及当前文档状态。

<a id="choose-your-setup"></a>

## 🧭 选择你的配置

| 你拥有的设备 | 从哪里开始 |
| --- | --- |
| **102-LD + 102-FL** | [首次 Python 遥操作](python-sdk/README.md)，再进入 [LeRobot](lerobot/README.md) 学习流程 |
| **102-HD + 102-FL** | [Python 配置及 HD 按键要求](python-sdk/README.md)；重构集成使用独立的 [HD/FL LeRobot 指南](lerobot/lerobot-stararm102/README.md) |
| **仅 102-FL** | [检查通信](python-sdk/README.md#check-communication-without-commanding-motion)，再体验 [ACT 演示](lerobot/examples/act_pick/inference.md) 或 [ROS 2](ros2-humble/README.zh.md) |
| **102 主臂 + Galaxea A1／Lumos Touch／YAM** | [跨品牌搭配导航](integrations/README.md)：选择型号并核对当前配置状态 |
| **102 主臂 + Seeed reBot** | [reBot 兼容性及上游配置](integrations/seeed-rebot/README.md)；Python FL 示例不是 reBot 驱动 |
| **零件／DIY 装配** | [硬件索引](hardware/README.zh.md)；完整装配教程仍在准备中 |

LD 和 HD 是主臂，FL 是执行任务的从臂。仅有主臂不能运行提供的自主 ACT 任务。“6+1”表示 FL 的六个机械臂关节和一个夹爪控制通道；主臂有相应的手柄控制。

<a id="before-connecting"></a>

## 🔌 连接前准备

阅读 [硬件配置](docs/hardware-setup.md)，确认供电、接线和端口。通过 [兼容性表](docs/compatibility.md) 选择一个环境。Python 遥操作和 ACT 演示无需 ROS。

<a id="control-and-configuration-tools"></a>

## 🎛️ 控制与配置工具

使用 Star Arm 102 网页界面进行连接、遥操作和三维姿态显示。Wiki 提供工具入口、各型号功能和配置说明。

[![Star Arm 102 网页控制界面预览](media/images/web-control-preview.jpg)](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)

**[机械臂网页控制指南 →](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)** · **[全部机械臂与舵机工具 →](tools/README.md)**

*截图时未连接硬件。工具版本、下载和详细操作说明由 Wiki 统一维护。*

<a id="development-paths"></a>

## 🛠️ 开发路径

| 路径 | 用途 | 指南 |
| --- | --- | --- |
| 跨品牌搭配 | 从臂专用要求、软件路径和验证状态 | [搭配导航](integrations/README.md) |
| Python 示例 | 通信检查及 LD/HD → FL 直接遥操作 | [Python SDK 示例](python-sdk/README.md) |
| LeRobot | 校准、示范采集、策略及已发布 ACT 模型 | [选择集成方案](lerobot/README.md) |
| ROS 2 Humble | RViz、MoveIt、Gazebo 和机器人系统开发 | [ROS 2 指南](ros2-humble/README.zh.md) |
| 硬件 | 各型号 STEP、BOM、图纸、打印参考及状态 | [硬件资源](hardware/README.zh.md) |
| 伙伴应用 | 自然语言任务控制及伙伴维护的机器人应用 | [伙伴集成](integrations/README.md) |

ACT 发布版本和重构后的 HD/FL 集成使用不同的关节表示，请保持独立环境。参见 [版本及验证状态](docs/compatibility.md)。

<a id="documentation-and-support"></a>
<a id="documentation-index"></a>
<a id="repository-structure"></a>

## 📚 文档索引

按下方索引查找指南，或通过目录树了解文件位置。

| 文档类别 | 入口 |
| --- | --- |
| 入门与配置 | [开始使用](docs/getting-started.md) · [硬件配置](docs/hardware-setup.md) · [兼容性](docs/compatibility.md) |
| 产品参考 | [规格及关节映射](docs/specifications.md) · [硬件资料](hardware/README.zh.md) |
| 编程与学习 | [Python SDK](python-sdk/README.md) · [LeRobot](lerobot/README.md) · [ACT 示例](lerobot/examples/act_pick/README.zh.md) · [ROS 2](ros2-humble/README.zh.md) |
| 搭配与工具 | [跨品牌搭配及伙伴应用](integrations/README.md) · [控制与配置工具](tools/README.md) |
| 排错与验证 | [排错指南](docs/troubleshooting.md) · [验证记录](docs/validation.md) |
| 仓库说明 | [更新记录](CHANGELOG.md) · [贡献指南](CONTRIBUTING.md) · [许可范围](LICENSE.md) |

### 仓库目录结构

下方展示主要入口，省略单个资源文件、历史教程和本地缓存。

```text
Star-Arm-102/
├── README.md
├── README.zh.md
├── hardware/
│   ├── 102-ld/
│   ├── 102-hd/
│   ├── 102-fl/
│   └── robot-description/
├── integrations/
│   ├── galaxea-a1/
│   ├── lumos-touch/
│   ├── yam/
│   ├── seeed-rebot/
│   └── butterfly/
├── lerobot/
│   ├── examples/act_pick/
│   ├── lerobot-robot-stararm102/
│   ├── lerobot-teleoperator-stararm102/
│   └── lerobot-stararm102/
├── python-sdk/
├── ros2-humble/
│   └── src/
├── tools/
├── docs/
├── media/
├── scripts/
├── tests/
├── .github/
├── AGENTS.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE.md
```

`hardware/` 存放机械资料；`integrations/` 按从臂搭配及伙伴应用组织入口。实现代码位于 `python-sdk/`、`lerobot/` 和 `ros2-humble/`。`tools/` 链接 Wiki 中的客户工具；`scripts/` 和 `tests/` 用于仓库维护。

<a id="related-projects"></a>

## 🌐 相关项目

- [PiPER-Mate](https://github.com/servodevelop/piper-mate) — Fashion Star 的 PiPER-Mate 项目与遥操作资源。
- [Fashion Star CAN 总线 SDK](https://github.com/servodevelop/servo-canbus-sdk)
- [Fashion Star UART/RS485 SDK](https://github.com/servodevelop/servo-uart-rs485-sdk)
- [Fashion Star LeRobot 分支](https://github.com/servodevelop/lerobot) · [上游 LeRobot](https://github.com/huggingface/lerobot)

软件目录和模型发布链接保持有效。英文为默认入口；已有中英文 README 同步维护板块、图片、命令及状态。仅有英文的详细文档仍可从对应链接访问。[历史中文首页](README.legacy.zh.md) 仅供追溯，不作为当前操作指南。

## 硬件资源状态

| 型号 | 已提供的参考文件 | 尚不完整或待核对 |
| --- | --- | --- |
| [102-LD](hardware/102-ld/README.zh.md) | 主要零件 STEP、LD 装配导出、图纸、BOM 和 3MF 参考 | 版本一致性、已确认打印参数、独立 STL、型号专用 URDF、装配指南 |
| [102-HD](hardware/102-hd/README.md) | 共用主体 STEP 及 HD 按钮零件、BOM 和 3MF 参考 | HD 装配／图纸、版本一致性、独立 STL、型号专用 URDF、装配指南 |
| [102-FL](hardware/102-fl/README.md) | 主要零件 STEP、FL 装配导出、图纸、BOM 和 3MF 参考 | FL link1 打印参数冲突、版本一致性、独立 STL、型号专用 URDF、装配指南 |

参见 [详细硬件状态](hardware/README.zh.md#resource-status) 和 [交接发现](hardware/handoff-review.zh.md)。文件已提供不代表已经形成完整、经过实物验证的制造发布版本。
