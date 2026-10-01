# Product overview and joint mapping

[Home](../README.md) · [Hardware setup](hardware-setup.md)

Star Arm 102 provides six arm joints and a gripper/handle channel. LD and HD are leaders; FL is the actuated follower. The HD adds a button-based locking function; its exact software behavior depends on the integration.

| Model | Role | Next step |
| --- | --- | --- |
| 102-LD | Leader for teleoperation | [Python](../Python_SDK/README.md) or [release-compatible LeRobot](../Lerobot/README.md) |
| 102-HD | Leader with button-board support | [Python](../Python_SDK/README.md) or [refactored LeRobot](../Lerobot/lerobot-stararm102/README.md) |
| 102-FL | Follower for teleoperation and policy execution | [ACT model](../Lerobot/examples/act_pick/README.md) or [ROS 2](../ROS2_HUMBLE/README.md) |

## Joint IDs and names

| Servo ID | Release-compatible LeRobot | Refactored LeRobot | ROS description |
| --- | --- | --- | --- |
| 0 | `Motor_0` | `shoulder_pan` | `joint1` |
| 1 | `Motor_1` | `shoulder_lift` | `joint2` |
| 2 | `Motor_2` | `elbow_flex` | `joint3` |
| 3 | `Motor_3` | `wrist_flex` | `joint4` |
| 4 | `Motor_4` | `wrist_yaw` | `joint5` |
| 5 | `Motor_5` | `wrist_roll` | `joint6` |
| 6 | `gripper` | `gripper` | `joint7_left` (with a mimicked right finger) |
| 7, when fitted | Not part of the seven action channels | HD button board | Not an arm joint |

Matching IDs do not mean matching units, signs, scaling, or calibration. See [plugin compatibility](compatibility.md). Do not transfer joint values between these interfaces without the appropriate conversion.

For product dimensions, payload, and the exact supplied configuration, use the official [LD](https://fashionstar.com.hk/store/product/star-arm-102-ld/), [HD](https://fashionstar.com.hk/store/product/star-arm-102-hd/), and [FL](https://fashionstar.com.hk/store/product/star-arm-102-fl/) specifications. The [LD engineering drawings](../Hardware/cad/README.md) provide mechanical reference files. Motion limits in a URDF or configuration describe that software model and are not a substitute for the limits of your hardware revision.
