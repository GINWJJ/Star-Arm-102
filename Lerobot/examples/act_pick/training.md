# Train your own ACT task

[Try the supplied policy first](inference.md) · [Choose a LeRobot integration](../../README.md)

Phase one provides an English path to the released model and a starting point for collecting your own task. A complete step-by-step training course belongs to the later Wiki phase.

## What is available now

- The released 100,000-step ACT checkpoint and [scene photographs](README.md).
- [Calibration and teleoperation](../../README.md) for the release-compatible plugins.
- A [recording and starter training example](../../lerobot-stararm102/README.md#record-your-own-demonstrations) for the refactored HD/FL integration. Its dataset has different joint features and is not interchangeable with the released model.

The archive includes `train_config.json`: 100,000 steps, batch size 8, seed 1000, four data workers, ACT chunk size 100, and AdamW learning rate `1e-5`. It also contains the policy configuration and normalization processors. The dataset path in that file points to the original training machine; it is not a downloadable dataset URL.

The release does not include the training dataset, a complete software environment lock, or an evaluated success-rate report. The recorded configuration is useful reference material, but those missing pieces prevent a claim of exact reproducibility.

## Workflow for a new task

1. Select one plugin generation and save its package versions and calibration IDs.
2. Fix the cameras, workspace, objects, and task definition. Keep camera names and image settings consistent.
3. Verify small-motion teleoperation and record a short sample before collecting a full dataset.
4. Inspect images, joint values, task completion, and timestamps. Collect varied demonstrations within the task you intend to evaluate.
5. Train ACT against that dataset and save the training configuration, checkpoint, processor files, and environment together.
6. Evaluate supervised trials in the same setup. Record attempts, successes, failure types, and setup changes before making performance claims.

For the general workflow, see the [official LeRobot documentation](https://huggingface.co/docs/lerobot/). Match commands to the LeRobot version you installed.

## Later Wiki course

The next documentation phase should supply illustrated recording steps, dataset review, a complete tested training command, checkpoint selection, failure analysis, and repeatable evaluation. It should link back to the versioned code and model instructions in this repository.
