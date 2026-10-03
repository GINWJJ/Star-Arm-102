# Star Arm 102 硬件资料

[English / 状态总表](README.md) · [交接核对报告](handoff-review.zh.md)

按实物型号选择：[102-LD](102-ld/README.md)、[102-HD](102-hd/README.md)、[102-FL](102-fl/README.md)。

LD 与 HD 共用机械主体，但 HD 另有按钮底座、按钮盖和 UK-01 按键板，舵机、线材和紧固件也存在差异。因此分别提供各型号入口和文件。不能把 LD 整机模型或 BOM 直接当作 HD 版本。

英文首页的状态表区分已提供、部分提供、待核对、存在冲突和未提供。STEP 主打印件的文件数量齐全，不代表整机制造资料齐全或已经过装配验证。交接 Excel 和 3MF 保留原文及原始内容，当前不是已确认的量产发布包。

三个型号均有 `robot-description/urdf/` 和 `robot-description/meshes/` 目录入口；目前没有确认可用的型号专属模型。仓库原有 ROS 模型保留在[共享模型目录](robot-description/README.md)，没有用存在疑问的交接 URDF 覆盖。
