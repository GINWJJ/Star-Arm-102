# Repository documentation rules

- English is the default customer entry. If a README has a Chinese counterpart, keep both complete and synchronized in the same change, including section order, images, tables, links, commands, compatibility, and validation status.
- Read both versions before changing either. Check translation meaning manually; structural checks are not proof of semantic equivalence.
- Use README.md and README.zh.md for new pairs. Preserve the existing Butterfly README.zh-CN.md filename for link compatibility. Do not create README_zh.md aliases.
- Historical guides must be labeled as archives and linked from both current versions. Do not substitute an old guide for a current translation.
- Run `python scripts/check_docs.py` and `python scripts/check_readme_sync.py` after documentation changes.
- Use lowercase and hyphens for resource directory names; preserve language and framework identifiers.
- Browser operations default to the Codex in-app browser. Use Chrome only when explicitly requested by the user.
