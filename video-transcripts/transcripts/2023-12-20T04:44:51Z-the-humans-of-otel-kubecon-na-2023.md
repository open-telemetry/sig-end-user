# The Humans of OTel - KubeCon NA 2023

Published on 2023-12-20T04:44:51Z

## Description

We caught up with some of the contributors, maintainers, and practitioners of OpenTelemetry at the OpenTelemetry Observatory ...

URL: https://www.youtube.com/watch?v=coPrhP_7lVU

## Summary

In this YouTube video, a group of OpenTelemetry contributors and maintainers, including Tyler Yahn, Amy Tobey, Carter Socha, and others, discuss the evolution and significance of Observability in software systems. The conversation covers the integration of logs, metrics, and traces as essential components of Observability, emphasizing the importance of having these signals connected to provide valuable insights during troubleshooting and system monitoring. The participants share their personal definitions of Observability, which range from understanding application behavior to being able to address issues swiftly in production environments. They also highlight the collaborative nature of the OpenTelemetry project, its journey from various predecessor projects, and the community's efforts to create a vendor-neutral standard for telemetry data. Throughout the discussion, the group expresses a strong preference for traces as the most effective telemetry signal, citing their depth and usefulness in operational contexts.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions of speakers and their roles in OpenTelemetry  
00:02:30 Discussion about the OTel CLI tool and its features  
00:04:00 Overview of the importance of Observability in software systems  
00:06:30 Different definitions of Observability from various speakers  
00:10:00 The evolution of Observability and the integration of metrics, logs, and traces  
00:13:45 The significance of having unified telemetry data for better analysis  
00:17:00 Speakers share personal experiences that led them to OpenTelemetry  
00:20:30 The community aspect of OpenTelemetry and its impact on the Observability landscape  
00:25:00 Favorite telemetry signals and why traces are favored by many  
00:28:00 Closing thoughts on the future of OpenTelemetry and Observability  

Feel free to ask for more details or specific moments!

# OpenTelemetry Community Discussion

**Participants:**
- Tyler Yahn, Maintainer for OpenTelemetry Go SIG
- Amy Tobey, Senior Principal Engineer at Equinix
- Carter Socha, Product Manager and Maintainer of OpenTelemetry Demo
- Bogdan, Former Maintainer of Java and Collector
- Constance Caramanolis, Contributor to OpenTelemetry Collector
- Juraci, Software Engineer and Collector Developer
- Jacob Aronoff, Maintainer for OpenTelemetry Operator
- Alex, Contributor and Maintainer of OpenTelemetry
- Purvi, Senior Software Engineer

---

## Introductions

**Tyler:** I'm Tyler Yahn, a maintainer for the OpenTelemetry Go SIG. We're working on some auto-instrumentation and specification.

**Amy:** I'm Amy Tobey, a senior principal engineer for digital interconnection at Equinix. I maintain a tool called OTel CLI.

**Carter:** Hi, I'm Carter Socha. I work on a couple of different things. I'm one of the few product managers floating around, but I helped start the OpenTelemetry Demo, which I'm a maintainer of. I also work in the SIG security to help improve the project's security response process.

**Bogdan:** My name is Bogdan. I took a break for parental leave, so I'm just jumping back in. I’ve done a lot of things, including being a member of the TC and GC, and I was a maintainer of the Collector.

**Constance:** Hi, I’m Constance Caramanolis. I’m one of the OG contributors to OpenTelemetry. I worked on the OpenTelemetry Collector and contributed to the configuration aspects.

**Juraci:** My name is Juraci. I'm a software engineer and have been working with OpenTelemetry or Observability for a few years now. I was a maintainer on Jaeger and part of OpenTracing.

**Jacob:** I’m Jacob Aronoff, a maintainer for the OpenTelemetry Operator project.

**Alex:** Hi, I'm Alex, a contributor and maintainer in OpenTelemetry. I even wrote a book about it.

**Purvi:** Hey, my name is Purvi. I am a senior software engineer and have worked a lot with browsers and JavaScript.

---

## Observability Discussion

**Purvi:** So, what does Observability mean to you?

**Carter:** To me, Observability means that when you wake up at 2:00 AM to fix a problem, you can resolve it. Ideally, you can revisit that code the next day and find a way to prevent the issue from occurring again.

**Bogdan:** I think Observability is the capability of monitoring your production environment and determining when something goes wrong.

