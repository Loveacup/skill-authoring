# Local SkillHub Adapter

Read this reference only when a task changes placement, provenance, runtime exposure, generated entrypoints or governance records in a locally managed skill collection. "SkillHub" here describes an optional local arrangement, not a bundled product or a required dependency. Ordinary portable skill editing needs no hub, registry or note-taking application.

This adapter explains how to discover local authority. It does not replace [import](import.md), [release](release.md), or the live rules at the target.

## Start from the target

Locate the user-designated collection entrypoint and the nearest instructions governing the named target. Discover actual paths and formats from those sources; do not assume another installation's directory layout. Add only the record needed for the current decision:

| Decision | Read |
|---|---|
| Edit a maintained skill without changing ownership or exposure | Its source record, maintained source and source/target instructions, if present. |
| Choose canonical placement or promote from intake | The relevant placement policy and target rules; resolve origin before choosing authority. |
| Reconcile source, canonical and runtime drift | The affected copies and provenance; consumer records only when exposure is implicated. |
| Review an upstream update | The actual upstream revision or lock entry and evidence of local customization. |
| Change runtime exposure | The named consumer's configured loader path and placement policy. |
| Change generated entrypoints | The configured source, generator and supported check mode. |
| Write governance documentation | The explicitly mapped destination and its owner rules. |

If an installation has no such record, do not fabricate one or create a governance system just to edit a skill. Resolve the necessary ownership with the user. Missing authority blocks the dependent write, not unrelated read-only work. A local exception applies only to its named target; it grants no general lifecycle management, reverse synchronization or runtime-control authority.

## Respect directory meaning

Distinguish maintained source, intake, canonical content, runtime exposure, evidence and cold history where those roles exist. Directory names alone do not establish their meaning. Do not point a consumer at a collection root, archive or evidence directory merely because it contains a `SKILL.md`. A source checkout can be a load target only when the host supports it and the user has authorized that arrangement.

## Change authority records only within scope

A skill edit, import or runtime observation does not imply permission to mutate ownership, lock or consumer records. Follow the actual installation's approval rules. When the active request already authorizes the exact record and target, continue without redundant approval; otherwise prepare the proposed delta and stop before writing it.

After authorization, change only entries whose represented state actually changed. Record observed revisions, placement, exposure and blocked facts. A ledger row does not prove filesystem state; a lock entry does not prove compatibility; a registry entry does not prove consumer behavior. Leave unrelated taxonomy, credentials, audits and configuration untouched.

## Generated entrypoint stubs

Determine whether an entrypoint is generated before editing it. Change its declared source through the designated generator only when authorized, then use the existing check mode if available. Generator output is not authority to repoint a discovered consumer. Do not copy generated local stubs into portable source or treat them as independently maintained policy.

## Optional documentation writeback

Use only a destination explicitly mapped by the installation or the user, whether it is a Markdown project record, a note-taking application or another supported store. Update the record only when the authorized work changed the state it owns. Keep execution evidence, architecture changes and classification changes with their respective owners.

Do not guess a vault path, recursively read private notes or duplicate raw logs into distributable documentation. No relevant state change means no writeback. This skill ships no writeback service or integration.

## Apply the shared workflows

Use [import](import.md) for reconciliation, preserving legitimate host-only, private, generated and richer local safety content. Use [release](release.md) for authorized application, exposure, publication, repointing or retirement. These remain distinct actions.

Verify the named consumer's actual loader after an authorized deployment. Hashes, links and records prove only the property inspected. Do not invoke schedules, watchdogs, profile management or baseline changes unless the named target and request require them.

## Result

Report the authority inspected, exact records changed or deliberately unchanged, placement, exposure, consumer observation when applicable, documentation destination when used and claims blocked by missing evidence. A prepared proposal is not an applied hub state.
