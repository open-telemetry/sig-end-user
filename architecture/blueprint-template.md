---
title: '{Blueprint Name, e.g., Centralized Observability Platform on Kubernetes}'
linkTitle: '{Blueprint Name, e.g., Centralized Observability Platform on Kubernetes}'
---

_Before filling in this template, read the [Blueprint authoring guidelines](./blueprint-guidelines.md)._

## Summary

This blueprint outlines a strategic reference for {target audience, e.g., Platform Engineering teams} operating in {environment, e.g., large-scale, multi-tenant Kubernetes clusters}.

It addresses the friction often found when attempting to {core goal, e.g., provide a "paved road" for observability across microservices owned by multiple teams}.

By implementing the patterns in this blueprint, organizations can expect to achieve the following outcomes:
 - {Outcome 1, e.g., out-of-the-box high-quality telemetry produced by services deployed in a Kubernetes cluster}.
 - {Outcome 2, e.g., consistent SDK configuration and context propagation}
 - {Outcome 3, e.g., governance over data quality and correct use of telemetry signals}
 - {Other outcomes...}

## Background

{Background, e.g. Organizations are widely adopting a cloud native Platform Engineering team to reduce cognitive load and abstract complexity for the rest of their organization, and this also applies to observability...}

## Common Challenges

Organizations operating in this environment typically face a distinct set of challenges that hinder effective observability:

### 1. {Challenge 1, e.g. Fragmented Instrumentation Standards}

{Description of the challenge, e.g., in multi-tenant Kubernetes clusters, distinct teams often adopt different instrumentation standards.}

This leads to:
- {Impact 1, e.g. Inconsistent Metadata: Telemetry lacks common resource attributes (e.g., `service.version`, `k8s.cluster.name`), breaking correlation across the stack.}
- {Impact 2, e.g. High Cognitive Load: Developers must manually configure SDKs for every new service, increasing toil and the risk of misconfiguration.}
- {Other impact...}

### 2. {Challenge 2, e.g. Inefficient Data Collection at Scale}

{Challenge description and impact as documented above}

### n. {Challenge n}

{Challenge description and impact as documented above}


## General Guidelines

### 1. {Guideline 1: e.g., Decouple Instrumentation from Configuration}
<small>Challenges Addressed: {Challenge Numbers, e.g., 1, 3}</small>

{Description of the guideline, e.g., we recommend shifting responsibility over default configurations from application developers to platform teams by using the OTel Operator, ensuring consistent SDK configuration.}

By implementing this guideline, organizations can expect to achieve:
- {Outcome 1, e.g. adoption of required Resource attributes becomes frictionless without developer intervention.}
- {Outcome 1, e.g. context propagation works out of the box through service boundaries and asynchronous execution units.}
- {Other outcomes...}

### 2. {Guideline 2: e.g., 2. Centralize Common Processing}
<small>Challenges Addressed: {Challenge Numbers, e.g. 2}</small>

{Guideline description and expected outcomes as documented above}

### n. {Guideline n}
<small>Challenges Addressed: {Challenge Numbers, e.g. n}</small>

{Guideline description and expected outcomes as documented above}

## Implementation

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


## Reference Implementations

The patterns described above have been successfully implemented by the following end-users:

- {Link to Reference Implementation 1}
- {Link to Reference Implementation 2}

## Appendix

### 1. {Appendix 1, e.g. Common Issues and Troubleshooting}


### n. {Action n}
