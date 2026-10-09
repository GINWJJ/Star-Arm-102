# Star Arm 102 FL 机器人描述

[← 102-FL 硬件资源](../README.zh.md)　|　<sub>[English](README.md) / **简体中文**</sub>

FL 从臂夹爪结构。

[下载完整 ZIP](star-arm-102-fl-urdf.zip) · [浏览源码目录](stararm102_fl_description/)

这是 **ROS 1 / catkin** 软件包。ZIP 与源码目录包含相同文件；请保留整个软件包目录，URDF 需要读取其中的网格。

将 `stararm102_fl_description/` 放入 catkin 工作空间的 `src/`，构建并加载工作空间环境后运行：

```bash
roslaunch stararm102_fl_description display.launch
```

RViz 使用默认布局打开；将 Fixed Frame 设为 `base_link`，添加 RobotModel 显示项。关节限位、质量、惯量及 ROS/Gazebo 运行尚未验证。碰撞形状定义不代表查看器会自动阻止穿模。

[ROS 2 使用指南](../../../ros2-humble/README.zh.md) · [许可范围](../../../LICENSE.md)
