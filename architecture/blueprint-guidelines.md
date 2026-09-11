# Blueprint Authoring Guidelines

This document contains the authoring guidance for [`blueprint-template.md`](./blueprint-template.md). Read it before
you start filling in the template.

## Overview

A blueprint SHOULD be structured in a way that conveys a journey, from a current state to a desired state. The OTel
Blueprint template is heavily influenced by the approach to strategic thinking popularized by Richard Rumelt in
_Good Strategy/Bad Strategy_. Some optional reading if you want the background before writing a blueprint:

- [Summary](https://itsadeliverything.com/good-strategy-bad-strategy-the-difference-and-why-it-matters-by-richard-rumelt)
- [Interview](https://www.youtube.com/watch?v=4uWKEG0s9Kc)

Some modifications must be applied to that framework, as OTel Blueprints are not scoped to solve a specific set of
challenges for a single organization, but rather a common set of challenges as identified in end-user reference
implementations, feedback surveys, and OpenTelemetry Live sessions.

Effectively, an OTel Blueprint is structured in four core areas:

- **Summary**: Introduces the target audience and environment, and the benefits from applying said blueprint. This
  MUST be placed at the start of the document.
- **Common Challenges**: The challenges to solve that, once solved, will generate the largest value for a particular
  organization.
- **General Guidelines**: The pattern that, if implemented, would solve the Common Challenges identified in the
  previous block. Guidelines MUST NOT be included if they don't apply to at least one of the documented challenges.
- **Implementation**: The list of actions to implement the General Guidelines, highlighting a plan that takes into
  consideration interdependencies between these actions (i.e. coherently).

Additionally, OTel Blueprints SHOULD optionally include these other sections:

- **Background**: A brief introduction to the environment and the audience.
- **Reference Implementations**: Links to reference implementations that implemented some, or all of the General
  Guidelines. It is strongly encouraged to back blueprints with reference implementations that implement them. This
  MUST be placed after the Implementation section.
- **Appendix**: Any information that would make other sections too verbose. Include here sections like code
  snippets, step-by-step operating guides, common issues and troubleshooting guidelines, etc. This MUST be placed at
  the end of the document.

The template uses an example, "Centralized Observability Platform on Kubernetes", to illustrate some of the defined
blocks. The following conventions guide the author:

- Text in `{curly brackets}` denotes details that MUST be filled in by the author, with examples inside the curly
  brackets.
- These guidelines exist so that authors don't need markdown comments embedded in the template itself to know what's
  expected of each section.

Authors MAY add more sections or reword any text within each of the sections, but MUST NOT remove any of the
mandatory sections listed above.

## Summary

A brief, high-level overview of the intended audience, the applicable environment, and the outcomes achieved. It
should answer the following questions:

- Who is the intended audience for this blueprint? Identify the type of team or engineering role that will read this
  blueprint and apply it.
- What type of environment does this blueprint apply to? Identify the stack where these recommendations will be
  applied.
- What is the core goal and the outcomes that this blueprint will drive when applied? As one-liners, identify the
  value that organizations get from applying this blueprint.

## Background

OPTIONAL. A brief introduction to the environment in scope, or the intended audience. This section is optional,
however authors SHOULD consider adding it in order to keep the summary to a few paragraphs.

## Common Challenges

This section describes the inherent friction points of this specific environment/scenario, as backed by reference
implementations, feedback surveys, and live sessions.

- What typically breaks or slows down adoption?
- How does this affect business or engineering practices?
- What is normally a hard problem to solve and thus requires a coherent strategy?

Authors MUST NOT focus on solutions, or goals, here. They SHOULD simply state the challenges that target audiences
normally see in the environments in scope, as documented in existing reference implementations. In particular, they
MUST avoid thinking about the need for a particular solution within these common challenges. For instance, they MUST
NOT state something like "because of a lack of distributed tracing, we must provide a way to configure a
TracerProvider". They SHOULD leave those statements for the Implementation section, so that actions can connect back
to guiding policies.

This section SHOULD focus on the root causes or the pivotal issues that, if resolved, deliver the most impact.
Authors SHOULD NOT go into deep details, and they SHOULD NOT aim to cover every known problem in the environments in
scope. Instead, they SHOULD highlight why particular challenges are important and the impact they have.

This section MAY include diagrams that explain the high-level architecture or organizational structure where this
blueprint applies. Authors SHOULD use Mermaid.js with default styles to create diagrams.

A few additional practices help keep this section sharp:

- **Don't list challenges for the sake of listing challenges.** Not all challenges are equal. Focus on the ones that
  deliver the most value if solved, not on every improvement opportunity you noticed.
- **Quantify impact.** You don't need exact numbers, but every challenge listed should have a tangible effect on
  business or engineering outcomes (e.g. "the lack of automation in setting up instrumentation results in lower
  engineering efficiency and developer productivity").
- **Illustrate challenges, don't just describe them.** A diagram or a real screenshot of live account data makes a
  challenge land faster than a paragraph of prose (e.g. a broken link between two systems that should share a standard).

## General Guidelines

This section contains a set of guidelines, or recommendations, that guide the general architectural philosophy to
solve the common challenges. This is the North Star of the blueprint, so it MUST focus on the end-goal.

- What does the resulting architecture look like after all actions are implemented?
- How does it solve the documented challenges?
- What additional benefits does it bring?
- How can this optimize the way that teams operate or interact with each other?

The author SHOULD define the boundaries for decision-making, both in terms of architecture (i.e. what part of the
stack this applies to) and organization (i.e. what personas this affects and how they use OpenTelemetry tooling).

Each guideline MUST address at least one challenge presented in the Common Challenges section. If a guideline does
not directly help with any challenges, it MUST NOT be included. The author SHOULD ensure that recommendations explain
the value of applying them — the "so that" behind the guideline. For example, a guideline should not simply state
"Declarative config is provided to teams as a centralized config file", but rather "Declarative config is provided
to teams as a centralized config file so that a consolidated set of domain-specific properties are applied with
minimal friction, allowing configuration owners to quickly perform changes at scale".

Diagrams SHOULD be used here to illustrate the North Star architecture or proposed interaction modes between teams.
Authors SHOULD use Mermaid diagram definitions with default styles to facilitate maintenance.

A few additional practices help keep guidelines actionable:

- **Name what you're deliberately not recommending yet, and why.** A guiding policy is as much about what it rules
  out as what it commits to. If a real alternative exists and it's premature to recommend it, say so explicitly and name
  the constraint. Don't silently omit the alternative or try to recommend everything at once.

## Implementation

The specific technical implementation of the General Guidelines. This section aims to be more prescriptive, and list
a series of actions that, if taken in a particular order, will help implement policies with maximum efficiency.

List the concrete first steps (proximate objectives) that can be taken first, and those that can be done later,
either by criticality or dependency between different tasks (e.g. in order to provide standard OTel pipelines, you
first need to deploy a Collector gateway).

Actions SHOULD reinforce each other (e.g. if the guideline is "standardization," an action to "let teams choose their
own tools" would be incoherent). They MUST also link back to the guideline they help implement. If an action does
not help implement a guideline, it MUST NOT be included.

Actions SHOULD link to specific parts of the OpenTelemetry documentation, and they MUST NOT repeat aspects already
documented elsewhere.

A few additional practices help keep actions concrete:

- **Avoid vague actions.** "Implement changes" isn't helpful — state the concrete deliverable expected once the action
  is complete.

## Reference Implementations

Links to real-world adoption that validates this blueprint. This connects the theory to practice.

## Appendix

Each optional subsection here should represent an aspect that can reinforce the guidelines and actions presented
above. It SHOULD NOT be a replacement for user documentation which can be found or contributed elsewhere in
OpenTelemetry Docs. It SHOULD be focused on providing useful resources for readers and to extend guidance or actions
presented above.

Include here sections like code snippets, step-by-step operating guides, common issues and troubleshooting
guidelines, etc.
