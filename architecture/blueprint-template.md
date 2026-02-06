---
title: {Blueprint Name, e.g., Centralized Observability Platform on Kubernetes}
linkTitle: {Blueprint Name, e.g., Centralized Observability Platform on Kubernetes}
date: {Date}
author: {Author}
---

<!--
A blueprint SHOULD be structured in a way that conveys a journey, from a current state to a desired state.
For this purpose, the OTel Blueprint template is based on the approach to strategic thinking popularised by Richard Rumelt in Good Strategy/Bad Strategy. See useful materials before starting to write a blueprint:

- Summary - https://itsadeliverything.com/good-strategy-bad-strategy-the-difference-and-why-it-matters-by-richard-rumelt
- Interview - https://www.youtube.com/watch?v=4uWKEG0s9Kc

Some modifications must be applied to that framework, as OTel Blueprints are not scoped to solve a specific set of challenges for a single organization, but rather a common set of challenges as identified in end-user reference architectures, feedback surveys, and OpenTelemetry Live sessions.

Effectively, an OTel Blueprint is structured in four core areas:

- Summary: Introduces the target audience and environment, and the benefits from applying said blueprint.
    This MUST be placed at the start of the document.
- Common Challenges: The challenges to solve that, once solved, will generate the largest value for a particular organization.
    This is referred to as the “Diagnosis” in Rumelt’s framework.
- General Guidelines: The pattern that, if implemented, would solve the Common Challenges identified in the previous block.
    Guidelines MUST NOT be included if they don’t apply to at least one of the documented challenge.
    This is referred to as “Guiding Policy” in Rumelt’s framework.
- Implementation: The list of actions to implement the General Guidelines, highlighting a plan that takes into consideration interdependencies between these actions (i.e. coherently).
    This is referred to as “Coherent Actions” in Rumelt’s framework.

Additionally, OTel Blueprints SHOULD optionally include these other sections:

- Background: A brief introduction to the environment and the audience.
- Reference Architectures: Links to reference architectures that implemented some, or all of the General Guidelines.
    It is strongly encouraged to back blueprints with reference architectures that implement them.
    This MUST be placed after the Coherent Actions section.
- Appendix: Any information that would make other sections too verbose (e.g., code snippets, step-by-step guides, etc).
    This MUST be placed at the end of the document.

This template uses an example, i.e. "Centralized Observability Platform on Kubernetes" to illustrate some of the defined blocks.
Two types of punctuation are used to guide the author:

- Text in {curly brackets} denotes details that MUST be filled in by the author, with examples inside the curly brackets.
- Text in <!- - markdown comments - -> denotes guidance that MUST not be included in the final document.

Authors MAY add more sections or reword any text within each of the sections, but MUST not remove any of the mandatory sections listed above.
-->

## Summary
<!--
A brief, high-level overview of the intended audience, the applicable environment, and the outcomes achieved.
It should answer the following questions:

- Who is the intended audience for this blueprint?
    Identify the type of team or engineering role that will read this blueprint and apply it.
- What type of environment does this blueprint apply to?
    Identify the stack where these recommendations will be applied
- What is the core goal and the outcomes that this blueprint will drive when applied?
    As one-liners, identify the value that organizations get from applying this blueprint.
-->

This blueprint outlines a strategic reference for {target audience, e.g., Platform Engineering teams} operating in {environment, e.g., large-scale, multi-tenant Kubernetes clusters}.

It addresses the friction often found when attempting to {core goal, e.g., provide a "paved road" for observability across microservices owned by multiple teams}.

By implementing the patterns in this blueprint, organizations can expect to achieve the following outcomes:
 - {Outcome 1, e.g., out-of-the-box high-quality telemetry produced by services deployed in a Kubernetes cluster}.
 - {Outcome 2, e.g., consistent SDK configuration and context propagation}
 - {Outcome 3, e.g., governance over data quality and correct use of telemetry signals}
 - {Other outcomes...}

## Background
<!--
OPTIONAL. A brief introduction to the environment in scope, or the intended audience.
This section is optional, however it authors SHOULD consider it in order to keep the summary to a few paragraphs.
-->

{Background, e.g. Organizations are widely adoption a cloud native Platform Engineering to reduce cognitive load and abstract complexity for the rest of their organization, and this also applies to observability...}

## Common Challenges
<!--
This section describes the inherent friction points of this specific environment/scenario, as backed by reference architectures, feedback surveys, and live sessions.

- What typically breaks or slows down adoption?
- How does this affect business or engineering practices?
- What is normally a hard problem to solve and thus requires a coherent strategy?

Authors MUST NOT focus on solutions, or goals, here.
They SHOULD simply state the challenges that target audiences normally see in the environments in scope, as documented in existing reference architectures.
In particular, they MUST avoid thinking about the need for a particular solution within these common challenges.
For instance, they MUST NOT state something like “because of a lack of distributed tracing, we must provide a way to configure a TracerProvider”.
They SHOULD leave those statements for the Coherent Actions section, so that actions can connect back to guiding policies.

