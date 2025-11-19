# OTel/Prometheus Interoperability User Feedback Panel

Published on 2024-05-01T19:33:21Z

## Description

In this panel, a joint venture of the #OpenTelemetry End User SIG and the OTel/Prometheus Working Group, moderator David ...

URL: https://www.youtube.com/watch?v=9a3ctZhJj-o

## Summary

The YouTube video features a panel discussion on Prometheus and OpenTelemetry (OTEL) interoperability, moderated by David Ashpole from Google. The panelists include Iris, Nikos Takas, Vijay Samuel, and Dan Bromitt, who share their experiences with using Prometheus and OTEL in their observability stacks. The discussion covers various topics, including challenges faced in integrating these tools, the importance of maintaining compatibility to avoid breaking changes, and the need for consistent metric collection practices. The panelists express a desire for improved features in future versions, such as enhanced OTLP support and standardized naming conventions to streamline the user experience. Overall, the conversation highlights the complexities of observability in large organizations and the ongoing efforts to enhance the integration between Prometheus and OpenTelemetry.

## Chapters

00:00:00 Introductions and panelist overview  
00:05:00 Dan discusses his observability stack and challenges with store environments  
00:08:30 Vijay explains instrumentation and Prometheus/OpenTelemetry setup  
00:12:00 Nicholas shares current use of OpenTelemetry and challenges with resource consumption  
00:14:30 Iris talks about using Victoria Metrics and experimenting with OpenTelemetry  
00:20:00 Discussion on the challenges of adopting OpenTelemetry and Prometheus together  
00:26:00 Panelists share feedback on upcoming features in Prometheus 2.0 and 3.0  
00:30:00 Discussion about the impact of breaking changes in large organizations  
00:37:00 Panelists provide thoughts on the benefit of OTLP support and configuration simplicity  
00:42:00 Audience participation and final remarks from panelists

# Prometheus OTEL Interoperability Panel Transcript

**Welcome and Introductions**

Everyone who's able to join for this Prometheus OTEL interoperability panel, David reached out to us to see if we could get some end-user feedback on ensuring that Prometheus and OpenTelemetry (OTEL) work well together, which is always awesome. We have four panelists and David is our moderator who will be asking questions. Let's have everyone introduce themselves, starting with David.

**David Ashpole:**
Sure. I'm David Ashpole. I work for Google and right now I'm working with the Prometheus OTEL work group. We're trying our best to ensure that the protocols, exporters, and all components that integrate OpenTelemetry and Prometheus work well and consistently, helping users who use both to have a good experience.

**Iris:**
Hello everyone, I'm Iris. I work as a senior observability engineer at Miro. My life revolves around Prometheus and OpenTelemetry recently. It’s nice to be here!

**Nikos Takas:**
Hello everyone. My name is Nikos Takas, and I'm an engineer at Corelogs, currently working on observability units. I'm a Prometheus Operator Maintainer and also a Persis Maintainer. I've been working on getting some code into Prometheus to help with the Prometheus 3.0 and OTLP ingestion as well. My daily focus is on Prometheus, OpenTelemetry, metrics, and related topics. Pleasure to be here!

**Vijay Samuel:**
Hi, my name is Vijay Samuel. I help with observability. I think I've met most of you, it's nice to see you all again.

**Dan Bromitt:**
Hi, I'm Dan Bromitt, Senior Manager of SRE at Home Depot for the Store and Payments Systems. We use many OTEL and observability-adjacent tools. Great to have you all here!

**Observability Stack Overview**

Let's go person by person to discuss what your observability stack looks like and how you're using Prometheus and OpenTelemetry in that stack. We'll start with Dan.

**Dan:**
We observe services across a wide range of compute environments, including on-prem virtual machines in our data centers, primarily using GCP and GKE, and within our stores, where we run OpenTelemetry collectors alongside Prometheus installations. 

Most use cases with OpenTelemetry and Prometheus involve Kubernetes in the cloud, which is fairly standard. However, our challenges arise in store environments where we have miniature data centers. We need to ensure everything is functioning correctly, as network connectivity can be spotty, resulting in some stores being offline daily. This makes backfilling metrics challenging due to timestamps and other issues.

**Vijay:**
Starting with instrumentation, we've standardized on a mix of the Prometheus Java client and Micrometer for Java applications. We use community-supported Prometheus clients for JavaScript, which expose metrics for everything not considered managed. These endpoints are scraped by OpenTelemetry collectors deployed on all our internal Kubernetes clusters. 

