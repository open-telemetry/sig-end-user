# OTel Q&amp;A feat. Daniel Dias and Oscar Reyes of Tracetest

Published on 2024-06-17T19:00:22Z

## Description

Oscar Reyes and Daniel Dias of Tracetest talk about the integration of trace-based testing (TBT) using Tracetest into the OTel ...

URL: https://www.youtube.com/watch?v=KR8j11FECgc

## Summary

In this OTEL Q&A session, hosts Daniel Dias and Oscar Reyes from Tracetest discuss the integration of trace-based testing into the OpenTelemetry (OTEL) community demo, which simulates a telescope shop with several interacting microservices. Daniel, a software developer and CNCF ambassador from Brazil, and Oscar, a lead software engineer from Mexico, explain trace-based testing, which uses traces emitted by systems to make assertions about their state, particularly in complex, distributed services. They elaborate on how Tracetest implements this testing through a two-step process of triggering the system and pulling traces for validation. They also recount the challenges faced during integration, such as ensuring context propagation across service boundaries and adapting existing integration tests into trace-based tests. The integration has led to improved community practices, such as incorporating trace tests into CI/CD pipelines, enhancing testing efficiency and reliability. Overall, the discussion highlights the benefits of combining trace-based testing with OpenTelemetry to improve software quality in distributed systems.

## Chapters

00:00:00 Welcome and intro
00:01:10 Guest introductions
00:02:20 Trace based testing explanation
00:04:00 Tracetest implementation overview
00:06:18 Automation and YAML usage
00:07:39 OTEL community demo introduction
00:09:04 Tracetest integration story
00:12:00 Traceability tests discussion
00:16:30 Challenges during integration
00:20:30 Benefits of trace based testing

**Host:** Welcome everyone who has been able to join us today. This is super exciting to have. We have both Daniel Dias and Oscar Reyes from Tracetest joining us today for OTEL Q&A, and we haven't had an OTEL Q&A for a while. So I'm so glad that both of you were able to join us today. For those of you who are here today, thank you for joining, and also tell your friends that we will be posting a recording of this on the OTEL YouTube channel. So that's OTEL official, for anyone who couldn't make it. And we'll also provide the links on socials once the recording is made available. 

So with that, let's get started. Why don't I get you to introduce yourselves?

[00:01:10] **Daniel:** I can go first. So hello everyone. I'm Daniel Dias, a Brazilian living and complaining in Argentina right now because of the weather. I am a software developer at Tracetest, and while I'm not helping the team evolve with new features, I'm bragging about the features somewhere. That's all. And Daniel, he's also an ambassador, so he's really proud to have one ambassador in CNCF ambassador too. CNCF ambassador, right? Yes. Newly minted, right? Just, yes. I became my ambassador last week, last month. Yay.

**Oscar:** For my part, I'm Oscar Reyes. I'm Mexican. I live in Mexico. And I'm a lead software engineer here at Tracetest. And yeah, I'm really happy to be here and talk about Tracetest and OpenTelemetry.

**Host:** Awesome. Okay. First things first, for folks on the call who might not be familiar, can you tell us what trace-based testing is?

[00:02:20] **Daniel:** When we call, say about trace-based tests, the main idea is that we want to, we use traces emitted by systems to assert how the screen state of the trace, the state is. So we call some component on the system, wait for a while until the trace is generated, and we start to make assertions to this trace to guarantee that everything is right. 

**Oscar:** Yeah, and this is really helpful for distributed services where you have a lot of moving pieces, and if the entire system is instrumented, you can get a lot of, you can have a lot of assertions around the generated OpenTelemetry data or the traces, right? You can validate that certain spans exist, but you can also go deeper and validate things like the attributes or the execution time of the spans, those sort of things. So it's a multi-layer level of testing and the entire spans or traces that your system generates.

**Daniel:** That's awesome. And the thing I love about trace-based testing is we're already emitting traces in our code. So why not take advantage of that? So I feel like it's a two-for-one deal. Which is very awesome. 

**Host:** The other thing that I wanted to ask, so how does Tracetest implement trace-based testing?

[00:04:00] **Oscar:** Maybe I can answer this one and you can complement what I say, Daniel, if you want to. What trace-based, the way that trace-based does it is that we have a two-step process. The first one is triggering your system, the system on their test. Currently, we support things like HTTP, gRPC requests. We also support Kafka, that was actually integrated by Daniel. And then we have other types of integrations for other types of systems like Cypress or Playwright. So that's the first half of what Tracetest does, triggers their system on the test. 

And then the system address will need to generate or will generate those instrument, the traces and the spans and put in somewhere, in a tracing backend. Tracing backend, it could be something like Jaeger or Tempo or any other providers that you will store the traces. And then the second half of what Tracetest will do is pull for those traces, based on the configuration that you have. So we will wait, depending on the way that system works, that system that generates all of the entire trace in one, a couple of seconds. You have other ones that generate that have long-lasting processes that could take five minutes. So we support all those variables. 

And so we wait for the trace to be ready. We pull that into the Tracetest system. Based on the trace ID that we generate on the first step, that will work as a parent ID, and then the assertions on the spans, the sessions, and the test space will be triggered against that generated traces or telemetry data. So I guess, there will be a three-step process: trigger, trace, or getting the trace, and then test. That's how we're calling our three-step process.

