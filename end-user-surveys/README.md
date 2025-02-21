# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry community surveys
This document is intended to outline best practices for long running and durable OpenTelemetry community surveys. 

The OpenTelemetry community would like to gather data about end-users including their experiences, preferences, perceptions and opinions about OpenTelemetry. This data can be used to inform priorities within various OpenTelemetry projects.

# Community survey best practices

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

### Survey reminders
##### Original survey design guidelines
- Be respectful of the survey-takers' time, in general try to keep the survey short in duration, with specific and targeted questions. You can always ask if you can follow up with them to get deeper context.
- We want to measure improvements too, so using trendable questions helps us assess how we’re doing 
- We encourage mix of general and targeted surveys

##### Guidelines from [Stripe](https://stripe.com/en-cz/guides/atlas/survey-design-principles)
1. Make answers options collectively exhaustive, 
2. Make answer options mutually exclusive
3. Use language that encourages people to be subjective
4. Limit yourself to one free response question
5. Use public facing copy standards
6. Avoid asking topics that don't immediately relate to a product
7. Respect users’ time.
8. Test the survey with fresh—and diverse—eyes.
9. Describe in detail the key concept of your question.
10. Never ask about multiple concepts in a single question.
11. It’s all relative—be precise.
12. Revise leading questions.
13. Avoid agree-disagree scales.
14. Let people disagree

##### Guidelines from [Survey Monkey](https://www.surveymonkey.com/learn/survey-best-practices/?)
1. Limit yourself to two open-ended questions
2. Ask a series of closed-ended questions, then include a single textbox question to capture any other feedback
3. Put open-ended questions on a separate page towards the end of your survey
4. Make sure that open-ended questions are optional
5. Avoid jargon, technical language, or acronyms. Especially if your audience is supposed to reflect the general population.
6. Keep your questions as short as possible. People will be less willing to read long questions and may misunderstand what you’re asking.
7. If your question has special instructions, add them (in parentheses). Here are a few examples: (select all), (select up to 3)
8. Avoid leading questions (written in a way that influences survey responses), loaded question (assumes something about the respondents that might not be true), double-barreled questions ( asks people to give only one answer to two different questions), absolutes (always, every, etc.).
9. Be careful with sensitive questions (religion or faith, ethnicity, race, gender, age, sexual orientation, and income). For example, provide ranges for salary. Explain how the data will be used and ask them closer to the end of the survey. 
10. Pair close-ended questions with open-ended questions.
11. Ideally aim for less than 10 questions.
12. Use screening questions to ensure that the survey is relevant to the respondent.
13. Only require answers to questions that are necessary to achieve the survey goals.
14. Give context – who you are, what you do, why you are surveying them, How you’re going to use their information or feedback.

##### Andrej's tips
1. Make sure you get maximum out of the surveying tool (randomization, etc.)


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

Survey best practices resources were heavily inspired by these resources: 

- [Survey Research Step-by-step Guide](https://www.scribbr.com/methodology/survey-research/)
- [Types of Survey Questions](https://www.smartsurvey.co.uk/survey-questions/types)

### Basic survey template

Surveys header information should include:

* Purpose of the survey
* How long the survey will be open (usually one month)

All surveys should included the following basic demographics questions:

- How large is your organization? (options: 0-50, 50-100, 100-1000, >1000)
- What industry do you work in? (options: Technology, Manufacturing, Aerospace, Retail, Finance, Healthcare, Automotive, Hospitality, Research, Travel & Leisure, Media, Advertisement, other)
- What type of team do you work on? (options: Dev, DevOps, Operations, SRE, Platform Engineering, Observability, Sysadmin, Sales Engineering, DevRel, other)
- Do you work for an Observability or APM vendor? (options: yes/no)
- Are you running OpenTelemetry in Production? (option: yes/no)
- Where in your Observability journey is your organization? (options: Beginner - Learning about observability / Have used monitoring tools; Intermediate - We are setting up an observability practice; Expert - We have a well-established observability practice)

To start a new survey:
* Open up the [survey template](https://docs.google.com/forms/d/1NsOBVcajq3tm4wDrZTt-5bEG5pR3YfK2yccFGVqVzWI/edit), click on the 3 vertical dots on the top right hand side of the screen, and select `Make a copy`
* Enable the survey by going to the `Responses` tab on the top middle, and toggle `Not accepting responses`

Survey template owner is @avillela