For about 90-95% of our metrics, we send data directly to our gateway APIs, which can handle proprietary formats. We're also encouraging the use of the OpenTelemetry SDK for metrics to streamline our processes. The backend is predominantly Prometheus-first, utilizing the Prometheus storage engine with Thanos for long-term storage. Over time, we aim to have a unified system for metrics, traces, and eventually logs.

**Nikos:**
Our setup is quite simple. We're leveraging OpenTelemetry Collector for traces and are starting to explore logs. For metrics, we currently use a mix of Prometheus servers and agents but aim to replace the Prometheus agent with the OpenTelemetry Collector to utilize its pipeline capabilities. However, resource consumption is a challenge that is currently blocking us from fully transitioning.

**Iris:**
For us, the architecture is straightforward. We're mainly using Prometheus clients and Victoria Metrics for custom metrics, with everything in Prometheus format. We're experimenting with OpenTelemetry, especially for host metrics since it’s more convenient for collection. We also run a monolith alongside Kubernetes, using the Prometheus receiver and adding script jobs to OpenTelemetry for areas challenging to cover with Victoria Metrics. Our goal is to have a uniform way of collecting all data, especially since tracing is already handled by OpenTelemetry.

**Challenges in Using Prometheus and OpenTelemetry**

**Nicholas:**
My struggles primarily revolve around user experience and understanding how to set up metrics properly. It took time to grasp the nuances of configuring the collector and managing attributes. The biggest issue was switching from the Prometheus receiver to the OpenTelemetry operator and figuring out how to run the target allocator without it. 

**Dan:**
One major struggle has been the lack of support for certain legacy systems. We tried to leverage the Java agent for observability on older microservices that ran on unsupported versions of Java and Tomcat. The configuration of OpenTelemetry for telemetry over a messaging framework was also a challenge for our engineers. 

**Vijay:**
Our biggest struggle was scrape parity. Initially, there were significant differences in how Prometheus and OpenTelemetry Collector handled scenarios like label names starting with an underscore. Thankfully, many of these issues have been addressed through PRs we filed.

**Iris:**
Our challenges mostly stem from the size of our organization. With 700 engineers using our observability platform, any change can disrupt their dashboards or alerts. We’re moving slowly to ensure that transitions don’t negatively impact user experience.

**Looking Ahead: Future Developments**

**Iris:**
I'm excited about the upcoming features, especially the Prometheus 2.0 exporter and receiver. We’re testing it heavily to prepare for our next move. The support for dots in metric names and the uniformity it brings to our engineers is also something I’m looking forward to.

**Nicholas:**
For me, the remote write 2.0 is significant as it promises better resource consumption. I'm also looking forward to the OTLP ingestion in 3.0, which will facilitate more seamless integration between OpenTelemetry and Prometheus.

**Dan:**
The OTLP support will simplify our configuration as we centralize our metrics. We’re also curious about handling late data with OTLP and how that will integrate with our existing infrastructure.

**Vijay:**
I'm interested in the OTLP ingestion and how it will allow for a seamless experience where the instrumentation matches the backend metrics without unnecessary transformations. It’s crucial that we preserve names and avoid breaking changes.

**Audience Interaction**

If there's anyone from the audience who would like to share feedback or thoughts, the floor is open.

**Audience Member:**
I would like to emphasize the importance of keeping conventions consistent across both ecosystems to minimize the learning curve for engineers. 

**Moderator:**
Thank you, everyone for your valuable insights. This discussion has been incredibly beneficial. We look forward to more community discussions in the future. 

**Thanks and Farewell**
Thank you for joining us!

## Raw YouTube Transcript

