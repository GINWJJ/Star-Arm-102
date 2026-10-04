# Cross-Brand Compatibility and Evidence

[Pairing directory](README.md) · [Software environments](../docs/compatibility.md)

Status reviewed: October 3, 2026. **Pending** means this repository does not yet provide sufficient pairing-specific instructions or test evidence; it does not mean the pairing is impossible. **Upstream documented** means an external guide exists, not that this documentation update bench-tested the hardware.

| Follower | LD leader | HD leader / button behavior | Direct Python | LeRobot teleoperation | Data collection | Training / inference |
| --- | --- | --- | --- | --- | --- | --- |
| [Galaxea A1](galaxea-a1/README.md) | Pending | Pending / pending | Pending | Pending | Pending | Pending |
| [Lumos Touch](lumos-touch/README.md) | Pending | Pending / pending | Pending | Pending | Pending | Pending |
| [YAM, model pending](yam/README.md) | Pending | Pending / pending | Pending | Pending | Pending | Pending |
| [Seeed reBot B601-DM / B601-RS](seeed-rebot/README.md) | Confirm exact 102 leader revision against upstream | Exact HD revision and buttons pending | No dedicated example here | Upstream documented | Upstream documented | No pairing-specific validated policy here |

The reBot row refers to the [upstream LeRobot main-branch guide for B601-DM and B601-RS](https://huggingface.co/docs/lerobot/main/rebot_b601), reviewed on October 4, 2026. Follow its source-install instructions and select the matching motor family and adapter. Its leader is named StarArm102 / reBot Arm 102; this is not blanket confirmation for every LD or HD revision. DM and RS configurations must be validated separately.

## Evidence needed for a validated entry

Record the exact follower and leader revisions; firmware, SDK and plugin versions or commits; operating system and Python version; adapters and wiring; calibration procedure; joint or Cartesian mapping; gripper behavior; HD button behavior where applicable; and test date and results.

Validate communication, teleoperation, data recording, training, and inference separately. A demo video alone does not specify a reproducible environment. A virtual model following a leader does not establish real-follower control. Galaxea A1 and A1Z must be tracked separately.

The supplied Star Arm 102-FL ACT policy is not a cross-brand pretrained policy. Different action spaces, kinematics, calibration, grippers, or cameras require their own integration and evaluation.
