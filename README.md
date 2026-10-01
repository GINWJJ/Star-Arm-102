<h1 align="center">🦾 Star Arm 102</h1>

<p align="center">
  <strong>Open-Source 6+1 DOF Robot Arm for LeRobot</strong><br>
  Teleoperate. Learn from demonstrations. Run your first AI task.
</p>

<p align="center">
  <a href="docs/specifications.md"><img src="https://img.shields.io/badge/DOF-6%2B1-16A085?style=flat-square" alt="6 arm joints plus 1 gripper"></a>
  <a href="Lerobot/README.md"><img src="https://img.shields.io/badge/LeRobot-Integration-FFD21E?style=flat-square&amp;logo=huggingface&amp;logoColor=FFD21E" alt="LeRobot integration"></a>
  <a href="Python_SDK/README.md"><img src="https://img.shields.io/badge/Python-SDK-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python SDK"></a>
  <a href="ROS2_HUMBLE/README.md"><img src="https://img.shields.io/badge/ROS_2-Humble-22314E?style=flat-square&amp;logo=ros&amp;logoColor=white" alt="ROS 2 Humble"></a>
  <a href="Lerobot/examples/act_pick/README.md"><img src="https://img.shields.io/badge/ACT-Pretrained_Model-8B5CF6?style=flat-square" alt="ACT pretrained model"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-8B5CF6?style=flat-square" alt="English"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/语言-简体中文-64748B?style=flat-square" alt="简体中文"></a>
</p>

<p align="center">
  <a href="docs/getting-started.md"><strong>🚀 Get Started</strong></a> ·
  <a href="Lerobot/examples/act_pick/README.md"><strong>🤖 Try the ACT Model</strong></a> ·
  <a href="Lerobot/examples/act_pick/README.md#watch-the-demo"><strong>▶ Watch the Demo</strong></a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/">🌐 Official Website</a> ·
  <a href="https://fashionstar.com.hk/robot-arm/star-arm-102/">🦾 Series Overview</a> ·
  <a href="#where-to-buy">🛒 Where to Buy</a> ·
  <a href="#documentation-and-support">💬 Support</a>
</p>

<p align="center">
  <a href="https://fashionstar.com.hk/robot-arm/star-arm-102/">
    <img src="Media/images/11.png" alt="Fashion Star Star Arm 102 leader and follower arm family" width="880">
  </a>
</p>

<p align="center"><strong>Six arm joints + one gripper · LD / HD leaders + FL follower · Teleoperation & imitation learning</strong></p>

