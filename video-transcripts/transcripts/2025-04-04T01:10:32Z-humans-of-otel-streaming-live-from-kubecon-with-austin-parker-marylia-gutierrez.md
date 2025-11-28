# Humans of Otel Streaming live from Kubecon with Austin Parker &amp; Marylia Gutierrez

Published on 2025-04-04T01:10:32Z

## Description

Adriana Villela and Reese Lee interview #OpenTelemetry community manager Austin Parker about what's new in OpenTelemetry.

URL: https://www.youtube.com/watch?v=EL0UkhvFAmY

## Summary

In this live stream of "Humans of OA," host Reese, a senior developer relations engineer at New Relic, along with colleagues Adriana and guest Marilia, a staff engineer at Grafana Labs, discuss various aspects of open telemetry and its community. They explore Marilia's journey from an end user to a contributor, her experience with observability at Cockroach Labs, and her current role in maintaining components within the open telemetry project. Key topics include the significance of semantic conventions for databases, the importance of localization in documentation, and the roles within the open source community, such as contributor, triager, approver, and maintainer. Additionally, they highlight the growth of the open telemetry community and its ongoing projects, including the evolution of logging infrastructure and the introduction of AI in enhancing observability. The discussion wraps up with a mention of upcoming community events, including the OpenTelemetry Community Day, and the vibrant atmosphere of the CubeCon EU.

## Chapters

00:00:00 Introductions
00:05:50 Guest introduction: Marilia
00:06:58 Discussion about localization
00:12:40 Overview of contributor roles
00:19:00 Importance of semantic conventions
00:24:42 Updates on OpenTelemetry projects
00:30:24 Upcoming OpenTelemetry Community Day
00:32:18 Discussion about AI's impact on observability
00:34:34 Project updates and growth of OpenTelemetry
00:35:17 Closing remarks and acknowledgments

## Transcript

### [00:00:00] Introductions

**Reese:** Hello, welcome to a live stream of humans of OA. We are coming to you live from what had a little bit of subtitle issues, but we are here and we're so excited. My name is Reese. I am a senior developer relations engineer at New Relic and I am joined here by my lovely industry colleague Adriana and Marilia who is our first guest.

**Adriana:** Hey everyone, thanks for tuning in. My name is Adriana Vila. I work alongside Reese.

**Marilia:** Hi everyone. My name is Marilia. I am a staff engineer at Grafana Labs and also in open telemetry. I work in a few different groups. I am a maintainer for the contributor experience and I'm an approver for... 

**Reese:** I know you mentioned earlier about all the different parts that you're involved in and we're really curious because you started as an end user and then eventually started contributing. 

**Marilia:** Yeah. And so we would love to... On my prior job I was responsible for the observability. I used to work at Cockroach Labs and I was the manager for the observability there. So I started learning about hotel specifically because there we would be able to use that like maybe someone want to see some of those things outside of the database. So we created some endpoints here and there but it was very basic stuff. 

**Reese:** So this team is to work only on open telemetry. So your focus is just open telemetry. 

**Marilia:** So this is my day-to-day. I can have fun and just be on it.

**Reese:** That's awesome. I didn't realize that. That's so cool. And what would that be like with Java and .NET? I want to make sure that all SDKs are on the same level. 

**Marilia:** The other two were a little... Here, what are the things that we can add? So we have an owner for the PostgreSQL plugin that I was already touching. That's awesome. 

**Reese:** And actually you gave a talk yesterday about database monitoring.

**Marilia:** Exactly. So one of the other big ones. So fresh news, we just this week released the... Was it the release candidate two? So that means by the end of the month we're going to mark it as stable. So people can really start using it without any concerns. 

**Reese:** You mentioned that you're in the semantic convention SIG for databases and there's like a general semantic convention SIG, correct? What is it about the database semantic convention SIG that spun off?

**Marilia:** Yeah. So usually you have the general semantic conversion and on that one you have sometimes people from all of the other semantics that can give updates or discuss this particular name of the metric and spend an hour when you have a lot of people on the code that are not related to databases, so they don't have any input to give. It might be a waste of time. So it's kind of like you spin up different semantic conventions for each of like... Oh, we want to focus on database, we want to focus on the HTTP, we want to focus on RPC. So now you can bring people that have experience in that area and talk about it. 

**Reese:** The same way you can think about if you would have a SIG for SDK, you have so many languages. So we have now one SIG for each language. So it's kind of like the same idea.

**Marilia:** Yeah. Help keep it focused and easy to prioritize. And then we can always have the updates that we can bring to the main semantic one because when they generate a version, it's for all semantics. It's not as specific for the database. So you just merge that repo and whenever a new version comes in, it might be bringing updates for the database, might be from the HTTP, and so on. So we just can bring the update to the main ones like, "Hey, this one we're marking as stable." We have these updates and things like that. 

**Reese:** And then you mentioned, and I'm glad you were able to rattle off the long list of titles that you have in the community because I was like, "I am not going to remember all these," but they're so cool. 

**Marilia:** Um, so there's like different titles. There's an approver, then a maintainer. Okay, perfect. And then could you explain to us briefly what each... What's the distinction between each role?

**Marilia:** Yeah. So you started first as a contributor. So you can become a contributor not being a member of CNCF at all. So when you do a couple of contributions, you ask to become a member which is something I think everybody should do if you are doing because it's very easy to join. You just have to open a PR and say like, "Hey, I want to become an official member of CNCF and then OpenTelemetry." 

**Reese:** Then you are officially a contributor. 

**Marilia:** Then you pick something that is more interesting to you. So for example, I really like this language or I really like this specific component. Start joining the SIGs just to learn more about it, see how you can help. And when you start really helping out, start reviewing PRs, putting comments, creating issues for things that you mind and with time you get the status of triager, which is somebody that is helping when a lot of issues are coming up. You help exactly triage those issues and see things that make sense, things that actually they were not using correctly or there are actual bugs. 

**Reese:** Then from that you can become an approver. 

**Marilia:** That when you approve a PR, your approval actually counts because people can approve but to be able to merge, you need to have people with permission giving the approval and being able to merge. So the approver now has this... Whatever we approve, it counts and somebody who has the permission can just merge it in. And then you have the final one which is maintainer. So these are the people that can actually merge. Usually, they are the ones creating the releases, creating roadmaps, but they do get input from everybody that is contributing.

**Reese:** That's so exciting. That is really cool. Thanks for the overview. 

### [00:05:50] Guest introduction: Marilia

**Marilia:** Yeah. Um, the other thing that we wanted to ask... You know, you mentioned that you're working in the Portuguese localization. Talk a little bit about that. Talk about why it's important to have localization, how you got involved with that specifically, how that's been.

