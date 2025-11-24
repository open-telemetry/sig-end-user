# Humans of OTel: Live from KubeCon NA 2025!

Published on 2025-11-13T08:33:00Z

## Description

Streaming live from Atlanta, Georgia at KubeCon NA 2025 -- We are pleased to be speaking with Jacob Aronoff and Diana Todea!

URL: https://www.youtube.com/watch?v=NzbDui8hDdo

## Summary

In this live segment from KubeCon North America 2025, hosts Reese and Sophia discuss various topics related to open telemetry with their guest, Jacob Marino, a maintainer in the open telemetry community. Jacob shares insights from his recent talk on introductory concepts of open telemetry and Kubernetes, highlighting the surprising engagement from the audience, with a wide range of questions from beginners to experienced users. The conversation also touches on the collaborative efforts in the open telemetry community, including the introduction of a new auto-instrumentation project using the Zig programming language, and the importance of user feedback for improving documentation and functionality. The hosts also welcome Diana, a developer experience engineer and recent Open Source Community Star award winner, who discusses her contributions to localization efforts within the open telemetry community, emphasizing the challenges and motivations in translating technical documentation for various languages. The session concludes with a focus on the community's commitment to improving user experiences and engagement through better practices and collaborative efforts.

## Chapters

00:00:00 Welcome and intro
00:01:00 Guest introduction: Jacob
00:02:40 Jacob's talk experience
00:04:50 Audience Q&A insights
00:06:00 Community feedback challenges
00:08:40 Discussion on the injector project
00:10:50 Stability and project maturity
00:12:00 Graduation criteria explanation
00:14:50 Importance of documentation
00:27:20 Guest introduction: Diana
00:30:01 Localization efforts and challenges

**Reese:** Just the light. Oh, action. 

**Sophia:** Oh, you did. You did. 

**Reese:** Hello everybody. If you've been waiting around, we are so sorry for the delay, but we are very excited to be coming to you live from Atlanta, Georgia. But pretty much everybody was very surprised by a cold front that had us looking at 40°, which I think is 3°C, the past couple days. Luckily, it's warming back up, so thank goodness. But yeah, we are coming to you live from CubeCon North America 2025. I'm Reese and I am joined here by my co-host Sophia. 

**Sophia:** Hi. 

**Reese:** And our first guest, Jacob. 

[00:01:00] **Jacob:** Hello, my name is Jacob Marino. I'm a maintainer for, let's see, OpenTelemetry operator, OpenTelemetry Helm charts, hotel injector, and I maintain a few random collection things and I contribute to OpAmp and, and I'm missing one. [laughter] I was wondering who had a hands for all 10 honestly. 

**Reese:** If Josh Sar were here, he's everywhere. 

**Jacob:** That's every single group. 

**Sophia:** That's wild and awesome at the same time. 

**Jacob:** No, it was very impressive talking with him. Learned so much. 

**Reese:** So, how I feel talking to you all? Um, now Jacob, you did a talk or was it two talks? 

**Jacob:** Uh, one talk. So I gave a talk about two hours ago, three hours ago. 

**Reese:** Cool. 

**Jacob:** Very fresh. 

**Sophia:** It was packed. 

**Jacob:** It was like I was worried that—I've given this is my second time giving a talk. First talk that I gave was in Chicago two years ago. 

**Reese:** Oh, nice. 

[00:02:40] **Jacob:** And the room we got a very low slot, like it was like towards the end of the day on Thursday, I think. So it was a tough tougher day to give a talk. We had a solid audience, and for this one I was worried that with the content we were doing, which is like introductory to hotel and Kubernetes, I always worry with these introduction ones, you know, it's like is this going to be enough, is it going to be too much? So my fear is that nobody shows up and I'm speaking to an empty room. This was the reverse where it was a full room and people were standing in the room and then people got turned away from that door. 

**Sophia:** Oh my gosh. 

**Jacob:** Which I was happily surprised by. Then [laughter] I also like we only reserved five minutes for questions at the end because I was like, you know, I don't know what questions people will have. Usually people aren't asking a ton of questions like after they'll come up to you later, but it's like usually like a Q&A session does not last very long. So oh five minutes for questions, like that's fine. We do questions; there's a line of like 15 people waiting to ask questions. Like they just kept growing and growing. We stayed after for another 30 minutes just answering questions. 

**Reese:** Interesting. What level of questions? Like was it more, um, you know, people who are newer to the topic or who are asking like more like stage two kind of questions? 

**Jacob:** Huge range. So we had some people who were, you know, very introductory level, just like I'm getting my bearings here. How does this part of it work? You know, what's the deal with Prometheus and hotel and what do you use for a backend? You know, that's like a solid starter question. And then other people came in they were, "I've been using this chart for the past year and there's this one thing that I want to be able to do and when are you going to like do the work to like enable that and how can we like architect this?" Big range. 

**Sophia:** Very big and each one was like a different part of the area. 

**Jacob:** Okay, that's so cool. 

**Reese:** Yeah, very, very cool and very surprising. I'm always happy to because, you know, I think as a maintainer it's like we get people who come to us with [laughter] issues on GitHub and it's like you'll get someone complaining on a GitHub issue or like, "Hey, this thing broke. The most recent release broke me, um, you know, what are we doing about that?" 

**Sophia:** Broke! [laughter] 

**Jacob:** But no one's broke their spirit. You know, I've had releases break my spirit. 

**Sophia:** [laughter] 

[00:04:50] **Jacob:** But the real thing is we don't get positive feedback. We don't get a lot of questions because realistically most people are asking track or going on Stack Overflow, right? It's like they're not bringing the questions to us. So we don't really hear or understand what usage is. I mean, it's kind of the benefit [laughter] and the curse of open source is that like we don't necessarily get that user feedback directly. It's why like I love what you all do because getting the user feedback is one of the most valuable things to the community. Like in order for us to push forward, we need to know what isn't working right now where people just don't see the effort. 

**Reese:** Um, we actually—I hosted a meetup in New York last month, two months ago, something like that. 

**Sophia:** Yeah. 

[00:06:00] **Jacob:** And that was eye-opening because it was like wow, people are really using these things and things that I feel like I've talked about so many times are still not known, you know? And it's like I'll mention like how many people know what like the target allocator is in a show of hands and nobody raised their hand in a room of like 40, you know, senior SREs. I'm like, okay, uh, would anybody like it if you could do distributed, sharded, Prometheus scraping? And everybody raises their hand and I'm like, well we have that, like it's done, it's there, you know? You can use it, it's been a thing for a few years. You know, so I guess all to say the community just is still—there are still things for people to learn about the vast ecosystem that we have here. 

**Sophia:** Yeah, I think, you know, I think a common theme just in general is people not being aware of, you know, different abilities and features and yeah on the end you see too, you know, it's a bit of a challenge because like we feel like we're talking about it, um, you know, at our work and like in the Ozone community and then, yeah, like you said, we have all these conscious people who don't know and we're trying to figure out like where are they going for like how can we make them aware of, you know, all these cool things that are happening. 

**Jacob:** Um yeah, so, you know, one of the things we started doing is um the what's the hotel segment, which we just had our first one um a month ago or so. And so we're hoping to, you know, I don't know, have something we can point people to. 

**Reese:** Of course. 

**Sophia:** But you mentioned the injector. 

**Jacob:** I did. Tell us more about please do. So I am the, uh, I'm a maintainer for it but I'm mostly just doing reviewing because this is actually a joint effort between uh Splunk and D-Zero. Both of them have already written their own uh injectors for auto instrumentation. 

**Reese:** Oh, right. 

