# OTel Q&amp;A with Steven Swartz

Published on 2024-10-04T15:54:54Z

## Description

Join Steven Swartz in another OTel Q&A session where we discuss how OpenTelemetry is being adopted in their organization, ...

URL: https://www.youtube.com/watch?v=3c9Bnldt128

## Summary

In this YouTube Q&A session, Stephen Schwarz, a Form Engineering expert at a payment processing company, discusses his team's experience with observability using OpenTelemetry. The conversation, moderated by Dan, covers topics including the migration from a proprietary observability vendor to OpenTelemetry, the architecture and deployment strategies employed by Stephen's organization, and the challenges faced with scaling collectors. Stephen explains the use of the OpenTelemetry operator for automating instrumentation, the benefits of tail-based sampling, and the integration of Prometheus for monitoring metrics. He also shares insights on the learning curve for teams transitioning to OpenTelemetry and provides feedback for the OpenTelemetry maintainers regarding documentation and configuration examples. The session concludes with Stephen responding to audience questions, emphasizing the importance of community engagement in advancing observability practices.

## Chapters

Here are the key moments from the livestream with their corresponding timestamps:

00:00:00 Introductions and format explanation  
00:01:30 Stephen Schwarz introduces himself and his role  
00:05:00 Discussion on the architecture and programming languages used  
00:11:30 Overview of the OpenTelemetry setup and Kubernetes usage  
00:17:00 Explanation of tail sampling challenges and solutions  
00:22:00 Discussion about migrating from a proprietary observability vendor  
00:26:00 Challenges in scaling collectors and resource allocation  
00:31:00 Experience with the OpenTelemetry operator and contribution to the project  
00:37:00 Insights on manual vs. auto instrumentation in OpenTelemetry  
00:42:00 Audience Q&A session begins with various questions about implementation and best practices

# OpenTelemetry Q&A with Steven Schwarz

**Moderator:** Well, um, thank you everyone for joining. We have quite a good audience for our OpenTelemetry Q&A. We have Steven Schwarz with us today. 

**Format Note:** Just a quick note on the format which Dan actually posted in the chat. I’ll be asking Steven some questions, and then afterwards, time permitting, you’ll have the opportunity to post some questions for Steven as well using the link that Dan provided. 

---

**Moderator:** So, first things first, Steven, do you want to introduce yourself?

**Steven:** Yeah, sure! My title at work is Form Engineering, and I work for a company that does payment processing. So, when you're working with payments, you're dealing with money, and you need to be exact with your observability. My team manages all of the observability infrastructure for about a hundred technical folks. We try to be the experts in observability, sharing best practices and helping solve problems.

I joined this team almost a year ago, and the project I started on was migrating from another observability vendor that used proprietary instrumentation. We adopted OpenTelemetry and moved to a new observability vendor. Hopefully, some of those learnings are useful to others going through a similar process. 

I also really enjoyed contributing to the OpenTelemetry Collector contrib repo. I did that to unblock myself from a few bugs we faced, but it was also a great way to understand what the collectors are doing under the hood. I was completely new to Go, but the code is really approachable. I’d recommend taking a look if you haven't; it made my job a lot easier for sure.

---

**Moderator:** Thanks for the intro! Can you tell us a little bit about the architectures that you use in your organization? What programming languages are used and what’s the deployment landscape like?

**Steven:** Sure! I have an architecture diagram I can share. Is it a good time to do that?

**Moderator:** Yeah, go for it!

**Steven:** Okay, I believe my screen is visible. Everyone can see the diagram? 

**Moderator:** Yep, I can see it. Hopefully, everyone else can as well.

**Steven:** Great! Going from left to right, we can dive into specific parts that seem interesting. We are running on Kubernetes with multiple production clusters. Within each of those clusters, we are using the OpenTelemetry operator, which allows us to inject common SDK configuration into our teams' applications within their containers. It also lets us automatically turn on auto instrumentation, so we get consistent spans collected from all the apps.

Another unique part of our setup is that we are running OpenTelemetry as a sidecar. This means that alongside each instance of the application, we have a mini collector running, and the app can send all their telemetry over localhost to that sidecar. 

Currently, we are sending metrics and spans. For logs, it's a bit of a long story, but we aren't currently using logs through OpenTelemetry. For metrics, we use OpenTelemetry as sort of a hop; we also use Prometheus to scrape the sidecar before it pushes to Grafana.

Another interesting challenge we faced was getting tail sampling to work. We have spans coming from multiple Kubernetes clusters but only want to keep some of them. We don’t want to make the decision about which traces we keep until we have all the spans; maybe we wait to see if there’s an error. So, we have a separate cluster that all the spans go to in order to make that decision. We load balance to help scale that; we have collectors in that common cluster that load balance by Trace ID, so we don’t have a ton of spans piling up on one collector. That’s sort of a high-level overview of our setup.

---

**Moderator:** That's awesome! It’s really cool to see this kind of setup in real life, as I think that’s a burning question for a lot of practitioners: how do you set up your collectors? It’s nice to see that you’re using the OpenTelemetry operator. You're one of the few people I’ve spoken with recently who has been using the operator. What aspects of the operator are you currently using? Do you leverage the auto instrumentation capabilities? 