**Marilia:** Yeah. So I think it's really important because it's a barrier, like the language. And it's already hard for you to completely learn something completely new like on tech, but imagine if you don't even know the language. A lot of other countries, their first language is not English. It's not always you're going to find this documentation and it's not easily accessible for everybody. So actually, I started a while ago. I created my own blog post and I was like, "Everything that I'm creating there, I'm going to create it." And where people that actually met when I did like conference days in Brazil and there was the bad group. 

### [00:06:58] Discussion about localization

**Marilia:** So I started like, "Oh, I'm going to help them out." I like to review a lot of things and the good thing is a lot of things in English that you learn, like just experience living, so I can help out with the translation, the localization, and also decisions like what are the things that you don't translate at all because we're going to say tracer. We don't translate that. That makes sense because at the same time, you don't want to translate everything because then when they're going to search those words, they don't exist anywhere. 

**Reese:** But we have a lot of... 

**Marilia:** Yeah, but yeah, I think it's really good to just break this barrier and bring a lot of people who would have no idea. 

**Reese:** Yeah, that's so great. That's a lot of work. Um, I guess in some ways has it improved your Portuguese as a result?

**Marilia:** So, yeah, it's always funny because living outside for so long and sometimes I'm going to give a talk like in Portuguese and I was like here, so I know the right thing to use, but it's always a challenge. But we also try because there's not only Portuguese. We also have people working on the Spanish, French, and Japanese. 

**Reese:** So do completely different from the French, you know? 

**Marilia:** We also have this thing which is similar to the same. So we have the documentation one but we have different groups. So every time a docs page comes out, you like the localization, we translate. Yeah. So that is the idea. So right now that people are accessing more things like that. So we start with those ones and like the same thing for SDKs. I see which ones people are like downloading more. 

**Reese:** So we... 

**Marilia:** Some come in and do updates on the original one. So we do have something to... Because part of when you do localization, there is a new kind of tag that you had to put in what was the commit that you translated. Okay? Because it's really hard for people to know that somebody did an update somewhere. You had to really be paying attention. So the idea is to have something that would tell us, "Hey, those are behind. Just catch up," and things like that. 

**Reese:** So we were always up to date. 

**Marilia:** Oh, sorry. Go ahead. 

**Reese:** I was curious because when I was asking you, you know, all your different... That was like the first time I'd heard of that specifically because I know we have like translated some of our documentation but I didn't realize there were like specific teams working on these languages. 

**Marilia:** Um, so the localization SIGs, they are only translating documentation or what all involves?

**Marilia:** The official page like open telemetry.io, all the pages there, if you look at the top that didn't have anything, now if you're looking at the page at the top, you have a select there that you can change the language that you want. So whenever the page is translated, now you have... 

**Reese:** So cool! Learned something new today.

**Marilia:** I then joke that I have a PR with the translation to the Japanese even though I don't speak any Japanese and sometimes it goes wrong there too. 

**Reese:** Uh-huh. 

**Marilia:** It's a way to catch up. 

**Reese:** So like... And then it was like, "Okay, so the..." I was like, "Oh, let me see if any other languages translated the same thing wrong." Async or something. 

**Marilia:** Okay. Yeah, that's pretty big.

**Reese:** And then it was good that it was just like a word and I translated and I put a PR and I tagged the reviewers for Japanese. I was like, "I don't speak any Japanese. I put in this thing that I think is the right translation." Like there was a part for the translation, but we even like looking for... We want to add also more examples because we don't have a lot of examples. 

**Marilia:** If there is something, for example, you never did, so you try it yourself and you might for the future ones that are coming, that they know like more examples, more things to try out on.

**Reese:** Yeah, man. This is so exciting. I'm learning all kinds of new things.

**Marilia:** I know. 

**Reese:** Yeah, so many things that we're like when people ask like, "How do I start?" like so many of... You're going to be able to find somewhere something that is interesting. There's always something for you, right? 

**Marilia:** Yeah, it's really hard. Just try joining, just like listening. But at the same time, keep in mind that open source is different than a day-to-day job because sometimes what I see people find things was like, "How I... I found the things that like, oh, they need help with this, they need help with that," and then the things that I already have priorities like from even coming like, "Hey, can you take a look at this?" 

**Reese:** Up for grabs a few repos have them. 

**Marilia:** So we have things like for example contribute fest that we did here and a lot of them got tagged with contribute fest, but not all of them got actually worked on. So those are the ones that you know and you're going to find something and people in the community are very helpful like tag them on Slack, on the issue itself. They are happy to give you guidance as well.

**Reese:** Yeah, and I'll do a shameless plug for the end user SIG as well. We are always happy to have contributors. You can find more information in our show notes. 

**Marilia:** Part of like the end user SIG. The other thing I want to ask is the contributor experience. So if you want to like, "I want to contribute, like what is missing?" So for example, one of the projects that I did that was so like, "How do I start? I don't know how to set up locally." There was no like, "What is the dependency that you need?" So there was like nothing there. 

**Reese:** So I worked like as a mentor for the AI program template that all repos could use and started creating the PR so people have at least the basic things that they need to just at least start having things.

**Marilia:** Oh, that's amazing. 

### [00:12:40] Overview of contributor roles

**Reese:** And really quickly, actually, I want to ask about the contributor experience SIG because that one's a relatively new SIG, right?

**Marilia:** Yes. Can you tell us a little bit about that SIG, how it got started, and how you became a member?

**Marilia:** Was it because we saw this need of people complaining that they don't know how to start? They don't always understand like the path for like triager or like how... Like there is nobody there to guide. Okay, if nobody is going to be there for you, are you able to find all the documentation that you need to be able to follow the path that you want? Or like we didn't even know the challenges people were having a few of the things and we do like also surveys to find out people like how are you feeling like being a contributor and we started tackling the things like were the most concerned like documentation was the top one. So this is why I started that project and came in almost right away.

**Reese:** What are some of the upcoming things for the contributor experience?

**Marilia:** So for this one, I just finished this part, like this month for the template. So my next meeting is going to be actually picking up what is going to be the next one. But we do have like issues open that is just helping out like clarify things to people. And if anyone like also if you're listening, if you have something that is really like bothering you and you need, feel free to like message us or like open an issue directly on the repo there. We can't prioritize because we have a list there, but we are just prioritizing ourselves because we don't have necessarily feedback things, but react like thumbs up or really want this kind of thing and we will be able to put it in first.

**Reese:** Awesome. And I think we're almost ready for our next guest.

**Marilia:** Yeah, I think we're... So I guess we will continue our conversation. I guess as we get ready to bring on our next guest experience, they will be able to share like people just joining and people that have a lot of experience will be able to guide you as well just as I join the calls and you're going to be able to...

**Austin:** I'm just going to get the surprise out of the way. Uh, community manager for OpenTelemetry and we are so excited to have him on.

