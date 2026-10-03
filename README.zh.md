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

## 🌐 跨品牌 Follower 搭配

102-LD／HD 与其他品牌 Follower 的资料按具体型号组织：

- [Galaxea A1](integrations/galaxea-a1/README.md)：搭配说明及验证记录待补充。
- [Lumos Touch](integrations/lumos-touch/README.md)：搭配说明及验证记录待补充。
- [YAM](integrations/yam/README.md)：具体型号及搭配说明待确认。
- [Seeed reBot B601](integrations/seeed-rebot/README.md)：已有 B601-DM 上游 LeRobot 指南。

[搭配导航](integrations/README.md) · [能力与验证状态](integrations/compatibility.md)。分别确认 LD、HD 按键、遥操作、数据采集和推理支持；目录中列出型号不等于所有功能均已验证。

## 🎛️ 控制与配置工具

- [机械臂网页控制与调试指南](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)：工具入口、连接和操作说明。
- [机械臂与舵机工具导航](tools/README.md)：网页工具和桌面软件的 Wiki 入口。

工具本体、下载及详细教程统一由 Wiki 维护，仓库只提供导航与界面预览。

## 🤖 两种 AI 任务入口

| ACT 预训练任务 | 自然语言控制机械臂 |
| --- | --- |
| Fashion Star 提供的积木放置策略，使用指定双相机配置和 102-FL。 | Butterfly Community 伙伴项目：通过网页描述抓放任务，结合视觉和运动规划执行。 |
| [打开 ACT 指南](lerobot/examples/act_pick/README.md) | [查看伙伴项目接入说明](integrations/butterfly/README.zh-CN.md) |

伙伴报告已在 StarArm-102 与 RealSense D415 上完成实物抓放；具体 102 型号适配及我们的完整复测尚待确认。自然语言入口需要兼容的模型服务。

## 📚 使用文档

| 需求 | 当前英文入口 | 中文补充资料 |
| --- | --- | --- |
| 产品介绍与选型 | [首页](README.md) | [原中文产品介绍](README.legacy.zh.md) |
| 收到产品后开始使用 | [Getting started](docs/getting-started.md) | 以当前英文配置和兼容性说明为准 |
| Python 连接和遥操作 | [Python quick start](python-sdk/README.md) | [原 Python 说明](python-sdk/PYTHON_SDK_GUIDE.zh.md) |
| LeRobot | [选择集成方案](lerobot/README.md) | [原 LeRobot 教程](lerobot/stararm102.md) |
| ACT 预训练模型 | [模型入口](lerobot/examples/act_pick/README.md) | [原中文模型说明](lerobot/examples/act_pick/README.zh.md) |
| ROS 2 | [ROS 2 Humble](ros2-humble/README.md) | [原中文教程](ros2-humble/README.zh.md) |
| 硬件文件 | [Hardware](hardware/README.md) | [中文硬件索引](hardware/README.zh.md) |

中文补充内容不作为另一套独立维护的安装规范。旧命令、环境和默认端口可能与当前英文入口不同，尤其应先阅读 [LeRobot 两代插件兼容性](docs/compatibility.md)。原有中文文件、图纸、BOM 和示例代码中的中文注释不要求在第一阶段全部移除。

`Ctrl+C` 是退出程序的请求，不是硬件急停；拔下 USB 不保证电机立即停止或卸力。异常运动时应使用可控的伺服电源关闭方式，并避免进入运动范围。

第二阶段再完善图文和视频结合的双语 Wiki 教程。
