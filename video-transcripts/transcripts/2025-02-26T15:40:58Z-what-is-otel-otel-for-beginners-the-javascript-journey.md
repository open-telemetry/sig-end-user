# What is OTel? | OTel for Beginners - The JavaScript Journey

Published on 2025-02-26T15:40:58Z

## Description

Want to learn more about OTel but have no idea where to get started? OTel for Beginners - The JavaScript Journey series is ...

URL: https://www.youtube.com/watch?v=iEEIabOha8U

## Summary

In this introductory video titled "OTel for Beginners," Lisa Jung, a member of the OpenTelemetry (OTel) Communication and End User Special Interest Groups (SIGs), shares her journey of learning about OTel and aims to guide others through the process. The video explains the concept of observability in modern software systems, highlighting its importance for understanding and diagnosing issues within complex infrastructures. OTel is presented as an open-source framework that enables the generation, collection, management, and export of telemetry data, helping to avoid vendor lock-in by establishing a standard for data transmission across different observability backends. Lisa emphasizes the benefits of using OTel, such as reduced costs and simplified vendor transitions, and provides resources for viewers to begin their own OTel journey, particularly focusing on JavaScript in upcoming episodes. The video encourages viewers to engage with the OTel community for support and further learning.

## Chapters

00:00:00 Introductions
00:00:40 What is observability?
00:01:15 Importance of telemetry data
00:02:00 Introduction to OTel
00:03:30 Vendor lock-in explained
00:04:15 Benefits of OTel
00:07:15 OTel community resources
00:08:00 Getting started with OTel
00:08:00 OTel documentation overview
00:09:00 Upcoming JavaScript Journey episode

## Transcript

### [00:00:00] Introductions

**Lisa:** Hi! Welcome to OTel for Beginners. My name is Lisa Jung and I'm a member of the OTel Communication SIG and End User SIG. I recently began my journey with OTel and as a newbie, I had a tough time figuring out how to get started. I want you to have a different experience, so I'll learn alongside you and share what I'm learning through the series. Depending on which programming language you're working with, you'll follow a language-specific journey. In this series, I'll go through the JavaScript journey to get you started with OTel.

### [00:00:40] What is observability?

Before we get our hands dirty, let's talk about what OTel is and why you should consider using it, and the resources to get started. OTel stands for OpenTelemetry and it plays an important role in observing your system. So let's talk about observability first, then delve into how OTel fits into all of this. Our modern software systems can consist of complex, multi-layered, and distributed systems with many interdependencies. A system without observability is like a black box; we have no idea what's going on inside, so if something goes wrong, it's going to be more difficult and more time-consuming to solve the problem. 

### [00:01:15] Importance of telemetry data

With observability, we turn this black box into a glass box. As a matter of fact, it helps you collect the data necessary to visualize and understand what's going on in your system. How do we make this possible? First, you have your infrastructure or applications that you want to observe. You'll collect data from it and send the data to the observability backend of your choosing. Then connect the backend to a visualization frontend where you can query and use the data that you're interested in. The most common types of data collected for observability are metrics, logs, and traces. These are known as telemetry data. 

### [00:02:00] Introduction to OTel

Getting the telemetry data into the backend is an important part of understanding your infrastructure or applications, and this is where OTel comes in. OTel is an open-source framework. Using OTel, you can add software to your applications or systems to generate telemetry data. This process is known as instrumentation. Then it collects, manages, and exports telemetry data to an observability backend and the database for storage. Different aspects of OTel make this process possible, and we're going to talk about that in more detail as we go through the JavaScript Journey. For now, remember that OTel is focused on the generation, collection, management, and export of telemetry data. You can easily instrument your applications or systems, no matter their language, infrastructure, or runtime environment, and the storage and visualization of telemetry are intentionally left to other tools. 

### [00:03:30] Vendor lock-in explained

So why should we consider using OTel? Before we answer this question, let's talk about something that almost all of us have experienced. Now, if we dig through our drawers at home, we could probably find a bunch of cables of different types. Why? Because the devices we own come from different vendors, and each vendor has a specific type of cable and port to charge or connect your gadget. We're all familiar with buying multiple products from the same vendor and investing in additional accessories and apps specifically designed for that product. Before we know it, we get so used to using the line of products that switching over to another vendor could get pretty difficult. 

### [00:04:15] Benefits of OTel

The product from another vendor may operate differently, which will take some time to learn and get used to. It would also cost us more money because the additional accessories or apps we invested in don't work with a product from a new vendor. This is a problem known as vendor lock-in, where the costs of switching vendors are so high that customers feel stuck with what they have. Then things are slowly changing with USB-C ports becoming the universal standard. Let's take the newest model of phones as an example. It doesn't matter if you're using an iPhone or an Android. You could charge or connect many of these phones with a USB-C cable because a universal standard has been set. Users can use the same cable regardless of how many times they charge their phones. 