**Reese:** How am I still community manager? 

**Austin:** Wait, are you no longer the community manager? What? You're still community manager?

**Austin:** Yeah, I think I am. If you go and check the repo, I probably am. I mean, I do both jobs still. So, I'm a member of the OpenTelemetry governance committee. I also have been a maintainer on the OpenTelemetry website, uh, OpenTelemetry demo. I've been working in a working group, I guess you could say, like where we combine OpenCensus maintainers and OpenTracing maintainers where we, you know, came in and worked with some people. 

**Reese:** What have you seen as like the biggest changes since things started? 

**Austin:** When we first came to KubeCon, um, zero day event, you know, ask people how many people are using OpenTelemetry and it's like every hand in the room is going up, right? Like the growth of... 

**Reese:** Yeah, which was 2022. 

**Austin:** Um, the project updates room, you know, the project was given like a really small room. It was like pretty packed. Yeah. And over the years I've seen that room like get bigger and bigger. 

**Reese:** Yeah, I know they probably like a 200-seat room and there are still people standing in the back, right? 

**Austin:** Um, there was also a lot of, you know, there was a keynote yesterday that was actually the thing that I've been most excited about the growth of OpenTelemetry isn't necessarily but the opportunities that we see other people kind of taking and running with, right? 

**Reese:** Um, projects like Percy’s new vendors, new commercial solutions built on top of OpenTelemetry have been really exciting to see. 

**Austin:** Um, and I think, you know, that that's the sort of stuff that you...

**Reese:** Yeah, definitely. 

**Austin:** Yeah. It's been exciting to see it grow. I remember even like my first KubeCon was Detroit and there was, uh, there was an open observability day and then there was an OpenTelemetry unplugged with KubeCon North America and EU, which I'm super stoked about.

**Reese:** Um, what? 

**Austin:** Super busy too. We have hundreds and hundreds of people showing up for those. 

**Reese:** Yeah, it was great. 

### [00:32:18] Discussion about AI's impact on observability

**Austin:** Yeah. I mean, I feel like it's also one of those things where it's kind of like you can't really do three tracks, right? Like that's a bit like two is good. Seems like a good number, but there's observability talks, you know, throughout the week at KubeCon. I don't know. This used to be the Kubernetes club, right? This is the operations, uh, the SRE kids. And now, you know, security has a big presence in the CNCF. 

**Reese:** I think what we're seeing...

**Austin:** What I think is important is you in a lot of ways if you think about how a lot of technology that we still rely on today, you know, was built and maintained and came right, maybe someone... Maybe someone and if that's you, more power to you. Um, to America, we might need your help. 

**Austin:** Um, things became the de facto standards through whatever, you know, combination of factors happened, right? 

**Reese:** Like I think what's cool about C4 vendor you happen to use or so on and so forth. 

**Austin:** Now the downside is, you know, in 25 years my kid's going to copy me and be like, "What the what's this OpenTelemetry crap, dad?" 

**Reese:** Don't metaverse OpenTelemetry now. 

**Austin:** Oh man, also speaking of the future, yeah, we were curious about how do you think AI might impact OpenTelemetry? How it might impact or have an impact or... 

### [00:19:00] Importance of semantic conventions

**Austin:** Yeah. Uh, there's a lot of ways. I think one thing I was... So, it's funny because I was just talking to someone about this. Um, a project I've been working on kind of on the side is how to make better docs for LLMs because the documentation that we write for human beings is really good for human beings and LLMs are not human beings. They are something else. 

**Reese:** So you need to kind of give them documentation in a way that is similar to how you would give it to a human but distinct enough that it's not, you know, it's trickier than just saying like, "Oh, go read this web page," right? 

**Austin:** Because the web page has a lot of stuff that's for humans. We care about things like font sizes and colors and we care a lot about sort of the organization of information and we want to have pages that are single concept, right? So that you can focus on like what is the goal of this page and but then LLMs, there's a distinction you need. 

**Austin:** Um, you can... One interesting thing if you think about writing a document, you know, writing documentation is you're not supposed to use um, even if there's a more specific word like use more words not less, right? You have to kind of hit it at whatever reading level you expect people to be at. 

**Reese:** Even for that kind of stuff, but with LLMs, they actually don't have that disadvantage, right? 

**Austin:** Like you can give it a very large flowery word and if it's the most specific word, that's actually helpful because of the way the semantic search works. 

**Reese:** Um, precision in language is actually really important. 

**Austin:** So you wind up needing documentation that is the same documentation you give to humans because the concepts need to all match but is organized and structured in a different way, is much longer, has kind of everything in one big chunk, is optimized for the amount of tokens and the semantic values of those tokens. 

**Reese:** But the advantage of doing this right, of thinking about how do I give the LLM documentation is that LLMs are remarkable, you know, especially if you're using them as part of like AI-assisted coding, are remarkable at reducing toil. 

**Austin:** One of the things that I think, you know, all of us here have been working in observability for years and what is like the one thing nobody wants to do? Nobody wants to do a migration, right? 

**Reese:** No, you go tell someone like, "Oh, here's the new thing," they have to rewrite all this instrumentation, all these logs, all this stuff. They just be like, "Thanks, I'll pass." It's because it's a toil. It doesn't make sense, right? The existing stuff works well enough. 

**Austin:** It's maybe it could be better, but you know, we're not going to go dedicate however many engineers' lives for three months to rewrite all of our logging statements. But what if you just have an AI do it, right? 

**Reese:** The AI doesn't care. Doesn't complain. 

**Austin:** If you give it good instructions and good rules, it's able to, you know, make good decisions. 

**Reese:** Um, and it's not like you're replacing human effort, right? You're not replacing the programmer. You're not replacing the people that are responsible to maintain the system. You're easing the burden of modernizing what they're trying to do. 

**Austin:** And so you're actually benefiting those people a lot because even with, you know, improvements in AI-powered anomaly detection, whatever, right? 

**Reese:** Like we've been doing AI in observability for a while. 

**Austin:** LLMs just advance it a little bit, maybe a lot, we'll see. But even non-AI stuff, right? If you think about traditional sort of anomaly detection and heuristic-based detection, it's still machine learning. LLM machine learning. It's all machine learning. 

**Reese:** We've been doing machine learning for a while. 

**Austin:** And when you get to a certain size and complexity of your systems, you have to have it because there's just too much data for humans to process and go through. 

**Reese:** So let's figure out how we can... You know, that to me is like the impact of AI on observability on OpenTelemetry is we can make it easier for the observability tooling to understand OpenTelemetry and interpret what's happening in your system better and at the end of the day give you more time to do... 

**Austin:** We had talked about OpenTelemetry project updates, which took place yesterday, right? 

**Reese:** That sounds right. I'm losing track. 

**Austin:** Yeah, it is. It was yesterday. 

