# Star Arm 102-FL 硬件

[← 硬件资源](../README.zh.md)　|　[English](README.md) / **简体中文**

<p align="center">
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/09/102-fl-diy-kit-main-image-01.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/09/102-fl-diy-kit-main-image-01.webp" alt="Star Arm 102-FL DIY 套件" width="15%"></a>
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-02.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-02.webp" alt="Star Arm 102-FL 产品图片 2" width="15%"></a>
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-03.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-03.webp" alt="Star Arm 102-FL 产品图片 3" width="15%"></a>
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-04.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-04.webp" alt="Star Arm 102-FL 产品图片 4" width="15%"></a>
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-05.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-05.webp" alt="Star Arm 102-FL 产品图片 5" width="15%"></a>
  <a href="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-06.webp"><img src="https://fashionstar.com.hk/store/wp-content/uploads/2026/06/102-fl-main-image-06.webp" alt="Star Arm 102-FL 产品图片 6" width="15%"></a>
</p>

**本页导航：**

- [📂 资源目录](#resources)
- [📋 物料清单](#bill-of-materials)

<a id="resources"></a>

## 资源目录

| 目录 | 内容 | 状态 |
| --- | --- | --- |
| [assembly-guide/](assembly-guide/README.zh.md) | 主体机械臂装配视频 | ✅ 视频已提供<br>🟡 版本及接线覆盖待核对 |
| [step/](step/) | parts/ 零件模型；assembly/ 整机装配模型 | ✅ 文件已提供<br>🟡 配套版本待核对 |
| [printing/](printing/) | 3MF 打印项目；STL：[查看零件](printing/stl/) · [下载整套 ZIP](printing/stl/star-arm-102-fl-stl.zip) | ✅ 11 个独立零件 3MF 及整套项目已提供；11 个 STL 及整套 ZIP 已提供<br>🟡 link1 参数与 BOM 冲突；实物打印待验证 |
| [drawings/](drawings/) | PDF／DWG 图纸 | ✅ 参考文件已提供<br>🟡 版本待核对 |
| [robot-description/](robot-description/) | 型号专用 URDF 和网格 | — 待提供 |

<a id="bill-of-materials"></a>

## 物料清单

下表列出 102-FL 的 **29 项装机物料**；无图片的条目标为待补。

打印件名称与 STEP、STL 及独立 3MF 文件名一致。备注中的打印参数仅供参考，尚未完成实物打印验证。link1 的 BOM 参数为壁数 5／填充 50%，而原 3MF 为壁数 2／填充 15%，打印前需确认。

| 序号 | 名称 | 图片 | 描述 | 数量 | 备注 |
| :---: | --- | :---: | --- | :---: | --- |
| 1 | RX8-U50H-M | 待补 | RX8-U50H-M  半成品舵机，固件版本V330 | 2 | 装机件 |
| 2 | RA8-U35H-M | 待补 | RA8-U35H-M  固件版本V225 | 3 | 装机件 |
| 3 | RA8-U35H-M-C047 | 待补 | 半成品舵机，单轴后盖，固件版本V225 | 1 | 装机件 |
| 4 | RA8-U27H-M-C005 | 待补 | 半成品舵机，单轴后盖，D轴，固件版本V225 | 1 | 装机件 |
| 5 | star-arm-102-base-bottom | <img src="images/star-arm-102-base-bottom.png" alt="star-arm-102-base-bottom" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 2；填充 15% |
| 6 | star-arm-102-base-top | <img src="images/star-arm-102-base-top.png" alt="star-arm-102-base-top" width="90"> | PLA 3D 打印件（象牙白） | 1 | 分区域参数，详见 3MF |
| 7 | star-arm-102-link1 | <img src="images/star-arm-102-link1.png" alt="star-arm-102-link1" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 5；填充 50% |
| 8 | star-arm-102-link2 | <img src="images/star-arm-102-link2.png" alt="star-arm-102-link2" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 2；填充 10% |
| 9 | star-arm-102-link3 | <img src="images/star-arm-102-link3.png" alt="star-arm-102-link3" width="90"> | PLA 3D 打印件（象牙白＋黑色） | 1 | 分区域参数，详见 3MF |
| 10 | star-arm-102-link4 | <img src="images/star-arm-102-link4.png" alt="star-arm-102-link4" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 2；填充 15% |
| 11 | star-arm-102-link5 | <img src="images/star-arm-102-link5.png" alt="star-arm-102-link5" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 2；填充 15% |
| 12 | star-arm-102-link6-gripper | <img src="images/star-arm-102-link6-gripper.png" alt="star-arm-102-link6-gripper" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 4；填充 15% |
| 13 | star-arm-102-gripper-body | <img src="images/star-arm-102-gripper-body.png" alt="star-arm-102-gripper-body" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 4；填充 15% |
| 14 | star-arm-102-fingertip-left | <img src="images/star-arm-102-fingertip-left.png" alt="star-arm-102-fingertip-left" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 4；填充 15% |
| 15 | star-arm-102-fingertip-right | <img src="images/star-arm-102-fingertip-right.png" alt="star-arm-102-fingertip-right" width="90"> | PLA 3D 打印件（象牙白） | 1 | 壁数 4；填充 15% |
| 16 | 滚针轴承 | 待补 | AXK2035+2AS | 1 | 装机件 |
| 17 | PCBA | <img src="https://fashionstar.com.cn/wiki/snippets/shop-info/images/uc-01-primary.webp" alt="UC-01" width="90"> | UC-01 XT30 | 1 | 装机件 |
| 18 | 线材 | 待补 | PH-3Y 双头反向60芯 0.08 黑色硅胶排线L=120 mm  黑色编织线 | 4 | 装机件 |
| 19 | 线材 | 待补 | PH-3Y 双头反向60芯 0.08 黑色硅胶排线L=200 mm  黑色编织线 | 3 | 装机件 |
| 20 | 螺丝 | 待补 | HSCS M3*10 12.9级内六角圆柱头螺钉 | 1 | 装机件 |
| 21 | 螺丝 | 待补 | M3*22黑色内六角 | 4 | 装机件 |
| 22 | 螺丝 | 待补 | M3*10加硬包黑十字槽螺杆 | 1 | 装机件 |
| 23 | 螺丝 | 待补 | PB2.0*5 自攻十字槽加硬包黑沉头螺杆 | 30 | 装机件 |
| 24 | 螺丝 | 待补 | M2*4.5 预点胶十字槽螺杆黑色沉头 | 47 | 装机件 |
| 25 | 螺丝 | 待补 | M2*10 黑色内六角 | 8 | 装机件 |
| 26 | 螺丝 | 待补 | M2*8 黑色内六角 | 16 | 装机件 |
| 27 | 螺丝 | 待补 | M3*12自攻十字槽螺杆 | 2 | 装机件 |
| 28 | 螺母 | 待补 | M3防松螺母 黑色 | 6 | 装机件 |
| 29 | 垫片 | 待补 | M3*6*0.5 | 2 | 装机件 |

发现资料错误或需要帮助？请通过 [Support 支持中心](https://fashionstar.com.hk/support/) 联系我们，并注明型号及对应文件或条目。