Everyone who's able to join for this,
Prometheus OTEL interoperability panel, which, David reached out to us, to see
if we could get some end user feedback on making sure that Prometheus and OTEL
play nice, which is always awesome. So we've got, I believe 4 panelists,
correct me if I'm wrong, who will be, will be sharing their thoughts. And David is our moderator who will
be asking questions and why don't we get folks to introduce ourselves,
introduce themselves, start with David, and then we'll, have our
panelists introduce themselves. Sure. I'm David Ashpole. I work for Google. and, right now I'm working with the
Prometheus OTEL work group, and we're trying our best to make sure that
the protocols, the exporters, all the pieces that integrate OpenTelemetry
and Prometheus together work well, and consistently and, help users that are
using both, to have a good experience. Awesome. next panelist. Anyone want to hop in? I can start. Cool. Hello everyone. I'm Iris. I work as a senior
observability engineer at Miro. So my life is surrounds around
Prometheus and Open Telemetry recently. So yeah, it's nice to be here. Hello everyone. Pleasure to meet you. My name is Nikos Takas. and anything engineer at Corelogs, like
currently working on observability units. I'm a Prometheus Operator Maintainer
and also a Persis Maintainer. And I've been working with, trying
to get some codes into Prometheus to help with the Prometheus 3. 0 and O2LP ingestion as well. And my daily base is around
Prometheus OpenTelemetry. Metrical actors and so on. Pleasure to be here. Nice to have you. Let's see my name is Vijay Samuel. I'm, I help with observability. I think i've met most of you and nice to
see you all again Yeah, good to see you. And then our last
panelist, I think, is Dan. Is this Dan? I, hope so. I don't think we've actually met. Hi, yeah. there's so many Dan's. hey, I'm Dan Bromitt, Senior
Manager of SRE at Home Depot for the Store and Payments Systems. yeah. We use a lot of the OTEL and
observability adjacent tools. Cool. Great to have you. All right. so let's see. Why don't we go person by person and just
give an overview of, roughly what you're. Observability stack looks like
and how you're using Prometheus and OpenTelemetry in that stack. And why don't we start,
we'll go in reverse order. So Dan, why don't we start with you? Okay. So we have, we observe services across
a wide range of compute environments. That includes the data center. which are, on prem virtual machines. the cloud, which is GCP, primarily
GKE, primarily Kubernetes. And also, in our stores. those are primarily small
clusters inside of our stores. where we are also running
Open Telemetry collectors. and we are also running in parallel to
them, Prometheus installations as well. So the usage of the, of Open Telemetry
as regards to, Prometheus is in some cases, just the typical, Hey, it's
communities in the cloud is and we want to have multiple different projects
that we can share our metrics across all these different GCP projects. but the really. And that's fine. I think that's largely the,
I don't think that's any, groundbreaking stuff happening there. for us, we're, we are, have challenges
is in our store environments where it's, these things are, miniature data centers. Our, stores are, we have a miniature
data center in the back of every single store with a lot of racks
of network and server equipment. And we want to be able to make
sure that stuff is actually working and our customers are happy. The network connectivity is spotty. some of them are offline every single day. Some percentage of them are offline. being able to backfill
metrics, which is a challenge. hey, the metric was
collected at the right time. The store level, but then shipping
it up to a central Prometheus level, sometimes that backfill just doesn't
work because of timestamps and stuff. I'm sure that y'all are aware of. and the collection of it is the
configuration across a fleet of devices, a fleet of services
is, being able to configure all that is also a challenge for us. We're getting better at that on the
Kubernetes side, but it's still, that's a challenge that exists. Great. Thank you. Vijay, tell me about, what your setup
broadly looks like and which pieces of Prometheus and which pieces of
OpenTelemetry you're using together. sure. starting with the instrumentation, right? we made a forum for the most
part, we standardized on a mix of the Prometheus Java client. And and micrometer for Java applications. we use the, community supported,
Prometheus client for, JavaScript, and basically these expose, everything
else that's not considered managed. So Java and JavaScript are managed
languages, which means that there is a framework that people can build on top of. Everything else is the wild
west in the sense for Go, people use the standard Go client. and there's Python and a few other
languages that are there as well. All of these expose Prometheus
endpoints today and are scraped by OpenTelemetry collectors that
are deployed on every Kubernetes cluster that we host internally. This is the breadth of all our metric use
cases that are there, more than 90 95%. There is a smaller, group of, metric
use cases that, send in directly into our gateway APIs, which, can understand
more proprietary, formats, but they go through, sanitization and whatnot
before, entering into our metric store. And finally, there's also the newer breed
where we are trying to directly encourage some of the use cases to use the open
element A SBK, to require to instrument and then use GRPC into the collector
enrich, and then, write into the backend. The backend is predominantly Prometheus
first, meaning we use the Prometheus s spk to, build clustering and replication, on
top of the Prometheus storage in engine. All the characteristics of Prometheus
still apply, because, the same headlock, and everything stay the
same and we use, object store backed by Thanos for, long term, store. over time we want to get to a place
where We, we know people from, things like micrometer and, from this client
to just use Open Telemetry SDK because, on tracing, we are a hundred percent,
on, Open Telemetry, today and, we are starting to look at logs as well. So over time we want, metrics to be. within the same fold. Thanks, Vijay. Nicholas. our is like quite simple. At the moment, we are leveraging
OpenTelemetry Collector for traces and recently starting with logs. In metrics we are evaluating
because at the moment we are like using a mix of promeus servers
and promeus agent, to hemo writing metrics from many different places. and our main idea is replacing the
promeus, the Promeus agent by the open Telemetry collector and leveraging all
the Open Telemetry pipeline capabilities. but at the moment, we know it's a lot
of, Open Telem collector consuming more resources than the Prometheus
agent, in different aspects, and this is what is blocking us a bit because
we are running, very large, a huge amount of metrics, we are collecting
and, replacing the collector by the agent at moments, blocking because of
the resources, but we are, pretty busy. App that maybe this might be solved
when we have Prometheus ingesting OXLP natively, you don't need more of
the conversions between OpenTelemetry and the Prometheus format, at least
during the remote writing process. and the same idea of replacing
maybe Prometheus, client by the OpenTelemetry SDK and implementing
the, the OpenTelemetry since the instrumentation up to the storage
layer, mainly these at the moment. Cool. Thank you. And Iris, tell us a bit about
how you're using OpenTelemetry and Prometheus together. for us, it is pretty simple, the
architecture as well, we're using mostly Prometheus clients, we are not collecting
via Prometheus, most of the, of our metrics, especially custom metrics,
but we're using Victoria metrics, but everything it is Prometheus format,
because it is the open source Victoria metrics, we're also leveraging the, Node
exporter, for example, that is our main exporter currently that we're using. And we are at the moment experimenting
with OpenTelemetry, especially with host metrics, because it is more convenient
for us to run OpenTelemetry collector and use all its capabilities for metrics
collection, especially in the host level than to use a node exporter. We also are experimenting in some
cases because we are also running a monolith, except for Kubernetes. So we do use, the Prometheus receiver,
adding, script jobs to OpenTelemetry to reach in some places that, it is more
difficult for us through Victoria Metrics. But, yeah, currently
everything is Prometheus. Mostly, but we are thinking very hard
to move towards Open Telemetry as the case, because tracing is already in Open
Telemetry, partly is still open tracing. But the goal is to move everything there. So we want to have a uniform
way of collecting all our data. Cool. Sounds there's actually some
similarity between most everyone sounds like I believe everyone's
using primarily Prometheus libraries and instrumentation, but is thinking
of moving to Open telemetry. I think Iris, you touched
on that a little bit. Is it? Is it just that the you want
consistency between the way you're doing tracing, which is Open Telemetry
and the way you're doing metrics? Or is there something about the
like Open Telemetry instrumentation that's drawing you to migrate? we really like the Open
Telemetry SDKs for tracing. We've seen that it goes a long
way better than any other SDKs. before. considering that we are using this
for tracing, why not use it for the whole parts of application
for metrics in this case? And why not logging? So this is the main reason. Also, the infrastructure, not just
as the case, but the infrastructure makes it very easy the way that
it is very flexible for us to use the Open Telemetry infrastructure. So that really helps in this case. Hey, and David, I do want to call out
that, we are using the Open Telemetry Java agent in production, in stores and we are,
some of our legacy stuff is still using different libraries for collecting metrics
for emitting metrics, exposing metrics. but the majority of our new services
are using the Open Telemetry. Either go Ling library or Java
library to expose metrics. Very cool. All right. let's talk about challenges. Nicholas, why don't you start us off? I know you mentioned, performance
issues with the Prometheus receiver and the collector. what else during your journey of adopting
Prometheus and OpenTelemetry together has really been a struggle for you? Either that's still unsolved or
you were able to work through. That's a good point. I think that what I struggled with the
most in the beginning was mainly UX, DX. I don't know how to properly
call that, but, it took me a little while to understanding. Okay, we are the metrics, we
are not pushing the attributes, like these are such roots and
something like that to the metrics. And then we need to. Enabling on the remote writing to
send the metric info, so one or configuring the collector to expose the. these are attributes as metric labels,
this took my while to understand that, and after that, since I didn't start
using the operator, the OpenTelemetry operator, to make the, like switching
from the Prometheus receiver, to the, I just forget the name of the service. The target allocator helps a lot on the,
problems to discovering targets using a lot of services, but if you're not using
the OpenTelemetry collector, you need to figure out yourself how to run the target
allocator with the OpenTelemetry without the operator, like this is like easy to
do, but you need, I did need a lot of research and reading docs issues and so on
to make it work outside of the operator. I think that mainly the issues that I
found was related to UX at the moment. UX in terms of getting it all set up
or UX after you have it all set up and you're trying to use the data that you've. Ing Yeah. To, make the thing set up, set up and
configure the receivers and understanding the little needs regarding the Oh, Otting
writing the informs or not, and then the, issue that I mentioned regarding
the, setup of the Target loc allocator, part of the open tele collector. Also, you have everything there. it's. Quite okay to use this like at least
for us because we already know about the difference between oh the metrics
would not happen the units if we decide to not have the reboots is
there such reboots as metrics labels? We need to join with the info metric and
so on those kind of things we were aware. So we're pretty easy to get used to
this little niches at the moment. That's helpful. dan, what's been a struggle for you? either or was a struggle or still
is a struggle, using Prometheus and OpenTelemetry together. so first of all, the agent, the Java
agent, it only supports, so we tried to leverage it to add observability
to legacy microservices that had no provisions for observability
at all when they were created. they were running on a version of
java that the agent didn't support And a version of tomcat that the
agent didn't support So i'll tell you adoption was real rough for the first
six months, because of that I think it was java 7 which is frustrating. So I don't know if that's something
Open Telemetry fixes, but it was a problem and the other big one, I think
just the massive challenge is You If we the configuration of Open Telemetry
to send any sort of telemetry over a a push like a pub sub like any sort of
messaging framework like a pub sub or something configuring that was a little
bit challenging for our engineers to get it so that we could actually Hey,
we have the apps that the telemetry is collected from the apps locally And then
we're going to push it over some sort of messaging framework to get it to a central
location That was a little bit rough. And then the last one is the
timestamps, and I know that it's not an OpenTelemetry only challenge, I know
it's related to Prometheus, but if we have a location that's offline for a
while, it comes back online and tries to send out the metrics that it was
unable to send out while it's offline, those timestamps get totally borked. thanks, Dan. VJ, what were some of the biggest
struggle struggles you ever came? and what's still left to do? Our biggest struggles, was, scrape parity. and a lot of those, through
PRs that we filed on the collector, we have had addressed. Some of them are like, what if a
label name started with an underscore? what if, we wanted to disable
sanitization for whatever reason, if it started with, the, colon. So these are all scenarios where,
initially, Prometheus, greatly differed from, how OpenTelemetry
collector was handling it. specifically on the exporter,
the remote right exporter. So those are all solved now. So we don't have a problem, but that's
one of our biggest concerns as we try to marry these two, uhy, open
metrics and Open Telemetry, together. it's like we cannot afford any breakages. it should largely be, rather than,
if, going back to the document that, was shared upfront, It should be
relax the requirement, but still have ways to keep them as is so that like
when we try to move across versions, we don't have something break. And at the scale at which we
operate, if something breaks, then it's a catastrophic breakage. outside of that, I think, forward looking
on the collector itself, we are more of in wait for a few features to come out. Being able to scrape native histograms
and then report them into a Prometheus compatible backend and things like that. But we don't have
complaints per se right now. Certain things could be better
like Attribute processors could be a lot simpler to configure. They're very verbose right now,
but those have nothing, to do with the discussion we have right now. in summary, please don't break us. Yeah, please don't break us. Yes. Good feedback. Cool. And, Iris, what's, what
struggles have you overcome? What, struggles still remain? our struggles come mostly from
the size of the organization. Our organization is quite big. So we, just for, to envision it, we
have at least 700 engineers that are using our, our observability platform. And, we have to say most of
them, of course, are front end engineers, back end engineers. So they're not, I'm not going
to say fully proficient. They know their metrics. And everything, but, of course, if we
make a big change and, it's different, it could ruin their dashboard. It could ruin their alerting, and
it is a very unpleasant, experience. So that has been our challenge so far
and why we are moving very slowly. Because, if we change the
way that we're collecting information and then the metrics. even if the formalities it is different,
it could be a big change and 700 people to get adapted to this change needs time. So we are going very gradual with it. Prometheus is known territory for everyone
that works on the team and for all the engineers that have had experience
with their metrics at the moment. So it's it's safe, of course, OTEL
Collector needs a lot of, digging into the documentation, finding out more,
testing and trials, so it makes it a bit slower, but mostly our biggest
challenge that we're overcoming slowly, but still we are not there, is, the
experience of our engineers, so we don't ruin their, dashboard, their,
observability, performance in general. Great. Thanks. So I know we just touched on this a little
bit, but, I think there was, I think it was actually a Prometheus blog that came
out maybe a couple months ago, about 2024. And some of the cool things that
are coming, some of the things I can think of are Prometheus remote, right? To, OTLP support and the Prometheus
receiver, Delta support for Prometheus, supporting Dots, WooHoo,
stability, or even, Support for OTLP and some of the, Promethease. exporter ecosystem that
already exists today. Iris, we'll start with you again. which of those are, or is there
anything else that really stands out as something that you're
really looking forward to having? Can I say all of the above? I'm very excited for all of them, but
if I had to distinguish maybe, the exporter and receiver, the version 2. 0, it's going to be very nice. we were using it heavily on. testing heavily with it right now for
our next move and the support of dots. Why not? Again, it comes from the organization and
having things more, like more uniform. It's, it helps us a lot and, and
the experience of our engineers. Yeah. that's actually really interesting to me. So you're really excited for Prometheus 2. 0. When I talk to some people,
they're like, there's Prometheus 2. 0 and OTLP, but you're
excited for Prometheus 2. 0. Tell me a little bit
more, more about that. I was talking mostly about
the Prometheus exporter and receiver, in Autel Collector 2. 0, right? That's, what Yeah, sorry. Sorry. No, that's fine. That's fine. But yeah, I'm looking
forward for Prometheus 3. 0 as well. It's a great technology and of course
the support of OPLP will be awesome. Yeah, very cool. Let's go to Nicholas. Cool. Wow I guess it's a mix
of the remote write 2. 0 I guess it's going to be massive
people is working hard to have a like better protocol consuming less
resources and You know Since most of the people is using OpenTelemetry,
they are emoting writing for. Some Prometheus based system I
have in this remote writing 2. 0 will help people saving resources,
networking, CPU and memory. Apart of that, I guess for the 3. 0, of course, the OTLP ingestion
on GA is going to be nice. Of course, there are a lot of working
that people is doing on the Prometheus team, making, out of order samples
ingestion, be enabled by default. This is something very important
to supporting auto allopinate. I guess the, next one just to be
a little bit different from we, I guess it's the UTF eight support
and the metric label and name. I guess it's going to be nice. It's going to have some proximity
between open and Perme to use, metric names and labels. I guess it's going to be used
very useful for usability and join the different communities. Cool. Thanks. you're welcome. Dan, tell me about what
you're looking forward to. Yeah, so the otlp That
is a very cool thing. it will simplify some of our config
It was we get to this the central gmp, where everything's stored. To the I shouldn't use acronyms to the
central google manage prometheus that we run where all of our metrics are
ultimately stored one of the things That we're not really clear on is,
Hey, if we have data that is late. So if we have a no TLP bit of
telemetry that has a timestamp, that is five hours late. Is that still going to get stored? And we haven't really been able to
find the answer to that question. So we're just assuming that we'll
test it and see once it comes out. Yeah, we can think. Prometheus is going to
support out of order writes. I'm not sure about the It's
already supporting, actually. It's already supporting. It's behind a feature flag and you can
just enable it and configure how much behind you want in gesture samples. Yeah, so the out of our rights thing. That's yeah, that's good. That's cool. It's the stuff that has a timestamp. That's super behind is the
one where it's really unclear. Cool. Yeah, we can sync up afterwards. And, Vijay, what are you excited about? It's coming soon. actually a lot of things. the ODLP in just is interesting. the part that we, would really hope for
is that, when we support it, it should be in a way that, okay, I instrumented
this way on, on my application. And I see the same way on. Prometheus, no, addition of underscore
total or, milliseconds or whatever and keep the dots as is and things like. But the part that's still, somewhat
unclear and we hope to see more clarity is how do the resource
attributes and, the metric attributes play along inside of Prometheus. what if there are name
coalitions and things like that? that is somewhat unclear, but, if
the, fundamental thing is that we want the instrumentation and, what they
query to perfectly match, especially when they are just using GRPC to
send, out from the client directly. Delta Temporality is something
that, some of the folks who started off directly on Open Elementary. SDKs. I felt that, oh, this is nice. It is nice to have, but it's not supported
on Prometheus because you drop it on the floor in the collector right now. That's there. but outside of this, this list,
I know, one of my wish list items is like exemplars persistence. That's something that, that's,
not there yet on Prometheus. It's still the circular ring buffer. That's there. hopefully someone can get to it by three. Oh, it's a nice thing to have,
which we, and we rely quite heavily on exemplars today. Oh, cool. Actually, I learned something. I didn't know exemplars
weren't persistent. Yeah, so they're not persistent and
recording rules don't support it. for the latter, there's a PR
which I never got to finishing, but someday it will be there. but the persistence is something
that no one has picked up yet. Oh, cool. Thanks, Nicholas. Okay, so one of the things that we've
talked about a little bit so far, it seems like most people are in agreement
that breaking changes are really hard. You have big organizations, big
deployments, and like when we mess with things in terms of
how things are translated, that can really have a big impact. And at the same point, it seems
like there's at least some agreement within this group that, we are
excited for UTF eight support, and we really want to be able to preserve
the original Open Telemetry, data that is coming from the application. V. J. I'll put you on the spot. What do you think the right way
to strike that balance is for us? on your doc, I think, I had a discussion
with some of our leads internally as well, like option one seems, pretty appealing
to us in the sense that, at least today what we do is we separate installations
between, things that are going after Prometheus endpoints versus things that
are emitting through gRPC directly. Okay. So it still gives us the opportunity
to say that, Hey, receiver, Prometheus receiver and remote write exporter. Make sure that everything that Prometheus,
mandates today, enforce them on the scrape endpoints, but OTLP receiver and, whatever
is writing to our Prometheus backend. make sure that, you are passing things the
way that OpenTelemetry standards, mandate. So it gives us a balance, in keeping
things as is, but things that we are moving to the next generation, we
are moving it, in, the right way. so we have done this in quite
a few evolutions where, we used to run a modified OpenTSDB first
before we moved into Prometheus. That's how we bridged the gap, initially. And this would be like a second generation
where, Moving from, say Prometheus, semantics into open, telemetry semantics. I would hope everything goes behind
either a configuration or a feature flag, to keep the standard, the
current standardization configurable. to the specification that's there
today on open metrics and allow us to disable them as we need it. So to be clear, do you think there's
a difference between push and pull? Or is it that, it should keep or
that we should make it preserve the names by default, but always
give people an escape hatch? I think you said that you like. That like OpenMetrix and Prometheus scrape
endpoints still follow the Prometheus conventions, but for pushing Prometheus
remote write and OTLP, you want to be able to just preserve it as is. Do you think there's a distinction there? Only for the, the OTLP. Prometheus remote write, however
we feel it needs to be, it can be done whichever way. but for things that are coming in through
OTLP, it should pass through the pipeline exactly the way that, the, sender intended
it, that's, what we're, particular about. And, on the scrapes. through either content negotiation or
whatever, the behavior can be, decided one way or the other, but we want to
keep the scrapes as is because we have like more than 4 million scrapes that
happen, and if something changes, then everything blows up at that point. So don't, break client side. Yes, exactly. Okay, that's very good feedback. Do you see these push and pull use
cases being in the same pipeline and the exporting side needing to be
automatic, needing to automatically decide whether it does that translation
or not based on the source, or would you expect to have separate pipelines
configured for those use cases? I would vote for simplicity in the sense
that we are okay to run two pipelines. Okay. And I don't, at least the way
that we are deployed right now. we, I don't see a way in which,
both, push and pull can, co exist. so we would anyway run them
as two separate pipelines. So it's, probably fine. So no, no additional complexity required
on the exporter side is what I'm, doing. Yeah. Okay. So just the configuration to decide which
of those options you want and then you'll set up a pipeline for each of them. Correct. Sounds good. Thank you. Very cool. Thank you. Iris, I'll ask you a similar question. So you, have a very large
organization, right? You've said, 700 engineers. Yeah. Yeah. are you using prom QL? You said you mostly are use Prometheus
and are familiar with Prometheus. Are you then using a lot of prom QL? Yes. all prom QL for metric query. have you seen the UTF eight prom QL. Proposals are read. Sorry to put you on the spot. No, I actually did skim through
it right before this meeting. but I think that most of our issues,
maybe I misunderstood, while I was going through the proposals is the first one
to change open metrics to allow Open Telemetry name would probably solve this. what makes me say that is that, yes,
there is differences, but usually when you are making queries, especially if you
are offering that to a wide organization, you are using an engine that is very
intuitive when coming to finding the attributes, the labels, the metric names. So as long as we, for example, a
Prometheus backend is able to support Open Telemetry metrics, UTF 8, That
should solve the problem of a common engineer that does not know a lot
about observability to build a PromQL query, for example, so that is a, that
is very, good first solution for this. I remembered my question now. Thank you. Thank you. Iris. Nicholas. Oh, shoot. I remember it again. Nicholas, my question for you. part of what we're talking about here
is a difference between Prometheus best practices that have been codified
as the open metric standard and the Open Telemetry semantic conventions
that have come and, given new ways of, say, writing metrics or naming things. are you happy with the way that
these two ecosystems have evolved? And, what do you think the best
approach is for users to try and give them a, a reasonable experience? Should we let them both be, or
would you like to see the, either OpenTelemetry or OpenMetrics
change such that they both work? They align in terms of how things
should be named or that sort of thing. That's a really good and
tough question, actually. personal feeling, Prometheus and
OpenTelemetry are communities that stay away for a little while
and and we develop up the things. very separately, and personally, what
I would like to see, I think that maybe the open domain entry, we should look
more how the things is working when we have, high adopted systems, like
we have with premature, different from the tracing and the logging, telemetry
data type where we have many different data stores, like on the CNCF space. For the metrics, we, actually only
have Prometheus based project. Like maybe we should look more
how Prometheus is doing the things and avoiding change much. how this is working because most like
in the end what users want to do is to use in the new things without from need
to changing or rewriting everything you know if we look to how the like metrics
how we are trying to unite the metrics between OpenTelemetry and OpenMetrics we
are trying to get some okay neutral moment here like where We, agree with each other,
but in the end, I guess we're going to introduce some, chance to the end user. And I guess that we can unite effort
between the different communities to avoid these in the future. for example, oh, we think when we
decide if when OpenTelemetry user groups start discussing how metrics we would
like the feeling that I had is like we didn't get close yet to the Prometheus
ecosystem and so on and trying to, oh, let's try to solve most of the
issues that we have in Prometheus, but without introducing a total different
metrics naming convention just to be easier with the end users, cool. Thank you. That makes sense. Cool. thank you everyone so much for coming. Those are the questions I had prepared
and I, really appreciate the feedback. I know we're ending a little early, I guess, since we're done a little
early, we could, if anyone here who's, in the audience, As they want
wants to share their feedback, we can definitely open up the floor. Any takers? Oh, I'd like to mention just
one more thing if it's okay. On the, querying side as well, if we can
keep the conventions, fairly alike, there are a few options that, try to distinguish
things with double quotes and whatnot. that would be new things
that we need to teach folks. if we are just using, introducing
UTF 8, conventions into label names and metric names by keeping
the style exactly the same. That's still perfectly, fine because
people are just gonna assume that we are just introducing new metric names
and new label names rather than new conventions that they need to abide by. So if that can be taken
into consideration, that would be great as well. You're talking about having to
put UTF 8 names inside of quotes. yeah, exactly. Yeah, I think that was considered. I can give you pointers afterwards
if you want to know the details of like why it's a struggle. Okay, sounds good. I, I was at the Prometheus Dev
Summit earlier today, and one of the things they were discussing was
introducing OTLP export support into the Prometheus client libraries. is that something that would
be useful to, this group here? And if so, one of, one of the things they
weren't quite clear on where they wanted to land was whether that OTLP support
needed to be part of Each, Prometheus client library, or if it would be okay
if there was a third party, or separate repo bridge that had to be combined
with the Prometheus client library and an OTL SDK to make it function. does anybody here have thoughts on that? Can I chime in? Is that allowed? Sure. So the, when, so in, in our environment,
we use a lot of different metrics solutions and we are trying to reach
standardization when metrics are moving from one location to another, it's a
mess when we have to have a bunch of different infrastructure set up to
facilitate moving metric for data dog versus moving metrics for infrastructure. Prometheus, right? It's just a mess. So the as much as we can get into O. T. L. P. So that way we can have
everything moving through the same infrastructure for observability. that just simplifies our entire ecosystem. So the more we get into O. T. L. P. The happier everybody on my teams will be, in our case, like if, this proposal
came out a couple of years ago, we would have probably bounced on it because,
at least, the problem that, some of our use cases, especially things that
run like, cron jobs, folks use, the Prometheus client and use, push gateway. those use cases we would have ideally
like to replace it with the non push gateway based, implementation
because the push gateway semantics don't necessarily work always for us. we just want to be able to send
it into the gateway and put it on storage as quickly as possible. for those kinds, it's useful, but in
today's world, if someone is trying to achieve such a use case, we'd rather
recommend them to move to the opened elementary SDK, because there is a defined
pattern for us to go after in that. Any other thoughts or
feedback from anyone? Thank you everyone for joining. This was a really great discussion. Really appreciate it and looking forward
to having, more community discussions. Great. Thanks, Adriana. Thank you. Thank you for the opportunity. Thank you very much. Bye bye. Bye.