**Reese:** Milk? That doesn't sound like a good bagel. 

**Austin:** I wish it said bagel clock. This is probably a great... This is probably a great visual bit for the... 

**Reese:** And it's been... It attracted my attention ever since I came up here and now it's like I've been obsessed. I've been waiting for the appropriate moment to drop the bagel clock into the conversation. 

**Austin:** You did it. 

**Reese:** There you go. This is what we call commitment to the bit. 

**Austin:** Yes. 

**Reese:** Project update. Um, yeah, project update. 

**Austin:** So, um, can you give folks a, uh, OpenTelemetry right now is the second or first biggest project in the CNCF, depending on how you count it, but contributing across, you know, dozens and dozens of repositories. 

**Reese:** We're maintaining APIs, SDKs, tools in, you know, dozen plus languages. A lot's going on, right? 

**Austin:** At this point, the project is really too big almost to have kind of a single narrative of whatever we're doing, but there's a few areas that we wanted to focus on. 

**Reese:** We're starting to see a lot of great adoption of OpenTelemetry by the sort of broader community outside of... 

**Austin:** Just so we're starting to see more CNCF projects natively integrate OpenTelemetry. 

**Reese:** Um, we're starting to see... 

**Austin:** Are integrating OpenTelemetry into their frameworks and into the, in Dino's case, into the runtime itself, right? So if you're writing a JavaScript app and you're using Dino, you pass in a config, you don't have to do anything, which is great. That's the vision for the project. 

### [00:24:42] Updates on OpenTelemetry projects

**Reese:** So um, beyond that, you know, beyond the kind of growth we're seeing in adoption, we're seeing a few, you know, longer-term projects that we are proceeding along. 

**Austin:** So one thing that we've been working on over the past six to eight months, we've had a lot of progress there. We have a system-level profiler that is being worked on. It uses eBPF and other various technologies to let you use profiling across your services on a node. That is still in alpha like it's not done. It's not ready, but pretty soon that should be ready for people to start banging on. 

**Reese:** Another important thing we're doing is that we are evolving our logging infrastructure or logging APIs. 

**Austin:** So tradition originally we would just bridge to your existing logging API because there's a lot of those. There's log4j, there's various facades in Go and .NET and wherever, but one of the pieces of feedback we were going out and finding these sort of consistent metadata across services and libraries and domains is people need... People needed a structured way to emit structured events, right? 

**Reese:** Things like that you and I would probably call the LOG. Some people would call it an event. 

**Austin:** And one thing I have learned is that the third rail of observability is talking about logging at all because people are very, very precious about what the word logs means to them. 

**Reese:** I've noticed. 

**Austin:** Oh, true. 

**Reese:** Yeah. You don't mess with people's logs. 

**Austin:** Yes. So what we've kind of come to realize through this whole process is that we need some sort of API-level answer to that and we're pretty close to have... You know, we have some OTAs and some specs in flight on this, but the idea is that there will be an OpenTelemetry logging API that will exist to let you emit structured events. 

**Austin:** And a structured event is really just a fancy way of saying a structured log that has a known schema, right? In the same way that semantic conventions in OpenTelemetry let you apply schemas to your telemetry, to your logs, or sorry, to your metrics and traces. 

**Reese:** You'll be able to say, "Hey, here's a client-side ROM event," or "Here's a, you know, out of memory exception," or any of the various things that can happen. 

**Austin:** Um, you'll be able to say, "Hey, here's a generative AI prompt, for example." And what we'll do is you'll be able to either take that and use it like you would use a span event today and bundle it in with the span or you'll be able to emit it separately through the log record sign through the logging signal and then have your backend either stitch them together or process them independently or do whatever, right? 

**Reese:** Like once it's out of our hands, we don't really care what you do with it. 

**Austin:** But that's probably the two big in-flight things I would say. 

**Reese:** Beyond that, um, a lot of work is happening on other things. Stabilizing the collector, stabilizing various other SDKs and APIs. 

**Austin:** Um, shout out to our JavaScript SIG which just released JS SDK 2.0. 

**Reese:** Know which, uh, my understanding is this fixes a lot of problems that people have had with especially with bundling it and things around ESM modules. 

**Austin:** I don't quite know what all that is. It sounds very scary. 

**Reese:** The JS devs assure me it's very important. 

**Austin:** But seriously, I think it's actually a really good sign of the health of that project, right? That they have been able to get enough feedback about like, "Hey, these are the decisions that worked and didn't work to create a 2.0." 

**Reese:** Know, and then for an end user, I was actually talking to someone Monday, um, Sunday at Cloud Native Rejects about this who maintains an integration into OpenTelemetry into his company's product. And he was like, "Oh yeah, the migration was like five minutes," right? 

**Austin:** Wow! 

**Reese:** Because the API and the SDK are independent, so an SDK change is really very... You know, it's not a huge... It's not a lot that you have to do to take those updates. 

**Austin:** So that's something that for obviously other maintainers can't may or may not decide to do it, but we're, you know, it certainly seems that a lot of maintainers are thinking about, "Well, maybe it's a good idea to go back. It's been five, six years, right? Like you can learn a lot, you get a lot of great feedback over that time." 

**Austin:** And there's things that we would probably do differently in every language if we had a do-over. 

**Reese:** So thanks to the OpenTelemetry architecture, you can kind of get that do-over, which is cool.

**Austin:** That's great. 

**Reese:** Um, how are we on time? I'm not sure because we have... 

**Austin:** Are we on time, producer? 

**Reese:** Okay. Well, I guess this could be a good opportunity for us to plug some upcoming stuff like OpenTelemetry Community Day.

**Austin:** Yes, OpenTelemetry Community Day in Denver, Colorado coming up this summer. Um, June 25th or 26th. It's the same week as Open Source Summit. Go look on the web. Um, the CFP is closed, unfortunately, but we will be, uh, we should be announcing the schedule on that here pretty soon. 

### [00:30:24] Upcoming OpenTelemetry Community Day

**Reese:** Um, even if you aren't planning on, you know, plan on speaking, highly recommend everyone that's in the US, North America to come out to that. It's going to be a great... 

**Austin:** And we are also, no promises, but we're trying to do a community day in Europe this year. So stay tuned. If not this year, definitely next year.

**Reese:** Is it going to be part of Open Source Summit EU or that... That would be the plan, but nothing's set in stone. 

**Austin:** Um, but we've definitely... One of the fun facts at the, um, project update is that about 50% of our contributors are actually not in the US in OpenTelemetry. 

**Reese:** Um, and we've seen now that's US and then everywhere else, right? 

**Austin:** So, but if you look at... If you break it down by like region, so you go like North America, EMEA, APAC, other, then we like the line for EMEA is just like doing this and the US one is kind of doing this a little bit. 

