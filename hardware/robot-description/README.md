# Star Arm 102 robot description

[← Hardware Resources](../README.md)

[ROS description package](../../ros2-humble/src/stararm102_description/README.md)

This is the authoritative copy of the existing robot model, moved from the ROS package. Its exact LD/HD/FL applicability and production revision have not been confirmed. Do not treat it as a validated model for all variants.

- [URDF](urdf/star-arm-102.urdf): link geometry references, joints, limits, masses and inertia.
- [Meshes](meshes/): nine STL files shared by visual and collision elements. These are simulation resources, not validated printing files.

The URDF retains `package://stararm102_description/meshes/...` references. For ROS 2, build from the complete repository following the [ROS guide](../../ros2-humble/README.md). The ROS package installs the URDF and meshes from this directory into its package share directory. Edit models here rather than maintaining a second copy inside ROS.

For other viewers, configure a package resolver mapping `stararm102_description` to this directory. A loader without package-URI support requires adapted mesh paths. Download both `urdf/` and `meshes/`, not the URDF alone.

The relocation changes only paths and filenames, not joint definitions or physical parameters. LD/HD servo differences and FL applicability need engineering review before model-specific versions are published. See the repository [license scope](../../LICENSE.md).