**Steven:** The main aspects we’re using are injecting the common SDK configuration. That saves us a ton of time because we don’t have to get teams to make code changes; we can manage that centrally and push it out to all the teams. 

We also use the auto instrumentation, where they just add a line to their pod configuration to get the instrumentation. The other capabilities you mentioned, we aren’t using those, but we are using the sidecar, which is part of the OpenTelemetry operator.

---

**Moderator:** I have to put a plug in for the operator; auto instrumentation is so cool! It’s a minimal effort for teams. 

**Steven:** Absolutely! The less effort you can make for teams, the better. Even getting them to add the annotation can sometimes take time, so I think it made the migration go much faster by minimizing the work they had to do.

---

**Moderator:** I wanted to ask: you mentioned that you migrated from a previous vendor using their proprietary telemetry solution. What made you decide to do that migration?

**Steven:** Cost was a big factor; it was hard to control costs with the previous vendor. Additionally, the support wasn’t good, and a lot of stakeholders were unhappy with it. We wanted more control over costs, which the collector gives us.

---

**Moderator:** Have you experienced any challenges in scaling your collectors? You mentioned that you have a sidecar deployment pattern. 

**Steven:** Yes, for the sidecars, we run one for each pod or instance of the application, so that scales on its own, which is quite nice. The tricky part with the sidecar is configuring how many resources to allocate, like how much memory to request from Kubernetes. Every application is slightly different in volume, and there’s currently no way for a specific application to request a specific amount of memory; we need to configure that in our centralized configuration. This creates a lot of coordination overhead if we want to tune that. We’ve only had to tune it for one application so far, so it's been quite easy to scale the sidecars.

---

**Moderator:** What about your load-balanced collectors? Did you encounter any challenges in setting that up?

**Steven:** Yes, there was a regression at the beginning that caused a memory leak in one of the components we were using for handling spans and metrics. That was an issue I fixed as part of my contribution to the open-source community. 

Our setup is quite memory-intensive because we have to cache our metrics in memory for Prometheus to scrape them. So, it’s been about keeping memory at a reasonable level. We use the Kubernetes Horizontal Pod Autoscaler to watch the memory of each instance of the collector and make scaling decisions based on that.

One thing I’ve noticed is that when our vendor has an outage, telemetry starts to pile up, causing a spike in CPU and memory. If the outage lasts a long time, the memory usage could become a problem for the collectors.

---

**Moderator:** Going back to the OpenTelemetry operator, what made you decide to use it in the first place?

**Steven:** I heard about it from a colleague, who recommended it. It fit with the platform ethos of trying to get out of the way of developers and allowing them to do things without needing to be heavily involved.

---

**Moderator:** What was your experience running it? Did you find it straightforward?

**Steven:** Generally, it was very smooth compared to the collector itself. When we had minor issues, the maintainers were very responsive in the Slack channels.

---

**Moderator:** Are you building your own collector distribution?

**Steven:** Yes, we are. When we faced some bugs, we couldn’t wait for them to be pushed to the main distribution, so we forked it to fix issues earlier. Once that happened, we started making other changes, so it’s been a bit hard to get off the fork, but it’s something we want to do.

---

**Moderator:** Does that involve using the OpenTelemetry Collector Builder tool when you deploy your collectors?

**Steven:** Yes, we are using that tool. We copied the list of components from the Dockerfile to build it.

---

**Moderator:** You mentioned your own customizations, which led you to contribute back to the collector. How was that experience?

**Steven:** It was a good experience. People were helpful during the code review. It took a while to get the code merged, though, and I had to deal with merge conflicts due to version upgrades. I think there’s room to merge things faster after approval to avoid those conflicts.

---

**Moderator:** Have you done any manual instrumentation as well?

**Steven:** Yes, we had to show teams how to convert their manual instrumentation from the proprietary format to the OpenTelemetry format. It’s still a slow process; I think the benefits of tracing aren’t obvious to everyone, so I need to provide more examples of why it’s useful to motivate teams to add more metadata to their spans.

---

**Moderator:** Does your team ever get asked to instrument stuff for other teams?

**Steven:** Not specifically for their applications, and I’m glad to hear that. 

---

**Moderator:** I noticed from your diagram that it looks like you're primarily using Java apps. Is that correct?

**Steven:** Yes, mostly Java. We do have some Go as well.

---

**Moderator:** How did you find the learning curve for instrumenting stuff in OpenTelemetry?

**Steven:** Java has a good API, and the instrumentation process is pretty intuitive. We use Micrometer, a Java library for metrics, so the teams didn't have to change anything to get the metrics to work. With Go, it’s a bit more manual and harder to use than the Java one. I’m curious if anyone has used the auto instrumentation for Go; we aren't currently using it, but it would be nice to get that working.

---

**Moderator:** Do you have any general feedback for the OpenTelemetry maintainers about your experience?

