# OTEL in Practice Fireside Chat December 2022

Published on 2023-09-25T04:00:25Z

## Description

In this special Holiday 2022 edition of OTel in Practice, join the OTel End User Working Group as they talk about the group's ...

URL: https://www.youtube.com/watch?v=TYrIP_LkwgU

## Summary

In this video from the OpenTelemetry in Practice series, the format diverges from the usual deep dive discussions as presenters share shorter talks. Adriana, who has a background in Kubernetes and previously worked at HashiCorp, discusses observability in HashiCorp products and demonstrates running the OpenTelemetry demo application using Nomad, showcasing its integration with various services like Vault and Console. Jess (Jessatron) presents a fun and creative project that uses OpenTelemetry to generate heat maps from images, specifically designed for educational purposes. Rhys talks about ways for end users to engage with the OpenTelemetry community, highlighting the End User Working Group's initiatives to foster involvement and communication between users and maintainers. Overall, the session emphasizes community engagement, practical applications of OpenTelemetry, and innovative uses of observability tools.

## Chapters

00:00:00 Introductions
00:01:46 Guest introduction: Adriana
00:05:30 Observability in HashiCorp products
00:10:24 Demo of OpenTelemetry demo app
00:20:00 Transition to Jess's presentation
00:21:36 Guest introduction: Jess (Jessatron)
00:22:48 Demo of heat maps with OpenTelemetry
00:31:12 Discussion on educational uses of heat maps
00:32:00 Guest introduction: Rhys
00:33:06 End User Working Group initiatives

## Transcript

### [00:00:00] Introductions

**Speaker 1:** Thank you. So the OpenTelemetry and practice series is traditionally a pretty serious talk series where every month we go deep into implementing OpenTelemetry in a particular language. We talk to an end user who is actually implementing it in production, and we talk to usually a maintainer of the project who can talk about the best ways to implement it. This is a little bit different of a format because we decided to do three or four short talks that didn't fit well together. 

### [00:05:30] Observability in HashiCorp products

**Speaker 1:** Adriana is going to lead off today with talking about observability for HashiCorp products. She currently works at Lightstep and used to work fully in a Hashi shop. Yes. Then a little bit later we'll have Rhys talking about how end users can get involved with the project, which I expect to be highly interactive. Jess "Jessatron" is going to give us a talk about using OpenTelemetry to make ASCII art in heat maps, which is cool. You are trying to get your team to learn about OpenTelemetry and pay attention. 

### [00:01:46] Guest introduction: Adriana

**Speaker 1:** Adriana, you ready to? 

**Adriana:** Yeah, I'll start. So I'm ad-hocing this. As Rin mentioned, I used to work at a Hashi shop. I actually have a Kubernetes background and was thrust into this HashiCorp world where my previous employer ran their containerized workloads on Nomad. I found myself in a situation where I had to quickly understand this Nomad thing because I was managing a platform team, which supported Nomad, Console, and Vault for the entire enterprise. 

**Adriana:** That's how I began my dabblings in the Hashi world. From that, I ended up becoming a HashiCorp Ambassador because I dug in, blogged about it, and continued to do so. At the same time, at this former company, I was also managing an observability team. I came to learn about observability at around the same time that I came to understand Nomad. These were two things that I was doing at the same time, learning about at the same time, which led me into OpenTelemetry. 

**Adriana:** Now that I work at Lightstep, I've had a chance to contribute more in the OpenTelemetry community. As I mentioned before, I've worked in the comms area, contributed some content to the doc site, made some contributions to the demo app, and I was actually pleasantly surprised to learn about the demo app, which I think launched relatively recently. 

### [00:10:24] Demo of OpenTelemetry demo app

**Adriana:** I like it because it showcases OpenTelemetry, like what you can do with OpenTelemetry. I think the original version of the demo app that came out, you could run everything in Docker Compose locally. Then more recently, the team created Helm charts for this one. That got me thinking, "Hey, if this thing runs in Kubernetes, wouldn't it be super cool to get this thing to run on Nomad?" 

**Adriana:** It's been part of my wish list ever since I learned about the OpenTelemetry demo app Helm charts. I finally carved out some time to do this, and I got it up and running in a local Hashi environment on my machine. There's this really cool tool called HashiCube, which is similar to running Minikube or K3s or whatever, like one of these local Kubernetes dev environments. It's a similar sort of thing for the Hashi stack, which was created by a third-party company called Serbian. 

**Adriana:** I love using this tool because it gives me a full-fledged Hashi environment, similar to what you would get in a data center, but obviously smaller scale. In real life, Nomad by itself is kind of useless, so you need the power of Console for service discovery, Vault for secrets management, along with Nomad to get all this stuff to really have a robust system to manage your containerized workloads. 

**Adriana:** I have this HashiCube running on my machine locally, which I can show you. I'll do a little screen share. Well, first I'll show you my HashiCube. Oh wait, am I sharing the right one? 

**Adriana:** I have like so many windows. The correct HashiCube? I don't know. 

**Adriana:** Okay, so this is my HashiCube startup sequence. What it is, is basically using Vagrant to provision either a VirtualBox VM, or I'm on an M1 Mac and VirtualBox and M1 Macs don't play nice. I think there's possibly a version of VirtualBox that plays nice with M1 Macs now, but at the time it didn't. 

**Adriana:** The maintainers of HashiCube basically stand up all these Hashi products in a single Docker image. This version of HashiCube that I'm running, where you can see the tail end of the startup sequence here, is running Vault, Console, all in one Docker image. 

**Adriana:** If I share my Nomad console here, you can see the problem when I lose sight of all my windows. Oh, here we go. Okay, so this is Nomad, and these are all of the services that make up the hotel demo app running on Nomad locally on my machine, which is pretty freaking exciting. 

**Adriana:** I basically had to go through the Helm chart for the hotel demo Helm chart. There's a folder in the Helm chart repo that shows the rendered YAML, so I basically started with the rendered YAMLs and went through the process of translating these Kubernetes manifests for each service into the equivalent Nomad job spec, which is what you see here. 

**Adriana:** For example, looking at the feedback service, this is running on Nomad. If we go over here, we can see there's a lot of stuff here. We can see the logs of the true flag service. Nothing terrible is happening. Here we go, it's running. 

**Adriana:** We can see from our dashboard here that all of the services are up and running. It's made up of all these different services written in different languages. Plus, I also had to convert, I had to "nomadify" Redis, Postgres, we had the hotel collector, and there was one more. There was Prometheus and Grafana, and I used Traefik for load balancing so I can expose my services to the outside world. 