**Jacob:** And they're essentially donating a merge of both of those projects to the tot alpha version of this for their customers. Um, so we're just testing out that everything is working the way we need to. [clears throat] There's a lot of really random edges here. Um, interestingly enough, this does introduce a new language to hotel, which is exciting, which is it's very rare for us to not use a language in a project that is meant to instrument languages. 

**Sophia:** Right. 

**Jacob:** And we are now using Zig in the project. 

**Sophia:** Zig. 

**Jacob:** Zig um is a fun language that is sort of a merge between like Go, Rust, C++, and C. 

**Reese:** Oh, super fun. [laughter] 

[00:08:40] **Jacob:** But so the real value of it is it doesn't require uh a lot of like core Linux dependencies. So like GCC is one that we really think about a lot. Uh, if you're on AWS, something that I've been bitten by is not all of the nodes have GCC. And so when you're trying to do injection, like say you're trying to run a load balancer like to or Envoy, um, is similarly injected like we inject auto instrumentation and that will just not work. It used to not work. I think they've changed this but it used to not work uh on certain types of AWS nodes. So we have that same issue because we're trying to inject to all these different environments. So, Zig is pre-built with a bunch of these C libraries, but from scratch, part of its standard library and not based on anything existing. So it has all of its own dependencies. So, the benefit of this injector project is that we're going to be able to really meet users where they're at without needing to know a ton about their environment. And that's the real problem today. 

**Sophia:** Yeah. 

**Jacob:** Um, so it's an exciting project. I think we're a few months away from it being alpha beta. Other people are on the release timeline. Ted Young is thinking a lot about the release timeline there. 

**Sophia:** Um, but all TC. 

**Jacob:** TD, that's so cool. 

**Reese:** Yeah. What are the parts of, you know, whether it's something working on or not working on directly that you are excited about? 

[00:10:50] **Jacob:** Good question. I think that the biggest thing for the project right now that everybody cares about is stability, right? I think that uh we're trying to get to the place where users can reliably get, you know, a new update without them needing to do any configuration changes, without needing to worry about uh components being deprecated, things like that, right? I talked to, at that meetup in New York, I talked to a developer at a major bank who was, you know, they've developed all of their own uh custom components for the collector and so every time that we've been doing these reworkings, the collector's architecture, they need to then refactor a bunch of their code as well. And you know, after a few months you lose track of all these updates. So it becomes like a weeks-long project to keep up to date. When you have to do that, their release cycle is every quarter, right? It gets a lot to manage and a lot to update. So for the users, I think what people really want to see is that level of maturity and stability. We can get to that graduated status with the CCF would be huge. That would be massive for the project to have. Uh, I think it would really—I mean our adoption already has been really high. I think that's when we would come to the next level. 

**Sophia:** Great. Can you explain a little bit for those of us like CCS stages like what going from incubated, incubating projects to graduated means? 

**Jacob:** Sure. 

**Sophia:** Yeah. 

**Jacob:** I'm not the best. I can tell you what I know. I'm definitely not the person in charge of this. There are people who are far more confident in the stability part of this governance than I. 

**Sophia:** Yeah. 

**Jacob:** So I will speak on only what I know. 

**Sophia:** That's all we're asking for. [laughter] 

[00:12:00] **Jacob:** So right now we're in, as you said, the project is relatively lenient in terms of its standards. There are standards, but graduation is really strict, I would say for good reason, right? Like you want to be sure that when you are considered a graduated project you have a healthy community, which [laughter] we definitely do. You have stability guarantees, which is the main thing we're working towards, and lastly, adoption. So adoption has to be at a certain amount of companies; you have to have testimonials [laughter] from those companies about how the project's been helpful. That's another thing that we have plenty of. So now it really just comes down to stability and stability. You can think of Kubernetes as the example here. Kubernetes is, you know, the first graduated project. I imagine it's the first one. Maybe there maybe someone beat them to it, but you don't [laughter] know. But essentially, every time that Kubernetes improves their security and reliability, uh, you know, release stability, anything like that, it raises the bar for everybody else to continue to improve. So as we are getting towards stability, Kubernetes is chugging along, you know, really positively and improving their posture constantly. So it's up to us to not only meet where we started for our graduation criteria, but also to continue building towards that. So that means that you're going to see more security features, much more security guarantees, which is going to be very helpful for enterprises. M um, you're going to hear more about quarterly releases rather than uh the sort of disparate release calendar that we have today. Uh, you'll hear more about documentation which is also going to be huge. So uh later when that comes on, I assume that we'll be talking about some mobilization efforts and documentation. 

**Reese:** Ah yes, uh that is super, super valuable, right? 

**Jacob:** Um, all of that is going to get us to that graduation phase. Uh, it's just time, it's time and effort and uh we have a dedicated group of people who want to see this happen and are spending, you know, all of our time at all of these large companies trying to make that happen. Very exciting. 

**Sophia:** Awesome. 

**Reese:** That is very exciting. And if you are yourself an open end user and um your company is using in fashion, um, and you want to share your story, we would love to have your story as part of um our legacy [laughter] our catalog. 

**Jacob:** Yeah. 

**Reese:** Like to help, you know, help graduate the project and help take us out to us. Um, we'll have it in the show notes um after this. But yeah, it's pretty easy. As long as you remember me Slack, you can find us at hotel-dash-dash-and-dash. 

**Jacob:** I think that's all the dashes. 

**Reese:** I thought we were going to dash zero. [laughter] 

**Jacob:** Oh, so we're like dash. 

[00:14:50] **Reese:** And similarly, if anybody wants to help out with documentation, documentation is one of the best ways to contribute to the project. It is so valuable. We had somebody for the operator group contribute a whole uh bit of documentation for the target allocator and it was so well done. Adriana did this as well, super helpful, and it has been such a resource for me to be able to point users that come into our Slack, come into our S meetings to just say, "Hey, you have a question about this? We have a full document to answer everything you might need to know about it." That has been such a way to offer. Um, it's lovely. So, great way to contribute and get started. Doesn't require writing code. Requires asking questions and writing a bunch of stuff down. 

**Sophia:** Yeah. And I can confirm that everyone that I met in the local community has been super helpful. Um, anything you know you can take on and be responsible for, like documentation, that's something that you're taking off their plate. So I know they're having to help you. And it's also cool to see your work on an official website. 

**Jacob:** Yeah. Like, uh, definitely join the communication SIG for that. I'm currently in it and we're working on a lot of refactoring of the documentation, like just like the early stages since I'm more of a beginner with the OpenTelemetry and everything. I've been working on kind of refactoring those beginner level documentations. So like it's been really helpful getting people like acquainted with that and localization efforts too. Like I know Lisa is working on a lot of localization efforts. 

**Reese:** So yeah, it'll help. 

**Jacob:** Super helpful. And the beginner stuff especially. I mean, again from the talk today I think it's just so—it was so useful to learn where people are at in their implementation journeys, right? Uh we do have people that really need reference architectures, a ton of code examples, right? These things help project adoption that also make it so that users actually are delighted by the experience, right? Ultimately, that's what I think we all want to see and that's what users want. Like you want to be able to install hotel wherever you need it and not have to scour the internet to figure out how to make it work, right? Different companies have so many different needs and so getting started is always going to be the most important thing for us to really nail. 

**Sophia:** Uh, the next thing that I heard from, uh, when I did the event in New York is reference architectures and showing how we can do hotel in all of these various environments, so that people can have some code samples to copy from, uh, some architectures to, you know, design around. I was just talking with an engineer at [company name] and they are really interested in understanding how to do various trace sampling architectures, right? Where we can really have like a whole, as you said, catalog these architectures to show people. And we all of our companies, like you know, when I was at [another company name], we had all these architectures internally that we would post blog posts about to share. 

