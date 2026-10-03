# Get started with Star Arm 102

[Home](../README.md) · [Troubleshooting](troubleshooting.md)

## 1. Identify your equipment

Check the product/order label before selecting software. The arms look similar; use the model label rather than appearance alone.

| Model | Role | First task |
| --- | --- | --- |
| 102-LD | Manually operated leader | Read its seven servo IDs, then teleoperate a compatible follower |
| 102-HD | Leader with a lock-button integration | Confirm the supplied button board/firmware, then use the HD instructions |
| 102-FL | Powered follower | Check communication and calibration before sending motion commands |

![Star Arm 102 overview](../media/images/11.png)

For ordering and product identification, see the [official series page](https://fashionstar.com.hk/robot-arm/star-arm-102/). A parts kit first needs assembly; [available DIY resources](../hardware/README.md) are organized by LD, HD, and FL with per-model availability status.

For a third-party follower, use the [cross-brand pairing directory](../integrations/README.md) and its hardware-specific preparation. The FL steps below are for Star Arm followers.

## 2. Prepare and connect

Follow [hardware setup](hardware-setup.md). You need the correct power adapter for each arm, a fixed base, USB data cables, and a computer. The customer examples target Ubuntu 22.04. Cameras are needed for the ACT demo, but not for a first communication or direct teleoperation check.

**Success:** each connected arm has an identifiable serial port, and its model and power adapter match. USB port numbers in examples are placeholders.

## 3. Select one path

| Your setup / goal | Follow this guide |
| --- | --- |
| LD + FL: first movement | [Python direct teleoperation](../python-sdk/README.md) |
| HD + FL: first movement | [Python direct teleoperation](../python-sdk/README.md), including HD button configuration |
| FL only: confirm the connection | [Communication check](../python-sdk/README.md#check-communication-without-commanding-motion) |
| FL + two cameras: run the provided model | [Pretrained ACT model](../lerobot/examples/act_pick/inference.md) |
| LD + FL: record demonstrations | [LeRobot release-compatible setup](../lerobot/README.md#release-compatible-environment) |
| HD + FL: LeRobot with button integration | [Refactored HD/FL setup](../lerobot/lerobot-stararm102/README.md) |
| Leader + Galaxea A1 / Lumos Touch / YAM | [Choose your follower pairing](../integrations/README.md) |
| Leader + reBot B601 | [reBot guide](../integrations/seeed-rebot/README.md) |
| ROS 2 development | [ROS 2 Humble](../ros2-humble/README.md) |

Do not install all paths into one environment. The [compatibility table](compatibility.md) explains which combinations have release evidence and which still require hardware validation.

## 4. Check before motion

Use the Python communication check to identify servos before direct teleoperation. LeRobot users must also run their selected plugin's calibration procedure and keep the same device ID in subsequent commands. Each guide describes its own zero/reference convention; do not copy calibration files across plugin generations.

**Success:** all seven servo IDs respond; calibration, when required, is saved; a small leader movement produces the expected follower movement. Start without cameras so that communication and motion can be checked independently.

## 5. Continue to the ACT demo

After basic checks, set up the two cameras and reproduce the [ACT workspace](../lerobot/examples/act_pick/inference.md#prepare-the-follower-and-cameras). Start with one trial. You do not need to train this supplied policy yourself.

If a step fails, stop there and use [troubleshooting](troubleshooting.md). Include the model, environment, command, and full error when [reporting an issue](https://github.com/servodevelop/Star-Arm-102/issues/new/choose).
