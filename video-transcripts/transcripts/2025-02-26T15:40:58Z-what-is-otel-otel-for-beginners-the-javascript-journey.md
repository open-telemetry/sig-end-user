# What is OTel? | OTel for Beginners - The JavaScript Journey

Published on 2025-02-26T15:40:58Z

## Description

Want to learn more about OTel but have no idea where to get started? OTel for Beginners - The JavaScript Journey series is ...

URL: https://www.youtube.com/watch?v=iEEIabOha8U

## Summary

In this introductory video titled "OTel for Beginners," Lisa Jung, a member of the OpenTelemetry (OTel) Communication and End User Special Interest Groups, shares her personal journey of learning OTel and aims to guide viewers through the process. The video explains the importance of observability in modern software systems and how OTel serves as an open-source framework to generate, collect, manage, and export telemetry data, thereby preventing vendor lock-in. Lisa emphasizes the advantages of using OTel over proprietary solutions, including reduced switching costs and ease of use across different observability backends. She also highlights the resources available for getting started with OTel, including official documentation, YouTube tutorials, and community support on Slack. The next episode will focus on beginning the JavaScript journey with OTel.

## Chapters

Sure! Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions to OTel for Beginners  
00:01:30 What is OpenTelemetry (OTel)?  
00:02:45 Importance of Observability  
00:04:00 Turning a Black Box into a Glass Box  
00:05:30 Types of Telemetry Data: Metrics, Logs, and Traces  
00:07:15 Instrumentation and Data Collection in OTel  
00:09:00 The Problem of Vendor Lock-In  
00:11:30 Comparison of OTel to USB-C Standard  
00:14:00 Benefits of Using OTel for Observability  
00:16:15 Resources to Get Started with OTel  

Feel free to ask if you need more details on any specific section!

# OTel for Beginners

Hi! Welcome to OTel for Beginners. My name is Lisa Jung, and I'm a member of the OTel Communication SIG and the End User SIG. I recently began my journey with OTel, and as a newbie, I had a tough time figuring out how to get started. I want you to have a different experience, so I'll learn alongside you and share what I'm discovering through this series.

Depending on which programming language you're working with, you'll follow a language-specific journey. In this series, I'll guide you through the JavaScript journey to help you get started with OTel. 

## What is OTel?

Before we get our hands dirty, let's talk about what OTel is, why you should consider using it, and the resources available to get started. OTel stands for **OpenTelemetry**, and it plays an important role in observing your system. 

Let’s discuss observability first, then delve into how OTel fits into this concept. Our modern software systems can be complex, multi-layered, and distributed, with many interdependencies. A system without observability is like a black box; we have no idea what's going on inside. If something goes wrong, it becomes more difficult and time-consuming to solve the problem.

With observability, we turn this black box into a glass box. It helps you collect the data necessary to visualize and understand what's happening in your system. 

### Making Observability Possible

How do we make this possible? First, you have your infrastructure or applications that you want to observe. You'll collect data from it and send that data to the observability backend of your choosing. Then, you connect the backend to a visualization frontend where you can query and use the data that interests you. 

The most common types of data collected for observability are **metrics, logs,** and **traces**. These are known as telemetry data. Getting this telemetry data into the backend is crucial for understanding your infrastructure or applications, and this is where OTel comes in.

OTel is an open-source framework. Using OTel, you can add software to your applications or systems to generate telemetry data. This process is known as **instrumentation**. OTel collects, manages, and exports telemetry data to an observability backend and the database for storage. 

Different aspects of OTel make this process possible, and we'll discuss these in more detail as we go through the JavaScript journey. For now, remember that OTel focuses on the **generation, collection, management,** and **export** of telemetry data. You can easily instrument your applications or systems, regardless of their language, infrastructure, or runtime environment, with the storage and visualization of telemetry intentionally left to other tools.

## Why Should We Use OTel?

Now, why should we consider using OTel? Before we answer this question, let's talk about something many of us have experienced: the issue of **vendor lock-in**. 