**Daniel:** Cool. Do you have anything to add on to that or you're good?

**Oscar:** All right, cool. And if I remember correctly, because it's been a while since I played with Tracetest, but you can create your trace-based tests using YAML, right? Everyone's favorite thing that they love to hate.

**Daniel:** Yeah, I think one of the things that we have pushing in the past few months is not only allowing things to have these three steps, but also how they can automate and simplify the way to introduce trace-based testing in their systems. Either if you use it through a system of Git actions or CI/CD processes, sorry, or you have them in a, I don't know, in a cron job. 

[00:06:18] With the automate way that we provide, you can use our CLI, you can use the different tools that we provide, like our TypeScript library, so you can pretty much graph the specifications and the YAML files, as you said, even JSON files from the system. If you go to the UI or either use the CLI to export them, you can put it in your report and execute everything from there. So it's like you have multiple ways of interacting with the system and with the test definitions, either through the UI, through the CLI, or the libraries that we also support.

**Host:** Cool. Awesome. Before we go on, I do want to mention to folks who are watching, if anyone has any questions, do feel free to pop them into the chat and we will also have a Q&A portion at the end. I just wanted to mention that quickly. 

[00:07:39] Okay. I guess the main reason why we called Daniel and Oscar to do Q&A is that they did something super cool last fall, which was they integrated trace-based testing, a la Tracetest, into the OTEL community demo. So first of all, can one of you explain what the OTEL community demo is for folks who aren't familiar with it?

**Oscar:** I can answer that. The main idea of the OpenTelemetry demo is that it emulates a telescope shop, but with one major thing. Under this shop, we have a bunch of microservices that interact with each other, each one with one responsibility on the system. So we have one API to make payments, another one to do shipping and everything else. And the main idea of this demo is just to show, with a different technology, a different language, how you can integrate OpenTelemetry to your system and how you can see this data integrated across a bunch of mobile services.

**Daniel:** Awesome. Yeah. And it's, it's a great way for getting started with OTEL, especially if you're like, Oh, this is so overwhelming seeing it in a relatively complex example, just kind of goes to show the power of OTEL, which I always think is so cool. And it's not terribly awful to get started with the OTEL demo. I definitely recommend to folks who haven't tried it out to give it a go. 

Okay. So now that we understand what the OTEL demo is, let's talk about how you got Tracetest integrated into the demo. 

**Oscar:** Maybe I can start with the first half of the story and then Daniel can continue after that. So almost a year and a half ago, we were looking for different partnerships or different ways to contribute with the community and just push OpenTelemetry further. We discovered the OpenTelemetry demo. And I was on a task on let's try to just contribute and see how we can help and grow the community. 

And the first thing that I was, that I worked on, it was to switch or migrate the existing front-end application that was built entirely in Go, Golang with a front, with a server-side rendered front end. Just templates, HTML templates, things like that to an actual front-end application. So we, I switched that to, from Go to Next.js. So Next.js on the, having React involved and also introducing the actual front-end instrumentation of the application by using the tools and the web, the browser site, OpenTelemetry libraries. So in that case, it is continuously connected across, starting from the browser all the way to the backend services. And that was pretty much my contribution, my contribution on the OpenTelemetry demo. 

**Daniel:** And then, after Daniel joined and did other stuff. So you want to go next? Continue, Daniel.

**Oscar:** After a while, we started to see the OpenTelemetry demo because it is great. Every time that you need to see, oh, I will start programming in Ruby and I need an API. If you go to OpenTelemetry demo, you will see an API there and you can see, oh, this is how you integrate things there or Python or everything else. But looking to the tests that we have in OpenTelemetry demo at the time, they had integration tests, but just on the API level. 

[00:12:00] So we could test some features of each API, but we could not see how they act together. And sometimes this is painful, mainly when you have background processes. For instance, if you have an API that emits messages to a Kafka queue, and we have another API that reads data from this Kafka queue, how do you guarantee that this second service got the message correctly and is doing something correct? We did not have this at that time. Looking to this test site, I thought, what if we do a trace-based test? So we started discussing a little bit. One of the members of the OpenTelemetry team, also demo team, also asked us, because they say, oh guys, we developed some new things on the OpenTelemetry demo, but we did not notice that we changed the slide a little bit, some traces, and something is wrong. It's weird to understand, we need to manually inspect everything. We started to do traceability tests on that. 

**Oscar:** We started looking at each one of the integration tests, and we started writing a counterpart traceability test, but for a small difference. Instead of just seeing the API response, we also are seeing what are the APIs that we are calling behind the scenes, and we are testing these APIs too. And so my thing as well was that for us, part of that section, I don't know if it was a month or a couple of weeks, there was a specific service that was, the telemetry was failing or was broken, right? And the team didn't find out until that time passed and someone, I don't know, saw that problem. And then based on that also pushed the idea on using Tracetest to catch those problems as well, right? 

And recently, we had another situation where the Kafka link, the Kafka SDK for Go changed it, changed the ownership from Shopify to IBM. And some things changed on this API. They use Tracetest to change the telemetry, update this library, and assert that everything was fine. This was another thing that was good too.