**Steven:** I think we figured out a lot by ourselves, and it took several iterations to get to this point. More example configurations would be helpful for common problems, like tail sampling. Monitoring collectors is another area where I had to dig through the codebase to find what metrics are exposed, so documentation on useful metrics to monitor would be great.

---

**Moderator:** Thank you for the feedback, Steven. Now, let’s check the questions from the audience.

---

**Dan (Moderator):** We have many questions from the audience, which is great! Feel free to vote for the ones you find most interesting. I have marked one of them as answered already. 

Starting with the question about tail sampling: Do you only use tail-based sampling, or do you also use head-based sampling?

**Steven:** We only use tail sampling. It’s more work to set up, but having the full trace to make sampling decisions allows us to make the best choices.

---

**Dan:** How do you handle container sizing on the collector sidecars? 

**Steven:** We don’t have one size that fits all. It would be nice if pods could add an annotation for the resources they need. Currently, we have a centralized configuration that creates sidecar configurations for different resource combinations, which requires coordination.

---

**Dan:** Do you use serverless? If so, do you have any tips for instrumenting serverless workloads with OpenTelemetry?

**Steven:** We don’t use serverless, so I don’t have any advice there.

---

**Dan:** You mentioned using FluentD for logs. Are you considering moving to the OpenTelemetry log file receiver?

**Steven:** It's something I’d like to explore. We had issues with logs initially, so we pivoted to using FluentD, but I’m curious to see if others have found good solutions for durability in logs.

---

**Dan:** Regarding monitoring your collectors, do you use OpenTelemetry to monitor your OpenTelemetry collectors?

**Steven:** Yes, we use Prometheus to get metrics from the collectors and FluentD to collect logs, and that’s worked pretty well.

---

**Dan:** You have a dedicated platform team managing the collectors. Do you have thoughts on not having a collector gateway and sending telemetry data directly to your observability provider?

**Steven:** We decided to use collectors to control costs and provide durability if the vendor goes down. While it simplifies things, there are trade-offs.

---

**Dan:** Do you find that developers are aware of auto instrumentation, or do they tend to do manual instrumentation unnecessarily?

**Steven:** Yes, we have seen some redundant data from applications that instrument on their own. It comes down to education and tracking cardinality to help teams understand when they can disable unnecessary instrumentation.

---

**Dan:** How do you manage sampling policies? Can teams dial that configuration themselves?

**Steven:** We have a simple setup where we sample based on errors and trace lengths. Teams can force sampling by adding an attribute to their span, but we monitor its use to prevent issues.

---

**Dan:** Do you currently use any configuration that may not be supported through environment variables, like metric views?

**Steven:** We haven’t had to do that much. When we do, we usually show teams a merge request to copy paste from our configurations.

---

**Dan:** How do you handle supply chain security for the OpenTelemetry SDKs? 

**Steven:** I created a wrapper dependency to manage OpenTelemetry library versions that work together, but it can cause dependency conflicts in some cases.

---

**Dan:** Is the OpenTelemetry operator your preferred solution, or can it be used in parallel with SDKs?

**Steven:** So far, we haven’t had issues with teams deviating from the injected configurations, but I’m curious how that will evolve over time.

---

**Dan:** Are developers using the LGTM Docker container from Grafana for local testing and troubleshooting OpenTelemetry implementations?

**Steven:** Not yet; they can only test by deploying to our clusters. We need a better local testing solution.

---

**Dan:** If you had a magic wand, what would you love to add, remove, or change in OpenTelemetry and why?

**Steven:** I would get rid of Prometheus in our architecture because we rely on it for aggregating data for cost savings. The collector doesn’t currently offer that functionality, so it would simplify our architecture.

---

**Dan:** Are you using multiple OpenTelemetry backends for processing, or does everything go to one vendor?

**Steven:** We have one vendor that we’re pushing to; we don’t push anything internally to anywhere else.

---

**Dan:** Given the potential for bottlenecks in collectors, do you see disadvantages in having the SDK export data directly to the back end?

**Steven:** It could be easier to handle smaller amounts of data directly from the pods, but it shifts the back pressure to the application, which could be impactful.

---

**Moderator:** Thank you, Steven, for joining us today and for answering all these questions. It was great to see such engagement from the audience! 

**Steven:** Thank you, Dan, for hosting this and thanks to everyone for the great questions. It’s a topic that really interests people, and I appreciate the engagement. 

If anyone out there would like to participate in OpenTelemetry Q&A or OpenTelemetry in practice, we’re always looking for folks to share their use cases. You can DM either Dan Reyes or me or message us in the user channel in the CNCF Slack. 

We’ll post the recording of this session on YouTube, so let anyone know who may have missed it. Thank you again, everyone!

## Raw YouTube Transcript