**Adriana:** What that looks like then, to be able to access the hotel demo app's endpoints, and hopefully my computer won't crash here, I have an endpoint called hotel-dash-demo.localhost, which is accessible. This is just something accessible off my localhost. 

**Adriana:** The Jaeger UI is exposed as part of my demo app configuration, so we see Jaeger is up and running here. We've got the demo app's UI running here, so we can buy stuff, we can check stuff out. Let's buy this telephone. 

**Adriana:** If we check Jaeger, we can look to see... Sorry, the screen sharing thing is getting in my face. We can see our traces. I think the hamsters are running really, really hard here. We can see it's produced some traces here that we can see. 

**Adriana:** In addition, when I modified this, there are also some Grafana dashboards, so some cool dashboards that come pre-loaded, pre-configured. You can see there's some stuff going on here with the hotel collector, and there's also this demo dashboard which gets some stats from the recommendation service. 

**Adriana:** That's basically it. I can show you also what a job spec looks like in Nomad. 

**Adriana:** I want to see more traces. 

**Adriana:** Oh, you want to see more traces? Yeah, right. I picked the saddest trace. Yeah, that's what happens when you're ad-hocing it. Okay, let me pull up a more interesting trace. I think the recommendation service has interesting traces that we can see. Checkout's usually good. 

**Adriana:** Cool, let's find some traces. 

**Adriana:** Oh yeah, look at all those services. Yeah, there's some colors. Look at it go to all the different services. Yeah, this is actually pretty cool. You're right, I picked the dinkiest to showcase all this. 

**Adriana:** All this is happening on my machine in this Docker image that's running all the Hashi things, which is super cool. I did want to show also what a Nomad job spec looks like. Let me just share my screen for that. 

**Adriana:** Nomad is like an alternative to Kubernetes, right? 

**Adriana:** Exactly. It's interesting too because it doesn't just run containerized workloads; it can run VM workloads. It can even run like a JVM or IIS. So it's kind of cool that way. 

**Adriana:** Here we go. Sorry, I was looking for the one. Okay, so let me pick... 

**Adriana:** A job spec is like a Kubernetes deployment? 

**Adriana:** Yeah, exactly. So here I'll... I've got a Kubernetes deployment. I'll put it side by side here. 

**Adriana:** All right, cool. Okay, so this is the feature flag service. On the right, we've got the feature flag service definition. This is our Nomad job specs. Unlike Kubernetes where you have all these different YAML files that make up the various objects for that make up your manifest, everything is self-contained in one job spec file which is written in HCL, which is HashiCorp Configuration Language. 

**Adriana:** I liken it to... I mean, if you've used Terraform, this looks familiar. I find HCL is like if JSON was slightly improved. That's what it would look like. I do find it's easier to read than JSON. But this is basically what it looks like here. 

**Adriana:** For example, in our network definition, you see that we define two ports, 8081 and 50053, which lo and behold we defined those over here in our service YAML for the feature flag service. 

**Adriana:** If we scroll over to this task definition, we're saying that we're using the Docker driver. This is saying, "Okay, we're using a containerized workload. Let's find the equivalent in the manifest." 

**Adriana:** Here we go to our deployment, and we can see where we define our image. I've defined an image pull timeout because sometimes my network doesn't like to behave, so I don't want Nomad to crap out after five minutes and say, "Sorry, I can't pull your image, sucker," and then fail my deployment. 

**Adriana:** Over here we've got the ports configuration basically saying, well, just like here we're saying that this container requires these two ports. Well, on the left side here in our HCL, we see that our HTTP and gRPC ports that we defined up here, that's what they're pointing to. 

**Adriana:** The other thing that I wanted to point out was over here in this template stanza. Basically, these groupings and the curly braces, they call them the stanzas. I'm defining two additional environment variables, but they're defined in a slightly different way because they're referencing services from other Nomad job specs. 

**Adriana:** Here, to be able to reference, for example, our database service to get the information, so the IP address and the port of the database service, we can't hard code that information because that stuff can potentially change, especially the IP. 

**Adriana:** In order to get that information to define this environment variable, we have to use... We basically have to look up this service in Console, which, as I mentioned, is for service discovery. 

**Adriana:** To find out what the information of that service is, you refer to it by service name. So if we open over here, I'm going to open this FF Postgres. This is the job spec for Postgres. I have a service named FF Postgres service, which if we look over here... Here we go. 

**Adriana:** It basically says, "Hey Console, I want to pull up a service called FF Postgres service, and pretty please tell me the address and port number of the service so I can plug it into this environment variable." 

**Adriana:** We use the template stanza to do this kind of dynamic definition, and we have to tell it that the destination is going to be an environment variable because one of the things that you can do with the template stanza as well is you can use it for configuration files. So similarly, it's very similar functionality to a config map in Kubernetes. 

**Adriana:** Here is where we define our resources. This is in megahertz for CPU, and our memory is in megabytes. The other thing that I wanted to point out is here I've got some rules on restarting the service. 

**Adriana:** Because there's no dependencies that you can define in your services in Nomad, like you know how you would do in Docker Compose saying, "Hey, this service is dependent on that service?" You don't have that kind of dependency definition in Nomad. 

**Adriana:** Basically, the jobs start when they start, which means that, for example, this feature flag service is actually relying on the database and the hotel collector to be up and running. Well, what if the feature flag service starts before the hotel collector and the database startup? 

**Adriana:** If we don't put some restart rules in place, then when it starts up and these two services aren't up or one of these two services isn't up, it'll crap out, and then that's it. It's dead. 

**Adriana:** What we want to do is put some restart rules in here, basically saying within the span of two minutes, we're going to try to restart this thing ten times with a 15-second interval between restarts. 

**Adriana:** Either after ten attempts or two minutes, whichever comes first, if this fails to restart, we're basically going to say, "Okay, we're just going to wait a little bit and reattempt that again." The default mode for this is fail. 

**Adriana:** If it doesn't successfully restart in ten attempts within two minutes, it would completely fail, and that means your whole application deployment fails because of all these dependent services. 

**Adriana:** This gives you some protection saying, "Okay, we'll keep trying, we'll keep trying until things are up and running," which ends up being very convenient. 

**Adriana:** The final thing that I wanted to point out was that we also have these checks here. These are basically health checks. They're similar to the types of health checks that you would see in Kubernetes, like liveness probes and readiness probes. 

### [00:20:00] Transition to Jess's presentation

**Adriana:** I wanted to show you actually what that looks like in Console really briefly. Let me just pull that up. 

**Adriana:** Yeah, and we're going to move on to Jess Citron after the console showing. If you have more, Adriana, think them up, please. 

