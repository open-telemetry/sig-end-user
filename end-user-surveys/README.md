# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry community surveys
This document is intended to outline best practices for long running and durable OpenTelemetry community surveys. 

The OpenTelemetry community would like to gather data about end-users including their experiences, preferences, perceptions and opinions about OpenTelemetry. This data can be used to inform priorities within various OpenTelemetry projects.

### Survey pipeline

You can find information about upcoming surveys in our [survey pipeline](https://github.com/orgs/open-telemetry/projects/90/views/5). 

Key info about the survey pipeline:
- Generally, we collect data for surveys for 1 month. In that timeframe, and according to previous surveys, we can expect to collect around 100 response. This is usually enough of a statistical population for those running the survey.
- We run up to 6 surveys per year. We don't want to increase survey fatigue of our community too much. With 6 surveys, we have 50/50 balance between when we ask our community to fill in a survey and when we do not.
- We do not run multiple surveys concurently because we don't want surveys to steal each others' thunder. What we want to do instead is getting in touch ahead of time and together prioritizing the survey schedule in a way that works for everyone.
- We make exceptions to the above mentioned when it makes sense. No rules are set in stone.

### Community survey principles
- User feedback should be a mix of qualitative and quantitative:
  - Qualitative to validate/invalidate hypotheses
  - Quantitative to set a baseline for key results and segment customers
- All user feedback will be collected anonymously except direct customer interviews
- Raw data should be transparent to the community/world
- The end user working group will reach consensus on key milestones, including:
  - Recurring/perpetual survey design
  - Survey Hypotheses
  - Measuring Key Results
  - Survey Best Practices
  - Summarizing and reporting results

### Survey design guidelines

1. Aim for less than 15 questions that are short and concise
2. Group questions into logical sections
3. Use demographic questions (filtering, grouping)
4. Start with easy, closed-ended questions
5. Use up to one open-ended question
6. Set questions to 'Required' only if necessary
7. Use clear language without jargon and acronyms.
8. Do not collect Personally Identifiable Information (PII)
9. Avoid leading questions (written in a way that influences survey responses)
10. Avoid loaded question (assumes something about the respondents that might not be true)
11. Avoid double-barreled questions (asks people to give only one answer when asking about two things) 
12. Avoid absolutes (always, every, etc.)
13. Be careful with negation in a questions
14. Ensure questions options are mutually exclusive (e.g. 1-9, 10-99)
15. Include 'Other' option if relevant

For mode details check guidelines from [Stripe](ttps://stripe.com/en-cz/guides/atlas/survey-design-principles), [Survey Monkey](https://www.surveymonkey.com/learn/survey-best-practices/?), [Harvard Law School](https://hnmcp.law.harvard.edu/wp-content/uploads/2012/02/Arevik-Avedian-Survey-Design-PowerPoint.pdf), [Scribbr](https://www.scribbr.com/methodology/survey-research/), or [Smart Survey](https://www.smartsurvey.co.uk/survey-questions/types)

### Helpful questions and considerations: 

- Audience identification: 
  - Who will participate in the survey? What is their user role?
  - Do you need any segmentation or demographic information to meet your survey goals?
  - How many participants do you need for success? 
- Establish survey intent & goals:
  - What are you looking to learn/identify/measure?
  - How will the data be used?
  - What are the survey key results?
- Crafting survey questions: 
  - What is the problem/feedback you want to gather data on?
  - Should you be looking for quantitative or qualitative information, or both?
- Distribution channels: 
  - Where will the survey be advertised?
  - How will end-users be invited to participate? 
- How do you plan to analyze & distribute the survey responses: 
  - How will the data be reported? 
  - What can be summarized? 
  - Do you have any conclusions, insights or recommendations?

### Basic survey template

Surveys header information should include:

* Purpose of the survey
* How long the survey will be open (usually one month)

All surveys should included the following basic demographics questions:

- How large is your organization? (options: 1-49, 50-99, 100-999, 1000+)
- What industry do you work in? (options: Technology, Manufacturing, Aerospace, Retail, Finance, Healthcare, Automotive, Hospitality, Research, Travel & Leisure, Media, Advertisement, other)
- What type of team do you work on? (options: Dev, DevOps, Operations, SRE, Platform Engineering, Observability, Sysadmin, Sales Engineering, DevRel, other)
- Do you work for an Observability or APM vendor? (options: yes/no)
- Are you running OpenTelemetry in Production? (option: yes/no)
- Where in your Observability journey is your organization? (options: Beginner - Learning about observability / Have used monitoring tools; Intermediate - We are setting up an observability practice; Expert - We have a well-established observability practice)

To start a new survey:
* Open up the [survey template](https://docs.google.com/forms/d/1NsOBVcajq3tm4wDrZTt-5bEG5pR3YfK2yccFGVqVzWI/edit?ts=68c840e5), click on the 3 vertical dots on the top right hand side of the screen, and select `Make a copy`
* Enable the survey by going to the `Responses` tab on the top middle, and toggle `Not accepting responses`


Survey template owner is @avillela