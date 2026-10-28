# Provenance and maintenance

## Maintained source

[Loveacup/skill-authoring](https://github.com/Loveacup/skill-authoring) is the standalone maintained source. Its root `SKILL.md` is the skill entrypoint; `references/` is the complete portable reference family.

## Origin and attribution

This package was extracted on 2026-10-28 from the reviewed v6.3.0 working-tree candidate in `shared/skill-authoring` of [Loveacup/jz-skills](https://github.com/Loveacup/jz-skills). The source checkout HEAD was `499f4f9462515b2e731e236cb294fe1a8fc4454c`; that commit is a repository baseline, **not the commit containing the uncommitted v6.3.0 candidate**. The standalone initial commit captures the selected candidate plus the portability and documentation changes described here.

The original skill identifies its author as **Hermes Agent**; that metadata is retained. The source family was maintained by **Loveacup (Alex Cai)** and contributors. Earlier public content remains available in [the collection history](https://github.com/Loveacup/jz-skills/tree/862dc7a1d96f12a539ba530a7ed3b97ad9978ed1/shared/skill-authoring). This repository starts a new Git history rather than importing unrelated collection commits or private state.

The source skill declares `license: MIT`, and the collection README states MIT. No root LICENSE file was present in the inspected source checkout, and the original repository's license API returned 404 during extraction. The owner explicitly selected MIT for this standalone repository; [LICENSE](LICENSE) supplies its complete terms. This notice does not relicense external works cited by the skill.

## What crossed the boundary

All 13 candidate Markdown files were explicitly selected: the root and twelve references. Authoring, evaluation, evolution, collection governance, agent-instruction guidance, import, release, privacy and core requirements remain available.

- Added this repository's source URL to skill metadata, retaining its author and version.
- Rewrote the optional local SkillHub adapter as a portable discovery contract. No personal directories, installation-specific registries, note-vault mappings or private operational policy are required.
- Clarified historical source links and removed local branch/deployment identifiers and private-backup descriptions from public history notes.
- Added complete English/Chinese READMEs and AI setup guides, an original conceptual SVG, the MIT license and a small offline link/version checker.

No runtime tree, private audit, raw conversation, credentials, deployment logs, local source registry or original `.git` history is included. Packaging does not itself update installed consumers, retire the old entry or archive the original collection. Research citations are design inputs, not bundled code or dependencies; their original licenses remain with their owners.

## Maintenance

Keep portable guidance here. Keep installation bindings and private experience in their authorized local owners. Behavioral changes preserve the [core requirements](references/core-requirements.md) and use the existing [changelog](references/changelog.md); ordinary small skills need not adopt this repository's record layout.
