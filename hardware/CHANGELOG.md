# Hardware resource changes

## Unreleased

- Split customer resources into `102-ld/`, `102-hd/` and `102-fl/`. HD shares the main body but includes dedicated button parts and different BOM selections.
- Import traceable handoff STEP/drawing references and unmodified BOM/3MF source documents. Preserve prior LD files rather than overwriting unconfirmed revisions.
- Add availability and review status at the project root, hardware root and model indexes.
- Add model-specific `robot-description/urdf/` and `robot-description/meshes/` entries with explicit pending status. Keep the existing runtime model unchanged in the shared description directory.
- Record original filenames, checksums, unresolved conflicts and exclusions in the handoff review and manifests.
- Use lowercase, hyphen-separated resource names and `assembly-guide/` for tutorials. Keep conventional README and CHANGELOG names.

This is resource organization and source review, not a hardware release, certification or physical validation. No new hardware license is granted.