**Jacob:** We have a lot of companies that are using hotel as part of the ingestion path as well, which involves a lot of this architectural work. Similarly, a lot of companies that are contributors to hotel also are obviously using the tooling themselves for their own company's observability. We should reach out to the people who are doing that and try to publish what are the reference architectures that hotel maintainers use ourselves, right? 

**Sophia:** I think that would be really useful for people who are trying to implement this right now. 

**Reese:** Absolutely. 

**Sophia:** And so are we planning to host them like in a repository or like on sites directly? 

**Jacob:** Oh, I think would be the best. I think, you know, we have documentation places, the operator group, and I think the idea of everything being the doc is going to be the way to go. 

**Reese:** Right. 

**Jacob:** Like centralizing it and making sure that it's well organized, which is a lot of the work that you're doing, super valuable. 

**Sophia:** Of course. 

**Jacob:** But I think it just—it needs to be there right now. I think it exists on a few different company blogs, a few different companies— 

**Sophia:** Head scattered. 

**Jacob:** —bringing that together I think would be really, really valuable. 

**Reese:** One reason let's do it. 

**Jacob:** Right? There's so many companies like contributing. So there's definitely a bunch of references that people in our community could use. 

**Sophia:** Yes. 

**Jacob:** Yeah. 

**Reese:** Absolutely. And so many people are, people are so friendly, right? Like back to that, like going to uh the hotel booth. We've had so many people who have never come up to us before and are just asking great questions, and we have so many people who just, you know, we hang out there because we love to talk to people about this. It's rare that you get to have this level of engagement with end users, right? Uh, that direct type of engagement is so valuable and so people coming by has been one of my favorite experiences of it always. I think the reason that I love to come to these is just getting to talk to people, hearing people's problems, digging in because then it helps us plan what I like what I need to do for the next two years, right? I can take that feedback on it. 

**Sophia:** What, um, so in during your time here at CubeCon, like from the audience questions that you had at your talk and people who come through the OpenTelemetry observatory, do you have—are you seeing any like general trends as to like what people are leaning toward or needing more help with? 

**Jacob:** Yeah. So I say the main thing that is of concern to me is around OpAmp, which has been getting a lot of—there are a lot of talks in OpAmp this CubeCon. I don't know if that if we've noticed that there were at least four that mentioned it, which is a lot. 

**Sophia:** Could you explain that a little bit more for us? 

**Jacob:** Nothing. [laughter] Sorry. 

**Sophia:** We're slowing down a little bit. 

**Jacob:** So, OpAmp is the uh Open Agent Management Protocol, uh, part of the hotel project but is also designed to be in the same way that hotel is very vendor-neutral, it's neutral to agents as well. So, it's not just for the collector necessarily to be for a lot of different uh agents out there. The goal of the protocol is to enable things like uh component status reporting, health reporting, and remote configuration. And remote configuration is definitely the top of the town is what I would say. 

**Sophia:** Yeah. Okay. Very cool. 

**Jacob:** Um, and so in that vein, what it sounds like users really want is a way to dynamically update what the collector can do, what the SDKs can do, uh, in real time. And that's challenging. The way that the collector was designed was never really with remote configuration in mind. There are ways to reload the process. Like we can actually go in and restart the process from the collector binary. Like you just do that, right? 

**Sophia:** Yeah. 

**Jacob:** But it's different than a remote. What users really want is a way to push a rule to a collector and the collector accepts it and continues going. 

**Sophia:** Yeah. 

**Jacob:** So that's what a company like Bindplane has already built. Uh, and so what we want to do is take a lot of the lessons from what Bindplane has been successful with and obviously we're working with them as well. They are big contributors to uh, the idea is that we work all together to improve the provider posture here and improve the SDKs as well so that we can actually realize this vision that people can dynamically update their configurations wherever they might be. [laughter] Uh, but it's challenging. I mean that that's like a really tough topic. 

**Sophia:** Yeah. 

**Jacob:** There's a lot of companies in hotel have done this work beyond Bindplane before. Elastic comes to mind. They have their own protocol for doing road configuration already. 

**Sophia:** Okay. Okay. 

**Jacob:** We've talked with a few of their containers and there's definitely some like room for some good collaboration that we've talked about. 

**Sophia:** Awesome. 

**Jacob:** I think it's all to be seen, but this is definitely the thing that we hear a lot about. The thing that I hear a lot about on the operator side is in Kubernetes, how can I do uh, call it not just remote configuration but layered configuration. So what this means is how can I make it so that if I'm running in an enterprise company that I'm in a multi-tenant environment, I want like a base collector. I want to overlay. I want my teams to be able to overlay different pieces of config on top of that collector for their needs. 

**Reese:** Right. 

**Jacob:** It's a really complicated topic. 

**Sophia:** Yeah, it's really— 

**Jacob:** Sounds like it. And the thing that I sort of struggle with is how do we make this extensible and configurable but also simple to understand. The problem with this, that it starts getting into a lot of moving parts, and as soon as you start to introduce more moving parts is when complexity, and usually reliability, both complexity increases and reliability decreases, right? You need consistency and more moving parts, uh, will reduce that. It's sort of that—there's a great quote in reliability that I love. It's u—the most reliable system is the one that does—that never—that you, right? We know this quote. I'm totally botching it right now. [laughter] 

**Sophia:** No, I hear it. I hear it. 

**Jacob:** The idea is that like [laughter] the most reliable system is the one that like doesn't exist, right? 

**Sophia:** Right. 

**Jacob:** Because it's always achieving its goal of non-existing. And so if you want to really improve the reliability of the service, you delete it because then you don't have to care. Then it's at 100% because it's always giving you the same answers, which is nothing. 

**Sophia:** Yeah. [laughter] 

**Jacob:** [laughter] Sorry. 

**Sophia:** No, I'm here for it. I'm here for it. 

**Jacob:** Yeah. 

**Reese:** Someone—I’ll say that to, I don’t know, someone at the Ozone booth and they'll be like, "You totally messed up." 

**Sophia:** You know, [laughter] we'll have the correct throw in the shout out. 

**Reese:** Yeah. Thank you so much, Jacob. Um, we are going to bring on our next guest, Diana, in a moment. Um, and in the meantime, I really want to show off this baseball jersey. 

**Sophia:** Looks really good. 

**Reese:** But, um, our friends at Honeycomb have been kind enough to um, sponsor for the hotel community. Um, thank you, Austin Parker, for the design. Um, I would stand and show the back. It says uh the number 11 ACTUALLY I DON'T KNOW WHY IT SAYS 11 like [laughter] there. But yeah, it says maintainer on the back. Um, we'll have some pictures hopefully to show you. But yeah, you've got the logo over here and it says open too across the front. Very, very snazzy, very sharp. [laughter] Um, yeah. And it also comes in black, which I had the option, but I was like, the client looks sharp. Yeah. Um, and also, you can see the blue and the yellow very clearly. Yeah. Just wanted to show you a little bit of a conference fashion. Um, and then when we get um our second guest in a setup, I also want to show you her nails because they're amazing. 

**Sophia:** Oh yes. 

**Reese:** I don't know how close I can get. 

**Sophia:** Yeah. 

**Reese:** And like I said, we have a group right here. I'm very excited that it's for today. So that's why we're able to, you know, have lunch on right now. But yeah, I brought my winter puppy out. Um, it was intense, but we made it through and we are now day two of the main event with one more day to go and I hope everyone is doing well. 

**Sophia:** Staying hydrated. 

