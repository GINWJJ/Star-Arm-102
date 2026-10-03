# Hardware handoff review

Reviewed 2026-10-03. [Hardware status](README.md) · [中文核对报告](handoff-review.zh.md)

## What was imported

32 source files were copied without content changes: 21 STEP exports, four drawing files (two PDFs and two DWGs), four Excel workbooks, and three 3MF projects. Excel and 3MF files are explicitly marked **review required**, not approved customer releases. No existing workbook, drawing, mesh or URDF was overwritten. Shared body geometry was also copied into the independent HD directory as confirmed by the owner.

The source collection has 234 files excluding `.DS_Store`, about 569 MB. See [all-source inventory](handoff-inventory.json) and [copied-file mapping with SHA-256](handoff-imports.json). Source-relative Chinese filenames are retained in the manifests to trace the original files; public destination paths use lowercase and hyphens.

## Availability versus approval

The main printed-part names are covered by STEP files: LD 11, HD 13 (11 common body parts plus two button housing parts), FL 11. This is a file-coverage count against the named printed parts, not a claim that every component of the arm is open, printable, correctly toleranced or ready to manufacture. There is no HD-labelled whole-arm STEP in the handoff. Purchased servos and electronics are not counted.

Production release matching, BOM cleanup, printing trials and model-specific robot descriptions remain incomplete. The source files were not translated internally; English indexes identify their purpose and limitations.

## Findings requiring a decision

| Topic | Evidence | Treatment / required decision |
| --- | --- | --- |
| LD versus HD | HD BOM `Sheet1` rows 15–21 adds button cover/base and UK-01; cable and fastener quantities differ. HD 3MF also includes button parts and a handle rest. | Owner confirmed the common body with HD-specific accessories. Provide separate model folders and BOMs. |
| FL link1 print settings | FL BOM `Sheet1` row 6 specifies “层数5 密度50”. FL 3MF object 22 / part 21 has no wall/infill override; global settings are 2 wall loops and 15% sparse infill. LD/HD explicitly override link1 to 5 wall loops / 50%. | Do not silently adjust FL settings. Confirm whether 层数 means wall loops and which settings are intended. FL 3MF is a reference, not a validated print recommendation. |
| 3MF date labels | All three filenames say 20260807. Internal creation/modification dates are FL 2026-08-07, LD 2026-08-12 and HD 2026-08-25. | Preserve source label in filenames and record both dates. Request a hardware revision/release map. |
| HD BOM date | Filename says 9.10; workbook modified metadata says 2026-07-21. | Neither date alone establishes the actual BOM revision. Confirm with engineering. |
| Existing versus handoff LD BOM | Handoff adds AXK2035+2AS bearing and M2×10 screws, changes several screw specifications (e.g. M3×8 to M3×10 and M3×8 self-tapping to M3×12), and includes more packaging/spare details. | Keep both references. Do not replace old quantities in customer instructions until the intended revision is confirmed. |
| BOM images and internal fields | Several original workbooks store `#VALUE!` in image cells; the kit workbook also contains `_xlfn.DISPIMG`. Production/preparation sheets, packaging instructions and spare-set quantities are mixed with assembly items. | Preserve original Excel bytes for review. Confirm image rendering in the authoring application, separate build quantities from spares/packaging, and prepare an English customer BOM later. |
| LD kit versus assembled version | Kit workbook has different packing and spare quantities. | Keep as a separate workbook, not another name for the assembled BOM. |
| Flexible fingertips | Accessory BOM says TPU 90A, 60% infill; fingertip 3MF uses TPU profile with 80% infill and no object/part override. BOM labels both fingertip entries as left. | Accessory BOM/3MF not imported as an approved standard-arm package. Confirm left/right parts and settings. |
| Link3 variants | Separate 3 mm and 4 mm V2 STEP files plus a `link3_V2(test).3mf` exist. | Retain in source. Do not promote a test or thickness variant without model/revision approval. |
| Handle rest variants | Existing `star-arm-102-base-support.step` does not match curated `handle-rest.STEP` in STEP DATA. | Keep existing file, hold replacement. Confirm whether this is a different accessory or a revision. |
| Assembly exports and drawings | LD assembly STEP export is 2026-07-21; an older loose LD assembly is 2026-04-10. FL assembly is 2026-07-03. PDF title blocks are 2026/7/13; both carry KHZY-43. | Import explicit dated references, retaining old repository LD drawings. Confirm matched versions and drawing identifiers. No HD assembly/drawing has been invented. |
| URDF exports | LD ZIP uses `satr arm102_description-LD` (typo, spaces, uppercase/hyphen) and fixes joint5. Both ZIPs use ROS 1-style launch resources, lack the current gripper mimic setup and have meshes differing from the runtime model. Export logs report omitted CSV columns. | Do not replace the ROS 2 runtime model. Engineering must confirm axes, joint types/limits, gripper coupling, inertia and model identity; export warnings do not alone prove the URDF is unusable. |
| Standalone STL | No standalone manufacturing STL files were found; STL files inside URDF archives are simulation meshes. | Mark printing STL missing. Do not rebrand simulation meshes as printable parts or automatically generate geometry from an unapproved revision. |
| LD kit power adapter | Kit BOM `Sheet1` row 55 lists a domestic 12 V / 2 A supply, while the current repository setup lists LD 12 V / 3 A. | Confirm kit versus assembled-product requirements; do not silently change the setup power specification. |
| Camera/accessory BOM | Camera kit workbook includes procurement prices/notes and incomplete quantity data (tripod row). | Retain in source for cleanup; do not confuse internal purchasing notes with a customer BOM. |

## Duplicate and excluded files

- Drawing ZIP has four payload files matching the extracted drawing directory byte-for-byte. Follower STEP ZIP has 19 payload files matching its extracted directory after decoding ZIP filenames. These archives were not duplicated into customer folders.
- Eight existing part/reference STEP files match corresponding handoff STEP DATA after removing whitespace, although complete-file hashes differ. Existing exports were retained. This comparison is narrower than a general geometric-equivalence proof.
- Native `.SLDPRT` / `.SLDASM`, KeyShot `.bip`, `.smg`, tooling/jigs, temporary Excel lock files, logs, loose unnamed assemblies, old/test variants and unverified accessory packages were not bulk-copied. Original source files remain untouched.
- The 234-file inventory records each file's disposition. The mixed native-CAD directory was inventoried, not exhaustively opened as a SolidWorks assembly with all references resolved.

## Checks completed and limits

- All 21 imported STEP files read and transferred successfully in Open CASCADE; each produced a non-null shape passing BRep validity. [Detailed results](handoff-step-validation.json).
- All eight curated 3MF ZIP containers passed CRC checks. The three primary projects' global settings and object/part overrides were inspected. No slicing or physical print was performed.
- Six non-temporary Excel workbooks were inspected read-only for sheets, values, formulas and metadata. No spreadsheet recalculation, image repair or translation was performed.
- Both one-page handoff PDFs were rendered and visually checked for model identity, dimensions and title-block dates. DWG companions were preserved, not opened in a CAD application.
- Copied source bytes match their recorded SHA-256 checksums. No production-fit, interference, strength, robot motion, ROS runtime or electrical verification was performed.

Source-folder modification times are not treated as revision identifiers. Confirm a release matrix linking each model's BOM, assembly STEP, part exports, drawings and 3MF profile before describing the package as complete.
