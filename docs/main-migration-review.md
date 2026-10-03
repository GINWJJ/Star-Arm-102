# Main migration review — October 3, 2026

## Decision and scope

The phase-one branch can replace the current main entry by a fast-forward update. This is a repository coverage and software/documentation review, not a completed hardware qualification. The previous main commit remains in Git history.

## Coverage

The previous main contained 201 tracked files. Before the final repairs, 174 had byte-identical content retained somewhere in the phase-one branch, including renamed resources. The review restored two omitted `.gitignore` files, bringing that count to 176. The remaining 25 files are documentation, the root ignore rules, the direct Python entry, and ROS description packaging/paths reviewed for their purpose rather than byte identity.

- Original hardware CAD, drawings, BOM, media, simulation meshes, plugin implementations, and other source assets remain available under their new paths.
- Current documentation replaces conflicting older commands. Longer Chinese instructions remain in labeled historical guides, while eight current bilingual README pairs have matching structure and resources.
- Original store, website, video, and resource URLs remain represented. The obsolete uppercase LeRobot link now uses the current local path; the unsupported repository-wide MIT badge was removed in favor of component license scope.
- Direct Python control retains its leader/follower behavior and legacy leader flag, with explicit port selection and argument validation added.
- The URDF retains its original joint definitions, limits, transforms, and dynamics. Mesh filenames and installation paths changed; ROS launch defaults follow the new URDF filename.
- Restored the refactored LeRobot guide's own-checkpoint evaluation path with matching recording/training camera names and output paths. It remains an unvalidated hardware example.

## Validation

- 103 Markdown documents: local file/image links pass.
- Eight bilingual README pairs: section, table, image, command, and link-target checks pass. Translation meaning was manually reviewed.
- Seven mocked Python entry tests pass; no hardware connected.
- Python source parsing and refactored LeRobot shell syntax pass.
- URDF semantic comparison against previous main passes after normalizing mesh filenames.
- ROS description resource installation and all installed mesh references pass. This is not a full ROS/colcon/runtime test.
- 32 imported handoff files were hash-checked against their sources before the phase-one publication; exported CAD files preserve their original bytes.

## Remaining work

See [hardware status](../hardware/README.md#resource-status), [handoff review](../hardware/handoff-review.md), [cross-brand capabilities](../integrations/compatibility.md), and [runtime validation](validation.md).

Outstanding items include standalone printing STL, approved model-specific URDFs, complete assembly instructions/video, production-version reconciliation, BOM/print-setting conflicts, cross-brand setup packages and physical validation, and partner application end-to-end validation. Their status must remain visible until evidence is supplied.

## Migration effects

Top-level resource paths use lowercase and hyphens. Old external links to uppercase paths and removed duplicate README aliases may break on GitHub; update external documentation to the current URLs. Historical commits retain their original paths. Python import/package identifiers remain unchanged. The repository's workflow runs on main pushes and pull requests; workflow completion is separate from pushing the branch.