Star Arm 102 is developed by **[Fashion Star](https://fashionstar.com.hk/)**. Connect your arms, explore Python and LeRobot, or try the released ACT block-placement policy. This repository brings together the code, hardware resources, and guides for your first setup and subsequent development.

| 🦾 6+1 DOF | 🎮 Learn by demonstration | 🤖 Try a pretrained policy |
| :---: | :---: | :---: |
| Six arm joints and a gripper control | Teleoperate with an LD or HD leader | Start with the supplied ACT block-placement model |
| [Explore the hardware](docs/specifications.md) | [Set up teleoperation](Python_SDK/README.md) | [Open the model guide](Lerobot/examples/act_pick/README.md) |

📑 **Explore:** [Shop](#where-to-buy) · [ACT Demo](#try-your-first-ai-task) · [Choose Your Setup](#choose-your-setup) · [Development](#development-paths) · [Docs & Support](#documentation-and-support)

---

<a id="where-to-buy"></a>

## 🛒 Where to Buy

Explore the [Star Arm 102 series](https://fashionstar.com.hk/robot-arm/star-arm-102/) or visit the official store:

| Model | Role | Official store |
| --- | --- | --- |
| Star Arm 102-LD | Leader arm for teleoperation | [Shop 102-LD](https://fashionstar.com.hk/store/product/star-arm-102-ld/) |
| Star Arm 102-HD | Leader arm with button-based pose holding | [Shop 102-HD](https://fashionstar.com.hk/store/product/star-arm-102-hd/) |
| Star Arm 102-FL | Follower arm for teleoperation and policy execution | [Shop 102-FL](https://fashionstar.com.hk/store/product/star-arm-102-fl/) |

<a id="try-your-first-ai-task"></a>

## 🤖 Try your first AI task

**No training required for the supplied ACT demo.** Run the released block-placement policy on a Star Arm 102-FL after setting up its environment, calibration, and two cameras. A matching scene matters: this is a policy for a specific task, not a general-purpose grasping model.

<p align="center">
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7">
    <img src="Lerobot/examples/act_pick/docs/images/setup-front.jpg" alt="Watch the Star Arm 102 ACT block-placement demo" width="640">
  </a><br>
  <a href="https://github.com/user-attachments/assets/6774384d-f437-4aa9-a364-cd66eba965f7"><strong>▶ Watch Star Arm 102 in action</strong></a>
</p>

- [Run the pretrained model](Lerobot/examples/act_pick/inference.md): download, camera setup, calibration, and one trial.
- [Model release and original video](https://github.com/servodevelop/Star-Arm-102/releases/tag/act-pick-v1.0.0).
- [Training your own task](Lerobot/examples/act_pick/training.md): next steps and current documentation status.

<a id="choose-your-setup"></a>

## 🧭 Choose your setup

| What you have | Where to start |
| --- | --- |
| **102-LD + 102-FL** | [Python first teleoperation](Python_SDK/README.md), then [LeRobot](Lerobot/README.md) for learning workflows |
| **102-HD + 102-FL** | [Python setup and HD button requirements](Python_SDK/README.md); use the separate [HD/FL LeRobot guide](Lerobot/lerobot-stararm102/README.md) for the refactored integration |
| **102-FL only** | [Check communication](Python_SDK/README.md#check-communication-without-commanding-motion), then [ACT demo](Lerobot/examples/act_pick/inference.md) or [ROS 2](ROS2_HUMBLE/README.md) |
| **102 leader + Seeed reBot** | [reBot compatibility and upstream setup](docs/rebot.md); the Python FL example is not a reBot driver |
| **Parts / DIY build** | [Hardware index](Hardware/README.md); the full assembly tutorial is still in preparation |

LD and HD are leader arms. FL is the follower that executes tasks. A leader alone cannot run the supplied autonomous ACT task. “6+1” means six arm joints and one gripper control on FL; the leaders have a corresponding handle control.

<a id="before-connecting"></a>

## 🔌 Before connecting

Read [hardware setup](docs/hardware-setup.md) for power, wiring, and port identification. Use the [compatibility table](docs/compatibility.md) to select one environment. ROS is not required for Python teleoperation or the ACT demo.

<a id="development-paths"></a>

## 🛠️ Development paths

| Path | Use it for | Guide |
| --- | --- | --- |
| Python examples | Communication checks and direct LD/HD → FL teleoperation | [Python SDK examples](Python_SDK/README.md) |
| LeRobot | Calibration, demonstrations, policies, and the released ACT model | [Choose an integration](Lerobot/README.md) |
| ROS 2 Humble | RViz, MoveIt, Gazebo, and robot-system development | [ROS 2 guide](ROS2_HUMBLE/README.md) |
| Hardware | LD BOM, drawings, editable parts, and accessories | [Hardware resources](Hardware/README.md) |

The ACT release and the refactored HD/FL integration use different joint representations. Keep them in separate environments. See [versions and validation status](docs/compatibility.md).

<a id="documentation-and-support"></a>

## 📚 Documentation and support

- 🚀 [Start here](docs/getting-started.md) · 🔎 [Troubleshooting](docs/troubleshooting.md)
- ⚙️ [Specifications and joint mapping](docs/specifications.md)
- 💬 [Report a problem](https://github.com/servodevelop/Star-Arm-102/issues/new/choose)
- 📝 [Changes](CHANGELOG.md) · 🤝 [Contributing](CONTRIBUTING.md) · 📄 [License scope](LICENSE.md)

<a id="related-projects"></a>

## 🌐 Related projects

- [PiPER-Mate](https://github.com/servodevelop/piper-mate) — Fashion Star's PiPER-Mate project and teleoperation resources.
- [Fashion Star CAN bus SDK](https://github.com/servodevelop/servo-canbus-sdk)
- [Fashion Star UART/RS485 SDK](https://github.com/servodevelop/servo-uart-rs485-sdk)
- [Fashion Star LeRobot fork](https://github.com/servodevelop/lerobot) · [Upstream LeRobot](https://github.com/huggingface/lerobot)

Existing software directories and model release URLs are retained. Chinese supplementary guides remain available through the [Chinese navigation](README.zh.md); the English path is the default customer entry.