**Adriana:** Yes, I'll show this very briefly, but this basically shows all of our services. If we look at the feature flag service, we have two services, one for our gRPC and one for our HTTP. 

**Adriana:** This shows us that, hey, we're able to hit our endpoints, so it sends a signal back to Nomad like "all systems go, hurray hurray." 

**Adriana:** That's basically it in a nutshell. 

**Speaker 1:** Follow-up questions? Last parting thoughts? 

**Audience Member:** Nice job! 

**Speaker 1:** Yeah, I agree. Nice job! That was a super good demo and a good example of how to use the demo app. 

**Jess:** So just, Jessatron is actually going to show us something totally useless but super fun for training people or teaching how to make ASCII art into a heat map using OpenTelemetry. 

### [00:21:36] Guest introduction: Jess (Jessatron)

**Jess:** Right, right. I made this thing for Christmas, for Christmas gimmicks, I guess. I don't know. It's in a repo, honeycombio/happy-ollie-days, which is cute. You can clone this repo or run it, and if you give it your Honeycomb API key... 

**Jess:** This is Honeycomb. The UI is Honeycomb specific because it had to be specific to the display, but it does use OpenTelemetry. I'm going to give it a Honeycomb API key. Oh, it's still in my paste buffer. Great. 

**Jess:** Then I'm going to run this little app. This app is in Node, TypeScript, so it has created a bunch of spans in a trace using... where's my... here we go. Start active. 

**Jess:** It does a start active span in Node, and then for each... it's figured out what spans it wants to send, and then it does a start span for each of them and supplies a bunch of attributes, and then ends each one. They all go into one trace. 

### [00:22:48] Demo of heat maps with OpenTelemetry

**Jess:** It's given me a link to the datasets. Oh, it's a good thing I'm following that link because apparently my dataset is called Fufu Free, but then in the readme, it describes how to do this. 

**Jess:** If you do a heat map on the height field and you get the last 10 minutes, you're starting to see something. But then I need to pick graph... no, no, up here. Granularity five seconds. 

**Jess:** Oh, that's so cute! Isn't it cute? The cool part is that you can use this program. I mean, I don't know what it's going to look like in any other system because I've customized the heights to the bucket sizes that Honeycomb uses in heat maps, so you'd have to tweak the code to make it do something in some other heat maps. 

**Jess:** Oh, but it actually pulls this out of... where is it? Images now? There should be an images directory in here. Oh, input. Don't peak.png. So if you give it a PNG that's between 25 and 50 pixels tall and you probably want it between 1 and 200 pixels wide, then it can convert that into a heat map. 

**Jess:** Oh, it's converting the heat map based on the blue channel in the PNG. It uses the other one to get some attributes, which does some fun things in Honeycomb because you can pick bubble up and be like, "What is different about... oh, oh, check this out!" 

**Jess:** Okay, my new favorite feature of Honeycomb... wow, that stupid little... do me anything is gone! Okay, which is very useful sometimes, I'm sure, but not in here. 

**Jess:** Now that I've gotten rid of that, what is different about the spans in the second reindeer? Honeycomb does its little "what is different" analysis, and it says the reindeer name... that one has a reindeer name of Dancer. 

**Jess:** Then if you group by the reindeer name, you can go back and like, oh, oh, wait, hold on. I've got to do the trick of... wait, wait, give me the right 10 minutes. 

**Jess:** It wants to... like the Santa and his reindeer are moving on. I need to switch to absolute time. Okay, now let's group by reindeer name. 

**Jess:** Okay, now it's lost the granularity, so let's fix that granularity. Five seconds. Okay, but now... results tab, and we have the different reindeer names. 

**Jess:** There's no reindeer name. This, there's Dancer. This one is Rudolph, and this one is Prancer. 

**Jess:** Yeah, so it's cute that way. It's got different fields, and those are based... in case you want to use this yourself and supply your own image, those are based on the red channel in the PNG. 

**Jess:** There's a little key for how much red between 0 and 255 is in that color and what the fields are. So that's also encoded in a PNG, and you can do it yourself and make your own... this gets officially released on Monday, and it'll be advertised and stuff, but I'm not... none of that stuff am I telling you how to fix it yourself, so y'all are getting that. 

**Jess:** There's one other trick in this data, which is if you do a max of stack heights and group by stack group, then you get some nonsense. But if you change the graph settings to use a stack graph, then you start to get something. 

**Jess:** If you get the order right, stack group descending... come on, do it! A Christmas tree! 

**Jess:** Oh my God, that's awesome! You can also generate yourself because that is based on house.png, obviously. It used to be a house; now it's a Christmas tree. 

**Jess:** Of course, there's limitations. You have to have all the colors on top of one another, and you can't have a color that's both under and over, and you don't control what the colors actually show up as. But if you're clever, you can make your own PNGs. 

**Jess:** Oh yeah, I've got some groups on that. You can group by... oh, it is great by stack group. That wasn't necessary, but here's the names of them: star and background and tree and stuff like that. 

**Speaker 2:** Yes, where do people go to find this app? 

**Jess:** It is at honeycomb.io/happy-ollie-days. You can download this, and if you have a free Honeycomb account, or if you get it to work in another tool, that would be awesome. I would love to hear about it. 

**Speaker 3:** Oh, thanks, Johnny! 

**Jess:** Yeah, so that's that. 

**Speaker 3:** We'll find stop share. Maybe not. 

**Speaker 4:** Daniel's like, "I'm running, not walking, to try this out." 

**Jess:** It's fun. It's true. And I have a question, which is how do you think this can be useful to people as a tool to teach about heat maps and observability? 

**Jess:** Because you can... I mean, you can ask, like, "How do I draw it?" And the answer is that I send a different number of spans, which, of course, is this one, which of course I also stick all the intermediate data on the spans because that's what I debug it. 

**Jess:** No, that's clearly the wrong field. Show me the trace. I haven't made the trace cute yet. Someday I'll make this have a drawing in it too. 

**Jess:** Span count... how many... oh well. I send multiple spans per pixel if I want a dark color because Honeycomb says darker is more and lighter is fewer, so there's just one span in these. 

**Jess:** You know what? I can find that field if I do Bubble Up. What's different about these that only have one span at a time? There it is! 

**Jess:** Okay, so these only have one span at a time, and some of the darkest ones have ten spans at a time. 

**Jess:** If you think... if you can use it to be like, "How does a heat map..." Mostly it's just entertaining, and it does really illustrate like bubble up. 

**Jess:** All of these, most of these are letters, and some of them have... oh, they have different letters. 

**Jess:** Yeah, so Bubble Up is pretty well illustrated by this, I think. 