OTel has similar implications in observability as a USB-C does for phones. Let's do a quick review. We have our infrastructure or applications we want to observe. We want to collect telemetry data and send it to an observability backend for storage, so this data can be queried and visualized with an observability frontend. Say you have three observability backends to choose from: vendors A, B, and C. Each vendor often has proprietary instrumentations, agents, and or collectors. Now, let's say you picked vendor A. You're using their proprietary instrumentations, agents, or collectors and sending the data to their backend. 

But your needs change down the road; you want to switch your backend to vendor B. But switching vendors is not as simple as you might think. You can't just send the existing data from vendor A to B because vendor B requires its own instrumentation, agents, or collectors, so you can't accept data from vendor A's proprietary instrumentation. Now your development team has to change their instrumentation, possibly to a new proprietary instrumentation of vendor B. Now imagine doing this for thousands of Linux machines or dozens of applications. Is the cost of money, time, and effort worth the benefits of changing vendors? 

As you could see with this setup, the cost of switching vendors can get so high that customers can be effectively locked in by their choices. Now, imagine if all vendors accepted the same standard to send or receive telemetry data, similar to many phone companies accepting USB-C as a standard. When you switch vendors, you don't need to learn proprietary instrumentations, agents, or collectors each time. You just need one technology and learn a single set of APIs and conventions associated with it. Whatever data you generate with this technology is yours. You could send the data to any observability backend that accepts the standard, so you could easily switch vendors with substantially reduced cost, time, and effort. 

### [00:07:15] OTel community resources

This is exactly what OTel does for you. It creates an open standard, a set of guidelines, rules, or specifications to send and receive data. There's quite an incentive for the vendors to accept OTel. Many customers now prefer OTel to avoid vendor lock-in. They want to learn a single set of APIs and conventions rather than having to learn a new one every time they change a vendor. They also want to own their data and send the data to any observability backend that accepts these standards. Now, the vendors benefit from accepting OTel as well. Customers may already be familiar with using OTel. There's a vibrant OTel community that serves as a great resource because of that. Accepting OTel helps the vendors reduce their support and implementation costs. 

### [00:08:00] Getting started with OTel

On top of that, there is even more drive for innovation. Vendors are receiving the same data, so they have to innovate to stand out from the competitors. As you can see, there are many benefits to accepting open standards, and you can take advantage of these benefits by using OTel. Now that we covered what OTel is and why you should use it, let's go over the resources to get started. The links to all the resources are included in the description of the video. The best place to get started is the OTel documentation. The documentation is continuously being improved, so the page may look different by the time you watch this video. 

So use a link in the description to check out the latest page. The first place in the doc you should start with is the Language APIs and SDKs. As I mentioned earlier, your OTel journey will differ depending on the programming language you're working with. Select the language of your choice and you should end up on a page that lists all the resources to get started. Next, we have the official OTel YouTube channel. You'll find helpful videos along with the OTel for Beginners series on this channel. 

### [00:09:00] Upcoming JavaScript Journey episode

Last but not least, as you start your OTel journey, you'll come across a lot of questions. We have a huge community of OTel users on Slack. So join the CNCF Slack Channel, post your questions on the OpenTelemetry channel, and connect with other community members. Again, check the description of this video to access all these resources. In the next episode, we'll talk about how to get started with a JavaScript Journey, so stay tuned for that. Thank you for watching, and I'll see you in the next episode.

## Raw YouTube Transcript