well um thank you everyone for joining we have quite a uh a good audience for um for otel Q&A um we have uh Steven Schwarz uh today with us now um just a quick note on the format oh which Dan actually posted in the chat awesome um yeah so there I'll be asking Steph some questions and then afterwards um time permitting you'll have uh the opportunity to post some questions for Stephen as well in the uh in the link that Dan provided so um all right so first things first um Stephen do you want to introduce yourself yeah sure so uh my title at work is uh Form Engineering and I work for a company uh they do Payment Processing so you know when you're working with payments you're working with your money you need to be uh kind of exact with your your observability um what my team does is we manage all of the observability infrastructure we've got about a hundred uh technical folks that we're we're managing it for uh and we try and be sort of like the experts and observability and and share some of the best practices and you know help them solve their problems um so I recently join or I joined this team about almost a year ago and the project that I started on was actually migrating from uh another observability vendor where we're using proprietary instrumentation uh and we adopted open Telemetry and we moved to a new observability vendor uh so hopefully some of those learnings are you know useful to other uh folks going through that process um and also worth calling out is that I really enjoyed uh contributing to the open Telemetry collector contrib repo uh I had to do that to um unblock myself with a few bugs that we face but it was also just a really good way to uh you know understand what the collectors are doing under the hood uh I was completely new to goang but the the code is really approachable so yeah I I'd recommend taking a look if you haven't it's it's uh it made my job a lot easier for sure that's great thanks for the uh thanks for the intro now can you uh tell us a little bit about like uh the architectures that you use um in your organization like what programming languages are used and deployment landscape that kind of thing yeah so I have that architecture diagram I shared with you would it be a good time to share that yeah yeah go for it okay all right so believe my screen is visible everyone can see a diagram yep I can see it hopefully everyone else can as well well okay so go kind of left to right we can dive into uh specific parts that seem interesting um so we are running on kubernetes um we have multiple production clusters um and within each of those clusters we are using uh the open Telemetry operator uh and that gives us a way to inject like common configuration uh of the SDK into our uh you know our teams applications into their containers um and it also lets us to automatically turn on auto instrumentation uh so we get uh consistent spans collected uh from all of the all the apps and another uh sort of unique part is we we are using the open Telemetry uh we're running open tetes as a side car um meaning that uh alongside each instance of the application we we have a mini collector running and the app can send all their Telemetry over local hosts uh to that Sidecar um so we are currently sending metrics and spans uh logs we it's a bit of a long story but we we aren't currently using logs through open Telemetry um for metrics so we we use open Telemetry but it as sort of like a hop we we also use Prometheus um to scrape the side car before it pushes to uh grafana and another interesting uh challenge was um getting tail sampling to work um because we have spans coming from multiple kubernetes clusters and we only want to keep some of them um but we don't want to make the decision about which traces we keep until we have all the spans maybe we wait to see if there's an error um so uh we have a separate cluster that all the spans go to to make that decision um and we uh we load balance uh just to to help scale that we have these uh collectors in that common cluster they just uh load balance by Trace ID so we don't have a ton of spans piling up on on one collector and uh yeah that's sort of like a high level overview of our setup that's awesome um it's really cool to see like uh this kind of setup out in in real life because I think that's uh I do feel like that's kind of a burning question with with a lot of um our our practitioners is like how do you set up your collectors um so it's it's very nice to see um and and cool that you're using the open Telemetry operator um I think one of you're one of the few people that I've I've spoken with that's not to say people don't use the operator um but you're you're definitely one of the few people I've spoken with um recently who who has been using the operator uh what aspects of the operator are you currently using like do you do you leverage like the auto instrumentation do you um leverage the opamp capabilities um what's the other one uh for and due leverage like the The Collector uh deployment cap cap abilities like to you use all three or or combination uh so the main ones we're using are just you know injecting the common SDK configuration um that that saves us a ton of time we don't have to get teams to make code changes we can just manage that centrally and kind of push it out uh to all the teams um same with the auto instrumentation uh they just add you know a line to their configuration of their uh you know their pod and then they get the instrumentation um the other ones you mentioned we we aren't using but we are using the the side car which is the open Telemetry operator inject cool cool um yeah I I have to like put a plug for the operator um Auto instrumentation it is actually so cool it like you literally don't have to write code you just put an annotation in manifest and then well and and the uh instrumentation CR of course that you have to figure but like it's pretty cool I have to say um yeah yeah you know the least effort you can make for teams the better like even getting them to add The annotation you know can sometimes take time so uh it's it's yeah I think it made the migration go much faster being able to uh you know minimize the amount of work they have to do absolutely now um I wanted to ask because you you mentioned that you you had migrated from from a previous vendor using their own proprietary um Telemetry solution um what what what made you decide to do that migration yeah so um cost was a big one it was hard to control in previous vendor um and I guess support wasn't good so those are I think the main drivers I think just a lot of stakeholders were unhappy with it um and we wanted a bit more The Collector gives us a lot of control over uh cost um that this other vendor doesn't right right yeah that makes that makes a lot of sense now um another thing that I wanted to ask in terms of um scaling your collectors like have you experienced any uh any challenges in in scaling your your collectors because uh you know you mentioned that you have a sidecar deployment pattern um how many how many different side cars are you running at at a particular point in time like is it a lot that you're managing um yeah so the and for the side cards so we run one for each pod or instance of the application so that kind of almost scales on its own which is quite nice um so that that works um the tricky part with the sidecar is uh configuring the like how many resources to allocate like how much memory to ask from kubernetes uh just because every application you know is slightly different in their volume and um so and there's not really there currently there's not a way to uh like at the app for a specific application they can't say that they want a specific amount of memory we need to configure that in our centralized configuration so it creates a lot of coordination overhead if we want to tune that right um but we've only had to tune it I think for one one application so far um one of our monolist so that that has it's actually been quite easy to scale this uh the side C okay that's great that's great now what about uh what about your load balanced uh collectors um how have you did you encounter any like challenges in in setting that up yeah uh well I mean at the beginning we uh there's I think a regression that caused the memory leak um in one of the components we're using the span metrics one um so that that was a problem that was actually one of the things that I I fixed uh as like the open source contribution um and I guess our the way our setup is quite memory intensive because we have to Cache our metrics in memory uh for Prometheus to scrape them um so yeah it's really been a matter of keeping memory uh man I guess at a reasonable level um so right now we use uh the kubernetes horizontal pod a scaler to that watches the memory of the each of the instances of The Collector and it makes scaling decisions based on that yeah um it it works pretty well took some uh tinkering um one thing I've noticed and maybe other I'd be curious if other people have a good solution for this is when our vendor graa has because we're using when they have an outage uh I find the Telemetry starts to pile up um waiting for service to be restored and we see this big spike in CPU and memory so it's quite hard to uh uh I guess like I think if the outage were to go for quite a while probably the memory usage would just start to kill the kill the uh collectors or be very high uh so that's a bit of a problem um we still have right right um now another question that I had for you um just going back to the um Hotel operator um what made you decide to use the operator in the first place is it something that you had been made aware of or someone like did did you hear about it from from folks in the community uh so I I heard about it actually from a colleague um so it was their recommendation but it fit with the kind of platform I guess ethos of uh you know just getting try to get out of the way of the developers and yeah um you know have a way to uh I guess do things without the developers having to get involved right right yeah fair enough that that is one thing I I like about the operator now what was your experience in in in running it like was it something that you felt was straightforward um because I mean one of the things that's that we really value about these sessions is not only like learning how you're using these things in real life but also like learning like your user experience with using components of open Telemetry so um is it's something where felt like it was documented well enough did you have to do a little bit of digging poke around ask some questions in the operator slack um it was I'd say generally like compared to the collector itself it was very smooth but I guess it's a I mean anyways I'm not sure why that is but uh yeah it worked quite well um and the maintainers are when we did have sort of minor issues maintainers were very responsive in the slack channels awesome that that's good to hear i' I've had always really good experience also with the hotel operator maintainers so that's that's nice to hear as well great um now the other thing that I wanted to ask is um have you when you're using your collectors um are your are you building your own collector distribution um yeah we are um and that was because we uh when we fac some of those bugs um we couldn't wait until it was push to the main distribution um so we fored it just to to fix it earlier and then once that happened we kind of just had we started to make oh other changes so it's a bit hard to get off the fork now but it's something we do want to do now is that um does that involve using the otel collector Builder tool um when you're when you're deploying your your collectors um yeah it does uh I looked at sort of the the basically the docker file how they build the conty bro and just kind of copied uh the commands from there oh okay okay have you have you used the actual because there's um there's a a a tool where you basically specify like the components like which receivers which processors Etc that you want to include did you have you tried using that Tool uh yeah yes that's what we're using uh to build it uh we we copied like the list of components yeah oh okay okay got it got it sorry I misunderstood you um awesome um and you know you mentioned you you uh did your your own customizations and that um that kind of forced you to contribute uh back to the collector how is which is it sounds like you know it ended up being like a win-win for your team um how was the how was the experience of contributing back to the collector overall yeah it was um it was a good experience the you know people were helpful in uh you know during the code review it took a little while to get uh the code merged maybe this is a like I noticed um you know you'd have a separate person for approving it and then it would sit unmerged for a few weeks and then you get all these merge conflicts because like the the versions would be upgraded so I had to you know go back and update the go mod files a bunch of times so that that was I think maybe there's room to like once someone proves it to maybe merge it a bit faster but I don't know the sort of the rationale behind that yeah fair enough fair enough um and um the other thing I wanted to ask um you know what um you you mentioned that you um uh you mentioned that you use Auto instrumentation have you done any manual instrumentation as well yeah so the um yeah we we had to show teams because we had manual instrumentation using that proprietary format so we had to show teams how to convert it over to the otel format and then also educate them on how to um you know use otel manual instrumentation and how did that go um was did you find that teams were were um receptive to that um it's still I think they're slowly slowly doing it um it's I think tracing isn't maybe like the power of or the benefits of tracing isn't maybe as obvious so I think probably I just need more examples of like why it's useful to give them the motivation to to add more metadata to their spans for example right right right um now does does your team ever get asked to like instrument stuff for other teams um not uh not specifically for their applications yeah I'm very glad to hear one of my observability pet peeves well that's that's good to hear and so it looks like um now in terms of um the the instrumentation like it looks from your diagram that it's primarily like a Java app is that correct uh yeah yeah mostly Java we do have some some goang as well okay um now um have you um how did you find it in terms of like um you know all all the the stuff aside like the learning curve for for instrumenting stuff in open Telemetry um how did you find it like since you in a position to teach folks how to instrument their code with open Telemetry was it a big learning curve for your team as far as understanding how the uh how to how the manual instrumentation works worked for like both Java and go like did you notice any um anything that was like maybe easier in one language compared to the other or where you had to go back to the sigs to ask for clarification yeah the uh so Java it they've done a really good job with it I think the language just makes it easier um so yeah there because we use um like the kind of we use that micrometer which is like a Java library for mitting met metrics so they didn't actually have to change anything to get the metrics to work oh okay got it um and yeah the and the span API is pretty uh pretty intuitive as well U goaling I mean it's not my that's not my personal strength but I found it's a bit more manual uh it was it's definitely harder to use than the uh the Java one and right I'm curious if anyone's if anyone's used the auto instrumentation I haven't had a chance to play around with that but uh that would be we we're not currently using it for goaling but it would be nice if we could get that working yeah for folks uh for folks who are listening uh does anyone have have experience with that that would like to uh to share feel free to raise your hand if you do have any experience no takers all right um okay um the uh guess we're I'm just about done asking the questions um the only other thing is that I was going to ask is do you have any general feedback that you wanted to uh provide um to you know the open Telemetry maintainers around like your open to infmetry experience as far as like um using components like e of use uh you know you mentioned the the contribution experience you said it was a little bit challenging with with approving the PRS um anything else that you wanted to add to that um I think uh like it felt like we were kind of figuring out a lot of a lot of stuff out uh for ourselves uh like it took us quite a few iterations actually to get to this point um it might be hard to have a rest for every combination of like you know vendor and backend and and all that so that could be part of the problem um yeah I guess like more sort of uh example configuration or would be you know would be helpful like uh for example the these load balancing originally we actually had another set of uh collectors that all they did was load balancing yeah um but we realized oh we can actually load balance that you know th this deployment of collectors can low balance to itself um and that just is way easier to maintain so um yeah and I guess like sort of example configuration for common problems like tail sampling that we're doing right here right yeah that's really good piece of feedback I have heard from other folks as well that uh because you know we have the open Telemetry uh demo which is a great Showcase of I think it's really focused on on application instrumentation which is awesome um but I think there is definitely like a a desire from the community as far as um having some um like more collector specific use cases um and and specifically like stuff that's a little bit more complex than than what you would necessarily see in in the demo yeah for sure um another one is uh monitoring your collectors um I found I had to kind of dig through the code base to find like what metrics exposed like what are they doing um and I feel like that's probably there's probably some commment alerts or things that for most setups would be useful so maybe someone already has this but like uh you know some some we can document like hey these are useful things to monitor um the the actually the the dashboard that that for grafana they have that was pretty useful but uh I think on the alert side that would be uh that was I didn't find anything uh there right right cool well thank you for the feedback on that um now I guess we could um we can do one of two things uh we've got the uh the lean coffee board where folks can post questions for Stephen so I'm actually going to check the board oh we have some questions um yeah let's let's go through that and then if we have some time afterwards then Stephen you can ask some questions um to to our uh viewers as well okay okay um Dan do you wna do you want to take it on from here on uh the the questions from the board sure thing we've got many questions from the audience which is great um also feel free to go and vote for the ones that you think um are the most interesting there I have marked one of them as answered already because we talked about the collector um Builder and how you build your own dist for the collector on your side car uh starting from the the one that we talked about tail B uh sampling a little bit how you do the the how you use the obey sampling um but I wanted to ask this question here is like do you only use tail based sampling or do you also use head-based and any tips or uh thoughts on mixing these approaches uh yeah so we only use um tail sampling um I guess it if you like it's it's more work to get it set up but when you have the full Trace to make your sampling decision I find that you can make the the best decision um so yeah that's why we we just lean on tail sampling completely I guess we head B head Bas sampling there's always a risk and you're going to miss something important right because it's completely probabalistic so um yeah good point and moving on to the next one um how do you handle container sizing on the collector sidec cars you mentioned this already uh that you had to customize or tune one of the collector's uh collector sizes so do you have one size that fits all or anything you would like to improve in that setup or like resource allocation yeah so um I think what would be nice is if pods could add like an annotation or you know saying this is the resources I need uh instead what we have to do is kind of hacky um so for each side car it's like a separate res like kubernetes resource or configuration uh file so what we do is we have like a for Loop that goes through and creates uh those configurations for different resource uh combinations um so and so it's something we have to coordinate like hey you have to okay update the sidec card configuration that your pod wants to use to this otel sidecar 500 megabytes one CPU or you know so it's it's a bit of it's it's an extra coordination work there uh yeah cool um yeah okay next one is related to serverless um if you if you use serverless and um you know any tips or goas to look out for in instrumented serverless workloads with open Telemetry we don't use servus so don't have any uh advice there that's fine yeah I mean I I wanted to ask that in in case you you had some experience with that um also you mentioned that use fluent D for logs reading from standard out um are you considering moving to the otel lock file receiver um yeah it's something I'd like to explore we we sort of had a bit of a issue when we first tried using logs I'm curious if anyone has found a good solution for this um so what we wanted to do is uh like dur store our logs on disk so if there's like an outage we don't lose them um we ran into a bug with um the durable storage extension in The Collector uh and that kind of spooked us and we already had fluent D running so that's why we we kind of just pivoted to that but I don't know that was a while ago maybe and maybe people have had good success with with getting that durability uh for their logs yeah just to add on this uh with flu and D are you decorating your Logs with some of it semantic conventions or Trace ID span ID that you can so you can then correlate with your traces yeah we uh so we definitely have the logs and oh sorry the trace IDs and the span IDs and we're actually um adopting there's um a specification for the event uh I guess they call it like log events so it's sort of a structured format for logs uh in the opland Telemetry specification um so we're trying that out uh as well um yeah cool um do you use oel to monitor otel collectors and U we use um yeah it's like a big uh it's always speak Bol mud uh monitoring your monitoring but so these Prometheus to get the metrics from the collectors and fluent to collect the logs from the collectors and that that's worked pretty well um okay moving on to a bit more of your talking about your teams sounds like you uh you folks have DED a dedicated platform team uh that manages the oo collectors in your organization do you have any thoughts on the opposite of this where you have no collector Gateway or no collector um endpoint basically 100% of your Telemetry data is then sent to your observability provider uh yeah I guess in our case um we decided to use the collectors so that we could um do sampling uh to control costs of our traces um and also to try and um you know have some durability if uh I guess the vendor goes down we can kind of move that like retry logic and um off to the collector um yeah I'm curious if anyone has if anyone's doing that in in production it would definitely simplify things but I guess there's some tradeoffs as well there yeah I guess there's a trade-off as well of um authentication to a provider and so right is to sell in one place as well some of the benefits pros and cons I guess right um the next one it's related to um well we talked about Auto instrumentation the auto operator and how you inject those instrumentation packages and then we also talked about the fact that you are also using um like custom manual instrumentation um I guess the question is how do you find if your have your teams found that auto instrumentation is sufficient or is there a lot of custom instrumentation that's needed yeah so uh one thing I haven't talked about that I want to call it Les been great for us is um the SP metrics um component um so we we know we generate metrics so uh you know frequency latency eror error counts for every single span um and because we're using the automous instrumentation um every application emits the spans in the same format so basically out of the box without adding any uh instrumentation we get like I guess some vors call like APM or like red metrics so like all your API calls all your database queries um we have metrics on that automatically um so that that goes quite a long way and we can build like comment dashboards and commment alerts uh that all all these apps just get out of the box uh because of that standardization so it's a really good starting point um and then I guess so I like that is probably quite good but then if teams want to add metadata they they can um so yeah I would definitely recommend SP metrics uh if if that's like option for for people yeah I'm going to add a bit to this one as well do you find that you're as in like if you're moving from a from a from a world where like you know you had to instrument everything and now there is a lot of Auto instrumentation out there do you find that Engineers normally tend to not know about that auto instrumentation and they do it themselves so how do you manage that sort of like I guess learning or education piece saying that you may not need to instrument things is that is that has it been a challenge within your organization or everyone just uh yeah I i' say it is like we have some redundant uh like for example our API metrics like spring Boot and Java automatically emits some metrics so a lot of applications were getting some redundant data um so so yeah that that has been a problem uh but yeah so I guess it just comes down education and then having a way of tracking the cardinality if uh so when we've seen that like oh you're sending a ton of API metrics and we already have a capture the span metrics we can reach out to that team and say oh you can you can probably disable this you don't you don't really need this we don't even pay for it cool um regarding samplin um and then I'm assuming this is related to sampling policies can you advise on the is that the collector where you manage the policies for all traces or can teams Dial Dial that config up and down themselves uh so ours ours is pretty simple um so we sample you know errors we keep if the trace is longer than at something like 5 Seconds we keep but we do have an escape hatch if they add an attribute to their span to force sampling uh so far no one has like hasn't caused any problems um it might in the future you know teams overuse it but uh that that's work that's works so far and um related to some of that SDK conflict that you currently inject through the through the through environment variables um do you currently use any type of um other confli that may not be supported through environment variables like metric views for example is that do you have a way to apply defaults across the board for that type of uh config um I'm just reading the question oh I see um we haven't had to do that too much and when we have um we do have I mean our I guess our company's lucky and that we have sort of a tool that we can use to um it sort of generates uh applications from scratch um and then there's a way to sort of regenerate it the Regeneration doesn't work too well but um we know that most teams have a pretty similar format to their application so when we do need to make a change that we can't do with the operator um it's usually just boiler plate copy paste we can show them a merge request and they can copy it in but it does take you know can take a couple months for every team to adopt that cool okay um I guess one related to supply chain security um with the AEL sdks um so that do you how do you handle supply chain security so that otel sdks are safe to include them in application code or do you build them from sour yourself and then run your own security tests uh are you thinking this would be you know if there's like a c CB in one of the SDK versions how would we sort of manage patching that for everyone or I guess yeah or Downstream um or Upstream dependencies from from hotel packages yeah yeah um I mean for different reason I kind of created a wrapper dependency um that wraps like all the all the otel library versions that we use and we know they work together um just because we we found some versions were kind of incompatible um so from the app team's perspective they depend on one uh one dependency and then they get all the otel dependencies as transitive dependencies um so I suppose if we were to you know if there we need to upgrade it very quickly I guess it would just be one thing that they need to update um although that create like it works in theory but then it's also caused uh dependency conflicts just because at least how Maven Works in Java so I don't know if that's actually the best thing to do it might be more of a headache than it's worth cool um thank you okay so moving on to the next one uh related to um yeah so the auto operator and automatic instrumentation is that your preferred solution or can the oel operator used in parallel with sdks for example they not net in the case of the the person asking this question and you provide some balance of scalability and config configurability is there a recommendation here my immediate concern is that the manual instrumentation inside the application could make it difficult to configure and manage um at scale so it's this sort of like how how to balance um giving teams the flexibility to add manual sort of configuration and customization and then versus the sort of defaults that we inject for them um yeah so I mean so far we do I guess you know you can't override um the environment variables that are injected into um into the application automatically by the platform team uh um so far I guess it hasn't been uh too much of a problem um with teams teams haven't really wanted to deviate Too Much from the configuration that we've given them but yeah be curious longer term if that does cause problems thank you um that one this is an interesting one are your devs um using the lgtm docker container from grafana to develop Hotel implementation and then do local troubleshooting uh not yet right now they can only really test it and by deploying it to our clusters so we do need a better solution there um so they can test locally yeah I personally love there's like more and more solutions coming up that are open source that allow you to see that Telemetry in your own um computer I just testing uh so yeah a lot of uh really cool Solutions out there at the moment if you had a magic wand what's the thing that you would love to add remove or change in otel and why that is a logic question yeah I mean I think this is maybe short short cited but um if we could get rid of Prometheus in our architexture and the reasons we can't um right now is because we rely on Prometheus to um kind of aggregate our data together for cost savings um Source band metrics we we generate like 50 buckets uh histogram buckets for every span so it's it gets really expensive um and if each pod is you know has its own set of 50 buckets uh are cost scales with a number of PODS but we use Prometheus um to kind of like aggregate all the counts from all the pods and that like Cuts our cost significantly um I don't think the collector can do that today um so yeah that would I mean that would just make our architecture simpler makes sense um are you using multiple otel backends uh to process some of the things that internally uh compared to compared to your vendor or is it everything going to the vendor I guess um we have uh one one vendor if that that was the question that we're pushing to yeah so I guess but you're not um you're not pushing anything internally to anywhere else just everything goes to oh right yeah yeah we don't uh yeah okay and I think we've got time for one last one and that is given that the collector can quickly become a bottleneck due to back pressure and do you see any disadvantages having the SDK export that data directly to the back end except for the cost um con yeah I think that was similar to the other question about like why not just push directly to you know that your vendor from your your pod yeah it um it does make it easier to kind of scale you don't have to worry well yeah that's a good question I guess you're Shifting the back pressure then to your Apple um and then I'm then so yeah it might be though easier to handle if it's smaller amount of data but uh yeah that one I don't I don't I'm not too sure about Ben slots that' be interesting to discuss yeah that's um maybe easier to handle but also more impactful for the application so I guess there are pros and cons there as well right so if you're if you have your all your telemetry s of like shipped from your or out of your pod as soon as possible there are benefits for that as well right in terms of impacts so it's failed somewhere else in your infrastructure um because there will be at some point if your back end is down but um yeah pros and cons that's everything yeah and it seems like just looking at least the Java SDK they're pretty conservative about how much data piles up like I think it's like 1,000 24 spans is the max that will like buffer a memory before some low number that before we'll start dropping it because I guess they're really trying to lower the you know the footprint on the the application yeah exactly okay I think that's all we have time for um thank you very much Stephen for joining us we have we that was quite a lot of questions we went through from the audience uh thanks for everyone that joined and asked questions as well uh super nice to see uh engagement in as a session Q&A uh do you want to say a few words to um say goodbye yeah thanks uh thanks Dan and thanks for uh for doing the uh the questions yeah it's really nice to see the uh the engagement from from folks um in the uh in in the Q&A um I think this is a topic that really interests people so um we we love it when you engage also if anyone out there would like to participate in otel Q&A or otel in practice we are always looking for folks to share their use cases with us um you can just uh you can either DM either Dan reys or me um or if uh if you want you can also um just message Us in -- n- user our channel in the cncf slack um we are we we will be happy to hear your your use cases and have conversations and also as I mentioned recording for this will be up on YouTube so um anyone that you know that wishes they had attended but could not attend um let them know um we'll we usually post on the otel socials and also in the channel um once the video is up and thank you Stephen for for joining us um and and answering all the various questions we really appreciate your time yeah that was a lot of fun uh yeah thank you for hosting this