**Speaker 5:** I want to say what Bubble Up is for folks who aren't Honeycomb users. Bubble Up is Honeycomb's "what is different," so you can draw the box and it does the statistical analysis on what fields are different. 

**Jess:** It's just cute! 

**Speaker 5:** That was super good. 

**Speaker 6:** There are no questions? 

### [00:31:12] Discussion on educational uses of heat maps

**Speaker 7:** Do you want to go ahead and talk about end user working group work? 

**Rhys:** I mean, yes, but also how do I follow up? We're doing systematic and important and slowly marching through things. 

**Speaker 6:** Jessica, do the fun, creative stuff. 

**Rhys:** Yes, this is... I mean, I have some like one or two fun graphics, but it's not going to be anything as cool as Jess's. 

### [00:32:00] Guest introduction: Rhys

**Rhys:** I just wanted to talk real quick on something that we've surfaced just from talking to a wide variety of end users. A lot of people are not really aware of how to navigate the community on how they can get involved or that they even can get involved. 

**Rhys:** I'm not sure. I know there's a couple contributors on the call. Not sure everyone else's end user, but hopefully this will be of some utility for you. 

**Rhys:** A couple things we'll go over: this time of the community at large, some of the different parts of it, and then we'll talk about how you can get involved if you're interested in some of the different ways that you can get involved. 

### [00:33:06] End User Working Group initiatives

**Rhys:** We've mentioned a few times the end user working group that a lot of us are a part of. What is the end user working group? We have two primary goals. One is to foster a sense of vendor-agnostic community for end users, and two is to create a feedback loop between the end users and project maintainers, with the overarching goal of improving the project software. 

**Rhys:** What are some of the working group activities that we have implemented? So first of all, this is one of them. This is Rin's child. But we are very excited. "Hotel in Practice" is what it is, so every month keep an eye out for more fun talks, presentations, and casual conversations. 

**Rhys:** We have the monthly discussion groups now with a maintainer per session and in all regions: America, EMEA (which I just found out stands for Europe, Middle East, and Africa), and APAC (which I'm actually not sure where those things were, but it's Asia and the Pacific region). 

**Rhys:** Imagine where AC stands for. Those are all on the OpenTelemetry public calendars. We also have end user interview and feedback sessions where we will talk to an end user about their adoption, implementation, and challenges that they face and get the feedback shared back to the OpenTelemetry maintainers. 

**Rhys:** If you're interested, if you're an end user and you're interested in sharing feedback in one of these sessions, please reach out to myself, Rin, or Adriana. We would be happy to get you on the schedule. 

**Rhys:** We are also new for end user interviews. Moving forward, we're going to turn them into profiles for the OpenTelemetry blog to kind of make the implementation and adoption that other end users have done in their organizations more discoverable. 

**Rhys:** We also have a community survey, so that's another way that you can contribute if you don't really want to get too involved but you still want to have a way to share your thoughts and opinions on how using OpenTelemetry is for you. 

**Rhys:** Some of the stuff that's upcoming for the working group: we want to extend our user study function, and also the governance committee is going to work to implement a project management function for the specifications SIG to streamline the feedback loop from all the feedback that we're gathering at these sessions and activities and drive prioritization for work based on user feedback. 

**Rhys:** In-person meetups might be a thing coming to a town near you. Maybe we'll see. I think this would be a really fun thing to do, especially as a lot of us were just at KubeCon, and it seems like people are pretty into meeting in person again, so we'll see. 

**Rhys:** Six, probably most of you are maybe fully familiar with these, but I'll just go over them. Special interest groups: the goal is to improve the workflow and manage the project more efficiently. Each SIG meets regularly. You can access the meeting notes and recordings through the public calendar. 

**Rhys:** That's pretty much a thing or working group for pretty much all components. Languages of OpenTelemetry. There's also a governance committee and a technical committee, which I won't get too deep into. 

**Rhys:** You can kind of see the roles of each committee here. Show me for a second, and I can also share the slide deck too because there are some links to the resources that I mentioned in here. 

**Rhys:** Documentation? Yes, we have a lot of questions about documentation. If you do have questions, you can always talk to the ComSIG at hotel-dash.comms channel. Some languages we are aware are a little bit more comprehensive than others. 

**Rhys:** There is standardization and improvement work in progress at the moment. If you would like to help contribute, feel free to jump into the channel, attend one of their meetings, or open an issue directly in the repo. 

**Rhys:** I personally find it interesting to see what OTEPs have been proposed. They are open selling to enhancement proposals. It's a process for proposing changes to the spec, and they have to be cross-cutting changes that introduce new behavior changes or otherwise modify requirements. 

**Rhys:** It's kind of fun personally, I think, to go and look at what people are proposing or wanting to do. There's some interesting stuff in there. 

**Rhys:** Getting involved: the first one I want to cover is how do I get help using OpenTelemetry? There are multiple ways. CNCF Slack, you have to sign up for an account with the CNCF Slack instance. But once you get in there, there’s pretty much an ozone channel for whatever it is you’re looking for: languages, components, collector, etc. 

**Rhys:** There are also vendor-specific channels, or you can go to the general OpenTelemetry vendor channel if you're having problems with a specific vendor that you're using. 

**Rhys:** Of course, GitHub, you can open issues, jump in with comments on anything that's open. We also have the end user discussion groups, which I mentioned earlier. If you want to join and ask questions or share how you're using OpenTelemetry or help other people who are using OpenTelemetry in their organizations, that's another great way to get involved. 

**Rhys:** As far as contributions, we welcome any and all code and incoming contributions. If there's a specific language you're interested in or a specific component, go check out the SIG notes, see what they're talking about, or you can hop into any of the meetings and just kind of check it out. 

**Rhys:** Blog posts could be something that you've... you know, it could be something fun and so-called useless, but really, you know, if it brings so much joy, is it really useless? 

**Rhys:** So something fun that Jess did could be anything OpenTelemetry-related. We would love to see it. 

**Rhys:** As I mentioned, documentation: you are welcome to join the end user working group and give suggestions on things you'd like us to help with or do as for you as an end user. 

**Rhys:** Of course, you can also just share feedback, and there are different ways to do that. If you don't really want to get engaged with an interview, you are welcome to take part in our survey. I thought I linked it somewhere. 

**Rhys:** I have linked the survey in here. If you would like to share feedback that way, that is great. If you would like to participate in the end user working group or by way of the discussion group or end user interview, we would be very happy to have you. 

**Rhys:** And that's it. That's all I have. Thank you so much. I should have added more Jingle Bells and Christmas stuff. I feel not very festive, but I promise I am. 

**Speaker 1:** Fair, Jess. Thank you, Rhys. 

