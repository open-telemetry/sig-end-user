# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OTel Me Adobe Discussion
 
Suggested Interview Flow (30/60 minute duration)

## Pre-Stream Housekeeping (~5 min)
- [ ] Welcome the Adobe representatives and thank them for joining the preparation call.
- [ ] Introduce yourself and invite the Adobe representatives to introduce themselves.
- [ ] Walk through the planned discussion flow, covering adoption, architecture and design decisions, instrumentation, operational challenges, and lessons learned.
- [ ] Confirm whether the Adobe representatives have any additional updates or experiences they would like to share beyond what's documented in the reference implementation.
- [ ] Agree on how audience questions will be handled and reserve time for Q&A.

## Livestream Kickoff
- [ ] Could you briefly introduce yourselves, share your roles at Adobe, explain how you are involved in using or implementing OpenTelemetry at Adobe? 
- [ ] To get us started, could you introduce Adobe's published OpenTelemetry [reference implementation](https://opentelemetry.io/docs/guidance/reference-implementations/adobe/?utm_source=chatgpt.com), What does it cover, and how can it help teams get started with OpenTelemetry?
- [ ] What are the key architectural decisions reflected in this implementation?
 
## Warm-up questions (~3 / 10 min)
This section helps set the stage for the session and provides context that should allow for more insightful questions to be asked later.
- Could you briefly describe your responsibilities in Adobe's OpenTelemetry platform and how you work with the application/service teams?
- The reference implementation describes few challenges:
    - Chain Collectors: When telemetry passes through multiple Collectors, how does your team ensure that backend errors are propagated and visible to upstream Collectors? Have you encountered similar error-   visibility challenges elsewhere in the platform?
    - Operator and Collector version compatibility: How do you manage compatibility between Operator upgrades and different Collector versions across service teams?
    - Routing processor deprecation: How do you handle changes to Collector components when existing components are deprecated or replaced?  
- The reference implementation describes a Kubernetes-based deployment model using Helm charts and the OpenTelemetry Operator. Is this the primary onboarding approach for applications using the platform? Are there any significant exceptions?
- What types of workloads are currently instrumented with OpenTelemetry at Adobe, such as microservices, customer-facing APIs, event-driven services, or background processing jobs? Do they have different instrumentation requirements?

## Meaty questions (~15 / 25 min) 
This section will depend upon goals for the interview and what assumptions and/or hypothesis is being tested, some suggested questions are below:
- What challenges, if any, do application teams encounter when adopting OpenTelemetry, even with the simplified onboarding process?
- Are there situations where auto-instrumentation does not provide sufficient telemetry, requiring teams to add manual instrumentation using OpenTelemetry SDKs? What challenges arise in those cases?
- Based on your experience with chained Collectors and the broader OpenTelemetry ecosystem, what improvements would you like to see, particularly around error propagation and backpressure handling?
- What feedback have application teams shared about the ease of onboarding, configuring instrumentation, and getting the telemetry they need from the platform?
- Which teams or roles are most involved in improving and maintaining the OpenTelemetry platform at Adobe? How do they collaborate?
- How does Adobe engage with the OpenTelemetry community? Are there any challenges you face when contributing code, documentation, or feedback to the project?
- GenAI observability:
  - Is Adobe exploring OpenTelemetry for observing GenAI applications and AI agents? If so, how do you approach capturing telemetry such as LLM interactions, agent execution flows, and tool calls?
  - What is your perspective on OpenTelemetry's emerging GenAI semantic conventions? Do you see value in standardizing telemetry attributes across different AI frameworks and observability backends, even while the conventions are still evolving?

## Key Takeaways for OpenTelemetry Adoption
- [ ] Which parts of your implementation do you think other teams (both inside and outside Abode) should pay particular attention to when planning their own OpenTelemetry adoption?

## [Optional] Observer questions (~0 / 5 min)
- Ask the audience if they have any questions for the end user
  
## Turn the tables (~5 / 10 min)
- [ ] Ask the end user what questions, if any, you or the folks on the call can answer for them 

## Wrap it up (~3 min)
- [ ] Thank the end user for their time 
  

---- 
This guidance was heavily inspired by and adapted from Atlassian's Customer Interview Teams Playbook found here: https://www.atlassian.com/team-playbook/plays/customer-interview