**Host:** Cool, that's awesome. Just to make sure I understand correctly, when you started writing the trace-based tests, was it, your initial process was basically converting the initial integration tests into the trace-based tests? So you already had, you didn't have to worry about coming up with the tests. It was essentially a translation and then you did not just checking for the response, but additional stuff basically.

**Oscar:** Exactly. One difference on this approach is that first I started with the language that we all love that is YAML. So I did a copy and paste on the test. But when you see traces, you need to think a little bit of what types of traces this API calls does. What I did was first write a MO test, run a little bit, and then I swapped it to Tracetest UI because there we can see how is the shape of the traces that we are generating? And I could play a little bit, see, oh, I saw that the checkout service emits this, the trace that I can assert. The shipping service emits another trace, another span, sorry. And I could tweak a little bit and start building more complex tasks with that same. 

Oh, I want to test the service A and see if the service B, D, and E are working as well. And I think that's a really interesting part of telemetry in general, right? And producing traces and having all of the services instrumented, because for someone that is not familiar with the system, they can, it's easier to look at a trace and understand the process and the steps that are taken for a specific use case, instead of going line by line, looking at the code and trying to understand what is going on.

**Host:** And how long did it take to create all the trace-based tests, the initial set for the OTEL demo? Because I think it was, the announcement was made, I want to say, last KubeCon North America in Chicago, last fall kind of thing? Is that correct? Correct me if I'm wrong, please.

**Daniel:** Yes, it was fast. I believe that also to that we discussed it with our team about what was happening and checking, inspecting the integration codes. We were able to, in two or three days, to build all the tests for each one of the services and start discussing with the team, opening a PR and start discussing with the team, changes and other things that we could do.

[00:16:30] **Host:** Awesome. That's so cool. And, so once you implemented, in implementing the trace-based testing into the OTEL demo, what were some of the big challenges, the gotchas, the unexpected things that you encountered as part of this?

**Oscar:** The first thing that we noticed that we thought is how we could do this test without impacting the entire ecosystem. And the first decision that we took is, we know that OpenTelemetry demo uses Jaeger. So instead of, we will see the system outside of it. We will just check Jaeger and do every other operation on Jaeger. With that, it was pretty easy to do everything. The only thing that besides that is just to understand the services, understand how they are working to make our tests, it's generated some interesting things like, one service that I noticed that, first I thought that, the JSON that we sent for the service was in camel case and later we discovered during the execution of this case that this YAML, this JSON was in a snake case. So we started to tweak a little bit and start seeing how the things are and do proper tests for it.

**Host:** When you were writing the trace-based tests, you said you were looking, you're looking at your, you were using Jaeger, as part of your basis. Because I know, Tracetest, I guess there's a couple of approaches to pulling the traces, right? One is either you pull it like in the collector. So you add a config to the collector, or you can pull it directly from any of the supported observability backends. So what was the approach? So I guess my question is, was the approach that you took then was pulling it directly from Jaeger, like the traces?

**Oscar:** Yes, and to that, one thing that we noticed is that, since the example sent all the telemetry data to Jaeger, Prometheus, and everything else, we were secure to use Jaeger as it is. Because we know that sometimes if you have a huge system, you might use sampling, for instance, to just send a small portion of the tests of the traces for a tracing back. It was not the case. So this was important because we know that, oh, if you have sampling or you have some specific configuration on the collector, maybe you want to do a specific configuration on OTEL collector to send some of the just traces for Tracetest to do the things, but it was easier. The job was pretty easy that I thought. Since we had everything we ever needed.

**Host:** Yeah, that's an important distinction, too. Yeah, because I hadn't even thought of the fact that if you're pulling directly from the backend, you're basically pulling the traces that were emitted there versus if you're using the collector, if I recall correctly, you create a different, you create basically a second tracing pipeline, which then intercepts the traces, and then you use those to create your trace-based tests, and then you can put whatever restrictions you want on that for your trace-based test, which I guess gives you a little more freedom as well, like to play around and configure things.

[00:20:30] **Oscar:** Exactly. Cool. That's awesome. And then on a similar vein, what are some of the benefits that you started seeing after the integration was like with trace-based testing? Did they just start receiving high praise from the maintainers in the community demo where they're like, Oh my God, this has changed my life?

**Daniel:** One of the game changer things that I think it was, when I, when we saw the OpenTelemetry demo, maintainers starting to integrate trace tests on their CI/CD pipeline, because this, this was, this is something difficult. And I remember at the time that discussing with them, every time that they needed to change something, they did a bunch of final testing. And since we are humans. Sometimes we might forget testing some service or thinking about a user case. But, what they did was, oh, we will create a pipeline. We will build the entire system to see if everything is right. And after building the system, we will run trace tests and check if everything was right. 

And by doing that, they started to validate some PRs and discover, for instance, that, oh, this PR updated a component that is breaking some traces. And with that, they could start to evaluate and say, oh, okay, let us fix this PR and guarantee that everything is right. And this was painful before because sometimes you could approve a PR, merge it on the database, on the code base, and just two weeks later discover that something was missing. 

