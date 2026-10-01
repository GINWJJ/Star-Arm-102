# Troubleshooting and support

[Get started](getting-started.md) · [Compatibility](compatibility.md)

Stop at the first failing step. Check communication before calibration, motion before cameras, and camera images before running a policy.

| Symptom | Check | Expected result |
| --- | --- | --- |
| No serial device | USB data cable, power, one arm at a time; `python -m serial.tools.list_ports -v` | A port appears/disappears with that arm |
| Permission denied | Ubuntu `dialout` membership; log in again after adding the group | Port opens without running the application as root |
| Port busy | Close other control apps, serial monitors, and previous robot sessions | One process controls each bus |
| A servo ID is missing | Correct arm power, cable chain, IDs 0–6, 1,000,000 baud | Communication check lists all seven IDs |
| Button ID 7 not found | HD board present, correct mode/firmware; LD must not enable it | HD board responds, or button mode is disabled for a deliberate non-button test |
| Follower jumps or moves in the wrong direction | Stop; check leader/follower port assignment, zero/reference pose, plugin generation and calibration | Small movements track correctly before full teleoperation |
| Unknown LeRobot robot/teleoperator type | Active environment, a regular (not default editable) package install, and [type names](compatibility.md) | The selected type is registered by the installed plugin |
| Import fails after installing the HD package | Two packages share one import name | Recreate separate ACT and HD environments |
| Camera fails or views are swapped | Run `lerobot-find-cameras opencv`; inspect the images after reconnecting USB | `up` is overhead and `front` is frontal for the supplied ACT policy |
| ACT model cannot load | Point `--policy.path` to the full `pretrained_model` directory | Config, weights and processor files are together |
| Calibration not found | Use the same `--robot.id` and environment used during calibration | Correct file loads for that device |
| Dataset directory already exists | Choose a new `--dataset.root` and matching repo ID | A fresh run is saved without deleting previous recordings |
| Policy moves poorly | Compare the camera placement, scene, lighting, object and initial pose with the demo | Validate one trial before increasing the number of episodes |

If serial devices disappear unexpectedly, inspect system logs for the adapter and any service claiming it. Only change services such as `brltty` after confirming a conflict; it may be needed for an accessibility device.

## Report a problem

Use the [English issue form](https://github.com/servodevelop/Star-Arm-102/issues/new/choose). Include:

- Arm model(s), hardware revision and connection diagram/photo.
- OS, Python version, selected guide and repository commit.
- Package versions (`python -m pip freeze`) and GPU details for ACT.
- Exact command, full error, expected result, and first step that fails.
- Whether communication, calibration and basic motion each passed.

Remove access tokens and private paths from logs. For order-specific matters, contact the seller through your order channel and refer to the [official series page](https://fashionstar.com.hk/robot-arm/star-arm-102/).
