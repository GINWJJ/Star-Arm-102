<h1 align="center">🦾 Star Arm 102</h1>

<p align="center"><strong>面向 LeRobot 的开源 6+1 自由度机械臂</strong><br>中文导航与补充资料</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-64748B?style=flat-square" alt="English"></a>
  <a href="README.zh.md"><img src="https://img.shields.io/badge/语言-简体中文-8B5CF6?style=flat-square" alt="简体中文"></a>
</p>

仓库以 [English README](README.md) 为默认入口。首次安装、连接检查、遥操作和 ACT 预训练模型运行均提供英文说明；中文资料作为补充保留。

## 🛒 官网与购买入口

- [Fashion Star 中文官网](https://fashionstar.com.cn/) · [Star Arm 102 中文系列页](https://fashionstar.com.cn/robot-arm/star-arm-102/)
- [Star Arm 102-LD 主臂](https://fashionstar.com.cn/store/product/star-arm-102-ld/)
- [Star Arm 102-HD 带锁定功能的主臂](https://fashionstar.com.cn/store/product/star-arm-102-hd/)
- [Star Arm 102-FL 从臂](https://fashionstar.com.cn/store/product/star-arm-102-fl/)
- [淘宝购买](https://item.taobao.com/item.htm?ft=t&id=1045277992605)
- [English website](https://fashionstar.com.hk/) · [English series overview](https://fashionstar.com.hk/robot-arm/star-arm-102/)

## 📚 使用文档

| 需求 | 当前英文入口 | 中文补充资料 |
| --- | --- | --- |
| 产品介绍与选型 | [首页](README.md) | [原中文产品介绍](README.legacy.zh.md) |
| 收到产品后开始使用 | [Getting started](docs/getting-started.md) | 以当前英文配置和兼容性说明为准 |
| Python 连接和遥操作 | [Python quick start](Python_SDK/README.md) | [原 Python 说明](Python_SDK/PYTHON_SDK_GUIDE.zh.md) |
| LeRobot | [选择集成方案](Lerobot/README.md) | [原 LeRobot 教程](Lerobot/stararm102.md) |
| ACT 预训练模型 | [模型入口](Lerobot/examples/act_pick/README.md) | [原中文模型说明](Lerobot/examples/act_pick/README.zh.md) |
| ROS 2 | [ROS 2 Humble](ROS2_HUMBLE/README.md) | [原中文教程](ROS2_HUMBLE/README.zh.md) |
| 硬件文件 | [Hardware](Hardware/README.md) | [中文硬件索引](Hardware/README.zh.md) |

中文补充内容不作为另一套独立维护的安装规范。旧命令、环境和默认端口可能与当前英文入口不同，尤其应先阅读 [LeRobot 两代插件兼容性](docs/compatibility.md)。原有中文文件、图纸、BOM 和示例代码中的中文注释不要求在第一阶段全部移除。

`Ctrl+C` 是退出程序的请求，不是硬件急停；拔下 USB 不保证电机立即停止或卸力。异常运动时应使用可控的伺服电源关闭方式，并避免进入运动范围。

第二阶段再完善图文和视频结合的双语 Wiki 教程。