**Speaker 1:** And saying that, for those not following the chat, Johnny's saying they participate in some conferences related to DevOps, and they like to share about the power of observability and how OpenTelemetry can help us make our lives easier. 

**Speaker 1:** Do folks have questions? Since we've got 10 home minutes, we're happy to entertain if you have random questions about OpenTelemetry. We may or may not be able to answer them, but there's lots of knowledge in this room. 

**Speaker 2:** Yeah, and if anyone is having a specific question about Rhys's presentation, absolutely. 

**Speaker 3:** Well, actually, I was going to say about OpenTelemetry.net. We have a maintainer on the line. Is that Alan? 

**Alan:** Yes. 

**Speaker 3:** Yes, there are two. Mike Blanchard. Hello, Mike. Very important spot. That's why I'm like, it's okay if I call him out. 

**Speaker 2:** I will say that I tried to pull down the Honeycomb, the Happy Holidays happy hour. 

**Speaker 3:** Oh, it is... it's going to take a little bit of work, but I was going to try to see how easy it would be to get that reporting into a different tool than New Relic and see what it would look like. 

**Speaker 4:** I'm sure it would look probably amazing. 

**Speaker 2:** It will look mangled initially. 

**Jess:** I'm like, if you want to work at that, I'm happy to work with you on... I know where in the code it's choosing the height that works, and I also know how I use the browser tools in Honeycomb to figure out what height it was needing. 

**Jess:** Some of those tricks will also work in New Relic, so happy to work with you on that if you want because I would love to see what it looks like somewhere else. 

**Speaker 3:** I don't know if they're still doing them, but last year Grace and I were doing a lot of Legos for New Relic. I've got some of them here, and I wonder if they're like amazing art. 

**Speaker 4:** Oh, that's true. Grace is New Relic's social media person and a huge Lego fan. 

**Speaker 3:** But yeah, I think Legos tie in very well with ASCII art, and you know lots of tech people are Lego fans, so... 

**Speaker 5:** True, true. 

**Speaker 6:** Other questions that folks have? 

**Speaker 7:** We can also go ahead and end the call early. 

**Speaker 8:** Yeah, Ellen, I'm Jessatron at Honeycomb if you want to get in touch. 

**Speaker 7:** Yes, and I'll post the link to Jess's calendar. 

**Speaker 6:** Sounds good! 

**Speaker 7:** Yeah, nice to meet y'all! 

**Speaker 8:** You too! 

**Speaker 6:** Well, thanks everyone. It was great to see you all! 

**Speaker 7:** Yeah, great to see you. 

**Speaker 6:** It was fun to have a chatty group. Thank you all for joining, and a couple of you for putting yourself on video. That's always great for us. 

**Speaker 8:** Yeah, I'll Zoom to like see faces. 

**Speaker 6:** Cool. Thank you! 

**Speaker 7:** Yeah, feel free to reach out to any of us with questions or if there's anything you want to follow up on. Happy holidays!

## Raw YouTube Transcript

