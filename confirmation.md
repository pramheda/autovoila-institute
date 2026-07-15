# Frozen Confirmation

## 1. Purpose

Exploration is allowed to adapt.

Confirmation is intended to test a specific claim without quietly changing the test after observing the result.

A confirmation process is not a more polished exploratory run.

It is a different epistemic mode.

## 2. Entry criteria

A claim may enter confirmation when:

- it is precise;
- it is scientifically important enough to justify the cost;
- the proposed measurement is credible;
- major confounds have been investigated;
- the exploratory evidence is sufficient to motivate a clean test;
- and the institute can state in advance what outcomes would support, weaken, or refute the claim.

Human approval is required for high-stakes confirmation.

## 3. Freeze package

Before execution, preserve:

- exact claim;
- scope;
- hypotheses;
- primary outcomes;
- secondary outcomes;
- dataset-generation rule;
- inclusion and exclusion rules;
- model and training setup;
- evaluation prompts or code;
- statistical analysis;
- stopping rule;
- interpretation boundaries;
- and allowed technical recovery procedures.

Hash or otherwise version the package.

## 4. Freshness and separation

Use one or more of:

- fresh data;
- held-out evaluations;
- independently generated examples;
- a clean-room implementation;
- a separate model family;
- or an independent execution agent.

Do not expose hidden labels or desired outcomes to execution agents unless operationally necessary.

## 5. Allowed changes

Allowed changes are limited to technical recovery that does not depend on the observed scientific outcome.

Examples:

- retrying an interrupted job;
- replacing failed hardware;
- correcting a clearly pre-existing code bug;
- or restoring a corrupted artifact.

Record all changes.

## 6. Prohibited changes

Do not:

- replace the primary outcome because the result is null;
- add examples that favour the claim after seeing results;
- continue running seeds until significance appears;
- remove inconvenient data without predeclared criteria;
- change the interpretation boundary;
- or silently reclassify the run as exploratory.

If a necessary change compromises confirmation, mark the run invalid or exploratory and begin a new frozen confirmation.

## 7. Deviations

Maintain `deviations.md`.

For every deviation, record:

- what happened;
- when it was discovered;
- whether outcomes had been inspected;
- expected effect;
- decision;
- and who approved it.

## 8. Output

A confirmation report should state:

- the original frozen claim;
- protocol;
- deviations;
- primary result;
- uncertainty;
- capability controls;
- negative and contradictory evidence;
- what is now licensed to claim;
- and what remains exploratory.

A null result is a complete output.

## 9. Relationship to the research world

Confirmation produces evidence that updates the broader programme.

It does not erase exploratory branches.

A failed confirmation should cause the institute to reconsider:

- mechanism;
- scope;
- measurement;
- effect size;
- and real-world relevance.

---
