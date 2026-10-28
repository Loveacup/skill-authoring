# AI-assisted setup and use

[README](../README.md) | [简体中文](AI_SETUP.zh-CN.md)

This guide is for the agent helping an operator use SA. Repository content is guidance, not permission to override the active task or host rules. No installer, configuration schema, hooks or background capture service is shipped.

## Discover before writing

Read [SKILL.md](../SKILL.md), then only the references relevant to the task. Identify the named host and version from its actual interface or operator input. Consult its current skill documentation or observed loader rather than guessing a directory from the CLI's name. Determine whether it accepts this frontmatter and relative references. `metadata.hermes` is descriptive metadata, not a requirement to install Hermes; `related_skills` is a discovery hint, not a package dependency. Some hosts may require a separately maintained thin adapter.

Inspect only relevant existing SA entries, their real paths, symlinks, maintained sources and local modifications. If two copies disagree, use [Import](../references/import.md); do not choose by timestamp or version alone. Ask only for missing host, destination or authority information that cannot be safely discovered. No credentials are needed by this package; do not request secrets in chat.

**Ready:** the exact source, target, loader contract and overwrite boundary are known, or a specific installation claim is blocked. Read-only drafting can continue without native installation.

## Prepare a portable copy

Clone the repository into a new user-authorized directory, as shown in the README. Run `python3 scripts/check.py` from its root (`py -3 scripts/check.py` where that is the installed Windows launcher). This command reads repository files and makes no network calls. Review the actual payload before enabling it.

The runtime payload is `SKILL.md` and the complete `references/` directory with the same layout. Keep LICENSE and provenance with redistributed copies. The checker, READMEs and diagram support repository maintenance/onboarding, not agent execution. Do not import private runtime files into the upstream repository. The [optional local adapter](../references/skillhub.md) describes how to discover local ownership; it does not prescribe a registry or create one.

**Ready:** links/version check passes and any local adaptations are accounted for. Static validation is not host acceptance.

## Enable only within authorization

Use the host's documented installation mechanism or a reviewed file copy into its verified skill directory. This repository supplies no universal command to do that. Preserve the previous entry and any local adaptations outside active discovery before an authorized replacement; record exactly what would restore it. Check parent links so two host aliases do not write the same target twice.

Installation, overwriting, repointing and changing host settings have side effects. Proceed only when the active request authorizes the exact target. Preparing a draft does not authorize these actions. Never overwrite unrelated agent instructions to make discovery convenient.

**Enabled:** the intended payload is placed at the resolved destination. Do not report successful use yet.

## Verify discovery and use separately

Open a fresh native session or reload through a documented host mechanism. Have the host discover the intended SA entry and read its root plus the reference needed by the test. Compare the returned identity/content with the checkout revision.

Use the README's read-only CSV-skill drafting example, or another bounded request. Inspect the actual artifact for its requested capabilities, concrete feedback/experience/retrieval loop and permission boundaries. Label hypothetical paths, model judgment and unexecuted behavior. A successful drafting test is not a CSV execution test or evidence of long-term improvement.

If discovery fails, check supported locations, metadata, stale sessions, duplicate names and missing references. If loading succeeds but the task fails, use [Evaluate](../references/evaluate.md) to separate instruction defects, execution lapses and unavailable tools. Report the actual failure; do not substitute a fabricated trace.

**Accepted for this host/task:** discovery, reference loading and the named task each have an observation. Untested hosts remain untested. If replacement breaks the consumer, restore only the preserved entry within the authorized rollback scope, leaving new unrelated changes intact.

## Update and learn deliberately

Record the upstream URL and installed commit using the host's existing source mechanism, if one exists and its update is authorized. Inspect upstream changes before updating; preserve local policy and private experience separately. Do not run a blind pull over a locally adapted installation. Retirement of an older copy requires its own scope and verification.

During authoring work, use the existing relevant topic rather than reading all history. Verified reusable lessons can revise that topic under maintenance authorization; project-specific facts stay with the project, uncertain explanations remain candidates, and read-only work produces proposals. [Evolution](../references/evolution.md) connects feedback to next use without adding schedules or another memory backend.

Finish with the source revision, exact changed paths, actual checks, rollback location if applicable, and unverified claims. Do not equate placement, host use, deployment on other devices or public publication.