Hi! Welcome to OTel for Beginners. My name 
is Lisa Jung and I'm a member of the OTel Communication SIG and end User SIG. I recently 
began my journey with OTel and as a newbie, I had a tough time figuring out how to get started. 
I want you to have a different experience so I'll learn alongside you and share what I'm learning 
through the series. Depending on which programming language you're working with, you'll follow 
a language specific journey. In this series, I'll go through the JavaScript journey to get you 
started with OTel. Before we get our hand dirty, let's talk about what OTel is and why you 
should consider using it and the resources to get started. OTel stands for OpenTelemetry and it 
plays an important role in observing your system. So let's talk about observability first, then 
delve into how OTel fits into all of this. Our modern software systems can consist of complex, 
multi-layered, and distributed systems with many interdependencies. A system without observability 
is like a black box we have no idea what's going on inside so if something goes wrong it's going to 
be more difficult and more time consuming to solve the problem. With observability, we turn this 
black box into a glass box. As a matter of fact, it helps you collect the data necessary to 
visualize and understand what's going on in your system. How do we make this possible? First, 
you have your infrastructure or applications that you want to observe. You'll collect data from it 
and send the data to the observability backend of your choosing. Then connect the back end to a 
visualization front end where you can query and use the data that you're interested in. The most 
common types of data collected for observability are metrics, logs, and traces. These are known as 
telemetry data. Getting the telemetry data into the backend is an important part of understanding 
your infrastructure or applications, and this is where OTel comes in. OTel is an open-source 
framework. Using OTel, you can add software to your applications or systems to generate telemetry 
data. This process is known as instrumentation. Then it collects, manages, and exports telemetry 
data to an observability backend and the database for storage. Different aspects of OTel make 
this process possible, and we're going to talk about that in more detail as we go through 
the JavaScript Journey. For now, remember that OTel is focused on the generation, collection, 
management, and export of telemetry data. You can easily instrument your applications or systems, no 
matter their language, infrastructure, or runtime environment, and the storage and visualization of 
telemetry are intentionally left to other tools. So why should we consider using OTel? Before we 
answer this question, let's talk about something that almost all of us have experienced. Now, if we 
dig through our drawers at home, we could probably find a bunch of cables of different types. Why? 
Because the devices we own come from different vendors, and each vendor has a specific type of 
cable and port to charge or connect your gadget. We're all familiar with buying multiple products 
from the same vendor and investing in additional accessories and apps specifically designed for 
that product. Before we know it, we get so used to using the line of products that switching over 
to another vendor could get pretty difficult. The product from another vendor may operate 
differently, which will take some time to learn and get used to. It would also cost us more money 
because the additional accessories or apps we invested in don't work with a product from a new 
vendor. This is a problem known as vendor lock-in, where the costs of switching vendors are so high 
that customers feel stuck with what they have. Then things are slowly changing with USB-C 
ports becoming the universal standard. Let's take the newest model of phones as an example. 
It doesn't matter if you're using an iPhone or an Android. You could charge or connect many 
of these phones with a USB-C cable because a universal standard has been set. Users can 
use the same cable regardless of how many times they charge their phones. OTel has similar 
implications in observability as a USB-C does for phones. Let's do a quick review. We have 
our infrastructure or applications we want to observe. We want to collect telemetry data and 
send it to an observability backend for storage, so this data can be queried and visualized with 
an observability frontend. Say you have three observability backends to choose from: vendors 
A, B, and C. Each vendor often has proprietary instrumentations, agents, and or collectors. Now, 
let's say you picked vendor A. You're using their proprietary instrumentations, agents, or 
collectors and sending the data to their backend. But your needs change down the road, 
you want to switch your backend to vendor B. But switching vendors is not as simple as you might 
think. You can't just send the existing data from vendor A to B, because vendor B requires its own 
instrumentation, agents, or collectors, so you can't accept data from vendor A's proprietary 
instrumentation. Now your development team has to change their instrumentation, possibly to a 
new proprietary instrumentation of vendor B. Now imagine doing this for thousands of Linux machines 
or dozens of applications. Is the cost of money, time, and effort worth the benefits of changing 
vendors? As you could see with this setup, the cost of switching vendors can get so high that 
customers can be effectively locked in by their choices. Now, imagine if all vendors accepted the 
same standard to send or receive telemetry data, similar to many phone companies accepting USB-C 
as a standard. When you switch vendors, you don't need to learn proprietary instrumentations, 
agents, or collectors each time. You just need one technology and learn a single set of APIs and 
conventions associated with it. Whatever data you generate with this technology is yours. You could 
send the data to any observability backend that accepts the standard, so you could easily switch 
vendors with substantially reduced cost, time, and effort. This is exactly what OTel does for you. 
It creates an open standard, a set of guidelines, rules, or specifications to send and receive 
data. There's quite an incentive for the vendors to accept OTel. Many customers now prefer OTel to 
avoid vendor lock-in. They want to learn a single set of APIs and conventions rather than having to 
learn a new one every time they change a vendor. They also want to own their data and send the data 
to any observability backend that accepts these standards. Now, the vendors benefit from accepting 
OTel as well. Customers may already be familiar with using OTel. There's a vibrant OTel community 
that serves as a great resource because of that. Accepting OTel helps the vendors reduce their 
support and implementation costs. On top of that, there is even more drive for innovation. Vendors 
are receiving the same data, so they have to innovate to stand out from the competitors. As you 
can see, there are many benefits to accepting open standards, and you can take advantage of these 
benefits by using OTel. Now that we covered what OTel is and why you should use it let's go over 
the resources to get started. The links to all the resources are included in the description 
of the video. The best place to get started is the OTel documentation. The documentation is 
continuously being improved, so the page may look different by the time you watch this video. 
So use a link in the description to check out the latest page. The first place in the doc you 
should start with is the Language APIs and SDKs. As I mentioned earlier, your OTel journey 
will differ depending on the programming language you're working with. Select the language of your 
choice and you should end up on a page that lists all the resources to get started. Next, we have 
the official OTel YouTube channel. You'll find helpful videos along with the OTel for Beginners 
series on this channel. Last but not least, as you start your OTel journey, you'll come across a lot 
of questions. We have a huge community of OTell users on Slack. So join the CNCF Slack Channel, 
post your questions on the OpenTelemetry channel and connect with other community members. Again, 
check the description of this video to access all these resources. In the next episode, we'll 
talk about how to get started with a JavaScript Journey, so stay tuned for that. Thank you for 
watching, and I'll see you in the next episode.

