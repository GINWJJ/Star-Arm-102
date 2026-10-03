# Hardware setup

[Get started](getting-started.md) · [Hardware files](../hardware/README.md)

## Power and contents

Check the supplied adapter, arm label, and order packing list. Existing repository specifications list:

| Model | Listed power specification | Connector listed for the arm |
| --- | --- | --- |
| 102-LD | 12 V, 3 A | DC5521 |
| 102-HD | 12 V, 10 A | XT30 |
| 102-FL | 12 V, 10 A | XT30 |

These values are carried forward from the product specifications, not newly measured. Earlier accessory lists describe spare adapter cables separately; do not select a supply by the spare cable alone. If your supplied hardware differs, confirm the revision with Fashion Star before connecting power. Do not use a reBot follower's supply for a 102 leader.

Prepare a stable desk, base clamps, USB data cables, and the correct independent power supply for each arm. Check your order for cameras and mounts: a bare arm is not a complete two-camera ACT setup.

## Connect the arms

1. Switch off power before connecting or changing servo/power cables.
2. Fix the bases and clear the reachable area. Support the arms when torque is off; joints can move under gravity.
3. Connect each arm's servo bus to its own UC-01 hub as supplied. Use the supplied wiring; do not infer pin polarity from a photo.
4. Connect each hub to the computer with a USB data cable.
5. Connect the matching supply to each arm and power on.

```text
                    Ubuntu computer
                    /             \
                 USB               USB
                  |                 |
             Leader UC-01      Follower UC-01
                  |                 |
               LD / HD             FL
                  |                 |
           Matching supply    Matching supply
```

USB provides the data connection; it does not replace the servo power supply. A single FL uses only the right-hand branch. The ACT demo additionally connects two cameras to the computer.

## Identify serial ports

Connect one arm at a time and run:

```bash
python3 -m serial.tools.list_ports -v
```

This command requires `pyserial`, installed by the [Python setup](../python-sdk/README.md). On Ubuntu you can also inspect:

```bash
ls -l /dev/serial/by-id/
ls -l /dev/ttyUSB* /dev/ttyACM*
```

Some adapters do not expose a unique by-ID path. Label the cables and record which port belongs to each arm. Numbering can change after reconnection. The examples use `/dev/ttyUSB0` for the leader and `/dev/ttyUSB1` for FL; replace them with your actual ports.

For Ubuntu serial permissions:

```bash
sudo usermod -aG dialout "$USER"
```

Log out and back in, then check `id -nG`. For a temporary session, grant access only to the identified device, for example `sudo chmod a+rw /dev/ttyUSB0`. Do not change permissions on every USB device.

**Success:** both ports are visible and accessible. Continue with the [communication check](../python-sdk/README.md#check-communication-without-commanding-motion).

## Reference pose and stopping

Before direct Python teleoperation, place both arms in their matching physical zero/reference poses. The script resets multi-turn counts on connection; it does not run LeRobot calibration. If the reference pose for your hardware revision is unclear, confirm it before commanding motion. For LeRobot, follow the selected plugin's calibration prompts instead.

`Ctrl+C` requests program termination; it is not a hardware emergency stop and does not guarantee torque removal or immediate motion cancellation. Know how to switch off servo power while keeping clear of moving parts. Never rely on unplugging USB to stop the arm. On unexpected movement or feedback errors, stop the session and check the setup before restarting.
