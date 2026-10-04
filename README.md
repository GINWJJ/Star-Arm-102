<h1 align="center">🦾 Star Arm 102</h1>

<p align="center">
  <strong>Open-Source 6+1 DOF Robot Arm for LeRobot</strong><br>
  Teleoperate. Learn from demonstrations. Run your first AI task.
</p>

<p align="center">
  <a href="docs/specifications.md"><img src="https://img.shields.io/badge/DOF-6%2B1-16A085?style=flat-square" alt="6 arm joints plus 1 gripper"></a>
  <a href="lerobot/README.md"><img src="https://img.shields.io/badge/LeRobot-Integration-FFD21E?style=flat-square&amp;logo=huggingface&amp;logoColor=FFD21E" alt="LeRobot integration"></a>
  <a href="python-sdk/README.md"><img src="https://img.shields.io/badge/Python-SDK-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python SDK"></a>
  <a href="ros2-humble/README.md"><img src="https://img.shields.io/badge/ROS_2-Humble-22314E?style=flat-square&amp;logo=ros&amp;logoColor=white" alt="ROS 2 Humble"></a>
  <a href="lerobot/examples/act_pick/README.md"><img src="https://img.shields.io/badge/ACT-Pretrained_Model-8B5CF6?style=flat-square" alt="ACT pretrained model"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-8B5CF6?style=flat-square" alt="English"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/语言-简体中文-64748B?style=flat-square" alt="简体中文"></a>
</p>

<p align="center">
  <a href="docs/getting-started.md"><strong>🚀 Get Started</strong></a> ·
  <a href="integrations/README.md"><strong>🌐 Cross-Brand Pairings</strong></a> ·
  <a href="#run-your-first-ai-task"><strong>🤖 Run Your First AI Task</strong></a> ·
  <a href="integrations/butterfly/README.md"><strong>💬 Natural-Language Control</strong></a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/">🌐 Official Website</a> ·
  <a href="https://fashionstar.com.hk/robot-arm/star-arm-102">🦾 Series Overview</a> ·
  <a href="#where-to-buy">🛒 Where to Buy</a> ·
  <a href="https://fashionstar.com.hk/support/">💬 Support</a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/store/collections/robot-arm/star-arm-102/">
    <img src="media/images/11.png" alt="Fashion Star Star Arm 102 leader and follower arm family" width="880">
  </a>
</p>

<p align="center"><strong>Six arm joints + one gripper · LD / HD leaders + FL follower · Teleoperation & imitation learning</strong></p>

## 📑 Contents

