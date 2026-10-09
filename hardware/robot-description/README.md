# Star Arm 102 Robot Descriptions

[← Hardware Resources](../README.md)　|　<sub>**English** / [简体中文](README.zh.md)</sub>

Choose the model for your arm. Each ROS 1 package includes URDF, visual/collision meshes, configuration and launch files, available as a source directory and a complete ZIP.

| Model | Source and instructions | Download |
| --- | --- | --- |
| 102-LD / 102-HD | [ld-hd/](ld-hd/) — leader handle and finger rings | [ZIP](ld-hd/star-arm-102-ld-hd-urdf.zip) |
| 102-FL | [fl/](fl/) — follower gripper | [ZIP](fl/star-arm-102-fl-urdf.zip) |

The LD/HD source retains a fixed `joint5`. HD-specific mass and inertia, joint limits and ROS/Gazebo runtime behavior still require validation. See each package's instructions before use.

## Existing ROS 2 Resources

The repository's [ROS 2 description package](../../ros2-humble/src/stararm102_description/README.md) continues to install [urdf/](urdf/) and [meshes/](meshes/) from this directory. These existing resources have different joint definitions from the ROS 1 packages above; their exact model applicability remains unconfirmed. The new downloads do not replace the ROS 2 runtime model.

URDF mesh paths use `package://stararm102_description/meshes/...`. Build from the complete repository following the [ROS 2 guide](../../ros2-humble/README.md). For another viewer, map `stararm102_description` to this directory and load both URDF and meshes.

See [license scope](../../LICENSE.md). Imported package metadata does not grant additional rights.
