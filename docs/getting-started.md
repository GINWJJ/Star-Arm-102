# Get Started with Star Arm 102

[← Home](../README.md)　|　<sub>**English** / [简体中文](getting-started.zh.md)</sub>

This guide starts with an assembled Star Arm 102. Connect your equipment, try the digital twin, then move on to real-arm teleoperation and your first AI task. You can start with a single arm.

> **Arm not assembled yet?** Start with the [DIY assembly guide](../hardware/diy-assembly/README.md), then return here to connect your equipment.

**Contents:**

- [🔌 1. Connect your arm](#connect)
- [🎮 2. Try the digital twin](#digital-twin)
- [🦾 3. Teleoperate real arms](#teleoperation)
- [🤖 4. Run your first AI task](#ai-task)
- [📚 Next steps and help](#next-steps)

<a id="connect"></a>

## 🔌 1. Connect your arm

Check your model label: **LD** is a hand-guided leader, **HD** is a pose-holding leader, and **FL** is a follower. Use the model label rather than appearance alone.

Fix the base and prepare the supplied power adapter, USB data cable and computer. Switch off power before changing servo or power connections. Each arm needs its own matching supply; USB carries data and does not replace servo power.

- **LD / HD + FL:** follow the [hardware wiring guide](hardware-setup.md). Connect each arm's UC-01 to the computer and identify the leader and follower ports separately.
- **LD / HD + another brand:** select your follower in the [cross-brand directory](../integrations/) and follow its connection requirements. Use that manufacturer's power and adapter instructions.
- **One arm:** connect only the device you have. A leader can be used with a virtual follower in step 2. For FL alone, begin with the [communication check](../python-sdk/README.md#check-communication-without-commanding-motion).

**Ready to continue:** the computer detects the connected device and you know which port belongs to it. Cameras are not needed for the initial communication check.

<a id="digital-twin"></a>

## 🎮 2. Try the digital twin

### Physical leader → virtual follower

Connect your LD / HD leader using the web tool's model-specific instructions. Move the leader and observe the virtual follower's response to become familiar with joint motion before connecting a real follower.

[![Web control interface preview](../media/web-control-preview.jpg)](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)

**[Open the web control guide →](https://fashionstar.com.hk/wiki/software/robot-arm/web-config-tool/)**

Follow the guide for supported devices, browser requirements and calibration. The image shows the interface without hardware connected.

### Web control → physical follower

**Instructions coming soon.** This entry will describe the supported follower models and connection procedure. For now, use the FL communication check in step 1; it does not command motion.

<a id="teleoperation"></a>

## 🦾 3. Teleoperate real arms

Have both a leader and a follower? Continue from virtual motion to physical following.

- **LD / HD + FL:** use the [Python direct teleoperation guide](../python-sdk/). HD users should also follow its button configuration instructions.
- **Cross-brand pairing:** follow the software and joint-mapping procedure for your model in the [pairing directory](../integrations/).

Check communication before commanding motion. For Star Arm 102, confirm all seven servo IDs respond. Follow the selected guide's reference-pose or calibration procedure, then make a small leader movement and check the follower's direction. The direct Python script resets multi-turn counts on connection; it does not perform LeRobot calibration. Do not copy calibration files between plugin generations.

**Ready to continue:** the follower responds in the expected direction and the stop procedure in your selected guide is understood.

<a id="ai-task"></a>

## 🤖 4. Run your first AI task

With 102-FL ready, set up the two cameras and the specified workspace, then run the supplied ACT block-placement policy. You do not need to train this policy yourself.

**[Run the pretrained ACT demo →](../lerobot/examples/act_pick/README.md)**

Follow the demo's environment and calibration instructions, and start with one trial.

<a id="next-steps"></a>

## 📚 Next steps and help

- **Record demonstrations and train:** [LeRobot](../lerobot/README.md); for HD button integration, see the [HD / FL setup](../lerobot/lerobot-stararm102/README.md).
- **Develop ROS 2 applications:** [ROS 2 Humble](../ros2-humble/).
- **Choose compatible software:** [Compatibility guide](compatibility.md). Install only the environment required by your chosen workflow; customer Python examples target Ubuntu 22.04.
- **Need help?** Start with [troubleshooting](troubleshooting.md). When [reporting an issue](https://github.com/servodevelop/Star-Arm-102/issues/new/choose), include your model, environment, command and full error message.
