# Star Arm 102 Leaders + Galaxea A1

[← Integrations](../README.md)　|　**English**

**On this page:**

- [⚙️ Hardware and supported functions](#page-section-1)
- [🐍 Python path](#page-section-2)
- [🤗 LeRobot path](#page-section-3)
- [📚 Resources to complete this guide](#page-section-4)

[Capability status](../compatibility.md) · [Common preparation](../common-setup.md)

**Status: pairing guide in preparation.** This is the entry for customers using a Star Arm 102-LD or HD leader with Galaxea A1. Pairing-specific adapters, executable instructions, and hardware test records have not yet been provided in this repository.

This page concerns **A1**. The **A1Z virtual model** shown in the web tool is a separate model and is not evidence of A1 real-arm control.

<a id="page-section-1"></a>

## Hardware and supported functions

| Item | Current status |
| --- | --- |
| Exact follower revision and gripper | To be documented |
| LD compatibility and mapping | To be documented and verified |
| HD compatibility and button behavior | To be documented and verified separately |
| Adapters, cables, power, and host requirements | Pairing-specific list pending |
| Joint / Cartesian mapping and calibration | Pending |

<a id="page-section-2"></a>

## Python path

The [Python SDK directory](../../python-sdk/README.md) currently provides LD/HD → Star Arm 102-FL examples. A Galaxea A1-specific follower driver and mapping must be documented before executable commands can be added here. Do not substitute this follower's port into the FL example.

<a id="page-section-3"></a>

## LeRobot path

The matching follower plugin, leader interface, pinned environment, calibration commands, and teleoperation example are pending. See [existing Star Arm integrations](../../lerobot/README.md) for context, not as installation instructions for this pairing.

Data collection, training, and policy execution each need their own validation. The supplied FL ACT policy is not a ready-to-run policy for this follower.

<a id="page-section-4"></a>

## Resources to complete this guide

- Tested leader and follower revisions, software versions, and source repository links.
- Wiring and equipment list; first-run commands and expected results.
- Joint or pose mapping, gripper behavior, and stopping procedure.
- Separate LD / HD results, including the HD button behavior.
- Pairing-specific Wiki tutorial and demonstration video.

For setup assistance, use [Fashion Star support](https://fashionstar.com.hk/support/). Include the follower model/revision, leader model, and whether you need Python teleoperation or a LeRobot workflow. Share reproducible software issues through [GitHub Issues](https://github.com/servodevelop/Star-Arm-102/issues/new/choose).
