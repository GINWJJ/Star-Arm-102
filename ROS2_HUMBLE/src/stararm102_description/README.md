# Star Arm 102 robot description

This package supplies URDF, meshes, and RViz resources. Start with the [ROS 2 Humble guide](../../README.md) for installation and launches.

The model has six revolute arm joints and an actuated gripper finger with a mimicked second finger. Read the URDF limits and axes for the specific description used by your launch; do not substitute linear gripper units for its rotary joint values.

See [joint naming across interfaces](../../../docs/specifications.md#joint-ids-and-names). The physical driver's initialization and servo conversion are implemented in `robo_driver`, not in this description package.
