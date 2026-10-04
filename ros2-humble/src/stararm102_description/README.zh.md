# Star Arm 102 机器人描述

[← src](../)　|　🌐 [English](README.md) / **简体中文**

本包从 `hardware/robot-description/` 安装作为统一来源的 [URDF 和网格](../../../hardware/robot-description/README.md)，同时安装 launch 和 RViz 资源。请在完整仓库中构建；单独复制此 ROS 包会缺少模型源文件。安装和启动请先阅读 [ROS 2 Humble 指南](../../README.zh.md)。

模型包含六个旋转臂关节，以及一个主动夹爪手指和一个通过 mimic 跟随的手指。请核对启动文件使用的具体 URDF 中的限位和轴向；不要将夹爪直线位移单位直接代入旋转关节值。

参见 [各接口的关节命名](../../../docs/specifications.md#joint-ids-and-names)。实物驱动初始化及舵机数值转换在 `robo_driver` 中实现，不在本描述包中。

[历史中文资料（非当前操作指南）](legacy-guide.zh.md)
