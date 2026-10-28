<div align="center">

# Skill Authoring

**Build skills that exercise judgment, preserve capabilities, and learn from real work.**

English | [简体中文](README.zh-CN.md)

[Quick start](#quick-start) · [Use with an AI](#use-with-an-ai) · [How it works](#how-it-works) · [Guides](#guides)

![Conceptual learning loop: use a skill, observe meaningful feedback, retain scoped experience, retrieve it at the next decision, revise and verify. The executing agent performs the loop; no background service is installed.](assets/learning-loop.svg)

[Open the diagram at full size](assets/learning-loop.svg) for small labels on mobile.

**v6.3.0 · Markdown skill · MIT**

</div>

Skill Authoring (SA) is a reusable instruction package for agents that create, revise, evaluate or import skills, review a named skill collection, or improve instruction files such as `AGENTS.md`. It helps you decide what guidance is worth keeping and test whether a change serves the task.

It is **not an agent runtime, a CLI installer, a memory service or an autonomous optimization daemon**. Your agent reads the Markdown and performs the work using its existing tools and permissions. The diagram is a conceptual method, not a runtime screenshot or an automatic execution pipeline.

<a id="quick-start"></a>
## Quick start

### 1. Get a local copy

You need Git to clone, an agent that can read local Markdown for use, and Python 3.9+ only for the optional offline documentation check. No API key, package install or background process is required by SA itself. The commands below use `python3`; on Windows use your installed Python launcher, such as `py -3`.

Run in a parent directory where a new `skill-authoring` directory may be created; that directory must not already exist:

```sh
git clone https://github.com/Loveacup/skill-authoring.git
cd skill-authoring
python3 scripts/check.py
```

The check prints `PASS` with the version and local-link count, or exits nonzero with diagnostics. It checks the shipped Markdown links/anchors, version agreement and SVG structure. It makes no network calls and does not install the skill or prove agent behavior.

### 2. Try it without changing your agent configuration

Open an agent session with this checkout accessible and send:

```text
Read SKILL.md in this skill-authoring checkout. Then read the references relevant
to authoring and evaluation. Help me design a reusable skill for reviewing CSV
exports. Work in this conversation only: draft the skill, preserve both a quick
check and detailed-validation mode, and define a concrete feedback source,
authorized experience destination and next-use retrieval cue. Do not create,
install, publish or deploy files. Label hypothetical paths and untested behavior.
```

A useful first result is an inspectable skill draft with a precise trigger, both requested modes, a scoped learning loop and honest verification limits. This is a **drafting exercise**, not an executed CSV validator. If the agent cannot access local files, supply `SKILL.md` and the relevant referenced text explicitly; do not assume it fetched links.

### 3. Install only if you want native discovery

SA ships no installer and claims no universal skill directory. Ask your agent to discover its host's documented skill-loading mechanism, check for an existing `skill-authoring`, and propose the exact destination before any write. Install the **whole skill payload: `SKILL.md` plus `references/`**, preserving their relative layout. README files, the license, provenance and assets may be kept with the checkout; the checker is a repository maintenance tool, not a runtime dependency.

Preserve local adaptations and back up an existing entry before an authorized replacement. Open a fresh session, verify that the host discovers the intended entry and reads a relevant reference, then try a bounded task. A file copy or matching hash proves placement, not successful use. See the [AI setup guide](docs/AI_SETUP.md) for discovery, installation, updates and rollback.

<a id="use-with-an-ai"></a>
## Use with an AI

For an agent helping with installation, copy this request and name the host and authorized workspace:

```text
Read README.md and docs/AI_SETUP.md from Loveacup/skill-authoring. Inspect this
checkout and my named agent host's real loading mechanism. Find existing SA
entries and their maintained sources before proposing a destination. Prepare
within the workspace I authorize; preserve unrelated settings and local
adaptations. Do not invent an installer or a config file. Ask before installation
or repointing unless I have explicitly authorized that exact target. After an
authorized install, verify discovery, reference loading and a bounded task,
and distinguish placement from actual use. Do not publish private experience.
```

Once the skill is accessible, ask in ordinary language; a particular slash-command syntax is not required:

| Your goal | Example request |
|---|---|
| Create a reusable skill | "Use SA to draft a research skill that supports a short answer and a full cited report." |
| Repair an existing skill | "Inspect this skill and the failed output. Fix the implicated guidance without removing its other modes." |
| Add learning during use | "Connect verified corrections to this skill's existing topical notes and next-use retrieval, within its maintenance permissions." |
| Review a collection | "Audit only these five descriptions for task collisions; recommend changes without writing files." |
| Improve agent instructions | "Review this AGENTS.md for conflicting requirements and unnecessary always-on steps. Preserve its required tests." |
| Reconcile copies | "Compare the maintained and installed copies. Separate portable changes from private host adaptations before proposing a merge." |

For a read-only task, findings and candidate revisions stay in the authorized report. Mentioning learning is not permission to change files, collect additional data or deploy anything.

<a id="how-it-works"></a>
## How it works

**Judgment, not a universal itinerary.** A small entrypoint routes to specialist knowledge only when the task needs it. Exact interfaces and real safety boundaries stay concrete; ordinary reasoning and tool choices stay with the agent.

**Preservation before simplification.** Establish what an existing skill must keep delivering, then improve its guidance without silently deleting deeper modes or useful safeguards. Verification targets consequential uncertainty, not a fixed quota of tests or pages.

**Learning in both directions.** SA equips target skills to learn during their own use and uses authoring feedback and subsequent target results to improve its own methods. Meaningful signals become scoped experience; a retrieval cue brings that experience into the next relevant decision; bounded revisions are checked against actual outcomes. Candidates are not adopted just because a model assigns them high confidence. Lessons can be corrected, consolidated or withdrawn.

**Separate action boundaries.** Preparation, canonical application, runtime deployment, publication and retirement are distinct states. None automatically authorizes or proves another. Markdown guidance is not an executor sandbox.

<a id="guides"></a>
## Find the right guide

The skill and its detailed references are in English; both onboarding guides and READMEs are complete language counterparts.

| Need | Read |
|---|---|
| Agent-assisted setup and updates | [AI setup](docs/AI_SETUP.md) / [中文](docs/AI_SETUP.zh-CN.md) |
| Discover the entrypoint | [SKILL.md](SKILL.md) |
| Design or substantially revise a skill | [Author](references/author.md) |
| Build or operate the learning loop | [Experience-driven evolution](references/evolution.md) |
| Diagnose failures or compare behavior | [Evaluate](references/evaluate.md) |
| Review a named library or instruction file | [Collection governance](references/collection-governance.md) / [Agent instructions](references/agent-instructions.md) |
| Reconcile copies and ownership | [Import](references/import.md) / [Optional local adapter](references/skillhub.md) |
| Publish, deploy or retire an artifact | [Release](references/release.md) / [Privacy](references/privacy.md) |
| Understand maintained contracts and history | [Core requirements](references/core-requirements.md) / [Changelog](references/changelog.md) / [Research notes](references/research-notes.md) |

## Verification and limits

Run `python3 scripts/check.py` from a clean checkout. The checker supports the inline links, HTML links/images and GitHub-style heading anchors used here; it intentionally rejects reference-style link definitions so an unsupported syntax cannot silently bypass checks. It is not a complete Markdown renderer, external-link monitor or secret scanner.

The v6.3.0 candidate received a fresh-context document review and a bounded fictional-skill drafting trial, described in the [changelog](references/changelog.md). Those observations do not prove all-host compatibility, unattended capture, cross-model gains or long-term learning benefit. Native discovery and real task acceptance must be checked on the host where you install it. Cited research is design context, not an installed dependency or a performance guarantee.

## Contribute

Use [issues](https://github.com/Loveacup/skill-authoring/issues) for reproducible defects or proposals. Read the [core requirements](references/core-requirements.md) before behavioral changes, make the smallest complete revision, update the existing changelog as appropriate, and run the offline checker. Keep the two READMEs and setup guides aligned. For behavior claims, include the actual bounded task and result, not only a self-score. Sanitize examples and keep private transcripts, credentials, host bindings and audit logs out of commits.

## Source and license

Maintained at [Loveacup/skill-authoring](https://github.com/Loveacup/skill-authoring), extracted from the `shared/skill-authoring` family in [Loveacup/jz-skills](https://github.com/Loveacup/jz-skills). The original `author: Hermes Agent` metadata and historical source attribution are retained. See [PROVENANCE.md](PROVENANCE.md) for the extraction boundary and earlier history.

[MIT License](LICENSE). External works cited in the references retain their own terms; citations do not incorporate their implementations into this package.