- [Introduction](#introduction)
- [Where to Buy](#where-to-buy)
- [Explore the Web Controller](#web-controller)
- [Run Your First AI Task](#run-your-first-ai-task)
- [Cross-Brand Follower Compatibility](#cross-brand-pairings)
- [Hardware Resources](hardware/README.md)
- [LeRobot](lerobot/README.md)
- [Natural Language Control](integrations/butterfly/README.md)
- [ROS 2 Humble](ros2-humble/README.md)
- [Python SDK](python-sdk/README.md)
- [Control & Configuration Tools](tools/README.md)

[Development Paths & Repository Structure](#development-paths) · [Related Projects](#related-projects)

---

<a id="introduction"></a>

## 📖 Introduction

Star Arm 102 is developed by **[Fashion Star](https://fashionstar.com.hk/)**. Connect your arms, explore Python and LeRobot, or try the released ACT block-placement policy. This repository brings together the code, hardware resources, and guides for your first setup and subsequent development.

| 🦾 6+1 DOF | 🎮 Learn by demonstration | 🤖 Try a pretrained policy |
| :---: | :---: | :---: |
| Six arm joints and a gripper control | Teleoperate with an LD or HD leader | Start with the supplied ACT block-placement model |
| [Explore the hardware](docs/specifications.md) | [Set up teleoperation](python-sdk/README.md) | [Open the model guide](lerobot/examples/act_pick/README.md) |

LD and HD are leader arms for demonstrations; FL is the follower that executes tasks. A leader alone cannot run the autonomous ACT task.

<a id="where-to-buy"></a>

## 🛒 Where to Buy

Compare the [Star Arm 102 series](https://fashionstar.com.hk/store/collections/robot-arm/star-arm-102/). All three models offer 6+1 DoF and 420 mm reach; choose a leader for demonstrations or a follower for task execution. Assembled and DIY kit options are listed on the product pages.

**International store:**

| Shop | Product overview |
| --- | --- |
| **[Shop&nbsp;102&#8209;LD&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-ld/)** | **Lightweight leader arm** for hand-guided teaching, teleoperation, and demonstration collection; torque-disabled joints move freely |
| **[Shop&nbsp;102&#8209;HD&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-hd/)** | **Pose-holding leader arm** with high-torque coreless bus servos, for stable demonstrations and extended data collection |
| **[Shop&nbsp;102&#8209;FL&nbsp;→](https://fashionstar.com.hk/store/product/star-arm-102-fl/)** | **Follower arm** for teleoperation and policy execution; two high-torque brushless bus servo joints, with a specified 500g working payload |

**Chinese purchase channel:** [Taobao](https://item.taobao.com/item.htm?id=1045277992605&skuId=6239416958433). Select the required model and kit option on the listing.

<a id="control-and-configuration-tools"></a>
<a id="web-controller"></a>

## 🎛️ Explore the Web Controller

Get familiar with the Star Arm 102 web controller interface and workflow before connecting your arm. Device connection, teleoperation, and live hardware readback require compatible hardware; see the Wiki for model-specific capabilities and setup.

[![Star Arm 102 web control interface preview](media/images/web-control-preview.jpg)](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)

**[Open Web Controller →](https://fashionstar.com.hk/wiki/software/robot-arm/data/102-web-controller/Browser_SDK/)** · **[Robot arm web control guide →](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)** · **[All robot and servo tools →](tools/README.md)**

*Interface preview with no hardware connected. Tool versions, downloads, and detailed instructions are maintained in the Wiki.*

<a id="try-your-first-ai-task"></a>
<a id="run-your-first-ai-task"></a>

## 🤖 Run Your First AI Task

Watch the ACT block-placement demo below, then follow the guide to run the pretrained model on your own arm. You can also explore a partner application for natural-language control.

| 🤖 Try a Pretrained ACT Task | 💬 Control Star Arm 102 with Natural Language |
| --- | --- |
| Run the supplied block-placement policy. | Describe a pick-and-place task in Butterfly Community's browser interface. |
| **Fashion Star example** · 102-FL with the specified two-camera setup. | **Community / Partner Integration** · upstream reports StarArm-102 + RealSense D415; exact 102 variant compatibility is pending confirmation. |
| Prepare the documented environment, calibration, and matching scene. | Prepare the upstream application, depth camera, calibration, and a compatible AI model service. Our end-to-end validation is pending. |
| **[Open the ACT guide →](lerobot/examples/act_pick/README.md)** | **[Explore the partner integration →](integrations/butterfly/README.md)** |

### ACT block placement: watch, then try

**No training required for the supplied ACT demo.** Run the released block-placement policy on a Star Arm 102-FL after setting up its environment, calibration, and two cameras. A matching scene matters: this is a policy for a specific task, not a general-purpose grasping model.

<p align="center">
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7">
    <img src="lerobot/examples/act_pick/docs/images/setup-side.jpg" alt="Side view of the Star Arm 102 ACT workspace — watch the block-placement demo" width="640">
  </a><br>
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7"><strong>▶ Watch the ACT block-placement demo</strong></a>
</p>

- [Run the pretrained model](lerobot/examples/act_pick/inference.md): download, camera setup, calibration, and one trial.
- [Model release and original video](https://github.com/servodevelop/Star-Arm-102/releases/tag/act-pick-v1.0.0).
- [Training your own task](lerobot/examples/act_pick/training.md): next steps and current documentation status.

<a id="cross-brand-pairings"></a>

## 🌐 One Leader, Multiple Robot Platforms

Have a third-party follower? Explore Star Arm 102-LD / HD pairing resources by follower model, then choose the matching Python or LeRobot path.

| Follower | Pairing resources | Current status |
| --- | --- | --- |
| **Seeed reBot B601** | [Open reBot pairing guide](integrations/seeed-rebot/README.md) | Upstream LeRobot guide available for B601-DM |
| **YAM** | [Explore YAM pairing](integrations/yam/README.md) | Exact model and setup guide pending |
| **Galaxea A1** | [Explore A1 pairing](integrations/galaxea-a1/README.md) | Setup guide and validation records pending |
| **Lumos Touch** | [Explore Touch pairing](integrations/lumos-touch/README.md) | Setup guide and validation records pending |

**[Find your pairing →](integrations/README.md)** · **[Check capabilities and evidence →](integrations/compatibility.md)**

Support depends on the exact follower, leader revision, and software path. LD compatibility, HD button behavior, teleoperation, and learning workflows are tracked separately. Pending documentation is not a tested compatibility claim.

<a id="hardware-resources"></a>
<a id="hardware-resource-status"></a>

## ⚙️ Hardware Resources

| Model | Available reference files | Still incomplete or under review |
| --- | --- | --- |
| [102-LD](hardware/102-ld/README.md) | Main-part STEP set, LD assembly export, drawings, BOM and 3MF references | Version alignment, approved print settings, standalone STL, model-specific URDF, assembly guide |
| [102-HD](hardware/102-hd/README.md) | Shared-body STEP set plus HD button parts, BOM and 3MF references | HD assembly/drawings, version alignment, standalone STL, model-specific URDF, assembly guide |
| [102-FL](hardware/102-fl/README.md) | Main-part STEP set, FL assembly export, drawings, BOM and 3MF references | FL link1 print-setting conflict, version alignment, standalone STL, model-specific URDF, assembly guide |

See the [detailed hardware status](hardware/README.md#resource-status) and [handoff findings](hardware/handoff-review.md). Files being available does not mean a complete, physically validated manufacturing release.

**[Explore Hardware Resources →](hardware/README.md)**

<a id="development-paths"></a>
<a id="documentation-and-support"></a>
<a id="documentation-index"></a>
<a id="choose-your-setup"></a>
<a id="before-connecting"></a>

## 🛠️ Development Paths & Repository Structure

New to your arm? Start with [Get Started](docs/getting-started.md) to choose your equipment setup, check [hardware connections](docs/hardware-setup.md), and select a software path. See also [specifications and joint mapping](docs/specifications.md), [troubleshooting](docs/troubleshooting.md), and [validation records](docs/validation.md).

| Path | Use it for | Guide |
| --- | --- | --- |
| Cross-brand pairings | Follower-specific requirements, software paths, and validation status | [Pairing directory](integrations/README.md) |
| Python examples | Communication checks and direct LD/HD → FL teleoperation | [Python SDK examples](python-sdk/README.md) |
| LeRobot | Calibration, demonstrations, policies, and the released ACT model | [Choose an integration](lerobot/README.md) |
| ROS 2 Humble | RViz, MoveIt, Gazebo, and robot-system development | [ROS 2 guide](ros2-humble/README.md) |
| Hardware | Model-specific STEP, BOM, drawings, printing references, and status | [Hardware resources](hardware/README.md) |
| Partner applications | Natural-language task control and partner-maintained robot applications | [Partner integrations](integrations/README.md) |
| Control & Configuration Tools | Robot arm web control, servo debugging, and parameter configuration | [Tool directory](tools/README.md) |

The ACT release and the refactored HD/FL integration use different joint representations. Keep them in separate environments. See [versions and validation status](docs/compatibility.md).

<a id="repository-structure"></a>

### Repository structure

Main entry points are shown below; individual assets, historical guides, and local caches are omitted.

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

`hardware/` holds mechanical resources; `integrations/` organizes follower pairings and partner applications. Implementations live in `python-sdk/`, `lerobot/`, and `ros2-humble/`. `tools/` links to Wiki-hosted customer tools; `scripts/` and `tests/` support repository maintenance.

<a id="related-projects"></a>

## 🌐 Related projects

- [PiPER-Mate](https://github.com/servodevelop/piper-mate) — Fashion Star's PiPER-Mate project and teleoperation resources.
- [Fashion Star CAN bus SDK](https://github.com/servodevelop/servo-canbus-sdk)
- [Fashion Star UART/RS485 SDK](https://github.com/servodevelop/servo-uart-rs485-sdk)
- [Fashion Star LeRobot fork](https://github.com/servodevelop/lerobot) · [Upstream LeRobot](https://github.com/huggingface/lerobot)

Software directories and model release URLs remain available. English is the default entry; existing English and Chinese READMEs maintain matching sections, images, commands, and status. English-only detailed documents remain accessible through their links. The [historical Chinese homepage](README.legacy.zh.md) is retained for reference, not as the current operating guide.

[Changes](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [License scope](LICENSE.md)