**Reese:** So they're starting to get closer and closer together. 

**Austin:** But we've definitely, you know, one of the things I always love coming to KubeCon EU is we have so many, you know, our user community is so, you know, so vibrant here. 

**Reese:** Um, we have so many maintainers whose work is just fantastic and we really want to support our European end-user and contributor community. 

**Austin:** So we're very strongly going to be figuring out how to do a European Community Day.

**Reese:** Awesome. 

**Austin:** Oh, that's awesome. 

**Reese:** Yeah. I always love the vibe at the KubeCon EU. It's just very vibrant. 

**Austin:** And I think, um, at the keynote, um, they mentioned this was the biggest KubeCon so far. 

**Reese:** 12,000. 

**Austin:** Yeah, over 13,000 people. 

**Reese:** Over 13,000. That's the number I heard. 

**Austin:** Damn, that is wild. 

**Reese:** Yeah. No, they... I mean, I... 

**Austin:** And it's like, how's your KubeCon? And they say it's like, "Oh, it's my first." I'm like, "You're going to have that. Bring lots of water. Bring lots of water." 

**Reese:** But I love that we're still... That new people are still coming into this community, right? That we're really cool to see the growth of, you know, this community, right? 

**Austin:** Like to see it expand, to see it bring in new people, right? 

**Reese:** Like, oh my god. There's a ton of people that we know that all the three of us here know that careers, friendships, right? Friendships like that's given people the opportunity to really, you know... 

**Austin:** Yeah. 

**Reese:** Um, that's neat. 

**Austin:** Yeah. Also, it feels like a family reunion every time we're together, right? 

**Reese:** Yeah. No, it's great. It's like a family reunion with like a 10,000. 

**Austin:** Yeah. 

**Reese:** So a bunch of batteries and then we get on the other side. They have the retail technology exhibition. 

**Austin:** Yep. They actually get a red carpet. 

**Reese:** Very loud bugers walking around which was, um, exciting. It was definitely unexpected.

**Austin:** Yeah, I know. We were walking yesterday and we're like, well the tube... It was like there's like two stops. 

**Reese:** Yeah, there's a station at either end. 

**Austin:** Yeah. 

**Reese:** Yeah. 

**Austin:** And I heard that, um, it's actually faster if you time it right to take the tube. 

**Reese:** If you hit... If you hit the... 

**Austin:** It also depends on where you start from, but if you're from door to door, it's definitely faster. 

**Reese:** Yeah, it's nice. You just tap in and out. 

**Austin:** So... 

**Reese:** Oh, I know. 

**Austin:** Yeah, it's really... 

**Reese:** Discovered that. 

**Austin:** Oh, is that better than the... 

**Reese:** I just use Google Pay. 

**Austin:** Yeah, you can use your phone. 

**Reese:** Yeah. 

**Austin:** Yeah, yeah. 

**Reese:** It works well. 

**Austin:** Yeah, we have that in Toronto. I mean, we have, uh, tap in New York. They finally, um, it's Omni now. 

**Reese:** Omny instead of... 

**Austin:** This for another episode. 

### [00:34:34] Project updates and growth of OpenTelemetry

**Reese:** Um, live stream for you from KubeCon EU. Sorry guys, it's been a long week. 

**Austin:** Um, thank you so much for joining us. We will have, um, our lovely guests. 

**Reese:** Um, again, I'm Reese. This is Adriana. Thank you so much, Austin, for being here and Marilia for being here earlier. 

**Austin:** And also shout out to our behind the scenes. 

**Reese:** Um, but he is the one producing all this for you. All of our streams. 

**Austin:** Yes. 

### [00:35:17] Closing remarks and acknowledgments

**Reese:** Thank you so much and we will see you next time.

## Raw YouTube Transcript

