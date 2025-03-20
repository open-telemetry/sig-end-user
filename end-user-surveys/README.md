# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry community surveys
This document is intended to outline best practices for long running and durable OpenTelemetry community surveys. 

The OpenTelemetry community would like to gather data about end-users including their experiences, preferences, perceptions and opinions about OpenTelemetry. This data can be used to inform priorities within various OpenTelemetry projects.

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


<!--
### Survey design guidelines
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

##### [Harvard Law School](https://hnmcp.law.harvard.edu/wp-content/uploads/2012/02/Arevik-Avedian-Survey-Design-PowerPoint.pdf)

1. Questionnaire items should be precise
2. Avoid asking for a single answer to a question that actually has multiple parts.
3. Respondent should be able to read a question quickly, understand its intent and select or provide an answer
without difficulty. 
4. Negation in a question paves the way for easy misinterpretation.
5. Target the vocabulary of the population to be surveyed (be carful about jargon, abbreviations, biased terms).

#### [Survey Research Step-by-step Guide](https://www.scribbr.com/methodology/survey-research/)
1. Options should cover all the possibilities
2. Consider asking an open-ended follow up question for a more detailed explanation of what was asked in the closed-ended question before.
3. Language should be clear and precise. Avoid jargon or industry-specific terminology. Phrase your questions in a neutral way with a no indication for a prefered answer. 
4. Questioned should be ordered in a logical order.
5. Start with easy, non-sensitive, closed-ended questions that will encourage the respondent to continue. 
6. Related questions should be grouped together.

#### [Types of Survey Questions](https://www.smartsurvey.co.uk/survey-questions/types)
1.  Demographic questions are those that look to categorise the identity of the survey participants based on factors such as their age, gender, ethnicity, marital status, household income, employment, education level and location.
2. Dichotomous question should be used with care to avoid frustration or compromised results.
3. Hypothetical questions should be avoided, in general. If used, they should be implemented with great care. 

##### Andrej's tips based on reviewing the current surveys
1. Make sure your questions are configured correctly. 
2. Use template questions and standard scales (e.g. Likert scale)
3. Use tools to full extent
  - Provide details in the next question > There is an option for that in Google Forms
  - Make sure optional questions are not set to required
  - We should use conditional questions
4. Use rating numbers with explanations (1,2,3,4,5 > Strongly agree …. Strongly disagree)
5. Make the choices more balanced (Poor, Okay, Great, N/A
6. Long surveys (21 questions is too much)
7. Answer options shouldn't overlap (e.g. 1-100,100-200)
-->

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