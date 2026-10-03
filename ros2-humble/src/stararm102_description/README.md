# Star Arm 102 robot description

[English](README.md) · [简体中文](README.zh.md)

This package installs the authoritative [URDF and meshes](../../../hardware/robot-description/README.md) from `hardware/robot-description/`, alongside its launch and RViz resources. Build from the complete repository checkout; copying only this ROS package omits the model source files. Start with the [ROS 2 Humble guide](../../README.md) for installation and launches.

The model has six revolute arm joints and an actuated gripper finger with a mimicked second finger. Read the URDF limits and axes for the specific description used by your launch; do not substitute linear gripper units for its rotary joint values.

See [joint naming across interfaces](../../../docs/specifications.md#joint-ids-and-names). The physical driver's initialization and servo conversion are implemented in `robo_driver`, not in this description package.

[Historical Chinese material (not the current operating guide)](legacy-guide.zh.md)
