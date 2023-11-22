# Class 04

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

Enterprise network administrators use routing skills to handle large and complex multi-router topologies or connections. ISP backbone routers can and do malfunction on occasion, causing routing problems for everyday users. Routing issues can also arise when configuring VPN tunnelling between two complex LANs.

Routing is a fundamental mechanic in the overall operations of not only networks but the internet at large. In today's lab you'll practice configuring BGP on two routers.

## How does this topic fit?

**Where we've been**:
In the previous class we explored network segmentation.

**What are we focusing on today**:
Today we'll be exploring routing protocols.

**Where we're headed**:
In the next class we'll be configuring a VPN between two routers.

## Routing

### Why
- Proper network routing ensures that data packets take the most optimal paths through the network. This minimizes latency, reduces data transfer times, and improves overall network performance. Efficient routing helps in delivering a seamless user experience, especially for real-time applications like video streaming, online gaming, and VoIP.
- Good routing practices involve distributing network traffic evenly across available paths. This prevents network congestion on a single route and makes better use of network resources. Load balancing is essential to ensure that no single link or device becomes a bottleneck, thus maintaining a consistent quality of service.
- Effective routing strategies allow for multiple paths between source and destination. This redundancy helps maintain network connectivity even if one path or device fails. Redundant paths increase network reliability and reduce the likelihood of downtime, which is critical for businesses and organizations that rely heavily on network services.
- As networks grow, proper routing becomes increasingly important to manage the increased volume of traffic. Good routing practices ensure that the network can scale efficiently without sacrificing performance or reliability.
- Network routing can play a role in enhancing security. By implementing proper routing policies, administrators can segregate different types of traffic, establish access controls, and enforce security measures such as firewalls and intrusion detection systems. Proper routing also helps isolate and contain potential security breaches, limiting their impact.
- In larger networks that span multiple locations, geographic routing can optimize data transmission by selecting routes that are geographically closer to the destination. This reduces latency and improves overall network responsiveness.
- Network routing can prioritize certain types of traffic, such as voice or video data, to ensure consistent performance for critical applications. QoS mechanisms can be implemented through routing policies to allocate bandwidth appropriately.
- Proper routing can help reduce operational costs by ensuring that data takes the shortest and most cost-effective paths. This is particularly important for organizations with distributed operations and remote sites.

### What
- _______ is the process of determining the path that data packets should take from the source to the destination in a network.
- _______ is a unit of data that is transmitted over a network. It contains the actual data being sent as well as routing information.
- _______ is a network device that directs data packets between different networks or subnetworks based on routing decisions.
- _______ is the route that a data packet takes through a network from its source to its destination.
- _______ is a single step in a data packet's journey through the network, typically passing through a router or switch.
- _______ is the time delay experienced as data packets travel from the source to the destination. Lower latency indicates quicker data transmission.
- _______ is the distribution of network traffic across multiple paths or devices to prevent congestion and optimize performance.
- _______ is the provision of backup paths or devices in case of network failures, ensuring continuous connectivity.
- _______ is the ability of a network to recover quickly from failures and maintain its functionality.
- _______ is a routing strategy that selects paths based on geographical proximity to optimize data transmission.
- _______ are mechanisms that prioritize and manage network traffic to ensure specific levels of service for different types of data.
- _______ is the maximum data transfer rate of a network connection, measured in bits per second (bps).
- _______ is a set of rules that routers use to communicate with each other and exchange routing information.
- _______ is the automatic adjustment of routing paths based on real-time changes in the network.
- _______ is the manual configuration of routing paths by network administrators.
- _______ is a device that connects two different networks and facilitates communication between them.
- _______ is a database maintained by routers that contains information about available routes and their metrics.

### How
- Today's lab involves configuring BGP (Border Gateway Protocol) routing between two ***2811*** model routers to optimize network traffic between on-premises and cloud infrastructure for GlobeX. This includes setting up the routers, establishing BGP connections between them, configuring BGP settings (such as private AS values and neighbors), capturing screenshots of routing tables and configurations, and updating the network topology diagram. The lab requires hands-on configuration of routers and switches, capturing relevant data, and documenting the process.
- Some of the major concepts in this lab include:
  - **Routing Protocols:** Understanding the basics of routing protocols like BGP, RIP, and OSPF.
  - **BGP Configuration:** Configuring BGP settings, such as AS values, neighbors, and route sharing.
  - **IP Addressing:** Assigning IP addresses to interfaces for routers, switches, and hosts.
  - **Subnetting:** Defining network address ranges using subnet masks.
  - **Network Topology:** Understanding and creating network topology diagrams.
  - **Routing Tables:** Learning how to access and analyze routing tables on routers.
  - **Capturing Data:** Capturing screenshots of router configurations and routing information.
  - **Network Testing:** Performing tests like pinging between devices to ensure successful communication.
- In the demo and lab, we will be working with Cisco Packet Tracer again, to perform hands-on tasks related to configuring BGP routing.

### Experimentation and Discovery Ideas
- Imagine you're sending a data packet from your computer to a server located on the other side of the world. What are some of the factors that could influence the path this data packet takes through the network?
- Let's consider BGP (Border Gateway Protocol) configuration. Why might using private AS values be important in this context? How does this relate to the concept of scalability in networking?
- The lab mentions capturing screenshots of the routing tables and configurations. Why do you think having visual documentation of routing information could be valuable for network administrators and engineers? How might these screenshots aid in troubleshooting network issues?
- In networking, the term "redundancy" often comes up. Why might it be essential to design networks with redundancy in mind, especially when dealing with critical services or data transmission?
- The lab introduces the option of configuring dynamic routing using protocols like RIP or OSPF instead of BGP. How might the choice between these protocols depend on the specific needs of a network? Can you envision scenarios where one protocol might be more suitable than the others?

## Learning Objectives

### Students will be able to

#### Describe and Define

- Routing
- Routing protocols
  - OSPF
  - BGP
- Routing table
- Static routing
- Default routing
- Dynamic routing

#### Execute

- Create a network topology using routers, switches, and hosts.
- Configure BGP settings on the routers, establish BGP connections, and capture screenshots of the routing tables and configurations.
- Capture screenshots of successful pings between devices and updating your network topology.

## Helpful Resources

- [Cisco Packet Tracer](https://skillsforall.com/course/getting-started-cisco-packet-tracer){:target="_blank"}
- [Packet Tracer - BGP Configuration](https://www.packettracernetwork.com/tutorials/bgp.html#:~:text=BGP%20in%20Packet%20Tracer,network%20policies%20and%2For%20rulesets.){:target="_blank"}
- [Cisco IOS IP Routing: RIP Command Reference](https://www.cisco.com/c/en/us/td/docs/ios/iproute_rip/command/reference/irr_book/irr_rip.html){:target="_blank"}
- [Static Routing Configuration](https://www.computernetworkingnotes.com/ccna-study-guide/static-routing-configuration-guide-with-examples.html){:target="_blank"}

## Notes
