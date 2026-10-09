# Control Star Arm 102 with Natural Language

[← Integrations](../README.md)　|　**English** / [简体中文](README.zh-CN.md)

**On this page:**

- [💬 What this integration offers](#page-section-1)
- [📋 Before you start](#page-section-2)
- [✅ Reference version and validation](#page-section-3)
- [📦 Ownership and source code](#page-section-4)

**Community / Partner Integration — Butterfly Community Robot Arm**

[Star Arm 102 home](../../README.md)

Describe a pick-and-place task in a browser and let an AI service coordinate perception, grasp planning, and robot execution. The partner application also provides page-based control, camera calibration, and joint feedback.

**[See the partner's interface and task demonstration →](https://github.com/butterfly-community/robot-arm)**

**[Check compatibility →](compatibility.md)** · **[Setup and first task →](setup.md)** · **[Troubleshooting →](troubleshooting.md)**

<a id="page-section-1"></a>

## What this integration offers

- Natural-language tasks coordinated through application tools.
- RGB-D perception, camera-to-robot calibration, grasp planning, and ROS 2 / MoveIt motion planning.
- A browser interface for selecting targets and inspecting execution status.
- An upstream software-only mode for exploring the workflow without a connected arm.

The architecture uses AI tool calls and dedicated perception and planning services. This guide does not present it as an end-to-end VLA policy or a replacement for the ACT model.

<a id="page-section-2"></a>

## Before you start

The partner reports physical pick-and-place on StarArm-102 with a RealSense D415 and identifies RA8-U35H-M servos in its device documentation. Confirm the actual arm, servos, camera, and model configuration before using the hardware path. Compatibility across 102-LD, 102-HD, and 102-FL is not established by the project name alone.

The application has its own Docker-based stack. Natural-language tasks additionally need a compatible model service; basic page control and local perception have different dependencies. See [compatibility](compatibility.md).

<a id="page-section-3"></a>

## Reference version and validation

| Item | Status |
| --- | --- |
| Upstream | [butterfly-community/robot-arm](https://github.com/butterfly-community/robot-arm) |
| Documentation reference | [`08498c31c56cf339601851851225bf111f89c82d`](https://github.com/butterfly-community/robot-arm/tree/08498c31c56cf339601851851225bf111f89c82d) |
| Review date | 2026-10-03 |
| Review completed here | README, deployment and StarArm-102 documentation, and AI orchestration entry reviewed |
| Still pending here | Installation, software-only run, exact model compatibility, calibration, and physical pick-and-place validation |

This is a documentation reference, **not a tested release recommendation**. Upstream main may change; use the referenced documentation together with the matching source revision when evaluating this guide.

<a id="page-section-4"></a>

## Ownership and source code

The application is maintained by Butterfly Community. Its full source remains upstream; this directory contains integration documentation only. No upstream application code, model weights, or screenshots are redistributed here.

No repository-wide license file was found at the reviewed revision. Before incorporating or redistributing upstream code or assets, establish the applicable permission and license with the partner. Keep attribution and third-party license requirements with any future integration.

Use [Star Arm 102 support](../../README.md#documentation-and-support) for product questions and the [upstream issue tracker](https://github.com/butterfly-community/robot-arm/issues) for application questions. Include both the application revision and your exact hardware configuration.