**Alex:** I view it as a tool to ensure things are working as intended. It's about gaining insight into both black and white boxes.

**Constance:** I like to think of it as a murder mystery. You see clues and have many questions, and you use Observability to figure out what's going on.

**Juraci:** It allows us to understand problems in our systems without needing to know what's going wrong ahead of time. Observability is a spectrum; we won't achieve perfect Observability from day one, but we should have some telemetry to help us understand our systems.

**Amy:** Observability means understanding what's happening inside your applications, particularly in the code that matters to you.

**Jacob:** For me, Observability is essential. When something goes wrong, I can ask questions about my system and figure out what happened without needing to know exactly what to expect.

---

## OpenTelemetry Insights

**Tyler:** When did you all get involved with OpenTelemetry?

**Amy:** I got involved in 2019. I was brought in to instrument the entire stack for the Equinix Metal product.

**Carter:** I was introduced to OpenTelemetry through my org at Microsoft, which was already doing a lot in that space.

**Constance:** I was part of the early days when we were working on the incubation process.

**Jacob:** I got involved through working at Honeycomb, focusing on OpenTelemetry JavaScript, particularly on the browser side.

---

## Perspectives on OpenTelemetry

**Alex:** OpenTelemetry is about collaboration across the Observability space. It provides a vendor-neutral way to instrument systems.

**Carter:** It makes my life easier by integrating with both open-source and proprietary components, allowing me to see traces across all products I use.

**Amy:** OpenTelemetry is a collection of standards that brings together various telemetry signals like metrics, logs, and traces.

**Juraci:** OpenTelemetry is a set of tools that helps extract telemetry data out of applications, gradually leading to better understanding of the systems.

**Constance:** It's a wonderful community that helps make Observability better by working across vendor boundaries.

---

## Favorite Telemetry Signals

**Purvi:** What is your favorite telemetry signal?

**Jacob:** I’d probably say traces, as they provide a deeper understanding of operational behavior.

**Amy:** Traces are definitely my favorite too; they give you context.

**Carter:** Traces are the cooler version of logs. They give you more depth.

**Juraci:** I love traces. They allow you to quickly identify issues without overthinking.

**Constance:** Traces number one! They are elegant and useful.

**Alex:** Traces are magic because they correlate metrics and logs with context.

---

In summary, this engaging discussion among various contributors and maintainers of OpenTelemetry reflects their shared passion for improving Observability and making it accessible and useful across different environments and applications. Their varied experiences and insights highlight the importance of community collaboration in advancing the field of Observability.

## Raw YouTube Transcript

