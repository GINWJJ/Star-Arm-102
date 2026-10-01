# Validation record and hardware handoff

This page separates checks performed during the English-first update from checks that require a robot, cameras, GPU, or ROS host.

## Software and document checks

- Seven Python entry tests pass on Python 3.12, covering ping-only communication, missing devices, serial failures, resource closure, CLI validation, backwards-compatible option spelling, and help without hardware access.
- The local Markdown checker passes for all 38 Markdown files, including Chinese supplementary material. It does not verify remote services or heading fragments; customer-path heading links were reviewed separately.
- All repository Python files parse successfully without executing hardware control. The 38 shell snippets in the main English customer guides pass `bash -n`; this checks syntax, not hardware behavior. Git diff whitespace and the new workflow/issue-form YAML were also checked.
- Dependency resolution succeeds for Linux x86-64 / Python 3.10 with LeRobot 0.4.1, both StarArm plugins 0.0.1, torch/torchaudio 2.7.1, and torchvision 0.22.1. The resolver selected motor plugin 0.0.7. This was a metadata resolution check against PyPI, not installation of the CUDA 12.8 wheels or execution on Ubuntu.
- In separate macOS / Python 3.12 environments, dependency checks pass for both plugin generations. The release-compatible 0.0.1 plugins register successfully, and `lerobot-record --help` exposes their device types with motor plugin 0.0.6 and 0.0.7.
- The refactored package installs with LeRobot 0.4.1 and motor plugin 0.0.6; `lerobot-teleoperate --help` exposes `stararm102_hd` and `stararm102_fl` after a regular install. A default editable install did not expose them, so the guides now use regular installation. CLI checks used a dummy keyboard backend and opened no robot ports.
- The published ACT archive was downloaded and its SHA-256 matched `SHA256SUMS.txt`: `9d1b5272174ea2595badfa7362ae67bea5c8e1ec30137b1d46dcd21d30f27931` (191,108,326 bytes).
- Its configuration confirms seven state/action dimensions, `up` and `front` images at 3 × 480 × 640, CUDA as the saved device, and a 100,000-step training configuration. Download integrity and metadata checks do not establish inference performance.

Re-run the automated checks using [CONTRIBUTING.md](../CONTRIBUTING.md#check-a-change). Hardware validation was not performed during this documentation update.

## Before declaring a customer setup validated

Record the arm models/revisions, firmware if identifiable, OS, repository commit, package versions, camera models, and GPU/driver. Complete only the applicable path:

| Path | Acceptance check | Current status |
| --- | --- | --- |
| Wiring and reference pose | Confirm power/connector labels and provide revision-specific LD/HD/FL zero-pose photographs | Needs hardware owner confirmation |
| Python LD → FL | IDs 0–6 respond; small motions and gripper track correctly; stop behavior understood | Bench test required |
| Python HD → FL | Above, plus ID 7 and actual lock/unlock behavior | Bench test required |
| Release-compatible LeRobot | Calibration saved/reused and seven-channel motion checked | Bench test required |
| Refactored HD/FL | Calibration, directions, ranges, and button behavior | CLI discovery passed; bench test required |
| ACT | Clean Ubuntu/GPU installation; both camera views; one supervised task; saved local episode; repeat-trial results | Customer environment and bench test required |
| ROS 2 Humble | Clean build; RViz virtual plan; real driver initialization; small executed trajectory | ROS host and bench test required |
| reBot | Exact upstream version and supported leader/button combination | Upstream integration test required |

For ACT, count attempts and successes with a stated scene and criterion before publishing a success rate. For the direct Python path, a verified reference-pose illustration is still needed; do not invent one from a different arm's photo.

## Maintainer decisions still needed

Confirm the intended license for original code, documents, hardware designs, media, and model weights. Existing component licenses remain in place; [LICENSE.md](../LICENSE.md) records the current gaps.

The detailed bilingual Wiki course, model/dataset publishing strategy, and a tested end-to-end training curriculum remain the second phase.
