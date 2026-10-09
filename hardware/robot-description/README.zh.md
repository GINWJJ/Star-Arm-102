# Star Arm 102 机器人描述

[← 硬件资源](../README.zh.md)　|　<sub>[English](README.md) / **简体中文**</sub>

请选择对应手臂的模型。每个 ROS 1 软件包包含 URDF、外观与碰撞网格、配置和启动文件，同时提供源码目录与完整 ZIP。

| 型号 | 源码与说明 | 下载 |
| --- | --- | --- |
| 102-LD / 102-HD | [ld-hd/](ld-hd/) — 主臂手柄与指环 | [ZIP](ld-hd/star-arm-102-ld-hd-urdf.zip) |
| 102-FL | [fl/](fl/) — 从臂夹爪 | [ZIP](fl/star-arm-102-fl-urdf.zip) |

LD/HD 源模型保留了固定的 `joint5`。HD 专用质量与惯量、关节限位及 ROS/Gazebo 运行仍待验证。使用前请阅读对应软件包的说明。

## 现有 ROS 2 资源

仓库的 [ROS 2 描述包](../../ros2-humble/src/stararm102_description/README.zh.md) 继续从本目录安装 [urdf/](urdf/) 和 [meshes/](meshes/)。这些现有资源与上述 ROS 1 软件包的关节定义不同，具体适用型号尚未确认。新增下载不会替换 ROS 2 运行使用的模型。

URDF 网格路径使用 `package://stararm102_description/meshes/...`。请按照 [ROS 2 指南](../../ros2-humble/README.zh.md) 从完整仓库构建。其他查看器需将 `stararm102_description` 映射到本目录，并同时加载 URDF 和网格。

请参阅 [许可范围](../../LICENSE.md)。导入的软件包元数据不授予额外权利。