**Reese:** Staying hydrated is so large [laughter] and important. And yeah, I think we're ready to speak to our next guest, Diana. 

**Sophia:** Yes. Awesome. 

[00:27:20] **Reese:** Diana, welcome. And thank you guys. Congratulations on uh winning the Open Salt Community Star 2025. She was one of several winners. Um, the only one I want to point out, but that's why it's so important. Um, Diana, can you please introduce yourself? And also, the earrings. 

**Diana:** Yeah. Oh my gosh. Yes. Oh, those are gorgeous. Oh my goodness. Okay. Sorry. Continue. [laughter] 

**Reese:** Like, hold up your treasury. 

**Diana:** Yeah. Yeah, I'm Diana. Uh, I'm a developer experience engineer at Parametric and I work all my life in engineering uh in observability the last couple of, like, five years. Uh, and I discovered like I really like going and explaining things to the community. So I had a chance like years back to be a speaker on one of the first conferences I've ever been in my life. Uh, I was super nervous but I liked it a lot and I saw like so many women on stage giving talks that I felt like I needed to do more. 

**Sophia:** Of course. 

[00:30:01] **Diana:** Uh, so I kind of did that for two years. Uh, and actually last year, like I was hearing so much about OpenTelemetry, I said, "Oh, I want to get involved. I want to do something." Uh, and I got lucky because in the same moment when I thought about it, the foundation was like, "Oh, we are looking for observability people, we are looking for uh, let's get involved, we want to create the first open and learn fundamentals." Uh, I got in, so it was like first start with the documentation, reading questions, questions about and that's like simple months into certain words. I knew it was finally polished. So that was like for me the kick into like sense and slowly I kind of like I was like, okay, I'm sorry things, how about I'm going to do my company? That was like uh for my current company actually. Um, so uh it was like really interesting because I wanted like from explaining OpenTelemetry to the entire company, getting software engineers involved like instrumenting some things in like SDKs, uh, testing everything. 

**Reese:** Um, so yeah, production, so that was like a decision. 

**Diana:** Uh, but that was like a really cool experience that I've been talking about since one of my talks and explaining how, you know, companies, some particular companies that to be honest they're not super big times to build [laughter] in takes a very important. So I need to be involved in the community. So for me that was like a very, very experience also like understand [laughter] yeah, I thought about myself. Okay, but if right now I'm all alone and I still want to contribute, how can I do it? And I saw translating documents. 

**Sophia:** Oh, nice. That's interesting. 

**Diana:** I can do my own time. Start something, translations and yeah, can you um— 

**Reese:** So global organization, the projects or localization just refers to translating the documentation to different languages. 

**Diana:** Exactly. Yeah. So the idea that—okay, there may be a bit more um, other terms around localization. So it's not necessarily only the technical terms or the tech writing part, but there are like also like um how you're going to automate some CI, going to automate specific pipelines documentation. 

**Reese:** Right. Right. 

**Diana:** Can also be that and also how are you communicating a specific message uh in a language, right? Interpretation of concepts and terms and technology in other languages. So I think that's how I see things. 

**Sophia:** Well, you mentioned Spanish. Um, are you involved with other languages? Um, and can you also tell us like what other languages are being are for the project right now? 

**Diana:** Yeah. Yeah. Yeah. Um, so when um back when I got involved, I didn't think of this year, uh, Spanish was available, obviously English, French. 

**Reese:** Ah yes. 

**Diana:** And that was right. So from the beginning of the year up to now, I think three more languages emerged. So three more communities. Uh, I know for sure Bengali. 

**Reese:** Oh nice. 

**Diana:** And that's like so they really got together and they started to contribute more and more like their only technology. 

**Sophia:** Yeah. 

**Diana:** Um, Ukrainian, that's locked up recently. So I know for sure they need more contributors. Uh, so somebody came with the idea and they started to do that. Um, and I started, uh, for my own language Romanian. I'm native to Romanian. Uh, I started like a couple of months back and I said, "Look, yeah, I think it's an amazing opportunity for my language to represent and for developers back home to understand a bit more language. It's going to really perspective like it is a really nice community." 

**Reese:** Yeah, that's really beautiful. 

**Diana:** So like what is the hardest thing about localization that you find when you do that kind of work? 

**Diana:** Yeah, I think um definitely translating specific terms into your own language or in that particular language, but giving it the flavor or giving it like [laughter] that really gets the essence so it doesn't have to sound like a very dry terminology and that word captures the essence of the meaning. So for example, I don't know about—if you translate really like [laughter] literally a word from English or another language, it might sound a bit weird. So you have to like, oh, does it sound really like this in that language? I have to like, you know, modify it a bit. I have to give it like a nice ring to it so like you can get it, you know, it's kind of like, uh, people like it immediately and they want to use it, right? Um, so that's I think that's the difficult part and also the difficult part is that there are many, many languages that without technical terms directly in English, right? 

**Sophia:** Right. 

**Diana:** And when you want to translate it in that language quite like the appropriate meaning is like, okay, I know you know uses that word in my language and they always something in English, right? Oh, that get immediately, you know, it doesn't sound strange, so those are like words basically. 

**Reese:** That's so wonderful. 

**Diana:** Yeah, it's really cool. 

**Sophia:** Is there um like a way or um to kind of see, you know, the rate of adoption or involvement from the communities that now have these translations available? 

**Diana:** Um, in terms of metrics or in terms of adoption, I think that we are uh kind of primitive. Um, and I think that you need to correlate it a bit with a ground meeting event or with some type of local community that you could uh speak about it on site, right? 

**Reese:** Or this makes some noise back home for example. 

**Diana:** Uh, and say look, we are starting this, we are doing this. We need more contributors. Uh, we need, you know, like the people from the local communities. So like that for each one of us is very much needed whether online or on site. Uh, so for me, for example, I just started this with Romania. I started going like to people like I contributed before or knew from like events and I'm also Romanian. Around there, like can you put it, can you promote it? Like we are like actually entitling our language to be heard in the open community like really jumped into it and yeah, for sure, let's do it. 

**Reese:** Like a lot of people started. It's really nice. 

**Diana:** Yeah, I think as you know, native English speakers we get so used to everything being— 

**Reese:** To English. 

**Diana:** And honestly, you know, a lot of um non-native English speakers, you know, they usually speak multiple languages. Um, and so I think it's really impressive um and awesome the work that you all are doing. 

**Diana:** Yeah, I appreciate it. And also I think down the line people get motivated not only because of modernization but they start thinking, okay, uh, do I like overall open source? Uh, should I do something else maybe in another project? Uh, does it help me in like my work projects, whatever I'm doing? Uh, and I think this is how I practically, you know, promoted it to my community. I said if you guys like me, uh to say like I'm doing an open source project as your contributor like if your employer needs you to have this experience or maybe you want to go to a conference and talk about it. So all of these are very, very nice to have, you know, on your screen and you know, different age groups, you know, there, university or later on their career and I think it's really important to keep motivation because it can be sometimes really hard to start in your free time or remind yourself that you know [laughter] you have an objective online. It's kind of like a gateway project into contributing to open source a little bit. [laughter] 

**Reese:** I always keep telling them that I didn't necessarily start with the organization and I share my new stuff here. I'll definitely go for example—I being an engineer, I still like doing engineering work. 

**Diana:** Oh yeah. 

**Reese:** And I want to get involved in the codes part as well because I've been keeping an eye on everything that's happening talking like there are many, many things that for sure my company or other people will definitely find. 

**Diana:** Um, so yeah, you know, one project or one S is not enough. 

**Reese:** We're going to jump [laughter] into something else at some point and then the community especially is really, really and they keep talking about the same issues over and over again. 

