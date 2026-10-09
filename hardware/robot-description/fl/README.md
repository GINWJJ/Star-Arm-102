# Star Arm 102 FL Robot Description

[← Robot Description](../README.md)　|　<sub>**English** / [简体中文](README.zh.md)</sub>

Follower gripper geometry for FL.

[Download complete ZIP](star-arm-102-fl-urdf.zip) · [Browse source package](stararm102_fl_description/)

This is a **ROS 1 / catkin** package. The ZIP and source directory contain the same files. Keep the whole package together because the URDF references its meshes.

Place `stararm102_fl_description/` in your catkin workspace’s `src/`, build and source the workspace, then run:

```bash
roslaunch stararm102_fl_description display.launch
```

RViz opens with its default layout; set Fixed Frame to `base_link` and add a RobotModel display. Joint limits, masses, inertia and ROS/Gazebo runtime behavior have not been validated. Collision geometry alone does not make a viewer prevent intersections.

[ROS 2 guide](../../../ros2-humble/README.md) · [License scope](../../../LICENSE.md)
