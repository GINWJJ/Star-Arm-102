# Integrations: Follower Pairings & Partner Applications

[← Home](../README.md)

**On this page:**

- [🌐 Cross-brand follower pairings](#page-section-1)
- [🧭 Choose a workflow](#page-section-2)
- [🤝 Partner applications](#page-section-3)
- [🛠️ How these resources are maintained](#page-section-4)

Find [cross-brand follower pairings](#cross-brand-follower-pairings) or [partner applications](#partner-applications).

<a id="page-section-1"></a>

## Cross-brand follower pairings

Use this directory to explore Star Arm 102-LD / HD leader pairings with third-party followers. Start with your follower model, then choose its Python or LeRobot workflow.

| Your follower | Pairing guide | Current documentation status |
| --- | --- | --- |
| Galaxea A1 | [A1 pairing](galaxea-a1/README.md) | Pairing-specific code, setup instructions, and test records pending |
| Lumos Touch | [Touch pairing](lumos-touch/README.md) | Pairing-specific code, setup instructions, and test records pending |
| YAM — exact model to be confirmed | [YAM pairing](yam/README.md) | Model identification and pairing guide pending |
| Seeed reBot B601 | [B601 pairing](seeed-rebot/README.md) | Upstream LeRobot guide available for B601-DM and B601-RS; verify exact leader and variant |

These entries identify customer pairing needs. Listing a model does not establish tested support for both LD and HD, or for every software workflow. See the [capability and evidence matrix](compatibility.md) before choosing hardware or installing software.

<a id="page-section-2"></a>

## Choose a workflow

- **Python:** direct teleoperation requires a driver and mapping for the specific follower. The current [Python SDK examples](../python-sdk/README.md) target Star Arm 102-FL.
- **LeRobot:** use the pairing's documented follower plugin and leader interface. The [LeRobot directory](../lerobot/README.md) holds the existing Star Arm integrations; they are not universal follower drivers.
- **Wiki and tools:** [Control tools](../tools/README.md) link to the Wiki. Pairing-specific courses will be linked from each model guide when available.

Start with [common preparation](common-setup.md), then your model guide. For an all-Star Arm setup, use [getting started](../docs/getting-started.md).

<a id="page-section-3"></a>

## Partner applications

| Application | Purpose | Guide and validation status |
| --- | --- | --- |
| Butterfly Community Robot Arm | Natural-language task control and partner-maintained robot application | [Overview](butterfly/README.md) · [Compatibility](butterfly/compatibility.md) · [Setup](butterfly/setup.md) · [Troubleshooting](butterfly/troubleshooting.md) |

Partner applications are a separate category from leader–follower pairings. Check each application's model and environment requirements before use. See the [Chinese Butterfly guide](butterfly/README.zh-CN.md) for the complete Chinese version.

<a id="page-section-4"></a>

## How these resources are maintained

This directory owns pairing requirements, capability status, and navigation. Python implementations remain in `python-sdk/`, and LeRobot plugins remain in `lerobot/` or their linked upstream repositories. Each command sequence should have one authoritative location. Detailed tutorials and videos belong in the Wiki; tool binaries and vendor SDK copies are not mirrored here.

[Home](../README.md) · [Leader hardware](../hardware/README.md) · [Software environments](../docs/compatibility.md)
