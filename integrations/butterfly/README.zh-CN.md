# 用自然语言控制 Star Arm 102

[← 集成目录](../README.md)　|　🌐 [English](README.md) / **简体中文**

**本页导航：**

- [💬 此集成提供什么](#page-section-1)
- [📋 开始前](#page-section-2)
- [✅ 参考版本与验证](#page-section-3)
- [📦 维护方与源代码](#page-section-4)

**社区／伙伴集成 — Butterfly Community Robot Arm**

[Star Arm 102 首页](../../README.zh.md)

在浏览器中描述抓放任务，由 AI 服务协调感知、抓取规划和机器人执行。伙伴应用还提供网页控制、相机标定和关节反馈。

**[查看伙伴界面与任务演示 →](https://github.com/butterfly-community/robot-arm)**

**[检查兼容性 →](compatibility.md)** · **[配置与首次任务 →](setup.md)** · **[排错 →](troubleshooting.md)**

<a id="page-section-1"></a>

## 此集成提供什么

- 通过应用工具协调自然语言任务。
- RGB-D 感知、相机到机器人标定、抓取规划，以及 ROS 2／MoveIt 运动规划。
- 用于选择目标和检查执行状态的浏览器界面。
- 上游提供的纯软件模式，可在未连接机械臂时探索流程。

该架构通过 AI 工具调用以及专用感知和规划服务工作。本指南不将它描述为端到端 VLA 策略，也不将其视为 ACT 模型的替代品。

<a id="page-section-2"></a>

## 开始前

伙伴报告已使用 StarArm-102 和 RealSense D415 完成实物抓放，设备文档列出 RA8-U35H-M 舵机。使用真机路径前请确认实际机械臂、舵机、相机和模型配置。项目名称本身不能证明 102-LD、102-HD 和 102-FL 全部兼容。

应用有独立的 Docker 软件栈。自然语言任务还需要兼容的模型服务；基础网页控制和本地感知的依赖不同。参见 [兼容性](compatibility.md)。

<a id="page-section-3"></a>

## 参考版本与验证

| 项目 | 状态 |
| --- | --- |
| 上游 | [butterfly-community/robot-arm](https://github.com/butterfly-community/robot-arm) |
| 文档参考版本 | [`08498c31c56cf339601851851225bf111f89c82d`](https://github.com/butterfly-community/robot-arm/tree/08498c31c56cf339601851851225bf111f89c82d) |
| 核对日期 | 2026-10-03 |
| 已完成的审阅 | README、部署和 StarArm-102 文档，以及 AI 编排入口 |
| 本仓库尚待完成 | 安装、纯软件运行、具体型号兼容性、标定和实物抓放验证 |

这是文档参考，**不是已测试的版本推荐**。上游 main 可能变化；评估指南时请结合所引用文档及匹配的源代码提交。

<a id="page-section-4"></a>

## 维护方与源代码

应用由 Butterfly Community 维护。完整源码保留在上游；此目录仅提供集成文档，不重新分发上游应用代码、模型权重或截图。

核对的版本中未发现仓库级许可证。引入或重新分发上游代码、资源前，请与伙伴确认许可和授权范围。后续集成需保留归属及第三方许可要求。

产品问题请使用 [Star Arm 102 支持入口](../../README.zh.md#documentation-and-support)，应用问题请使用 [上游问题追踪](https://github.com/butterfly-community/robot-arm/issues)。反馈时同时提供应用版本和准确硬件配置。
