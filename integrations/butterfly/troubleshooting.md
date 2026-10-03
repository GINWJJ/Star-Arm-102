# Butterfly integration troubleshooting

[Integration overview](README.md) · [Setup](setup.md) · [Compatibility](compatibility.md)

| Symptom | First checks |
| --- | --- |
| Application does not start | Confirm the reference revision, required assets, image build order, and service logs against the upstream deployment guide. |
| Browser page cannot connect | Check the actual host address and exposed ports. The upstream documentation's example IP is not a universal address. |
| Page controls work but natural-language tasks fail | Check model endpoint, credentials, image input, and tool-call support; inspect the provider/application error. |
| Camera is unavailable or localization is wrong | Check device passthrough, selected stream, aligned depth, calibration-board dimensions, and the current camera-to-robot transform. |
| Servo port is unavailable | Check USB access and port selection, and close other programs using the same port. |
| Displayed joints or motion do not match the arm | Stop issuing movement requests. Check exact hardware, servo models, zero conventions, and the partner's pinned model and patches before retrying. |
| Software reports completion but the object was not moved correctly | Inspect the camera result, target selection, calibration, grasp, and execution feedback separately. Software-only mode cannot validate physical grip. |

For application-specific details, use the matching [deployment guide](https://github.com/butterfly-community/robot-arm/blob/08498c31c56cf339601851851225bf111f89c82d/docs/DOCKER.md) and [device guide](https://github.com/butterfly-community/robot-arm/blob/08498c31c56cf339601851851225bf111f89c82d/docs/STARARM-102.md).

For support, provide the upstream commit, arm model/revision, installed servo models, camera, host environment, simulated/physical mode, and relevant logs without credentials. Application questions belong in the [partner issue tracker](https://github.com/butterfly-community/robot-arm/issues); Star Arm 102 product questions can use [our support entry](../../README.md#documentation-and-support).