**Oscar:** Also want to call out the shout out that we got from Josh Lee. So I remember that when I first joined Tracetest, I saw one of his talks about trace-based tests, actually, something similar to quite what we're doing. And just having someone like him sharing out Tracetest or what it is and what it means for the OpenTelemetry community. It's just great. So I think that's part of what we, the work that we.

**Daniel:** That's so great. That's very cool to hear. And now that the trace-based testing has been integrated in the demo for several months, at this point, what changes have you seen since that initial integration, even to how you approach trade? Have there been any massive changes as to how you approach trace-based testing? Or has it mostly stayed the same? Have there been tweaks that you've had to make along the way?

**Oscar:** The one thing that was great is that they started to build some traceability tests, as they, I remember that I talked with Juliano, that is one of the maintainers, and when this Kafka thing happened, he told me, Daniel, we noticed that the Kafka SDK changed and we wanted to create a basic, to do some changes on the system and create a basic traceability test in it. And it was amazing. 

**Daniel:** And another thing that we loved was that before we had three types of tests running on OpenTelemetry demo, a front-end test, using, I forgot the name of the library.

**Oscar:** Cypress.

**Daniel:** Cypress, they had an API call, API test with AVA, and they had trace test, and they noted, oh, we don't need AVA and Cypress anymore. Since we are focusing on seeing traces and guaranteeing that the telemetry is right and the system is working. Three steps is enough for that. And it was amazing and a huge responsibility for us because now we know that they rely on us. We need to have a good API to everything. 

**Host:** That's so cool. That's such a success. And I love the fact, the great thing about the OTEL community demo too, is that it showcases OpenTelemetry all with open source tooling, including Tracetest, which I think is so cool and really speaks to the power of open source and the open source community. And you end up with this like really nice symbiotic relationship too, right? Because then, I assume you would get some more use cases for improving Tracetest as a whole based on how you see trace-based testing acting in the wild through the community demo.

**Daniel:** During the time that we started to write tests for OpenTelemetry demo, we detected that some of the tests were huge because we needed to embed a protobuffer file inside of each test. And when we started to see that, we noticed that, oh, the developer experience is bad for that because you cannot see what is happening and this moved us to change the CLI and think, let us simplify the test to guarantee that you can see the test and see what matters. And it was good. It was a two-way road. We were able to help them, the OpenTelemetry team, but the feedback that they gave us helped us to improve Tracetest too.

**Oscar:** That's awesome. And as you mentioned, you've got a few folks now writing their own trace-based tests. Have you felt then that, like just getting into that mindset of people writing, like other developers writing trace-based tests, has that, have you noticed, was that a major shift or was it organic once they saw the initial examples that were, that you both added to the repo?

**Daniel:** Believe that, that both things happened. For some developers that were used to OpenTelemetry, they noted that they could use this telemetry to test it, and it was. Sometimes it's way easier to test. For instance, I cannot think in an easy way to test a Kafka consumer without doing a bunch of code magic behind the scenes, and traces are good for that. 

So we had some examples of people using serverless knowing that it is difficult to communicate with several components and using Tracetest to help them. And we saw another developer saying, oh, we are starting to implement OpenTelemetry. We noticed that, with OpenTelemetry, we can test our system quickly. Tracetest helped them to drive and implement more things in OpenTelemetry and start doing things there. I believe that these two cases happened.

**Oscar:** Oh, that's so great. Final question. If you had a redo, would you change anything about how you integrated trace-based testing with the OTEL demo?

**Daniel:** First glance, I believe that nothing because I believe it was a perfect match. So we could do everything that we needed there. The only thing, the only thing that I think that I could do, and I think that I might do, if you are watching me, Pierre, Juliano, and company, I will haunt you in the future for that, is to add more tasks and start thinking in more interesting use cases that we can do and thinking more telemetry that we can show that.

**Host:** Amazing. This is great. We do have a question from the audience. Daniel asked, one of the biggest pains for distributed systems is ensuring correct context propagation across service boundaries, especially when async operations require in-service context propagation across threads and context may be instrumented properly. Can trace tests help identify where context is being broken when it shouldn't?

**Oscar:** I think I can answer that question. First of all, I think we have all been there. We have all felt the pain of why is my trace not being propagated to this backend system or this part of the app. And yes, actually, a great thing that, or a good thing that we are, one, one kind of standard or thing that we're pushing is TDD, but in this case, Trace-Based Driven Development. 

Where users can create assertions and test specs based on what they would expect the trace to look like. So if you already know that after a queuing system, there should be a worker that would process that message, you can pretty much, from the beginning, from the get-go, create a definition that would match. I would expect that span to exist. So if that span doesn't exist, it's because the context propagation is pretty much not, didn't work or the span, that's why the span doesn't exist, right? It's not there. So with this kind of technique that you can use, you can validate that the expected spans should be there and help you with the problem of your context propagation problem as well.

**Host:** Awesome. So you've answered Dan's question. Thank you. And then there was a follow-up question, can Tracetests make assertions on baggage?