I'm Tyler Yahn. I am a maintainer for the OpenTelemetry Go SIG. We're working on some auto-instrumentation there, and specification. I'm Amy Tobey. I am senior principal engineer for digital interconnection at Equinix. I maintain a tool called OTel CLI . - Oh, you maintain the OTel CLI!
- Yeah, that's my project. Yeah. So that mostly just has Traces right now. And I've been meaning to implement Logs and Metrics for a while and I think like Logs just went GA recently, so it's time to do it. But Traces have been so effective and people really like it that I haven't really had a lot of demand for them. Is the OTel CLI part of OpenTelemetry? It's not yet. I maintain it on our Equinix Labs GitHub account. It's not a lot of process. Mostly it's just me with a few folks like Alex and others that throw me a PR every now and then. But I've thought about bringing it back to the community. But I'd have to maybe be not as so far away from the standards as I am right now because doing it in the command line, a lot of the standards don't really translate very well. So I've strayed a little bit away from the standards in a few places. It would make sense. And I've talked to Austin about it. Hey, I got Ted Young with me! Hello! I'm Carter Socha I work on a couple different things. I'm one of the few product managers floating around, but I helped start the OpenTelemetry Demo, which I'm a maintainer of. I also work in the SIG security, which helps the project improve their security response process. My name is Bogdan. I took a break for parental leave so I'm just jumping back. Okay, what were you doing before? I done a lot of things, including member of TC, member of GC, maintainer of Collector. I was a former maintainer of Java, so I've done a lot. Hi. I'm Constance Caramanolis. I know that you were involved in OpenTelemetry and you are one of the OG contributors. Tell us about that involvement. Yeah, so I worked on the OpenTelemetry Collector. I contributed to that. I did a lot of config things. I was also on the OpenTelemetry Governance Committee. So I did a lot of the start, we were doing the incubation process, starting a whole gathering process, a POC, a lot of putting processes in place, getting adoption. Quite a few talks. KubeCon talks... My name is Juraci. I'm a software engineer and I've been working with OpenTelemetry systems or Observability for a few years now. I come from a Tracing background, so I was a maintainer on Jaeger. I was part of OpenTracing back in the day and I helped choose the name of the project that we have. And right now I'm a Collector developer. I help out on some components for OpenTelemetry Collector. And I'm also part of the Governing Committee for OpenTelemetry. And newly re-elected, right? I was just re-elected, yes. My name is Jacob Aronoff. I am a maintainer for the OpenTelemetry Operator project. Hi, I'm Alex and I'm a contributor and maintainer in OpenTelemetry Wrote a book about OpenTelemetry. I don't know what else. I do stuff with OTel. Cool. I am a contributor and maintainer of the OpenTelemetry Collector and the OpenTelemetry Collector Contrib repo and I have been spending a lot of time in various SIGs and specialty working groups around configuration and security. And previously I spent a bunch of time maintaining and contributing to Python. Hey, my name is Purvi. I am a senior software engineer. I worked over my career a lot with browsers and javascript. First question. We're here talking about Observability. So what does Observability mean to you? Yeah, that's a great question. Personally, I think Observability means that when you woke up at 02:00 a.m. To go fix a problem, you can fix it. And ideally, the next day you're able to look at that code again and find out a way to never have that problem exist. I think that's really what it means to me. It means being able to look at things coming out of the box and tell what's going on inside parts. Be very convenient. I like that. First of all, it's monitoring... But really, Observability is this nebulous term, but it did show up as part of a sort of shift in how we are thinking about monitoring our system. And I would say that shift is the way we used to do it was you had these different signals, you needed logs, so you had a logging system, you needed metrics, you made a metric system, you needed tracing, but you didn't know what that was, so you didn't do it. And instead of having these three separate, totally siloed systems, what we've been doing over the past couple of years, especially in the OpenTelemetry project, is trying to say it's really bad for these three things to be separate. Or the four things, if you include profiling. When you're using these tools, you use them together, you're moving back and forth between them, right? Like you get an alert based off of a metric that you set up. But when that alert goes off because errors or something spiked, the next thing you want, is to look at the logs that are in the transactions that are causing these alerts. You want to look at the logs that are in a particular transaction. You really want to have a trace ID stapled to all those logs, so you can actually look them up. So we want to actually use all these tools together. And in order to use all of these tools together, you need to have the data coming in, the telemetry actually be integrated, so you can't have three separate streams of telemetry. And then on the back-end, be like, I want to cross-reference. All of that telemetry has to be organized into an actual graph. You need a graphical data structure that all these individual signals are a part of. For me, that is what modern Observability is all about. It's about having all this data connected into a graph in such a way that we can leverage the machine to do what they're good at, to reduce the amount of time we need to spend investigating issues. Instead of being like, I wonder if this is the problem. Therefore I am going to collect all the logs and grep through them, try to whittle it down to something. I'm going to look at all the config files myself, try to figure out what's going on. You can just quickly get an answer to a lot of those questions and then move on to the next hypothesis. The amount of time you save with modern Observability, I think, changes how we actually practice, and that's an ongoing trend. But with OpenTelemetry going, effectively going GA this year, with tracing, metrics and logs now stable, yes, finally, only like two years late anyway. But the fact that we have that now, the fact that we now have telemetry that has all of these correlations baked into it, you're going to start seeing a new wave of analysis tools, all the existing ones out there, but also new ones being built, that leverage the fact that this data is available and that it's like a standard data format, kind of proprietary data format, stable data format. You can rely on it. So it's like okay to build your giant platform on top of this data or build some kind of like boutique analysis tool that just does one thing and does it really well. That's where I see it all going. And that's what Oobservability means to me. What does Observability mean to me... It means like, an application owner can see what's going on in their environment, and answer pertinent questions to them about their business and how they can improve their service. Observability is an overloaded term in our days, but it means the capability of monitoring and determining when something goes wrong in your production environment. Observability means...what does it mean to me? I use it as a tool to kind of making sure that things are working the way you want. It's getting insight into black boxes or even white boxes. I view it more as you kind of see things, but you have a lot more questions from it, and then you use Observability to actually figure out what's going on. So I like to call it murder mystery, usually. I like that. Yeah, I want to use that on a slide. You should. That's a good question. I think... not going to be strict on a definition, I think what this really means is it is a way for us to understand what a problem...we have a problem in our system...we should be able to answer or to determine what is going wrong or what's happening. And it doesn't matter if it comes from logs or metrics or training, as long as we can tell and understand what's going on. I think that's when we can say we have Observability. And it's not a yes or no. It is a spectrum. I don't expect to have Observability, perfect Observability from day one, but I am expected to have some sort of telemetry that helps me understand what's going on. So I think telemetry is like a path to getting perhaps utopic place where we understand everything about our systems. What does Observability mean to me... I think Observability is understanding what's happening inside of your applications. Maybe what's happening in the code you care about. Yeah. Oh my goodness. It means everything. Observability is life. I think Observability means that when something goes wrong, I can ask a question about my system and get a sense of what is happening without having to know ahead of time what to expect. Like I can just go and dig into my data and my services are instrumented well enough. Not like not perfectly, but well enough that I can just figure out what happened. And can I reproduce this thing that happened in probably production off in my own environment so that I can improve my code to manage it better next time. I like what you said about not instrumented perfectly. There is no such thing as perfect instrumentation. That's a lie. Just like there's no such thing as done code, right? That's also a lie. Or that the network will never break. That's a lie. Oh, that's such a good question. To me, Observability it's really about being able to get curious with your data and be able to have a lot more confidence about your production system. So being able to kind of squash things before they arrive. Testing in production is the best way to test your system because no matter what people say, Prod is always its own different animal. And if you have really good Observability, you can test in Prod. It's a much better experience for your users and for your developers too. Absolutely. When did you get involved with OpenTelemetry? I got involved in 2019, I think. Oh, so like early? Early, yeah, I was not at the original meeting, but yeah, I got in really early. I really love writing Go, and so that's where I started. But I was pretty quick into the specification and started working in that space and I think it was just coming from the pain point of using have to run systems. And being that person who has woke up at 2:00am. I wanted a better software solution for this and I think that I saw the value in it and I jumped in. We work in pain and trauma, right? Yeah, exactly. When I was hired into Equinix, they hired me to instrument their entire stack for the Equinix Metal product. So that's what I worked on for my first year. This was like three years ago, before all the fancy auto-instrumentation stuff was complete, adding instrumentation to all of our systems. So you are an OG user of OpenTelemetry. A little bit. The team I was working on at Microsoft, at least my org at least, was already doing a lot in the OpenTelemetry space, and that seemed to be where all the cool things were happening. And so that kind of got my interest. And then I got switched to working with a development team that was focused solely on OpenTelemetry, both for external purposes and internal purposes, because Microsoft uses OpenTelemetry really heavily internally. And so that's what got me introduced. And when I started looking around, wondering where I could start, I realized there was no real good example of how to use OpenTelemetry in the wild. And so that was a problem that I thought every vendor might have. And something we could solve together as a community, and we have. Cool. How long have you been working on OpenTelemetry? Since the beginning. So like 2019 or like, pre? Even pre. Did you start out with Ted in the...pre days? No. Actually, there were two competing projects that merged into OpenTelemetry. Right. So I was on the other project. Which one, OpenCensus? Yeah, I got involved with OpenTelemetry through working at Honeycomb. So I got involved with it, and I have a particular interest in OpenTelemetry JavaScript, and especially the browser side of OpenTelemetry JavaScript. It's really great to be involved with it. What's your definition of OpenTelemetry? I think OpenTelemetry is, I mean, it's a standard, I think it's a collaboration across the entire Observability space. And it is, I think, a path forward for all of instrumentation. The idea that you don't have any vendor lock-in, the idea that you can just take one code base and always have some way to look into a system, I think the future of how we're going to make software better in the long term. OpenTelemetry makes my life easier, because I can integrate it with open source components that I'm using, or proprietary components. And at the end of the day, all of the OpenTelemetry flows through to my Observability vendor, and I can see traces across all of my products that I use in one space. It is my project...of soul. I think OpenTelemetry gets really biased, but I feel like it's a really good combination of a lot of different views finally coming together, actually making the previously hard advancements easier, like gathering the data. The hard part is actually making sense out of it. And so they're finally coming together. It's worked out pretty well. in terms of collaboration to get metrics, traces, and logs. Oh, that's a deep question... Yeah, it is. On a technical side, it means OpenTelemetry for me is a set of tools that would help me get telemetry data out of my typical application. Sometimes also infra. But OpenTelemetry really is the tool that I can use in a vendor neutral way, get data out of my application so that I can get into that into that uptopic thing. If I had perfect instrumentation, then I can get into a uptopic place. But OpenTelemetry provides me the tools that I need to gradually get into that. Now, it does stop at a very specific place, in a sense, which is as soon as you send data out, that's where OpenTelemetry stops. That's where you get to the vendor or to the open source tools that provide the database, visualization tools, and so on. But a more deeper aspect, OpenTelemetry is where I have my colleagues, people that I work on a daily basis for a few years. Yeah. That's what OpenTelemetry is for me. What does it mean? What's the concept? OpenTelemetry is Observability backed by everybody. It's not a single vendor. It's letting you do the thing that is agnostic to where you send the data. In the same way that you don't have to relearn how to drive a car every time you step into a new car. You don't have to learn how to ride a bike based on the vendor of the bike that you buy from. You should be able to instrument your code no matter where you send that data. So that's how I sell it. That's how I think about it. Awesome. The other benefit is we as the maintainers, we have a lot of our maintainers here and approvers here, so we can collaborate and work together to figure out what's really needed in the next coming months. I described it almost like summer camp. There are some people where, oh, I haven't seen you in a few months. How you been? It's catching up. Like, I mean, OTel has been amazing. The project itself has been wonderful. It's one of the first projects to take a bunch of standards and condense them down into less standards. We took OpenCensus, OpenTracing, we brought Prometheus to the table. The Elastic Cache format is there. OpenTelemetry just is a wonderful community, that's all. Trying to make things better in the Observability landscape by working across vendor boundaries, which has just been something that I've never done in the past. I've never worked in an open source project where so many vendors are involved and so many end user communities are involved, and it's been great. Yeah. And that's what I like personally about OpenTelemetry, because everyone plays nice and I feel like it's a very deliberate, "No, we are not going to favor one vendor over another." And if a vendor tried to showboat, then it's pretty much shut down, which I think is great. We've just had a lot of really good folks at all the levels of the project trying to push everybody in the right direction, which I really appreciate. I'm going to give a shout out to Ted Young for, especially being one of those people that always just, he's over there somewhere. I can see him just like looking around, see, waving his head. He has no idea we're talking about him. OpenTelemetry to me is really all about the community. Like communities being able to take ownership of their own telemetry data, because vendors should not be determining the type of telemetry data that gets sent to your systems. Because Observability about your system is so personal to your system. And when you have vendor lock in or lock in through, like, the instrumentation of vendors, it can be very limiting. What is your favorite telemetry signal? That's a good question. I wish I had a good, nuanced answer there. Like, I don't know...metrics, I've known for the longest, I guess. But I think traces are probably a little closer because you get a lot more depth into operational behavior. So, yeah, I think I'd probably go with traces. It's also a little bit more automatic for you. You really have to understand what those metrics are and build them into something. Versus tracing, can show you based on just the structures they come with. So, yeah, I'll go traces. Oh, it's traces, of course. My favorite signal... Probably be the Bat Signal. If that thing could go on every time a system goes down, that would be. So I think I've heard this reference around...and I truly believe it. Traces are just the cooler version of logs. Like, it's like logs with a mustache, and maybe a top hat. Because essentially a span is just a log, but a trace-correlated log. So I'd probably say traces, but my backup answer is log. Signal? I think the most... I like metrics. I think we did try to change the way how metrics were done before, and we may not have been the most successful yet, but we are getting there. But it was a necessary change, and I feel like it changed something in the way how things were done. For tracing, I mean, we didn't change too much from other Dapr paper or other things, but for metrics, I think we changed. I love traces, especially because  you could... My favorite example is when I used to do...when I was at Lyft and I would get paged in the middle of the night... One service, four deep.. everything was going... Everything between that and the front was getting paged. You were able to actually figure out, like, okay, this one's the cause. Instead of overly thinking about it. That's what I love about it. It's very different paradigm than what we're used to talking about. Trace. Come on. They're beautiful. No, it is. Traces. Traces number one. They are the easiest to work with. They are so simple to get started, and they're just so much more useful than anything else. So traces all the way. Traces, because it's clearly the elegant log, but also you can just get metrics out of it. It has, like, everything you need in a signal. It's metrics and logs correlated with context. It's beautiful. They're magic. Oh, that's easy. It's tracing.

