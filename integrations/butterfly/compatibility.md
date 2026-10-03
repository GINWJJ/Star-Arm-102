# Butterfly integration compatibility

[Integration overview](README.md) · [Setup](setup.md)

The following describes the [reviewed upstream revision](https://github.com/butterfly-community/robot-arm/tree/08498c31c56cf339601851851225bf111f89c82d). It records upstream documentation, not a Fashion Star hardware test result.

| Component | Upstream configuration / requirement | What to confirm |
| --- | --- | --- |
| Robot | StarArm-102 with six arm joints and a gripper | Exact product variant, hardware revision, joint limits, and zero convention |
| Servos | RA8-U35H-M for the six axes and gripper | Actual installed models and supported firmware; do not infer these from bus IDs |
| Camera | RealSense D415 RGB-D camera | Device access, color/depth alignment, and calibration; other cameras need validation |
| Runtime | Docker-managed frontend, Rust/Dora services, perception compute, and ROS/MoveIt motion services | Host support, device passthrough, model files, build prerequisites, and compute requirements in upstream deployment instructions |
| Natural-language interface | Compatible AI model service with the required image and tool-call capabilities | Provider, credentials, endpoint compatibility, and any service charges |
| Software-only mode | Simulated camera data and virtual joint feedback | Software workflow validation only; not physical grasp reliability |

The reviewed deployment document lists separate base images, including Ubuntu 26.04, Python 3.11 for perception, and Node.js 24 for the frontend. These are components of the upstream container stack, not a claim that this repository's ACT or ROS 2 Humble environments can run the application unchanged. No minimum GPU/VRAM specification is asserted here.

## Model and driver boundary

The partner fixes its vendor model source to commit `0896306e40891c3ee4c97228e85dd708d61326de`, applies model/dynamics/ROS-interface patches, and uses its own Rust execution service. Do not replace these assets with this repository's current URDF or run both serial-control stacks against the same arm.

Review the partner's [StarArm-102 model and driver conventions](https://github.com/butterfly-community/robot-arm/blob/08498c31c56cf339601851851225bf111f89c82d/docs/STARARM-102.md) and [deployment requirements](https://github.com/butterfly-community/robot-arm/blob/08498c31c56cf339601851851225bf111f89c82d/docs/DOCKER.md). Joint mappings, camera extrinsics, and ACT calibration files are not assumed interchangeable.

## Validation still needed

- Match the partner's physical setup to a specific 102 product and revision.
- Record the host, compute hardware, software versions, and model-service configuration used for a successful setup.
- Reproduce the software-only workflow, then communication, calibration, and a physical pick-and-place task.
- Record observed limitations and results before marking an entry as Fashion Star validated.