If we dig through our drawers at home, we could probably find a bunch of cables of different types. Why? Because the devices we own come from different vendors, and each vendor has a specific type of cable and port to charge or connect your gadget. 

We're all familiar with buying multiple products from the same vendor and investing in additional accessories and apps specifically designed for that product. Before we know it, we become so accustomed to using a line of products that switching to another vendor can become quite difficult. 

A product from another vendor may operate differently, requiring time to learn and adapt. It would also cost us more money because the additional accessories or apps we've invested in don't work with a product from a new vendor. This challenge is known as **vendor lock-in**, where the costs of switching vendors are so high that customers feel stuck with what they have.

### The Shift Towards Universal Standards

However, things are slowly changing with **USB-C ports** becoming the universal standard. For example, with the newest model of phones—regardless of whether you're using an iPhone or an Android—you can charge or connect many of these phones with a USB-C cable because a universal standard has been established. This allows users to use the same cable, no matter how many times they charge their phones.

OTel has similar implications in observability as USB-C does for phones. 

### A Quick Review

Let’s review briefly. We have our infrastructure or applications that we want to observe. We want to collect telemetry data and send it to an observability backend for storage, enabling the data to be queried and visualized with an observability frontend.

Imagine you have three observability backends to choose from: vendors A, B, and C. Each vendor often has proprietary instrumentation, agents, and/or collectors. 

Let’s say you choose vendor A and start using their proprietary instrumentation, agents, or collectors to send data to their backend. But what if your needs change down the road, and you want to switch your backend to vendor B? Switching vendors isn't as simple as it seems. You can't just send the existing data from vendor A to B because vendor B requires its own instrumentation, agents, or collectors that cannot accept data from vendor A's proprietary instrumentation. 

Now your development team has to change their instrumentation, possibly to a new proprietary solution from vendor B. Imagine doing this for thousands of Linux machines or dozens of applications. Is the cost in money, time, and effort worth the benefits of changing vendors? 

As you can see, the cost of switching vendors can become so high that customers can be effectively locked in by their choices. 

### The Solution: OpenTelemetry

Now, imagine if all vendors accepted the same standard for sending or receiving telemetry data, similar to how many phone companies accept USB-C as a standard. When you switch vendors, you wouldn't need to learn proprietary instrumentation, agents, or collectors each time. You just need one technology and a single set of APIs and conventions associated with it. 

Whatever data you generate with this technology is yours. You could send the data to any observability backend that accepts the standard, significantly reducing the cost, time, and effort involved in switching vendors. This is exactly what OTel offers.

OTel creates an **open standard**, a set of guidelines, rules, or specifications for sending and receiving data. There’s a strong incentive for vendors to accept OTel. Many customers now prefer OTel to avoid vendor lock-in, wanting to learn a single set of APIs and conventions instead of a new one every time they change vendors. They also want to own their data and send it to any observability backend that accepts these standards.

Vendors benefit from accepting OTel as well. Since customers may already be familiar with using OTel, there's a vibrant OTel community that serves as a great resource. Accepting OTel helps vendors reduce their support and implementation costs. Moreover, it drives innovation because vendors receive the same data, compelling them to innovate to stand out from competitors.

## Getting Started with OTel

Now that we've covered what OTel is and why you should use it, let's go over the resources to get started. The links to all the resources are included in the description of the video.

1. **OTel Documentation**: The best place to start is the OTel documentation, which is continuously being improved. The page may look different by the time you watch this video, so use the link in the description to check out the latest version. Start with the **Language APIs and SDKs** section. Your OTel journey will differ depending on the programming language you're using, so select your language of choice to find all the necessary resources.

2. **Official OTel YouTube Channel**: You'll find helpful videos, including the OTel for Beginners series on this channel. 

3. **Community Support**: As you embark on your OTel journey, you may have many questions. We have a huge community of OTel users on Slack. Join the **CNCF Slack Channel**, post your questions in the **OpenTelemetry channel**, and connect with other community members.

Again, check the description of this video to access all these resources. 

In the next episode, we'll talk about how to get started with the JavaScript journey, so stay tuned for that. Thank you for watching, and I'll see you in the next episode!

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

