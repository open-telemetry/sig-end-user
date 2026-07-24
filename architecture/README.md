# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> Blueprints and Reference Implementations

This directory contains resources to help craft OpenTelemetry Blueprints and Reference Implementations.
For more information about what each of these are, or how to contribute, please visit https://opentelemetry.io/docs/guidance/.

## Contribution Process

This section describes the full journey for contributing a Blueprint or
Reference Implementation, from proposal to publication.

### Prerequisites

- Familiarity with the goals and scope of OpenTelemetry Blueprints and Reference Implementations
- A GitHub account and agreement to the Code of Conduct
- Reviewed existing blueprints and reference implementations proposals to avoid duplication

### Overview of the Workflow

1. Open a proposal issue in this (sig-end-user) repository, and state whether you intend to author it (do not open a docs PR yet)
2. Blueprints and Reference Implementation Team reviews the proposal
3. Proposal is approved, needs changes, or declined
4. Once approved, open a documentation PR against opentelemetry.io
5. Documentation review and merge
6. Blueprint or reference implementation is published

### Step 1 — Open a Proposal Issue

Propose a new blueprint or reference implementation by raising an issue in
this (sig-end-user) repository using one of the
following issue templates:

- [Blueprint proposal](https://github.com/open-telemetry/sig-end-user/issues/new?template=blueprint_proposal.yml)
- [Reference implementation proposal](https://github.com/open-telemetry/sig-end-user/issues/new?template=reference_implementation.yml)

Each template guides you through the details reviewers need — such as scope,
intended audience, challenges addressed, and target environment — and asks
whether you are willing to help author the document.

You do not need a finished document to open a proposal. If you already have
an early draft (for example, a Google Doc), you are welcome to link it so
the Blueprints and Reference Implementation Team can review the direction early.

> **Important:** Do not open a PR against opentelemetry.io at this stage.
> If no author volunteers, the issue is assigned the `needs-author` status
> label, signalling that the Blueprints and Reference Implementation Team is looking for someone to
> drive the discussion and work forward.

### Step 2 — Review & Approval

The Blueprints and Reference Implementation Team reviews the proposal. Status is tracked via labels (see the [Label Reference](#label-reference) below). The team may request changes, approve, or decline the proposal.

### Step 3 — Open the Documentation PR

Only after the proposal carries the `approved` status label.
Open the PR against the opentelemetry.io repository (see the note under
[Templates](#templates) for the correct destination) and reference the
original proposal issue in the pull request description using the following
format:

`open-telemetry/sig-end-user#<issue-number>`

### Step 4 — Documentation Review

Reviewers check technical accuracy, clarity, and adherence to templates.
Depending on the subject matter, respective SIG members may be invited to
review the content to ensure domain-specific accuracy.

### Step 5 — Published

Once the documentation PR is reviewed and merged, the blueprint or
reference implementation is published and available in the OpenTelemetry
documentation.

## Label Reference

The following labels are used to organize and track Blueprint and
Reference Implementation issues.

| Label                         | Purpose      | Description                                                                                      |
| ----------------------------- | ------------ | ----------------------------------------------------------------------------------------------- |
| `blueprints/ref-imps`         | Discussion   | General discussions related to both blueprints and reference implementations.                   |
| `blueprints`                  | Content type | Identifies an issue as relating to a blueprint.                                                 |
| `reference-implementations`   | Content type | Identifies an issue as relating to a reference implementation.                                  |
| `needs-author`                | Status       | The proposal is open but has no author yet.                                                     |
| `needs-review`                | Status       | Proposal is ready and waiting for the Blueprints and Reference Implementation Team to review.   |
| `in-review`                   | Status       | The Blueprints and Reference Implementation Team (and any invited SIG members) are actively reviewing. |
| `approved`                    | Status       | Proposal is approved. The contributor may now open a documentation PR against opentelemetry.io. |

## Templates

The templates contained here provide authors with a general structure, resulting in guidance that's easy to consume and replicable across different environments, for a consistent approach to architectural guidance.

See existing templates below:

- [Blueprint](./blueprint-template.md)
- [Reference Implementation](./reference-implementation-template.md)

**Please note**, blueprints and reference implementations resulting from the use of these templates must be contributed as pull requests to their respective subdirectories under the [guidance](https://github.com/open-telemetry/opentelemetry.io/tree/main/content/en/docs/guidance) directory in https://github.com/open-telemetry/opentelemetry.io