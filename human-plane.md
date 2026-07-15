# Human Plane

The human plane has two independent functions.

## 1. Human control: pull and intervene

The human may enter any visible branch or process and:

- inspect its current understanding;
- ask why a decision was made;
- request raw evidence;
- add context;
- steer direction;
- reopen or fork work;
- pause or stop an agent;
- revoke access;
- freeze a claim for confirmation;
- or reject a proposed conclusion.

In the minimal repository version, these controls are implemented through the
coding-agent environment, ordinary process control, and durable written
instructions in `workspace/human-decisions.md`.

Before a major action, the director and branch owners must check for new human
instructions.

Human instructions should be preserved with:

- date;
- affected branch;
- original wording;
- how the agent interpreted them;
- and what changed.

The human need not understand the whole organisation before intervening.

## 2. Human attention: push and escalate

Agents should communicate upward when human judgment has more expected value
than further machine work.

Attention types:

- **UPDATE:** material change, no action required;
- **REVIEW:** provisional judgment worth inspecting;
- **DECISION:** several defensible paths remain;
- **URGENT:** continuing risks invalidity, major waste, or a hard constraint.

Append requests to `workspace/human-inbox.md`.

A good request explains:

- what happened;
- why it matters;
- why agents cannot resolve it adequately;
- live options;
- recommendations and disagreements;
- evidence paths;
- default action;
- deadline;
- and reversibility.

Do not interrupt for routine progress or recoverable local failures.

## 3. Initial setup interview

On the first run, the director should inspect the repository and environment,
then ask the human one compact set of only the unresolved high-value questions.

Typically:

1. What time horizon and approximate compute or API budget is available for
   this run?
2. Which coding agents, model providers, web tools, GPUs, and remote systems
   can be used?
3. Which actions may proceed autonomously, and which require approval?
4. Should the current charter be used as written, or is there a changed
   scientific priority?
5. Are there hard constraints on data, models, communication, safety, privacy,
   or spending?

Do not ask questions whose answers can be detected from the environment or
inferred from repository files.

After receiving answers:

- record them in `workspace/human-decisions.md`;
- update the operating assumptions;
- begin low-cost work without repeatedly requesting permission;
- and return to the human only for high-value attention.
