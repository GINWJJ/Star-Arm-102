# Star Arm 102 robot description

[← src](../)　|　<sub>**English** / [简体中文](README.zh.md)</sub>

This package contains the ROS 2 [URDF](urdf/) and [meshes](meshes/), alongside launch and RViz resources. Start with the [ROS 2 Humble guide](../../README.md) for installation and launches. This model retains the existing ROS 2 joint definitions and is maintained separately from the ROS 1 downloads in each hardware model directory.

The model has six revolute arm joints and an actuated gripper finger with a mimicked second finger. Read the URDF limits and axes for the specific description used by your launch; do not substitute linear gripper units for its rotary joint values.

See [joint naming across interfaces](../../../docs/specifications.md#joint-ids-and-names). The physical driver's initialization and servo conversion are implemented in `robo_driver`, not in this description package.

[Historical Chinese material (not the current operating guide)](legacy-guide.zh.md)