This section SHOULD focus on the root causes or the pivotal issues that, if resolved, deliver the most impact
Authors SHOULD NOT go into deep details, and they SHOULD NOT aim to cover every known problem in the environments in scope.
Instead, they SHOULD highlight why particular challenges are important and the impact they have.

This section MAY include diagrams that explain the high-level architecture or organizational structure where this blueprint is applied to.
-->

Organizations operating in this environment typically face a distinct set of challenges that hinder effective observability:

### 1. {Challenge 1, e.g. Fragmented Instrumentation Standards}

{Description of the challenge, e.g., in multi-tenant Kubernetes clusters distinct teams often adopt different instrumentation standards.}

This leads to:
<!-- Impact of the challenge -->
- {Impact 1, e.g. Inconsistent Metadata: Telemetry lacks common resource attributes (e.g., `service.version`, `k8s.cluster.name`), breaking correlation across the stack.}
- {Impact 2, e.g. High Cognitive Load: Developers must manually configure SDKs for every new service, increasing toil and the risk of misconfiguration.}
- {Other impact...}

### 2. {Challenge 2, e.g. Inefficient Data Collection at Scale}

{Challenge description and impact as documented above}

### n. {Challenge n}

{Challenge description and impact as documented above}


## General Guidelines
<!--
This section contains a set of guidelines, or recommendations, that guide the general architectural philosophy to solve the common challenges.
This is the North Star of the blueprint, so it MUST focus on the end-goal.

- What does the resulting architecture look like after all actions are implemented?
- How does it solve the documented challenges?
- What additional benefits does it bring?
- How can this optimize the way that teams operate or interact with each other?

The author SHOULD define the boundaries for decision-making, both in terms of architecture (i.e., what part of the stack this applies to), organization (i.e., what personas this affects and how they use OpenTelemetry tooling). 

Each guideline MUST address at least one challenge presented in the Common Challenges.
If a guideline does not directly help with any challenges, it MUST NOT be included.
The author SHOULD ensure that recommendations explain the value of applying them.
For example, a guideline should not simply state "Declarative config is provided to teams as a centralised config file", but rather as "Declarative config is provided to teams as a centralised config file so that a consolidated set of domain-specific properties are applied with minimal friction, allowing configuration owners to quickly perform changes at scale".

Diagrams SHOULD be used here to illustrate the North Star architecture or proposed interaction modes between teams. Consider using Mermaid diagram definitions to facilitate maintenance.
-->

### 1. {Guideline 1: e.g., Decouple Instrumentation from Configuration}
<small>Challenges Addressed: {Challenge Numbers, e.g., 1, 3}</small>

{Description of the guideline, e.g., we recommend shifting responsibility over default configurations from application developers to platform teams by using the OTel Operator, ensuring consistent SDK configuration.}

By implementing this guideline, organizations can expect to achieve:
<!-- Outcomes of the guideline -->
- {Outcome 1, e.g. adoption of required Resource attributes becomes frictionless without developer intervention.}
- {Outcome 1, e.g. context propagation works out of the box through service boundaries and asynchronous execution units.}
- {Other outcomes...}

### 2. {Guideline 2: e.g., 2. Centralise Common Processing}
<small>Challenges Addressed: {Challenge Numbers, e.g. 2}</small>

{Guideline description and expected outcomes as documented above}

### n. {Guideline n}
<small>Challenges Addressed: {Challenge Numbers, e.g. n}</small>

{Guideline description and expected outcomes as documented above}

## Implementation
<!--
The specific technical implementation of the General Guidelines.
This section aims to be more prescriptive, and list a series of actions that, if taken in a particular order, will help implement policies with maximum efficiency.

List the concrete first steps (proximate objectives) that can be taken first, and those that can be done later.
Either by criticality or dependency between different tasks (e.g. in order to provide standard OTel pipelines, you first need to deploy a Collector gateway).

Actions SHOULD reinforce each other (e.g., if the guideline is "standardization," an action to "let teams choose their own tools" would be incoherent).
They MUST also link back to the guideline they help implement.
If an action does not help implement a guideline, it MUST NOT be included.

Actions SHOULD link to specific parts of the OpenTelemetry documentation, and they MUST NOT repeat aspects already documented elsewhere.
-->

### 1. {Action 1, e.g., Deploy a Collector Gateway}
<small>Guidelines Supported: {Guideline Numbers, e.g. 2}</small>

{Action description, e.g. Deploy a two-tier Collector Gateway. A first layer handles initial ingest and metadata enrichment, while a second layer handles tail-sampling and exporting to backend}.

Documentation:
- {Link to specific OTel Collector deployment patterns.}
- {Link to Helm Chart.}

### 2. {Action 2, e.g., Configure Standard Resource Attributes Automatically}
<small>Guidelines Supported: {Guideline Numbers, e.g. 2}</small>

### n. {Action n}
<small>Guidelines Supported: {Guideline Numbers, e.g. n}</small>


## Reference Architectures
<!--
Links to real-world adoption that validate this blueprint. This connects the theory to practice.
-->
The patterns described above have been successfully implemented by the following end-users:

- {Reference Architecture 1}
- {Reference Architecture 2}