thank you so the open Telemetry and practice series is traditionally a pretty serious talk Series where we every every month we go deep into implementing open Telemetry in a particular language and we talk to an end user and uh um what in who's actually implementing it in production and we talked to um usually a maintainer of the project who can talk about like these are the best ways to implement um and this is a little bit different of a format because we decided to do three or four short talks that didn't fit well together um Adriana is going to lead off today with um talking about observability for hashicord products um she currently works at lightstep and um used to um work um fully in a Hashi shop yes and then a little bit later we'll have Rhys talking about um how end users can get involved with the project which I expect to be highly interactive and um Jess jessatron um is going to give us a talk about um using open Telemetry to make asksy ASCII are in heat Maps which is cool you are trying to get your team to learn about open Telemetry and pay attention and utterly useless um Adriana you ready to yeah I'll start so I'm ad Hocking this uh all right so um as Rin mentioned I used to work at a Hashi shop so I have a I actually have a kubernetes background was thrust into this hashicorp world where my previous employer um they ran their containerized workloads on on Nomads so I found myself in a situation where I had to quickly understand this Nomad thing because I was managing a platform team which supported Nomad console and Vault for the entire Enterprise um so that's how I began my dabblings in the Hashi world and and from that I I ended up becoming a hatchery Corp Ambassador because I I dug in blogged about it and continued to do so um and at the same time at this former company I was also managing an observability team and I came to learn about observability team at around the same time that I came to understand um Nomad so these were two things that I was doing at the same time learning about at the same time which led me into uh open Telemetry so um now that I work at lightstep I've had a chance to contribute more in the open Telemetry Community as I mentioned before um I've uh I've worked in the in in the comms area so I've I've contributed some content to the doc site I've worked I've made some contribution demo app and I was actually pleasantly surprised to learn about the demo app which I think launched It's relatively recent right that the demo app came out and and I like it because it showcases open to limit like what you can do with open Telemetry and I think the original version of the demo app that came out you could uh run everything in Docker compose locally and then more recently there's um uh the the team created um home charts for this one and she got me thinking hey if this thing runs Brunetti's wouldn't it be super cool to get this thing to run a nomad and so it's been part of my wish list ever since I I learned about like the hotel demo app Helm charts I'm like okay finally carved out some time to do this and I got it up and running um in a local Hashi environment on on my machine so there's um there's this really cool tool called Hashi Cube which is similar to you know like running mini Cube or k3s or whatever like one of these like local kubernetes Dev environments similar sort of thing for the hashy stack um which was created by a a third-party company called uh Serbian and and I love using this tool because it gives me like a full-fledged Hashi environment similar to what you would get I mean obviously smaller scale to what you would get in a data center but it replicates the the type of setup because in in real life the um Nomad by itself is is kind of useless so you need like the power of of console for service Discovery involved for for Secrets management along with Nomad to get all this stuff um to to really have like a a robust system to manage your your containerized workloads so I have uh I have this Hashi Cube running on on my machine locally which I can show you um I'll do like a little screen share well first I'll I'll show you my hashiq oh wait did uh am I sharing the right one hearing your hashes cool I have like so many windows the correct cashy tube I don't know over the time yeah this well okay so it says this is this is my Hatchi Cube startup sequence so hashikub what it what it is so it's it's basically using vagrants to provision either a um VM a virtualbox uh VM or um I'm I'm on an M1 Mac and virtualbox and M1 Max don't play nice I think there's like possibly a version of virtualbox that plays nice with M1 Max now but at the time it didn't so the uh the maintainers of hashic cube basically stand up all these Hashi products in a single Docker image um so this version of hashikub that I'm running where you can see like the tail end of the startup sequence here um it's running mad Vault console all in one all-in-one Docker image and so if I share I'll share you my Nomad console here so you can see um problem when I lose sight of all my windows um the oh here we go okay so this is this is Nomad and these are all of the services that make up um the hotel demo app running on Nomad locally on my machine which is pretty freaking exciting um I basically so I had to go through the um the home chart there's a for the for the hotel demo Helm chart um there's a there's a folder in the helm chart repo that shows like the rendered yaml so I basically started with the rendered yamls and went through the process of translating um these these um kubernetes manifests for each service into the equivalent Nomad job spec which is what you see here so for example like we're looking at the feedback service this is running on on Nomad um and if we go over here we can see um there's a lot of stuff here so we can see the logs of the true flag service nothing terrible is happening here we go it's running so we can see from from our our dashboard here that all of the services are up and running so it's made up of like all these uh different um different Services written in different languages plus we also have I had to convert um I had to nomadify um redis postgres we had the hotel collector um what else there was one more out there was Prometheus and grafana and I used trafic for load balancing so I can expose my services to the outside world and so what that looks like then um so to be able to access the hotel demo apps endpoints and hopefully my computer won't crash here um so I have IX endpoint called Hotel Dash demo dot localhost which is accessible this is just uh just something accessible off my local host and then the uh so Jaeger UI is is is exposed um as part of the my demo app configuration so we see Jaeger is up and running here we've got the demo apps UI going uh running here so we can buy stuff we can check stuff out and buy let's buy this telephone and super and then if we check Like Jaeger we can look to see sorry the screen sharing thing is like getting in my face um we can see our traces I think the hamsters are running really really hard here we can see it's produced some some traces here that we can see here in addition um when I know modified this there is also a some grafana dashboard so some cool dashboards that come pre-loaded pre-configured you can see there's some stuff going on here with the hotel collector and then there's also this demo dashboard which gets some stats from the recommendation service so that's um that's basically it I can show you also like what a job spec looks like in Nomad um I want to see more traces oh you want to see more traces yeah right I picked like the saddest Trace yeah that's what happens when you're like ad Hocking it okay let me uh let's let's pull up a more interesting Trace I think the recommendation service has interesting traces that we can see checkout's usually good check out cool let's find some traces oh yeah look at all those look at all those Services yeah there's some colors look at it go to all the different services yeah this is actually pretty cool you're right I picked the dinkiest to Showcase all this right um and all this is happening like on my machine in this like Docker image that's running like all the hashy things um which is super cool um I did want to show also like what a um um what a nomad job spec looks like um let me just share my screen for that so Nomad is like it's an alternative to kubernetes right exactly exactly yeah and it's it's interesting too because it doesn't just run containerized workloads like it can run like VM workloads it can even run like a jvm or like IIs um so it's kind of cool that way um here we go sorry I was looking for the one okay so let me pick um let's hear it a job spec is like a kubernetes deployment yeah exactly so here I'll uh I've got kubernetes deployment I'll put it side by side here all right cool okay so this is the feature flag service on the right we've got the feature flag service service definition this is our um our uh our Nomad job specs so unlike um kubernetes where you have like all these different yaml files that make up the the various um objects for that make up your manifest everything is self-contained in one um job spec file which is written in HCL which is a hash report configuration language so I liken it to like I mean if you've used if you've used terraform like this it looks familiar um I I find HCL is like if if Json was like slightly improved that's what it would look like I do find it's like easier to read than Json but this is basically what it looks like here so for example over here um in our Network definition you see that we Define two ports 8081 and uh five zero zero five three which lo and behold we defined those over here in our uh in our service yaml for the feature flag service um and then if we scroll over to here so to this task definition we're saying that we're using the docker driver so this is saying okay we're using containerized workload let's find the equivalent in the uh in the Manifest all right here so we go to our deployment and we can see where we Define our image I've defined an image pull time out because sometimes my network doesn't like to behave so I don't want Nomad to like crap out after five minutes and say sorry I can't pull your image sucker and then fail my deployment um over here we've got the ports configuration basically saying well just like here we're saying that this container requires these two ports well on the left side here in our in our HCL we see that our HTTP and grpc ports that we defined up here that's what they're pointing to um and then the other thing that I wanted to point out was over here in this end definition these are our environment variables which on the most part correspond to the ones that we Define in our deployment I did exclude some like you know these kubernetes Hotel kubernetes ones because obviously we're not running this kubernetes we're running them in Nomad but the non-kubernetes ones I translated over to Nomad land um and then I wanted to point out also that um over here in this uh what's called the temp stanza so be basically these these the groupings and the curly braces they call them the stanzas I'm defining two additional environment variables but they're defined in a slightly different way because they're referencing Services um uh from from other Nomad job specs so um here to be able to reference for example our database service um to get the information so the IP address and the port of the database service um we can't hard code that information right because that stuff can potentially change especially the IP so in order to get that information to Define this environment variable we have to use we basically have to look up this this service in in console which as I mentioned is for service Discovery and so um to find out what the information of that Services you refer to it by service name so if we open over here I'm going to open this FF postgres so this is the job spec for postgres I have a service named FF postgres service which if we look over here to do here we go over here so it basically says Hey console I want to pull up a service called FF postgres service and pretty please tell me the address and port number of the service so I can plug it in to this environment variable and so we use the template stanza to do this kind of dynamic definition and we have to tell it that the destination is going to be an environment uh variable because one of the things that you can do with the template stands as well is you can use it for configuration files so similarly very similar functionality to a config map in in kubernetes and then here is where we Define our resources this is in um megahertz or CPU and our our memory is in um megabytes um um and then the other thing that I wanted to point out is here I've got some rules on restarting the service so because there's no dependencies that you can Define in your services and Nomad like you know how you would do in Docker compose saying hey this service is dependent on that service you don't have that kind of dependency definition in Nomad so um basically the jobs start when they start which means that like for example example this feature flag search is actually relying on the database and the hotel collector to be up and running well what if the feature flag service starts before the Hotel collector and the database startup um if we don't put some restart rules in place then um it'll when it starts up and these two Services aren't up or one of these two Services isn't up it'll crap out and then that's it it's it's dead so what we want to do is put some rest over here basically saying within the span of two minutes we're going to try to restart this thing 10 times with a 15 minute sorry a 15 second interval between restarts and either after 10 attempts or two minutes whichever comes first if this fails to restart um we are basically going to say okay we're just gonna wait a little bit and reattempt that again the default mode for this this normally is fail so if if it didn't if it doesn't successfully restart in in 10 attempts within two minutes it would completely fail and then that means your whole your whole application deployment fails right because of all these dependent services so this basically gives you some protection saying okay well we'll keep trying we'll keep trying until things are up and running which ends up uh being very very be convenient um and then the final thing that I wanted to point out was that um we also have these checks here so these are uh these are basically health checks they're similar to uh the types of health checks that you would see in kubernetes like liveness liveness probes and Readiness probes and I wanted to show you actually what that looks like in console really briefly um let me just pull that up yeah and we're going to move on to Jess Citron after the console showing so if you have more Rihanna think them up please yes I'll show this very briefly but this basically shows all of our services and then it shows like if we look at the feature flag service we have two Services one for our Jr PCR and so this shows us that hey like we're we're able to to hit our uh our endpoints so um it sends a it sends a signal back to Nomad like all systems go hurray hurray so that's basically it in a nutshell so okay follow-up questions last parting thoughts about nice job yeah I agree nice job that was a super good demo and yeah good example of how to use the demo app um so just a lot of thinking is um actually going to show us something totally useless but super fun for training people or teaching um how to make um ask KR into a heat map using open telemetry right right so I made this thing for Christmas uh for Christmas gimmicks I guess I don't know um it's in a repo honeycombio slash happy Ollie days um which is cute and and you can you can clone this repo or run it and get pod uh and if you give it your honeycomb API key this is Honeycomb like the the UI is Honeycomb specific because it had to be specific to the the display um but it does use open telemetry so I'm going to give it a honeycomb API key oh it's still in my paste buffer great and then I'm going to run this little app and this app is in node um typescript so it has created a bunch of spans and uh in a Trace using where's my here we go uh start active so it does a start active span and node and then um for each it's figured out what spans it wants to send and then it does a start span for each of them and supplies a bunch of attributes and then ends each one they all go into one Trace uh it's given me a link to the data sets oh it's a good thing I'm following that link because apparently would you go to the link go to the link there it goes apparently my data set is called Fufu free but then in the readme it describes how to do this if you do a heat map on the height field and you get the last 10 minutes and you're starting to see something but then I need to pick graph no no no up here granularity five seconds oh that's so cute isn't it cute and and the cool part is that that you can use this program I mean I don't know what it's going to look like in any other system because uh because I I've customized the um the heights to the bucket sizes that honeycomb uses in heat Maps so you'd have to tweak the code to make it do something in some somebody else's heat Maps oh but it it actually pulls this out of um where is it images now there should be an images directory in here oh input input don't peak.png uh so if you give it a PNG that's between 25 and 50 pixels tall and you probably want it between 1 and 200 pixels wide then it can convert that into a heat map oh it's converting the heat map based on the blue channel in the PNG it uses the other one to get some attributes which does some fun things in honeycomb because you can pick bubble up and be like what is different about oh oh check this out okay my new favorite feature of honeycomb w ow cut on this stupid little do me anything is gone okay which is very useful sometimes I'm sure but not in here okay so now that I've gotten rid of that uh what is different about the spans in the second reindeer um and honeycomb does its little what is different analysis and it says the reindeer name that one has a reindeer name of dancer and then if you Group by the reindeer name you can go back and like oh oh wait hold on I've got to do the trick of uh wait wait give me give me the right 10 minutes um it wants to like the the Santa and his reindeer are like moving on I need to switch to Absolute time okay now let's group By Reindeer name okay now it's lost the granularity so let's fix that granularity five seconds okay but now uh results Tab and we have the different reindeer names so there's no reindeer name this there's dancer this one is Rudolph and this one is Prancer um and yeah so it's cute that way it's got different uh fields and those are based in case you want to use this yourself um and Supply your own image those are based on the red channel in the PNG and then there's a little key for uh how much red between 0 and 255 is in that color and what the fields are um so that's also encoded in a PNG and you can you can do it yourself and make your own um this this gets like officially released on Monday um and it'll be advertised and stuff but but this but I'm not and none of that stuff am I telling you how to fix it yourself so y'all are getting that um and there's one other trick in this data uh which is if you do a Max of Stack Heights and group by Stack group um then you get some nonsense but if you change the graph settings to use a stack graph then you start to get something and then if you get the order by right stack group descending come on do it a Christmas tree oh my God that's awesome and and that you can also generate yourself because that is based on house.png obviously um it used to be a house now it's Christmas tree uh and of course there's limitations you have to have like um all the colors have to be on top of one another and you can't have a color that's both under and over and you don't control what the colors actually show up as but um if you're clever you can make your own pngs uh and then oh yeah I've got some groups on that you could you you can Group by um oh it is great by Stack group that wasn't necessary but here's the names of them star and background and tree and stuff like that yes where do people go to find this app it is at Honeycutt miles slash happy Ollie days and so yeah you can download this and if you have a free honeycomb account um or if if you get it to work in another tool that would be awesome I would love to hear about it oh thanks Johnny um yeah so that's that's that we'll find stop share maybe not Daniel's like I'm running not walking to try this out it's fun it's true um and uh I have a question which is how do you think this can be useful to people as a tool to teach about heat Maps observability yeah yeah because you can I mean you can ask like how how do I draw it and the answer is that um I send a different number of spans which of course is it this one which of course I also stick all the intermediate data on the spans because the owls what I debug it um no that's the clearly the wrong field uh show me the trace I haven't made the trace cute yet someday I'll make this have a drawing in it too um span you know count amount how many oh well uh I send multiple spans per uh pixel if I want a dark color because honeycomb says darker is more and lighter is fewer so there's just one Span in in these um oh you know what I can find that field if I do Bubble Up what's different about these that only have one um spans at once there it is okay so this spans at once these only have one span at a time and uh some of the the darkest ones have 10 spans at a time um so if you think if you can use it to be like how how does a heat map um mostly it's just entertaining and it does really illustrate like bubble up um letter all of these most of these are letters and some of them have oh they have different letters yeah uh so Bubble Up is pretty well illustrated by this I think um I want to say what Bubble Up is for folks who aren't honeycomb users Bubble Up is Honeycombs what is different so you can draw the Box and um and um it does the statistical analysis on What fields are different it's just cute that was super good there's not question threes do you want to go ahead and talk about um end user working group work I mean yes but also how do I follow up we're doing is systematic and important and slowly marching through things um Jessica to do the fun creative yeah yes yeah this is um I mean I have some like one or two fun Graphics but it's not gonna be anything as cool as Jesse Jesse trance um so you'll have to make two um yeah I just wanted to just talk real quick on something that we've surfaced um just from talking to a wide variety of end users is um a lot of people are not really aware of how to navigate the community on how they can get involved um or that they even can get involved um so I'm not sure um I know there's um a couple contributors on the call um not sure everyone else's end user um but hopefully this will be of some utility utility for you so a couple things we'll go over um this time of the community at large some of the different parts of it and then we'll talk about how you can get involved if you're interested in some of the different ways that you can get involved so we've mentioned a few times the end user working group that we a lot of us are a part of um what is the andeserving group we have two primary goals one is to Foster sense of vendor agnostic Community for end users and two is to create a feedback loop between the end users and project maintainers but the overarching goal of improving the um project software so what are some of the working group activities that we have implemented so first of all this is one of them um this is rin's child um but we are very excited um a hotel in practice is what it is so every month keep an eye out for more fun talks um presentations and you know casual conversations um we have the monthly discussion groups now with a maintainer per session and in all regions so America emea which is which I just found out stands for Europe Middle East and Africa and APAC which I'm actually not sure where those things were but it's Asia and the Pacific region imagine where AC stands for um and those are all on the open symmetry public calendars we also have end user interview and feedback sessions where we will talk to um an end user about their adoption implementation and challenges that they face and get the feedback uh shared back to the open telemetry maintainers so if you're interested if you're an end user and you're interested in Sharing feedback in one of these sessions please reach out to myself Rin or Adriana we would be happy to get you on the schedule and we are also new um for uh end user interviews moving forward we're going to turn them into profiles for the open slim shoe blog to kind of make the um implementation and adoption um that other end users have done and their organizations more discoverable and we also have a community survey so that's another way that you can contribute if you don't really want to get too involved but you still want to have a way to share your thoughts and opinions on how using a potomacy is for you some of the stuff that's upcoming for the working group um we want to extend our user study function and also the governance committee is going to work to implement a project management function for the specifications Sig to one streamline the feedback loop um from like all the feedback that we're gathering at these sessions and activities and drive prioritization for work based on user feedback and in person meetups this might be a thing coming to a town near you maybe we'll see um I think this would be a really fun thing to do especially as like I think you know we a lot of us are just at kubecon and it seems like people are pretty into meeting in person again so we'll see um and then six probably most of you are maybe fully familiar with these but um I'll just go over the go over them um special interest groups the goal is to improve the workflow and manage the project more efficiently each Sig needs regularly um you can access the meeting notes and recordings um through the public calendar and that's pretty much a thing or working group for pretty much all components um languages of open telemetry there's also a governance committee and a technical committee which I won't get too deep into they can kind of see the roles of each committee here show me for a second and I can also share the slide deck too because there are some links to the resources that I mentioned in here um documentation yes we have a lot of questions about documentation if you do have questions you can always talk to the comsig at Hotel Dash coms Channel some languages we are aware um are a little bit more comprehensive than others there is standardization and improvement work in progress at the moment if you would like to help contribute feel free to jump into the channel attend one of their meetings or open an issue directly in the repo so I personally find it this kind of interesting to see what um what oteps are have been proposed um they are open selling to enhancement proposals it's a process for proposing changes to the spec and they have to be cross-cutting changes that introduce new Behavior changes our Behavior or otherwise modify requirements and it's kind of fun personally I think to go and look at what people are proposing or wanting to do there's some interesting stuff in there okay and also getting involved um the first one I want to cover is how do I get help using a photometry there are multiple ways CNC of slack you have to sign up for an account with cncf slack instance but once you get in there um there's pretty much an ozone channel for um whatever it is you're looking for languages components collector Etc there's also vendor specific um channels or you can go to the general Hotel vendor Channel if you're having problems with a specific vendor that you're using and of course GitHub um you can open issues jump in with comments on anything that's open um and we also have the end user discussion groups which I mentioned earlier if you want to join and ask questions or share how you're using open Telemetry or help other people who are using open filament organizations that's another great way to get involved and for as far as contributions we welcome any and all code in oncoming contributions um if there's a specific language you're interested or a specific component go check out the Sig um Sig notes see what they're talking about or you can hop into any of the meetings and just kind of check it out blog posts um could be something that you've you know it could be something like fun and so-called useless but really you know if it brings so much joy is it really useless no so something you know fun that just did could be anything open until related basically we would love to see it um as I mentioned documentation you are welcome to join the end user working group and you know give suggestions on things you'd like us to help with or do um as for you as an end user and of course you can also just share feedback and there's different ways to do that if you don't really want to get engaged um with a interview um you are welcome to take part in our survey which I thought I linked somewhere I have linked the survey in here if you would like to share feedback that way that is great if you would like to participate in the Indies working group um or uh by way of the discussion group or end user interview we would be very happy to have you and that's it that's all I have thank you so much I should have added more Jingle Bells and Christmas stuff I feel not very festive but I promise I am Fair Justice thank you Reese and saying that for those not following the chat Johnny's saying um they participate in some conferences related to devops and they like to share about the power of observability and how open Telemetry can help us make more easy our lives do folks have questions um since we've got 10 home minutes we're happy to entertain if you have random questions about open Telemetry we may or may not be able to answer them but lots of knowledge in this room yeah and if anyone is having specifically a question about racist presentation absolutely well actually I was going to say about open telemetry.net we have a maintainer on the line is that Alan yeah yes there are two Mike Blanche Blanchard hello Mike very important spot that's why I'm like it's okay if I call him out I will say that I tried to uh pull down the um honeycomb um The Happy Holidays happy hour oh it is it it's gonna take a little bit of work but I was I was gonna try to see how easy it would be to get that reporting into a different tool than to like be Relic and see if that uh see what it would look like I'm sure it would look probably amazing it will look mangled initially I'm like if if you want to work at that and um I'm happy to work with you on like I know where in the code it's choosing the height that works and I also know like how I use the browser Tools in honeycomb to figure out what height it was needing um uh which uh some of those tricks will also work in new relics so happy to work with you on that if you want because I would love to see what it looks like somewhere else I don't know if they're still doing them but last year Grace and I were doing a lot of Legos for New Relic I've got some of them here and I wonder if they're like amazing art oh that's true Grace's New Relic social media person and a huge Lego fan um but yeah I think Legos tie in very well with asciar and you know lots of tech people are Lego fans so true true that works other other questions that folks have we can also go ahead and end with call Early yeah yeah Ellen I'm jessatron at honeycomb if you want to get in touch yes and I'll post the link to um Jessica trance calendar sounds good yeah nice to meet y'all you too well thanks everyone it was great to see you all yeah great to see you have a good fun to have a a chatty group thank you all for joining and a couple of you for putting yourself on video that's always great for us yeah I'll Zoom to like see faces cool thank you hey yeah feel free to reach out to any of us with questions or if there's anything you want to follow up on happy holidays