**Diana:** Yeah. So just recently talking about I heard about the same kind of issues in Kubernetes. So I'm kind of like went back and forth because I'm kind of like struggling with similar issues. So I think it's very good to keep an open mind open and keep going. For me at least personally this is what motivates us going forward. You can diversify your contributions, not stop, and we always find something. 

**Reese:** Thank you. 

**Diana:** Yeah, that's awesome. And then kind of pivoting a little bit. Um, I would love to know what you're looking forward to in the coming year for hotel. Like what are you excited about? What kind of trends you're seeing like implementation? 

**Diana:** Anything that has— 

**Jacob:** So um, just like the last couple of weeks been to like specific events. I saw a lot of interesting talks about yeah obviously projector and uh I think these are two things that are really interesting at the moment. 

**Sophia:** So instrumentation, particular end users need a lot more best practices so people don't see users and say, "Oh, but we don't know how to do all this instrumentation or we don't know like which to add." I don't know like what's the easy stuff you can implement? Like can we can you add some like best practices? Can you, right? 

**Diana:** You know, kind of like tell us, you know, like what would be like best starting point onboarding, let's say in this case. 

**Jacob:** Uh, and I've been hearing like uh community and for OpenTelemetry. 

**Reese:** Yeah. 

**Diana:** You know, uh, like get them in. 

**Sophia:** Yeah. [laughter] 

**Reese:** I know that you're complaining, BUT TELL US more about your use. 

**Diana:** Right? 

**Sophia:** Yeah, that's so cool. 

**Jacob:** Yeah. 

**Reese:** Um, I just wanted to know, you said that you wanted to get involved in more of the engineering side, the coding side. Is there somewhere specifically that you're looking forward to or some somewhere specifically that you would like to work in? Like anything exciting to you specifically? 

**Diana:** Uh, for instance, I'm very interested in the river and the river. 

**Sophia:** Can you explain it a little bit to us? 

**Diana:** Uh, yeah. Well, I—I don't know. 

**Reese:** No, right. Right. 

**Diana:** You're getting [laughter] 

**Reese:** I think people just last [laughter] maintainers and people that got involved and all the idea about this convention around it. 

**Diana:** Uh, and although I—I’m not sure like how they are implementing it like practically, something that I want to do is stop from going to so many events like [laughter] my laptop stuff like this. 

**Reese:** So, um, I think it needs a bit of time and time and you know, with my team and my brother. 

**Sophia:** That's awesome. I love it. 

**Reese:** Really cool. Awesome. Well, thank you so much, Diana. Congratulations again on your movie star award. It is so cute. And thank you so much, Sophia, for being my co-host. 

**Sophia:** Yes. Thank you so much, Reese, for being the host host. 

**Reese:** You're amazing. Our co-co-host [laughter] co-host. 

**Sophia:** Um, yeah, we hope to see you at a future soon. Um, Amsterdam in EU and soon for our next year. Um, and we'll have some show up. So check us, check it out there and talk to us if you like please. [laughter] 

**Reese:** See you everybody. Bye everybody. 

[music] 

[music]

## Raw YouTube Transcript