Hello, welcome to a live stream of humans of OA. We are coming to you live from what had a little bit of subtitle issues, but we are here and we're so excited. My name is Reese. I am a senior developer relations engineer at New Relic and I am joined here by my lovely industry colleague Adriana and Marilia who is our first guest. Adriana. Hey everyone. Um, thanks for tuning in. My name is Adriana Vila. I work alongside Reese and the Hi everyone. My name is Marilis. I am a staff stops engineer at Graphana Labs and also in open telemetry. I work in a few different groups. I am a maintainer for the contributor experience and I'm an approver for if you will earlier about all the different parts that you're involved in and we're really curious because you came you started as an end user um and then eventually like started contributing. Yeah. And so we would love to on my prior job I was responsible for the observability. I used to work on cockroach labs and I was the manager for the observability there. So I started learning like I learning about hotel specifically because there we did would be able to use that like maybe someone want to see some of those things outside of the database. So we created like some endpoints here and there but it was like very basic stuff like this team is to work only on open telemetry. So your focus is just open telemetry. So this is my dayto-day I can have fun and just be on it. That's awesome. I didn't realize that. That's so cool. And and what would that new like Java and net and I want to make sure that all SDKs are on the same level and the other two were a little here. What the are the things that we can add? So we have owner for the Postgress plugin that I was already like touching and there. That's awesome. And actually you gave a talk um yesterday about database monitoring. Exactly. So one of the other big ones. So fresh news. We just this week we released the was the release candidate too. So that means by the end of the month we're going to mark as stable. So people can really start using without any concerns. So um you know you you mentioned that you're you're in the semantic convention sig for for databases and there's like a general semantic convention sig correct. What is it about the database semantic convention sig that's sig spun off? Yeah. So usually you have the general semantic conversion and on that one you have sometimes people from all of the other semantics that can give like an updates or discuss this particular name of the metric and spend an hour when you have a lot of people on the code they're not related to databases so they don't have any input to give it might be waste of time so it's kind of like you spin up like different semantic conventions for each of like oh we want to focus on database we want to focus on the HTTP we want to focus RPC See, so you now you can bring people that have experience on that area and talk about it. The same way you can think about if you would have a SI for SDK, you have so many languages. So we have now one S for each languages. So it's kind of like the same idea. Yeah. Help like keep it like the work focused and easy to prioritize. Yeah. And then we can always have the updates that we can bring to the main semantic one because the when they generate like a version is for all semantic. is not as specific for the database. So it's you just merge that repo and whenever new version come in might be bringing updates for the database might be from the HTTP and so on. So we just like can bring the update like to the main ones like hey this one we're marking as stable. We have these updates and things like that. And then you mentioned and I'm glad you uh were able to rattle off the long list of titles that you have in the community because I was like I am not going to remember all these but they're so cool. Um so there's like different titles. Um there's a prover then a prover then a tainer. Okay perfect. And then could you explain to us briefly like what each what's the distinction between each role? Yeah. So you started first the like as a contributor. So become so you can become a contributor not being a member of CNCF at all. So when you do a couple of uh contributor contributions you ask to become a member which is something I think everybody should do if you are doing because it's a very easy to join. You just have to open a VR say like hey I want to become a official member of CNCF and then oh hotel and then you are far you're officially a contributor then you pick something that is more interested to you so for example I really like this language I or I really like this specific component start joining the sex just to learn more about it see how you can help and when you start like really helping out start reviewing PRs putting comments like creating issues for things that you mind and with time you get the status of triager which is somebody that is helping when a lot of issues coming up you help exactly triage those issues and see like things that make sense things that actually they were not using correctly or there are actual bugs then from that you can become an approver that when you approve a PR your approval actually counts because people can approve but to have be able to merge you need to have people with permission giving the approval and being able able to merge. So the approver now have this whatever we approve it counts and somebody who has the permission can just merge in. And then you have the final one which is maintainer. So is the people that can actually merge usually the ones creating the releases uh creating like road maps but they do get input from everybody that that is contributing. That's so exciting. That is really cool. Thanks for the overview. Yeah. Um the other thing that we wanted to ask um you know you mentioned that you're working in the uh Portuguese localization. Um talk a little bit about that like talk about why it's important to have localization how you got involved with that specifically how that's been. Yeah. So I think it's really important because it's a barrier like the language and it's already hard for you to like completely learn something completely new like on tech but imagine if you don't even know the language and a lot of other countries like they're the first language not English it's not always you're going to find this documentation and not easily accessible for everybody. So actually I started like a while ago. I created like my own blog post and I was like everything that I'm created there I'm going to create and where people that actually met when I did like conference dur days in Brazil and there was the bad group. So I started like oh I'm going to help them out. So I like to like review a lot of things and the good things a lot of things in English that you learn like just experience living. So I can help out with like the translation like the localization and also decisions like what are the things that you don't translate at all because we're going to say tracer we don't that makes sense because at the same time you don't want to translate everything because then when they're going to search those word don't exist anywhere but we have a lot of yeah but yeah I think it's like really good to just break this barrier and bring a lot of people they would have no idea. Yeah, that's so great. That's that's a lot of work. Um I guess in in some ways has it like improved your Portuguese as a as a result. So yeah, it's always funny because like living outside for so long and sometimes you I'm going to give a talk like in Portuguese and I was like here so I know the right thing to use but it's always always a challenge but we also try because there's not only Portuguese we also have like people work on the Spanish, French and Japanese. So do completely different than the French know. We also have this thing like which is like similar to the same. So we have the documentation one but we have different groups. So every time a docs page comes out um you like the localization s translate. Yeah. So that is the idea. So right now that people are accessing more things like that. So we start with those ones and like the same thing for SDKs. I see which ones people are like downloading more. So we and some come in and do an updates on the original one. So we we do have something to because part of the when you do a localization there is a new kind of like tag that you had to put in what was the commit that you translated. Okay? Because it's really hard for people to know that somebody did an update somewhere. uh you had to really be paying attention. So the idea is to have something that would tell us, hey those are behind just catch up and things like that. So we were always up to date and Oh, sorry. Go ahead. I was curious cuz um when I was asking you um you know all your different that was like the first time I'd heard of that specifically cuz I know we have like translated some um some of our documentation but I didn't realize there were like specific teams working on these languages. Um so the localization sigs they are only translating um documentation or what all involves so like the official page like the open telemetry.io All the pages there are are the ones. If you look at the now at the top that was didn't have anything. Now if you're looking at the page the top you have a select there that you can change the language that you want. So whenever the page is translated now you have so cool learned something new today. I then joke that I have a PR with the translation to the Japanese even though I don't speak any Japanese and sometimes it goes wrong there too. Uhhuh. So it's a way to catch up. So like and then when they was like, "Okay, so the I was like, "Oh, let me see if any other languages translated the same thing wrong." Async or something. Okay. Yeah, that's pretty big. Yeah. And then it was good that it was just like a word and I translated and I put a PR and I tagged the reviewers for Japanese. I was like, I don't speak any Japanese. I put it this thing that I think is the right tradition. Like there was a part for the translation, but we even like looking for we want to add also more examples because we don't have a lot of examples. If there is something like for example you never did so you try it yourself and you might for the future one that are coming that they know like more examples more things to try it on. Yeah, man. This is so exciting. I'm learning all kinds of new things. I know. Yeah. So yeah, so many things that we're like when people ask like how do I start like so many of you're going to be able to find somewhere something that is interesting. There's always something for you, right? Yeah, it's really hard and just try joining just like listening just but at the same time like keep in mind that open source is different than a dayto-day job cuz sometimes what I see people find things was like how I I so I found the things that like oh they need help with this they need help with that and then the things that I already have priorities like from even coming like from hey can you take a look at this up for grabs a few reples have them uh so we have things like for example contribute fast that we did here and a lot of them got tagged with country fest but not all of them got actually work on so those are the ones that you know and you're going to find something and people in the community are very helpful like tag them on slack on the issue itself they are happy to give you guidance as well yeah and I'll do a shameless plug for the end user sig um as well we are always happy to have contributors um you can find more information in our show notes part of like the end user saying the other thing I want as the is the contributor experience. So if you want to like I want to contribute like what is missing. So for example one of the project that I did that was so like how do I start? I don't know how to set up locally. There was no like what is the dependency that you need. So there was like nothing there. So I work like as a mentor for the AI program template that all repos could use and started creating like the PR so people have at least the basic things that they need to just at least start having things. Oh, that's amazing. And and really quickly, actually, I want to ask about the contributor experience SIG. Um because that one's a relatively new SIG, right? Yes. Um can you tell us a little bit about that SIG, how it got started? Um and how you became a M. Was it because we saw this need of people complaining that they don't know how to start? They don't always understand like the path for like trier or like how like there is nobody there to guide. Okay, if nobody is going to be there for you, are you able to find all the documentation that you need to be able to follow the path that you want or like we didn't even know the challenges people were having a few of the things and we do like also surveys to find out people like how are you feeling like being a contributor and we started tackle the things like were the most concerned like documentation was the top one so this is why I started that project and container almost right away. What are some of the upcoming things for the contributor experiencing? So for this one, I just finished this part like this month for the template. So my next meeting is going to be actually picking up what is going to be the next one. Uh but we do have like issues open that is just helping out like clarify things to people. Uh and if anyone like also if you're listening if you have something that is really like bothering you and you need feel free to like message us or like open issue directly on the report there we can't prioritize because we have a list there but we are just prioritizing ourself because we don't have necessarily feedback things but react like thumbs up or really want this kind of thing and we will be able to put it in first. Awesome. And I think we're almost ready for our next guest. Yeah, I think we're so I guess we will continue our conversation. I I guess as as we get ready to bring on our next guest experience, they will be able to share like people just joining and people that have a lot of experience will be able to guide you as well just as I join the calls and you're going to be able to and they are Austin Parker. I'm just going to get the surprise out of the way. uh community manager for open telemetry and we are so excited to have him on. How am I still community manager? Wait, are you no longer the community manager? What? You're still community manager? Yeah, I think I am. If you go and check the uh check the repo, I probably am. I mean, I do both jobs still. So, io and a member of the open tree governance uh committee. I also have been a maintainer on the open country website uh open country demo. I've working group I guess you could say like where we combine of open census maintainers and open uh tracing maintainers where we you know came in and and worked with some people. Um yeah, what have you seen as like the biggest changes since things started? Like when when we first came to CubeCon, um zero day event, you know, ask people who's how many people are using hotel and it's like every hand in the room is going up, right? Like the growth of Yeah. which 2022 um the project updates room, you know, the project was given like a really small room. It was like pretty packed. Yeah. And over the years I've seen that room like get bigger and bigger. Yeah. I know they probably like a 200 seat room and there are still people standing in the back, right? Um there was also a lot of you know there was a keynote yesterday that was actually the thing that I've been most excited about the growth of hotel isn't open telemetry necessarily but the opportunities that we see other people kind of taking and running with right um projects like Percy's new vendors new commercial solutions built on top of open telemetry have been really exciting to see Um, and I think, you know, that that's the sort of stuff that you Yeah. Yeah. Definitely. Yeah. It's been exciting to see it grow. I I remember even uh like my first CubeCon was uh Detroit and there was uh there was an open observability day and then there was an hotel unplugged with CubeCon North America and EU, which I'm super stoked about. Um what um super busy too. We have hundreds and hundreds of people showing up for those. Yeah. It was great. Yeah. Thank you. I mean, I feel like it's also one of those things where it's kind like it's you can't really do three tracks, right? Like that's a bit like two is good. Seems like a good number, but there's observability talks, you know, throughout the week at CubeCon. I don't know. This this used to be the Kubernetes club, right? This is the operations uh the SRE kids. And now, you know, security has a big presence in the CNCF. I think what we're seeing what I what I think is important is you in a lot of ways if you think about how a lot of technology that we still rely on today you know was built and maintained and came right maybe someone maybe someone and if that's you more power to you um to America we might need your help um things became the facto standards through whatever you know combination of factors happened right like I think what's cool about C4 vendor you happen to use or so on and so forth now the downside is you know in 25 years my kid's going to copy me and be like what the what's this open telemetry crap dad um don't metaverse open telemetry now oh man also Speaking of the future, yeah, we were curious about how do you think AI might impact open telemetry? How it might how it might impact or have an impact or Yeah. Uh there's a lot of ways. I think one thing I was So, it's funny cuz I was just talking to someone about this. Um, a project I've been working on kind of on the side is how to make better docs for LLMs because the documentation that we write for human beings is really good for human beings and LLMs are not human beings. They are something else. So you you need to kind of give them documentation in a way that is similar to how you would give it to a human but but distinct enough that it's not you know it's trickier than just saying like oh go read this web page, right? cuz the web page has a lot of stuff that's for humans. We care about things like font sizes and colors and we care a lot about sort of the organization of information and we want to have pages that are single concept, right? so that you can focus on like what is the goal of this page and but then LM it's there's a distinction you need um you can you like one interesting thing if you think about writing a document you know writing documentation is you're not supposed to use um even if there's a more specific word like use more words not less right you have to kind of hit it at whatever reading level you expect people to be at even for that kind of stuff but with LMS actually don't have that disadvantage right like you can give it a very large flowery word and if it's the most specific word that's actually helpful because of the way the semantic search works. Um precision in language is actually really important. So you wind up needing documentation that is the same documentation you give to humans because the concepts need all need to all match but is organized and structured in a different way is much longer has kind of everything in one big chunk is optimized for the amount of tokens and the um semantic values of those tokens. But the advantage of doing this right of thinking about how do I give the LM documentation is that LLMs are remarkable you know especially if you're using them as part of like AI assisted coding are remarkable at reducing toil. One of the things that I think you know all of us here have been working in observability for years and what is like the one thing nobody wants to do? Nobody wants to do a migration, right? No, you go tell someone like, "Oh, here's the new thing." They have to rewrite all this instrumentation, all these logs, all this stuff. They just be like, "Thanks, I'll pass." It's cuz it's a toil. It doesn't make sense, right? The existing stuff works well enough. It's maybe it could be better, but you know, we're not going to go dedicate however many engineers lives for three months to rewrite all of our logging statements. But what if you just have an AI do it, right? The AI doesn't care. Doesn't complain. you if you give it good instructions and good rules, it's able to, you know, make good deci, you know, make pretty good decisions. Um, and it's not like you're replacing human effort, right? You're not replacing the programmer. You're not replacing the people that are responsible to maintain the system. You're easing the burden of modernizing what they're trying to do. And so you're actually benefiting those people a lot cuz even with you know improvements in AI powered anomaly detection whatever right like we've been doing AI and observability for a while um LLM's just advance it a little bit maybe a lot we'll see but even nonAI stuff right if you think about traditional sort of anomaly detection and heristic based detection it's still machine learning LM machine learning. It's all machine learning. We've been doing machine learning for a while. And when you get to a certain size and complexity of your systems, you have to have it because there's just too much data for humans to process and and go through. So let's figure out how we can you you know that to me is like the impact of AI on observability on open telemetry is we can make it easier for the a make it easier for you those your observability tooling to understand hotel and interpret what's happening your system better and at the end of the day give you more time to do we had talked about um hotel project updates um which took place yesterday right that sounds right I'm losing track I'm losing Yeah, it is. It was yesterday milk. That doesn't sound like a good bagel. It's I wish it said bagel clock. This is probably a great This is probably a great visual bit for the And it's been It attracted my attention ever since I came up here and now it's like I've been obsessed. I've been waiting for the appropriate moment to drop the bagel clock into the conversation. You did it. There you go. This is what we call commitment to the bed. Yes. I update. Um, yeah, project update. So, um, can you give folks a, uh, open telemetry right now is the second or first biggest project in the CNCF, depending on how you count it, but contributing um, across, you know, dozens and dozens of repositories. We're maintaining APIs, SDKs, tools in, you know, dozen plus languages. A lot's going on, right? And at this point, the project is really too big almost to have kind of a single narrative of whatever we're doing, but there's a few areas that we wanted to focus on. We're starting to see a lot of great adoption of open telemetry by the sort of broader community outside of uh just so we're starting to see more CNCF projects natively integrate open telemetry. um we're starting to see are integrating open telemetry into their frameworks and into the in Dino's case into the runtime itself, right? So if you're writing a JavaScript app and you're using Dino, you pass in a config, you don't have to do anything, which is great. That's the vision for the project. So um beyond that, you know, beyond the kind of growth we're seeing in adoption, we're seeing a few, you know, longerterm projects that we are proceeding uh along. So one thing that we've been working on over the past 6 to 8 months, we've had a lot of progress there. We have a system level profiler that is being worked on. It uses EVPF and other various other technologies to let you use profiling across your services on a node. That is still in alpha like it's not done. It's not ready but pretty soon um that should be ready for people to start banging on. Another important thing we're doing is that we are evolving our uh logging infrastructure or logging APIs. So tradition originally we would just bridge to your existing logging API because there's a lot of those there's logj there's various facads in go and net and wherever but one of the pieces of feedback we were going out and finding these sort of consistent metadata across services and libraries and domains is people need people needed a structured a way to emit structured events, right? Things like that you and I would probably we would call the LOG. Some people would call it an event. And one thing I have learned is that uh the third rail of observability is talking about logging at all because people are very very precious about what lo what the word logs means to them. I've noticed. Oh, true. Yeah. It's you don't mess with people's logs. Yes. So what we've kind of come to realize through this whole process is that we need some sort of API level answer to that and we're pretty close to have you know we have some OTAs and some specs in flight on this but the idea is that there will be a open telemetry logging API um that will exist to let you emit structured events and a structured event is really just a fancy way of saying a structured log that has a known schema right in the same way that semantic conventions in hotel let you apply schemas to your telemetry to your logs or sorry to your metrics and traces. You'll be able to say hey here's a client side ROM event or here's a you know out of memory exception or or any of the various things that can happen. Um, you'll be able to say, "Hey, here's a generative AI prompt, for example." And what we'll do is you'll be able to either take that and use it like you would use a span event today and bundle it in with the span or you'll be able to emit it separately through the log record sign through the logging signal and then have your backend either stitch them together or process them independently or do do whatever, right? like once once it's out of our hands, we we don't really care what you do with it. Um but that that's probably the two big inflight things I would say. Beyond that, um a lot of work is happening on other things. Stabilizing the collector, stabilizing various other SDKs and APIs. Um shout out to our JavaScript uh SIG which just released uh JS SDK 2.0 know which uh my understanding is this fixes a lot of problems that people have had with especially with bundling it um and things around ESM modules. I don't quite know what all that is. It sounds very scary. The JS devs ensure me it's very important but but seriously I I think it's actually a really good sign of the health of that project, right? That they have been able to get enough feedback about like hey these are the decisions that worked and didn't work to create a 2.0 know and then for an end user I was actually talking to someone Monday um Sunday at cloud native rejects about this who maintains a integration into open telemetry into his company's um product and he was like oh yeah the migration was like 5 minutes right wow because the API and the SDK are independent in so an SDK change is really very you know it's not a hu it's not a lot that you have to do to take those updates so that's something that for obviously other maintainers can't may or may not decide to do it but we're you know it certainly seems that a lot of maintainers are thinking about well maybe it's a good idea to go back it's been 5 6 years right like you can learn a lot you get a lot of great feedback over that time and there's things that we would probably do differently in every language if we had a doover so thanks to the hotel architecture you can kind of get that doover which is cool that's great um how are We on time. I'm not sure cuz we have uh Are we on time, producer? Okay. Well, I guess this could be a good opportunity for us to plug some upcoming stuff like Hotel Community Day. Yes, hotel community day in Denver, Colorado coming up this summer. Um June 26 20 25th or 26th it's the same week as open source summit open source summit go look on the web um the CFP is closed that unfortunately but we will be uh we should be announcing the schedule on that here pretty soon um even if you aren't planning on you know plan on speaking highly recommend everyone uh that's in the US North America to come out to that it's going to be a great And we are also, no promises, but we're trying to do a community day in Europe this year. So stay tuned. If not this year, definitely next year. Is it going to be part of Open Source Summit EU or that that would be the plan, but nothing's in set in stone. Um but we've definitely one of the fun facts at the um project update is that about 50% of our contributors are actually not in the US in hotel um and we've seen now that's US and then everywhere else right so but if you look at if you break it down by like region so you go like North America EMIA APAC other then we like the line for EMIA is just like doing this and the US one is kind of doing this a little bit. So, they're starting to they're starting to get closer and closer together. But, we've definitely, you know, one of the things I always love coming to uh CubeCon EU is we have so many, you know, our user community is so, you know, so vibrant here. Um, we have so many maintainers whose work is just fantastic and we really want to support our European um, end user and contributor community. So, we're very strongly going to be figuring out how to do a European community day. Awesome. Oh, that's awesome. Yeah. I always love the vibe at the CubeCon EU is just very vibrant. And I think um at the keynote um they mentioned this was the biggest CubeCon so far. 12,000. Yeah. Over 13,000 people. Over 13,000. That's the number I heard. Damn, that is wild. Yeah. No, they I mean I And it's like how's your CubeCon? and they say it's like, "Oh, it's my first." I'm like, "You're going to have that. Bring lots of water. Bring lots of water." But I love I love that we're still that new people are still coming into this community, right? That we're really cool to see the growth of, you know, this community, right? Like to see it expand, to see it bring in new new people, right? Like Yeah. Oh my god. There's a ton of people that we know that all the three of us here know that careers, friendships, right? friendships like that's given people the opportunity to really, you know. Yeah. Um that's neat. Yeah. Also, it feels like a family reunion every time we're together, right? Yeah. No, it's great. It's it's like a family reunion with like a 10,000. Yeah. So, a bunch of batteries and then we get on the other side. They have the retail technology exhibition. Yep. They actually get a red carpet. Very loud bugers walking around which was um exciting. It was definitely unexpected. Yeah, I know. We were walking yesterday and we're like well the tube it was like there's like two stops. Yeah, there's a station either end. Yeah. Yeah. Yeah. And I I heard that um it's actually faster if you time it right to take the tube. If you hit if you hit the um it also depends on where you start from, but if you're from door to door, it's definitely faster. Yeah, it's nice. You just tap in and out. So Oh, I know. Yeah, it's really card. Discovered that. Oh, is that better than the I just use Google Pay. Yeah, you can use your phone. Yeah, you can use your phone. Yeah. Yeah. Yeah. Works well. Yeah, we have that in Toronto. I mean, we have we have uh tap in New York. They finally um it's Omni now. Omny instead of this for another episode um live stream for you from CubeCon EU. Sorry guys, it's been a long week. Um thank you so much for joining us. We will have um our lovely guests. Um again, I'm Ree. This is Adriana. Thank you so much Austin for being here and Maria for um being here earlier. And also shout out to our behind the scenes. Um but he is the one producing all this for you. All of our streams. Yes. Henrik said from Dana Trace. Thank you so much and we will see you next time.

