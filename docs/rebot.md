# Use a Star Arm 102 leader with reBot

[Get started](getting-started.md) · [Compatibility](compatibility.md)

The B601 follower uses a different motor bus from Star Arm 102-FL. Do not run `Python_SDK/stararm102_ro.py` against a B601, and do not connect the follower's supply to the 102 leader.

For the upstream integration, follow the [LeRobot reBot guide](https://huggingface.co/docs/lerobot/rebot_b601), including its installation, wiring references, calibration and single/bimanual commands. Upstream uses `rebot_102_leader` and `rebot_b601_follower`; older Fashion Star fork examples may use other names. Keep the complete workflow within one documented version.

The [Seeed reBot repository](https://github.com/Seeed-Projects/reBot-DevArm) lists Star Arm 102-LD compatibility. Check your exact follower variant (DM or RS) and adapter before installing. HD button/locking behavior is a separate capability: basic leader compatibility does not establish support for the HD board.

1. Identify the 102 leader and B601 variant.
2. Create a separate environment using the upstream guide.
3. Find each bus port and complete the guide's calibration steps.
4. Test small single-joint movements without cameras.
5. Add cameras or dual-arm operation only after the basic pairing passes.

**Success:** correct movement direction and gripper mapping, with no missing feedback. This documentation update has not performed a new bench test of the pairing. If your kit needs a supplier-specific fork or HD firmware, obtain its exact version before proceeding; do not mix commands from the refactored FL plugin with upstream B601 commands.