Just the light. Oh, action. >> Oh, you did. You did. >> Hello everybody. If you've been waiting around, we are so sorry for the delay, but we are very excited to be coming to you by from Atlanta, GEORGIA, BUT PRETTY MUCH EVERYBODY WAS um very surprised by a cold front that had us looking at 40° uh which I think is a 3° C um the past couple days. Luckily, it's warming back up, so thank goodness. But yeah, we are coming to you live uh from CubeCon North America 2025. I'm Reese and I am joined here by my co-host Sophia. >> Hi. >> And our first guest, Jacob. >> Hello, my name is Jacob Marino. I'm a maintainer for let's see open telemetry operator, open telemetry helm charts, hotel injector, and I maintain a few random collection things and I contribute to opamp and and I'm missing one. I can't remember. [laughter] I was wondering who had a hands for all 10 honestly. >> If Josh Sar were here, he's he's in he he's everywhere. >> That's every single group. >> That's wild and awesome at the same time. >> No, it was very impressive talking with him. Learned so much. >> So, how I feel talking to you all? Um, now Jacob, YOU DID A TALK OR WAS IT TWO TALKS? >> UH, one talk. So I gave a talk uh about two hours ago, three hours ago. >> Cool. >> Very fresh. >> It was packed. >> It was like I was worried that uh I've given this is my second time giving a talk. First talk that I gave was in Chicago 2 years ago. >> Oh, nice. >> And the room we got a very low slot like it was like towards the end of the day on Thursday, I think. So it was a tough tougher day to give a talk. uh we had a solid audience uh and for this one I was worried that with the content we were doing which is like introductory to hotel and kubernetes I always worry with these introduction ones you know it's like is this going to be enough is it going to be too much so my fear is that nobody shows up and I'm speaking to an empty room this was the reverse where it was a full room and people were standing in the room and then people got turned away from that door >> oh my gosh >> which I was happily like surprised by. Then [laughter] I also like we only reserve 5 minutes for questions at the end cuz I was I was like you know I don't know what questions people will have. Usually people aren't asking the ton of questions like after they'll come up to you later but it's like usually like a Q&A session does not last very long. So oh 5 minutes for questions like that's fine. I we do questions there's a line of like 15 people waiting to ask questions. like they just keep it kept growing and growing. We stayed after for another 30 minutes just answering questions. >> Interesting. What level of questions like was it more um you know people who are newer to the topic or who are asking like more like stage two kind of questions >> huge range so >> we had some people who were you know very introductory level just like I'm getting my bearings here how does this part of it work you know what's the deal with Prometheus and hotel and what do you use for a back end you know that that's like a solid solid starter question and then other people came in they were I've been using this chart for the past year and there's this one thing that I want to be able to do and uh when are you going to like do the work to like enable that and how can we like architect this big range >> very big and each one was like a different part of the of the area. >> Okay, that's so cool. >> Yeah, very very cool and very surprising. I'm always happy to cuz you know I think as a maintainer it's like we get people who come to us with [laughter] issues on GitHub and it's like you'll get someone complaining on a GitHub issue or like hey this thing broke the most recent release broke me um you know what are we doing about that broke [laughter] >> but no one's broke their spirit you [laughter] know I've had releases break my spirit >> but the uh the real thing is we don't get positive feedback. We don't get a lot of questions cuz realistically most people are asking track or going on Stack Overflow, >> right? It's like they're not bringing the questions to us. So, we don't really hear or understand what usage is. I mean, it's kind of the benefit [laughter] and the curse of open source is that like we don't necessarily get that user feedback directly. It's why like I love what you all do cuz getting the user feedback is one of the most valuable things to the community. like in order for us to push forward, we need to know what isn't working right now where people just don't see the effort. Um we actually I hosted a meetup in New York uh last month, 2 months ago, something like that. >> Yeah. Uh, and that was eye opening because it was like wow, people are really using these things and things that I I feel like I've talked about so many times are still not known, you know, and it's like I'll mention like how many people know what like the target allocator is in a show of hands and nobody raised their hand in a room of like 40, you know, senior SRRES. I'm like, okay, uh, would anybody like it if you could do distributed, sharded, retheus scraping? and everybody raises their hand and I'm like well we have that like it's done it's there you know you can use it it's been a thing for a few years you know so I guess all to say the community just is still there's still things for people to learn about the vast ecosystem that we have here >> yeah I think you know I think a common theme just in general is people not being aware of you know different abilities and features and yeah on the end you see too you know it's it is a bit of a challenge cuz like we feel like we're talking about it um you know at our work and like in the ozone community and then yeah like you said we have all these conscious people who don't know and it's we're trying to figure out like where are they going for like how can we >> make them aware >> of you know all these cool things that are happening. Um yeah, so you know, one of the things we we started doing is um the what's the hotel segment, which we just had our first one um a month ago or so. And so we're hoping to, you know, I don't know, have something we can point people to. >> Of course. >> But you mentioned the injector. >> I did. Tell us more about please do. So I am the uh I'm a maintainer for it but I'm mostly just doing reviewing because this is actually a joint effort between uh Splunk and D-Zero. Both of them have already written their own uh injectors for auto instrumentation. Oh, right. >> And they're essentially donating a merge of both of those projects to the tot alpha version of this for their customers. Um, so we're just testing out that everything is working the way we need to. [clears throat] There's a lot of really random edges here. Um, interestingly enough, this does introduce a new language to hotel, which is exciting, which is it's very rare for us to not use a language in a project that is meant to instrumental languages. Right. >> Right. >> And we are now using Zig in the project. >> Zig. >> Zig um is a fun language that is sort of a merged between like Go, Rust, C++, and C. Oh, super fun. [laughter] >> But so the real value of it is it doesn't require uh a lot of like core Linux dependencies. So like GIC C is one that we really think about a lot. Uh if you're on AWS, something that I've been bitten by is not all of the nodes have g. And so when you're trying to do injection like say you're trying to run a load balancer liketo or envoy >> um is similarly injected like we inject auto instrumentation and that will just not work. It used to not work. I think they've changed this but it used to not work uh on certain types of AWS nodes. So we have that same issue because we're trying to inject to all these different environments. So, Zigg is pre-built with a bunch of these C libraries, but from scratch, part of it standard library and not based on anything existing. So, it has all of its own dependencies. So, the benefit of this injector project is that we're going to be able to really meet users where they're at without needing to know a ton about their environment. And that's the real problem today. >> Yeah. >> Um, so it's an exciting project. I think we're a few months away from it being alpha beta. Other people are on the release timeline. Ted Young is thinking a lot about the release timeline there. Um, but all TC >> TD, that's so cool. >> Yeah. What are the parts of, you know, whether it's something working on or not working on directly that you are excited about? >> Good question. I think that the biggest thing for project right now that everybody cares about is stability, right? I think that uh we're trying to get to the place where users can reliably get you know a new update without them needing to do any configuration changes without needing to worry about uh components being deprecated things like that right I talked to at that meet up in New York I talked to a developer at a major bank who was you know they've developed all of their own uh custom components for the collector and so every time that we've been doing these reworkings the collector's architecture. They need to then refactor a bunch of their code as well. And you know after a few months you lose track of all these updates. So it becomes like a weeks long project to keep up to date. When you have to do that their release cycle is every quarter, right? It gets a lot to manage and a lot to update. So for the users, I think what people really want to see is that level of maturity and stability. We can get to that graduated status with the CCF would be huge. That would be massive for the project to have. Uh I think it would really I mean our adoption already has been really high. I think that's when we would come to the next level. Great. >> Can you explain a little bit for those of us like CCS stages like what going from incubated incubating projects to graduated means? >> Sure. >> Yeah. I'm not the best. I can tell you what I know. I'm definitely not the person in charge of this. There are people who are far more confident in the stability part of this governance than I. >> Yeah. >> So I I will speak on only >> that's all we're asking for. [laughter] >> So right now we're in as you said uh project is relatively lenient in terms of its standards. There are standards but graduation is is really strict I would say for good reason right like you want to be sure that when you are considered a graduated project you have a healthy community which [laughter] we definitely do uh you have stability guarantees which is the main thing we're working towards and lastly adoption so adoption has to be at certain amount of companies you have to have testimonials [laughter] from those companies about how the project's been helpful uh that's another thing that we have plenty of so now it really just comes down to stability and stability. You can think of Kubernetes as the example here. Kubernetes is, you know, the first graduated project. I imagine it's the first one. Maybe there maybe someone beat them to it, but you don't [laughter] know. But essentially, every time that Kubernetes improves their security and reliability, uh, you know, release stability, anything like that, it raises the bar for everybody else to continue to improve. So as we are getting towards stability, Kubernetes is is chugging along, you know, really positively and improving their posture constantly. So it's up to us to not only meet where we started for our uh graduation criteria, but also to continue building towards that. So that means that you're going to see more uh security features, much more uh security guarantees, which is going to be very helpful for enterprises. M um you're going to hear more about quarterly releases rather than uh the sort of disperate release calendar that we have today. >> Uh you'll hear more about documentation which is also going to be huge. So uh later when that comes on I assume that we'll be talking about some mobilization efforts and documentation. >> Ah yes, uh that is super super valuable right um all of that is going to get us to that graduation phase. Uh it's just time it's time and effort and uh we have a dedicated group of people who want to see this happen and are spending you know all of our time at all of these large companies trying to make that happen. Very exciting. >> Awesome. >> That is very exciting. And if you are yourself an open end user and um your company is using in fashion um and you want to share your story, we would love to have your story as part of um our uh legacy [laughter] our catalog. >> Yeah. like to help, you know, help graduate the project and help take us out to us. Um, we'll have it in the show notes um after this. But yeah, it's pretty easy. As long as you remember me Slack, you can find us at hotel dash dash and dash. >> I think that's all the dashes. >> I thought we were going to dash zero. [laughter] Oh, so we're like dash. >> And similarly, if anybody wants to help out with documentation, documentation is >> one of the best ways to contribute to the project. It is so valuable. We had somebody for the operator group contribute a whole uh bit of documentation for the target alligator and it it was so well done. Adriana did this as well. super helpful >> and it has been such a resource for me to be able to point users that come into our Slack, come into our S meetings to just say, "Hey, you have a question about this? We have a full document to answer everything you might need to know about it." That has been such a way to offer. Um, it's lovely. So, great way to contribute and get started. Doesn't require writing code. Requires asking questions and writing a bunch of stuff down. >> Yeah. And I can confirm that everyone that I met in the local community has been super helpful. Um, anything you know you can take on and be responsible for like documentation that's something that you're taking off their plate. So I know they're having to help you. And it's also cool to see your work on an official website. >> Yeah. Like uh definitely join the communication sig for that. I'm currently in it and we're working on a lot of refactoring of the documentation like just like the early stages since I'm more of a beginner with the open telemetry and everything. I've been working on kind of refactoring those beginner level documentations. So like it's been really helpful getting people like acquainted with that and localization efforts too. Like I know Lisa is working on a lot of localization efforts. So yeah, it'll help. >> Super helpful and the the beginner stuff especially. I mean >> again from the talk today I think it's just so it was so useful to learn where people are at in their implementation journeys >> right >> uh we do have people that really need reference architectures a ton of code examples right >> these things help project adoption that also make it so that users actually are delighted by the experience right that and ultimately that that's what I think we all want to see and that's what users want like you want to be able to install hotel wherever you need it and not have to scour the internet to figure out how to how to make it work, right? >> Different companies have so many different needs and so getting started is always going to be the most important thing for us to really nail. Uh the next thing that I heard from uh when I did the event in New York is reference architectures and showing how we can do hotel in all of these various environments. so that people can have some code samples to copy from uh some architectures to you know design around. I was just talking with an engineer at and they >> are really interested in understanding how to do various trace sampling architectures, right? where we can really have like a whole as you said catalog these architectures to show people and we all of our companies like you know when I was at our flight we had all these architectures internally that we would post blog posts about to share we have a lot of companies that are using hotel as part of the ingestion path as well which involves a lot of this uh architectural work similarly a lot of companies are like that are contributors to hotel also are obviously using the tooling themselves for their own company's observability. We should reach out to the people who are doing that and try to publish what are the reference architectures that hotel maintainers use ourselves, right? >> I think that would be really useful uh for people who are trying to implement this right now. >> Absolutely. >> For sure. Um are we planning to host them like in a repository or like on sites directly? >> Oh, I think would be the best. I think you know we have documentation places the operator group and I think the idea of everything being the doc is going to be the way to go >> right >> like centralizing it and making sure that it's well organized which is a lot of the work that you're doing super valuable >> of course >> uh but I think it just it needs to be there right now I think it exists on a few different company blogs a few different companies >> head scattered >> bringing that together I think would really really valuable. >> One reason let's do it, >> right? There's so many companies like contributing. So there's definitely a bunch of references that people in our community could use. >> Yes. >> Yeah. >> Absolutely. And so many people are people are so friendly, right? like back to that like going to uh the hotel booth. We've had so many people who have never come up to us before and are just asking great questions and we have so many people who just, you know, we hang out there cuz we love to talk to people about this. It's rare that you get to have this level of engagement with end users, right? Uh that direct type of engagement is so valuable and so people coming by has been one of my favorite experiences of it always. I think the reason that I love to come to these is just getting to talk to people, hearing people's problems, digging in because then it helps us plan what I like what I need to do for the next 2 years, right? I can take that feedback on it. What um so in during your time here at coupon like from the audience questions that you had at your talk and people who come through the open tree observatory do you have are you seeing any like general trends as to like what people are leaning toward or needing more help with or >> Yeah. So I say the the main thing that is of concern to me is around amp which has been getting a lot of there are a lot of talks in opamp this coupon. I don't know if that if we've noticed that there were at least four that mentioned it which is a lot. >> Could you explain that a little bit more for us? Nothing. [laughter] Sorry. >> We're slowing down a little bit. So, opamp is the uh open agent management protocol uh part of the hotel project but is also designed to be in in the same way the hotel is very vendor neutral it's neutral to agents as well. So, it's not just for the collector necessarily to be for a lot of different uh agents out there. The goal of the protocol is to enable things like uh component status reporting, health reporting, and remote configuration. And remote configuration is definitely the top of the town is what I would say. >> Yeah. Okay. Very cool. >> Um and so in that vein, what it sounds like users really want is a way to dynamically update what the collector can do, what the SDKs can do uh in real time. And that's challenging. The way that the collector was designed was never really with remote configuration in mind. There are ways to reload the process. Like we can actually go in and restart the process from the collector binary. Like you just do that, right? >> But it's different than a remote. What users really want is a way to push a rule to a collector and the collector accepts it and continues going. >> Yeah. So that's what a company like bind plane has already built. Uh and so what we want to do is take a lot of the lessons from what BL has been successful with and obviously we're working with them as well. They are big contributors to uh the idea is that we work all together to improve the provider posture here and improve the SDKs as well so that we can actually realize this vision that people can dynamically update their configurations wherever they might be. [laughter] Uh but it's challenging. I mean that that's like a really tough topic. >> Yeah. >> There's a lot of a lot of companies in hotel have done this work beyond my plan before. Elastic comes to mind. They have their own >> I work here. >> Oh yeah. [laughter] >> Elastic has uh their own protocol for doing road configuration already. >> Okay. Okay. >> We've talked with a few of their containers and there's definitely some like room for some good collaboration that we've talked about. >> Awesome. >> I think it's all to be seen but this is definitely the thing that we hear a lot about. The thing that I hear a lot about on the operator side is in Kubernetes, how can I do uh call it not just remote configuration but layered configuration. So what this means is how can I make it so that if I'm running in an enterprise company that I'm in a multi-tenant environment, I want like a base collector. I want to overlay. I want my teams to be able to overlay different pieces of config on top of that collector for their needs. >> Right. >> It's a really complicated topic. We >> Yeah, it's really >> sounds like it. And the thing that I sort of struggle with is how do we make this extensible and configurable but also simple to understand. The problem with this that it starts getting into a lot of moving parts and as soon as you start to introduce more moving parts is when complexity and usually reliability both complexity increases and reliability decreases right you need consistency and more moving parts uh will reduce that it's sort of that there's a great quote in reliability that I love it's u the most reliable system is the one that does that never that you right we know this quote. I'm totally botching it right now. [laughter] >> No, I hear it. I hear it. >> The idea is that like [laughter] the most reliable system is the one that like doesn't exist, >> right? >> Right. Cuz it's always achieving its goal of non-existing. >> And so if you want to really improve the reliability of the service, you delete it >> because then you don't have to care then it's at 100%. Cuz it's always it's always giving you the same answers which is nothing. Yeah. [laughter] [laughter] >> Sorry. >> No, I'm here for it. I'm here for it. Yeah. >> Someone I I'll say that to I don't know, someone at the Ozel booth and they'll be like, "You totally messed up." >> You know, [laughter] we'll have the correct throw in the shout out. >> Yeah. Thank you so much, Jacob. Um, we are going to bring on our next guest, Diana, in a moment. Um, and in the meantime, I really want to show off this baseball jersey. >> Looks really good. >> But, um, our friends at Honeycomb have been kind enough to um, sponsor for the hotel community. Um, thank you, Austin Parker, for the design. Um, I would stand and show the back. It says uh the number 11 ACTUALLY I DON'T KNOW WHY IT SAYS 11 like [laughter] there. But yeah, it says maintainer on the back. Um, we'll have some pictures hopefully to show you. But yeah, you've got the logo over here and it says open too across the front. Very, very snazzy, very sharp. [laughter] Um, yeah. And it also comes in black, which I had the option, but I was like, the client looks sharp. Yeah. Um, and also, you can see the blue and the yellow very clearly. Yeah. Just wanted to show you a little bit of a conference fashion. Um, and then when we get um our second guest in a setup, I also want to show you her nails because they're amazing. >> Oh, yes. >> I don't know how close I can get. >> Yeah. And like I said, we have a group right here. I'm very excited that it's for today. So that's why we're able to, you know, have lunch on right now. But yeah, I brought my winter puppy out. Um it was it was intense, but we made it through and we are now day two of the main event with one more day to go and I hope everyone is doing well. >> Staying hydrated. staying hydrated is so large [laughter] and important. And yeah, I think we're ready to speak to our next guest, Diana. >> Yes. Awesome. >> Diana, welcome. And thank you guys. Congratulations on uh winning the Open Salt Community Star 2025. She was one of several winners. Um, the only one I want to point out, but that's why it's so important. Um, Diana, can you please introduce yourself? And also, the earrings. >> Yeah. Oh my gosh. Yes. Oh, those are gorgeous. Oh my goodness. Okay. Sorry. Continue. [laughter] >> Like, hold up your treasury. [laughter] >> Yeah. Yeah. I'm Diana. Uh I'm a developer experience engineer parametric and I work all my life in engineering uh in observability the last couple of like 5 years. Uh and I discovered like I really like going and explaining things to the community. So I had a chance like years back to be a speaker on one of the first conferences I've ever been in my life. Uh I was super nervous but I liked it a lot and I saw like so many women on stage giving talks that I felt like I needed to know to do more. >> Of course. >> Uh so I kind of did that for 2 years. Uh and actually last year like I was hearing so much about open I said like oh I want to get involved. I want to do something. uh and I got lucky because in the same moment when I thought about it foundation was like oh we are looking for observability people we are looking for uh let's get involved we want to create the first open and learn fundamentals uh I got in so it was like first start with the documentation reading questions questions about and that's like simple months into certain words. I knew it was finally polished. So that was like for me the kick into like sens and slowly I kind of like I was like okay I'm sorry things how about I'm going to do my company. that was like uh for my current company actually. Um so uh it was like really interesting because I I wanted like from explaining open telemetry to the entire company, getting software engineers involved like instrumenting some things in like SDKs uh testing everything. Um so yeah production so that was like decision. Uh but that was like a really cool experience that I've been talking about since one of my talks and explaining how you know companies some particular companies that to be honest they're not super big times to build [laughter] in takes a very important. So I need to be involved in the community. So for me that was like a very very experience also like understand [laughter] Yeah, I thought about myself. Okay, but if right now I'm all alone and I still want to contribute, how can I do it? And I saw translating documents. >> Oh, nice. That's interesting. I can do my own time. start something translations and yeah, can you um so global organization the projects or localization just refers to translating the documentation to different languages. >> Exactly. Yeah. So the idea that okay there may be a bit more um other terms around localization. So it's not necessarily only the the technical terms or the tech writing part but there are like also like um how you're going to automate some CI going to automate specific u pipelines documentation. Right. Right. >> Can also be that and also how are you communicating a specific message uh in a language right interpretation of of concepts and terms and technology in other languages. So I think that's that's how I see things. >> Well, you mentioned Spanish. Um are you involved with other languages? Um and can you also tell us like what other languages are being are for the project right now? >> Yeah. Yeah. Yeah. Um so when um back when I got involved I didn't think of this year uh Spanish was available obviously English, French. >> Ah yes >> and that was right. So from the beginning of the year up to now I think three more languages emerged. So three more communities. Uh I know for sure Bengali. >> Oh nice. >> And that's like so they really got together and and they started to contribute more and more like their only technology. >> Yeah. >> Um Ukrainian that's locked up recently. So I know for sure they need more contributors. Uh so somebody came with the idea and they started to do that. Um, and I started uh for my own language Romanian. I'm native to Romanian. Uh, I started like a couple of months back and I said, "Look, yeah, I think it's an amazing opportunity for for my language to represent and for developers back home to understand a bit more language. It's going to really perspective like it is a really nice nice community." Yeah, that's really beautiful. So like what is the hardest thing about localization that you find when you do that kind of work? Yeah, I think um definitely translating specific terms into your own language or in that particular language, but giving it the flavor or giving it like [laughter] that that really gets the essence so it doesn't have to sound like a very dry terminology and that word captures the essence of of the meaning. So for example, I don't know about If you translate really like like [laughter] literally a word from English or another language, it might sound a bit weird. So you have to like al oh does it sound really like this in that language? I have to like you know modify it a bit. I have to give it like a nice ring to it. So like you can get it you know it's kind of like >> uh people like like it immediately and they want to use it right. Um so that's I think that's the difficult part and also the difficult part is that there are many many languages that without technical terms directly in English right >> and when you want to translate it in that language quite like the appropriate meaning is like okay I know you know uses that word in my language and they always something in English right oh that get immediately you know it doesn't sound strange so those are like words basically That's so wonderful. >> Yeah, it's really cool. >> Is there um like a way or um to kind of see, you know, the rate of adoption or involvement from the communities that now have these translations available. >> Um in terms of metrics or in terms of adoption, I think that we are uh kind of primitive. Um, and I think that you need to correlate it a bit with a ground meeting event or with some type of local community that you could uh speak about it on site, right? >> Or this makes some noise back home for example. Uh, and say look, we are starting this, we are doing this. We need more contributors. Uh, we need, you know, like the people from the local communities. So like that for each one of is is very much needed whether online or on site. Uh so for me for example I just started this with Romania. I started going like to people like I contributed before or new from like events and I'm also Romania. around there like can you put it can you promote it like we are like actually entitling our language to to be heard in the open community like really jumped into it and yeah for sure let's do it like a lot of people started it's really nice >> I think as you know native English speakers we get so used to everything being >> to English And honestly, you know, a lot of um non-native English speakers, you know, they usually speak multiple languages. Um and so I think it's really impressive um and awesome the work that you all are doing. >> Yeah, I appreciate it. And also I think down the line people get motivated not only because of modernization but they start thinking okay uh do I like overall open source uh should I do something else maybe in another project uh does it help me in like my work projects whatever I'm doing uh and I think this is how I practically you know promoted it to to my community I said if you guys like me uh to say like I'm doing a open source project as your contributor like if your employer needs you to have this experience or maybe you want to go to a conference and talk about it. So all of these are very very nice to have you know on your screen and you know different age groups you know there university or later on their career and I think it's really important to keep motivation because it can be sometimes really hard to start in your free time or remind yourself that you know [laughter] you have an objective online. It's kind of like a gateway project into contributing to open source a little bit. [laughter] >> I always keep telling them that I I didn't necessarily start with the organization and I share my new stuff here. I'll definitely going for example I being an engineer I still like doing engineering work. >> Oh yeah. And I want to get involved in the codes part as well because I've been keeping an eye on everything that's happening talking like there are many many things that for sure my company or other people will definitely find. Um, so yeah, you know, one project or one S is is not enough. >> We're going to jump [laughter] into something else at some point and then the community especially is really really and they keep talking about the same issues over and over again. >> Yeah. So just recently talking about I heard about the same kind of issues in Kubernetes. So I'm kind of like went back and forth because I'm kind of like struggling with similar issues. So I think it's very good to keep an open mind open and keep going. For me at least personally this is what motivates us going forward you can diversify your contributions not stop and we always find something. >> Thank you. >> Yeah that's awesome. And then kind of pivoting a little bit. Um I would love to know what you're looking forward to in the coming year for hotel. Like what are you excited about? What kind of trends you're seeing like implementation? Anything that has so um just like the last couple of weeks been to like specific events. I saw a lot of interesting talks about yeah obviously projector and uh I think these are two things that are really interesting at the moment so instrumentation particular end users need a lot more best practices so people don't see users and say oh but we don't know how to do all this instrumentation or we don't know like which to add. I don't know like like what's the easy stuff you can implement like can we can you add some like best practices can you right >> you know kind of like tell tell us you know like what would be like best starting point on boarding let's say in this case uh and I've been hearing like uh community and for open tele Yeah. >> You know, >> like get them in. Yeah. [laughter] >> I know that you're complaining, BUT TELL US more about your use, >> right? >> Yeah, that's so cool. Yeah. Um, I just wanted to know, you said that you wanted to get involved in more of the engineering side, the coding side. Is there somewhere specifically that you're looking forward to or or some somewhere specifically that you would like to work in? Like anything exciting to you specifically? >> Uh, for instance, I'm very interested in the river and the river. >> Can you explain it a little bit to us? >> Uh, yeah. Well, I I don't know. >> No, right. Right. You're getting >> I think people just last [laughter] maintainers and people that got involved and all the idea about this convention around it uh and although I I I'm not sure like how they are implementing it like practically something that I want to do is stop from going to so many events like [laughter] my laptop stuff like this. So, um I think it needs a bit of time and time and you know with my team and my brother. >> That's awesome. I love it. Really cool. Awesome. Well, thank you so much, Diana. Congratulations again on your movie star award. It is so cute. And thank you so much, Sophia, for being my co-host. >> Yes. Thank you so much, Reese, for being the host host. >> You're amazing. Our co- co-host [laughter] co-host. >> Um, yeah, we hope to see you at a future soon. um6 Amsterdam in EU and soon for our next year. Um and we'll have some show up. So check us check it out there and talk to us if you like please. [laughter] >> See you everybody. Bye everybody. [music] [music]