**Oscar:** It depends. If you are saying baggage, so for some specific metadata of OpenTelemetry, perhaps not. But what we can do today is that if you write custom attributes in your span, you define a bunch of attributes, you can test them. You can test them. Also, we are every time looking to the OpenTelemetry specification, seeing if there is more metadata that we should integrate to the API and doing it like error codes, span statuses, and everything else. I think we have something about span links, right? I want to do as well. I remember. Exactly.

**Host:** Nice. That's awesome. Does anyone else, who's listening have any additional questions? This has been really great. Thank you both, Daniel and Oscar for joining today. This has been really awesome. I think it's really cool. I'm a big fan of the OTEL demo and I think having trace-based testing integrated really, it's like a very tracing native approach to integration tests. I'm a huge fan, so it's super cool to see that integration in place and to see other folks, outside of both of you actually writing trace-based tests. Thank you.

**Daniel:** Thank you, everyone. And thank you, Adriana, for putting this together and for having us. It was great.

## Raw YouTube Transcript

Welcome everyone who has
been able to join us today. This is super exciting, to have. We have both Daniel Dias and Oscar
Reyes from trace test joining us today for OTEL Q&A, and we haven't
had an OTEL Q&A for a while. So I'm, I'm so glad that both of
you were able to join us today. For those of you who are here
today, thank you for joining, and also tell your friends that we
will be, posting a recording of this on the OTEL YouTube channel. So that's OTEL official, for
anyone who couldn't make it. And we'll also provide the
links on socials once the recording is made available. So with that, let's get started. Why don't I get you to
introduce yourselves? I can go first. So hello everyone. I'm Daniel Dias, a Brazilian
living and complaining in Argentina right now because of the weather. I am a software developer at Tracetest
and while I'm not helping the team evolve with new features, I'm
bragging about the features somewhere. That's all. And Daniel, he's also an ambassador,
so he's really proud to have one ambassador in CNCF ambassador too. CNCF ambassador, right? Yes. Newly minted, right? Just, Yes. I became my ambassador,
last week, last month. Yay. Congratulations. For my part, I'm Oscar Reyes. I'm Mexican. I live in Mexico. And I'm a lead software
engineer here at Tracetest. And yeah, I'm really happy to be here and
talk about Tracetest and OpenTelemetry. Awesome. Okay. first things first, for folks on the
call who might not be familiar, can you tell us what trace based testing is? When we call, say about trace based
tests, the main idea is that we want to, we use traces emitted by
systems to assert how the screen state of the trace, the state is. So we call some component on the
system, wait for a while until the trace is generated, and we start
to make assertions to this trace to guarantee that everything is right. Yeah, and this is really helpful for
distributed services where you have a lot of moving pieces, and if the
entire system is instrumented, you can get a lot of, you can have a lot
of assertions around the generated OpenTelemetry data or the traces, right? You can validate that certain
spans exist, but you can also go deeper and validate things like the
attributes or the execution time of the spans, those sort of things. So it's a multi layer level of
testing and the entire, spans or traces that your system generates. That's awesome. And the thing I love about trace
based testing is, we're already emitting traces in our code. So why not take advantage of that? So I feel like it's a two for one deal. Which is very awesome. the other thing that I wanted to
ask, so how does, so how does trace test implement trace based testing? Maybe I can answer this one
and you can complement what I say, Daniel, if you want to. what trace based, the way that
trace based does it is that we have a two step process. The first one is triggering your
system, the system on their, test. Currently we support things
like HTTP, gRPC requests. We also support Kafka, that was
actually integrated by Daniel. And then we have other type of
integrations for other type of systems like, Cypress or Playwright. So that's the first half of what Tracetest
does, triggers their system on the test. And then the system address will need
to generate or will generate those instrument, the traces and the spans and
put in somewhere, in a tracing backend. Tracing backend, it could be something
like Jaeger or Tempo or any other providers that you will store the traces. And then the second half
or what Tracer will do is. Pull for those traces, based on
the configuration that you have. So we will wait, depending on the,
on, on the way that system works, that system that generate all of the entire
trace in one, a couple of seconds. You have other ones that generate
that have long lasting processes that could take five minutes. So we support all those variables. And so we wait for the trace to be ready. We pull that into the trace test system. Based on the trace ID that we generate
on the first step, that will work as a, the parent ID and then the assertions
on the spans, the sessions and the test space will be triggered a against that
generated traces or, telemetry data. So I guess, there will be a three, three
step process trigger, trace or getting the trace and then test, that's how
we're calling our three step process. Cool. Daniel, do you have anything to
add on to that or you're good? All right, cool. And, if I remember correctly, because
it's been a while since I played with Tracetest, but, you can create your
trace based tests using YAML, right? Everyone's favorite thing
that they love to hate. Yeah, I think, one of the things that
we have pushing in the past few months is not only allowing things to have
these three steps, but also how they can automate and simplify the way to introduce
trace based testing their systems. Either if you use it through a
system of Git actions or CI/CD processes, sorry, or you have them
in a, I don't know, in a cron job. With the automate way that we provide,
you can use our CLI, you can use the different tools that we provide, like
the our TypeScript library, so you can pretty much graph the specifications
and the yamo files, as you said, even JSON files from the system. If you go to the UI or either
use the CLI to export them, you can put it in your report. And execute everything from there. So it's like you, you have multiple
ways of interacting with, the system and with the test definitions, either
through the UI, through the CLI or the libraries that we also support. Cool. Awesome. before we go on, I do want to mention
to folks, who are watching, if anyone has any questions, do feel free to
pop them into the chat and we will also have a Q& A portion at the end. I just wanted to mention that quickly. Okay. I guess the main reason why we,
called, Danielle and Oscar, to do Q&A is that they did something super
cool last fall, which was, they integrated trace based testing, a la
Tracetest, into the OTEL community demo. So first of all, can one of you explain
what the OTEL community demo is for folks who aren't familiar with it? I can answer that. the main idea of, the OpenTelemetry
demo is that it emulates a telescope shop, but with one major thing. we. Under this shop, we have a bunch
of microservices that interact with each other, each one with
one responsibility on the system. So we have a, we have one API
to make payments, another one to do shipping and everything else. And the main idea of this demo is just
to, is to show shook with a different technology, a different language, how you
can integrate OpenTelemetry to your system and how you can see this data integrated
across a bunch of mobile services. Awesome. Yeah. And it's, it's a great way
for getting started with OTEL. especially if you're like, Oh, this
is so overwhelming seeing it in, a relatively complex example, just kind
It goes to show like the power of OTEL, which I always think is so cool. And it's, not terribly awful to
get started with the OTEL demo. I definitely recommend to folks who
haven't tried it out to give it a go. Okay. So now that we understand what the OTEL
demo is, let's talk about how, you got Tracetest integrated into the demo. maybe I can start with the
first half of the story and then Daniel can continue after that. So almost, a year and a half ago,
we were looking for different partnerships or different ways to
contribute with the community and just push OpenTelemetry, further. we discovered this,
the OpenTelemetry demo. And I was on a task on let's try
to, Just contribute and see how we can help and grow the community. And the first thing that I was,
that I worked on, it was to, switch or migrate the existing front end
application that was built entirely in Go, Golang with a front, with
a server side rendered front end. just templates, HTML templates,
things like that to an actual front end application. So we, I switched that
to, from Go to, Next. js. So Next. js on the, having React involved and
also introducing the actual front end instrumentation of the application
by, Using the tools and the web, the browser site, OpenTelemetrylibraries. So in that case, it is
continuously connected across, starting from the browser all
the way to the backend services. And that was pretty much my,
contribution manager contribution on the OpenTelemetry demo. And then, then after Daniel
joined and did other stuff. So you want to, go next? Continue, Daniel. After a while, we started to see the
OpenTelemetry demo because it is great. Every time that you need to see,
oh, I, I will start programming in Ruby and I need an API. If you go to OpenTelemetry demo, you
will see an API there and you can see, oh, this is how you integrate things
there or Python or everything else. But, looking to the test that
we have in OpenTelemetry demo at the time, they had integration
tests, but just on the API level. So we could test some features
of each API, but we could not see how they act together. And sometimes this is painful. Mainly, when you have background process,
for instance, if you have an API that emits messages to a Kafka query, and we
have another API that reads data from this Kafka query, how do you guarantee
that, this second service got the message correctly and is doing something correct? We did not have this at that time. Looking to this test site, I thought,
what if we do a trace based test? So we started discussing a little bit. One of the members of the OpenTelemetry
team also, demo team, also asked us, because they say, oh guys, we developed
some new things on the OpenTelemetry demo, but we did not notice that
we changed the slide a little bit, some traces, and something is wrong. It's weird to understand, we need
to manually inspect everything. We started to do
traceability tests on that. We started looking at each one of
the integration tests, and we started writing a counterpart traceability
test, but for a small difference. Instead of just seeing the API response,
we also are, seeing what are the APIs that we are calling behind the scenes,
and we are testing these APIs too. And so my thing as well
was that for a, for us. Part of that section, I don't
know if it was a month or a couple of weeks, there was a specific
service that was, the telemetry was failing or was broken, right? And the team didn't find out until,
that time passed and someone, I don't know, saw that problem. And then based on that also pushed
the idea on using trace test to catch those problems as well, right? And recently, we had another situation
where, the Kafka link, the Kafka SDK for get goal and change it, change
the ownership from Shopify to IBM. And some things changed on this API. They use a trace test to change the
telemetry, update this library, and assert that everything was fine. This was another thing that was good, too. Cool, that's awesome. just to make sure I understand
correctly, when you started, writing the trace based tests, was it,
Your initial process was, basically converting the initial integration
tests into the trace based test. So you already had, you didn't have to,
worry about coming up with, the tests. you, it was essentially a translation and
then you did not just checking for the response, but additional stuff basically. Exactly. One difference on this approach is
that first I started with the language that we all love that is YAML. So I did a copy and paste on the test. But when you see traces, you need
to think a little bit of what types of traces this API calls does. what I did was first write a MO
test, run a little bit, and then I swap it to Tracetest ui because
there we can see, how is the shape of the traces that we generating? And I could play a little bit, see,
oh, I saw that the checkout service emit this, the trace that I can assert. The shipping service and meet
another trace, another spam, sorry. And I could tweak a little
bit and start building more complex tasks with that same. Oh, I want to test the service
A and see if the service B D and E are working as well. And I think that's a really,
that's a really interesting part of telemetry in general, right? And producing traces and having all of the
services instrumented, because for someone that is not familiar with the system, they
can, it's easier to look at a trace and understand the process and the steps that
are taken for a specific use case, instead of going line by line, looking at the code
and trying to understand what is going on, yeah. And how long did it take to, to create,
like, all the trace based tests, the initial set for the, for the OTEL demo? Because I think it was, the
announcement was made, I want to say, last, KubeCon North America in
Chicago, last fall kind of thing? is that correct? Correct me if I'm wrong, please. Yes, it was fast. I believe that, also to that we
discussed it with our team about what was happening and checking,
inspecting the integration codes. We were able to, in two or three days,
to build all the tests for each one of the services and start discussing
with the team, opening a PR and start discussing with the team, changes
and other things that we could do. Awesome. That's so cool. And, so once, once you implemented,
in implementing the, trace based testing into the OTEL demo, what
were, some of the big challenges, the gotchas, the unexpected things,
that you encountered as part of this? The first thing that, that we noticed that
we thought is how we could do this test without impacting the entire ecosystem. And the first thing decision
that we took is, we know that, open this demo uses Jaeger. So instead of, we will see
the system outside of it. We will just check Jaeger and do
every other operation on Jaeger. With that, it was pretty
easy to do everything. The only thing that besides that
is just to understand the services, understand how they are working to,
make our tests, it's generated some interesting things like, one service that
I noticed that, first I thought that, the JSON that we sent for the service was in camel case and later we discovered
during the execution of this case that this YAML, this JSON was in a snake case. So we started to tweak a little
bit and start seeing how the things are and do proper tests for it. When you were writing the trace based
tests, you, said you were looking, you're looking at your, your, you were
using Jaeger, as part of your basis. Because I know, trace tests, I
guess there's a couple of approaches to, to pulling the traces, right? One is either you pull
it like in the collector. So you add a config to the collector,
or you can pull it directly from any of the supported observability backends. So what was the approach? So I guess my question is, was, it the,
approach that you took then was pulling it directly from Jaeger, like the traces? Yes, and to that, one thing that we
noticed is that, since, since the example, sent all the, all telemetry data to
Jaeger, Prometheus, and everything else, we were secure to use Jaeger as it is. Because we know that sometimes if
you have a huge system, you might use sample, for instance, to just
send a small portion of the tests of the traces for a tracing back. It was not the case. So this was important because we know
that, oh, If you have sampling or you have some specific configuration on the
collector, maybe you want to do a specific configuration on OTEL collector to send
some of the just traces for trace test to do the things, but it was easier. The job was pretty, pretty
easy that I thought. Since we had everything we ever needed. yeah, that's an important
distinction, too. Yeah, because I hadn't even thought
of the fact that if you're pulling directly from the backend, you're
basically pulling the traces that were emitted there versus if you're using the
collector, if I recall correctly, you create a different, you create basically
a second tracing pipeline, which then intercepts the traces, and then you
use those to create your trace based tests, and then you can put whatever
restrictions you want on that, for, your trace based test, which I guess gives
you a little more freedom as well, like to, play around and configure things. Exactly. Cool. That's awesome. And then, on a similar vein, what
are some of the benefits that you started seeing, after the integration
was like with trace based testing? Did they just start receiving high
praise from the  maintainers in the community demo where they're like,
Oh my God, this has changed my life. One of the game changer things that
I think it was, when I, when we saw the OpenTelemetry demo, maintainers
starting to integrate trace tests on the, their CICD pipeline, because this,
this was, this is something difficult. And I remember at the time that,
discussing with them, every time that they needed to change something,
they did a bunch of final testing. And since we are humans. Sometimes we might forget testing some
service or thinking about a user case. But, what they did was, oh,
we will create a pipeline. We will build the entire system
to see if everything is right. And after building the system,
we will run trace tests and check if Everything was right. And by doing that, they started to
validate some PRs and discover, for instance, that, oh, this PR updated a
component that is breaking, some traces. And with that, they could start
to evaluate and say, oh, Okay, let's let us fix this PR and
guarantee that everything is right. And this was painful before because
sometimes you could approve a PR, merge it on the database, on the
code base, and just two weeks later discover that something was missing. Also want to call out the shout
out that we got from Josh Lee. So I remember that when I first
joined Tracetest, I saw one of, one of his talks about Trace
based tests, actually, something similar or, quite what we're doing. And and just having someone
like him sharing out Tracetest or what it is and what it means
for the OpenTelemetry community. It's just great. So I think that's part of
what we, the work that we. Daniel has done on the OpenTelemetry demo. That's so great. That's very cool to hear. And, now that the, now that, the trace
based testing has been integrated in the demo for several months, at this
point, what, what changes have you seen since that initial integration,
even to, to how you approach trade? Have there been any massive changes as
to how you approach trace based testing? Or is it mostly stayed the same? there have there been tweaks that
you've had to make along the way? The one thing that was great is that
they started to build some traceability tests, as they, I remember that I
talked with Juliano, that is one of the maintainers, and when this Kafka
thing happened, he told me, Daniel, We noticed that the Kafka SDK changed
and we wanted to create a basic, to do some changes on the system and create
a basic, a traceability test in it. And it was amazing. And another thing that, that we love it. It was that, before we had three types
of tests running on OpenTelemetry demo, a front end test, using, I
forgot the name of the library. Typress. Cypress. Cypress, they had an API call, API
test with AVA and they had trace test and they noted, Oh, we don't
need AVA and Cypress anymore. since we are focusing on seeing traces
and guaranteeing that the telemetry is right and the system is working. Three steps is enough for that. And it was amazing and a huge
responsibility for us because now we know that, they rely, they rely on us. We need to have a good API to everything. That's so cool. That's such a success. And, I love the fact, the great thing
about the OTEL community demo too, is that it showcases OpenTelemetry all with
open source tooling, including Tracetest, which I think is so cool and really
speaks to the, to the power of, open source and the open source community. And you end up with this like really
nice symbiotic relationship too, right? Because then, you get some more, I would
assume you would get some more use cases, for improving Tracetest as a whole. Based on how you see trace based
testing, acting in the wild through the community demo. During the time that we started to
write tests for OpenTelemetry demo, we detected that, some of the tests
were huge because we needed to embed a protobuffer file inside of each test. And when we started to see that, we
noticed that, oh, the developer experience is bad for that because You cannot see
what is happening and this moved us to change the CLI and think, let us
simplify the test to guarantee that you can see the test and see what matters. And it was good. It was a two way road. We were able to help them. The OpenTelemetry team, but the
feedback that they gave us helped us to improve Tracetest too. That's awesome. And as you mentioned, you've
got a few folks now writing their own trace based tests. Have you felt then that, like just getting
into that mindset of people writing like other developers writing trace based
tests, has that, have you noticed, was, that a major shift or was it organic
once they saw the initial examples, that were, that you both added to the repo? Believe that, that both things happened. For some, for some, some developers
that were used to OpenTelemetry, they, noted that they could use this,
telemetry to test it, and it was. Sometimes it's way easier to test. For instance, I cannot think in an easy
way to test a Kafka consumer without doing a bunch of code magic behind the
scenes and traces are good for that. So we had, some examples of people using
serverless knowing that is difficult to communicate with several components
and using trace test to help them. And we saw another developer
saying, Oh, we are you, we are starting to implement OpenTelemetry. We noticed that, with OpenTelemetry,
we can test our system quickly. Tristess helped them to drive and
implement more things in OpenTelemetry and start doing things there. I believe that, these two cases happened. Oh, that's so great. Final question. If you had a redo, would you change
anything about how you integrated trace based testing with the OTEL demo? First glance, I believe that
nothing because, because it, I believe it was a perfect match. So we could do everything
that we needed there. the only thing. The only thing that I think that I could
do, and I think that I might do, if you are watching me, Pierre, Juliano,
and company, I will haunt you in the future for that, is to add more tasks,
and start thinking in more interesting use cases that we can do, and thinking
more telemetry that we can show that. Amazing. This is great. We do have a question from the audience. Daniel asked, one of the biggest pains
for distributed systems is ensuring correct context propagation across
service boundaries, especially when async operations require in service
context propagation across threads and context may instrumented properly. Can trace tests help identify where
context is being broken when it shouldn't? I think I can answer that question. First of all, I think
we have all been there. We have all feel the pain
of why is my trace not being propagated to this, backend system
or this part of, of the app. And yes, actually, a great thing that,
or a good thing that we are, one, one kind of, standard or thing that
we're pushing is TDD, but in this case, Trace Based Driven Development. Where users can create assertions
and test specs based on what they would expect the trace to look like. So if you already know that after
a queuing system, there should be a worker that would process that
message, you can pretty much, from the beginning, from the get go,
create a definition that would match. I would expect that span to, to, exist. So if that span doesn't exist, it's
because the context propagation is pretty much not, didn't work or the span,
that's why the span doesn't exist, right? It's not there. So with this kind of technique that
you can use, you can, validate that the expected spans should be there and
help you with the problem of the, your context propagation problem as well. Awesome. So you've answered Dan's question. Thank you. And then there was a follow up question,
can Tracetests make assertions on baggage? It depends. If you are saying baggage, so
for some specific metadata of the OpenTelemetry, perhaps not. But, what we can do today is that,
if you write custom attributes in your span, you define a bunch
of attributes, you can test them. You can test them. Also, we are, We are every time looking
to the OpenTelemetry specification, seeing if there is more metadata
that we should integrate to, to the API and doing it like error codes,
span statuses, and everything else. I think we have something
about span links, right? I want to do as well. I remember. Exactly. Nice. That's awesome. Does anyone else, who's listening
have any, additional questions? This has been really great. Thank you both Daniel and
Oscar for, for joining today. This has been really awesome. I think it's, really cool. I'm a big fan of the OTEL demo and I think
having trace based testing integrated really, it's like a very tracing native
approach to, to integration tests. I'm a huge fan, so it's super cool to,
to see that integration in place and to see other folks, outside of both of
you actually writing trace based tests. Thank you. Thank you, everyone. And thank you, Adriana, for putting
this together and for having us. It was, great.

