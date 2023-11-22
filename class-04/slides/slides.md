<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 04

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 04 - Routing
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Network Design
  - Routing Protocols
- Demo

---

<!-- .element class="split-screen-with-title" -->

## Course Overview

<div>

<div align="left" style="font-size: 35px">

**Modules:**
- &shy;<!-- .element style="color: red;" -->**Module 1** Networking Tools, Concepts, and Fundamentals
- **Module 2** Network Infrastructure Design and Implementation
- **Module 3** Server Administration, Active Directory, and User Management
- **Module 4** Project

</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 1 - Networking Tools, Concepts, and Fundamentals

<div>

<div align="left" style="font-size: 40px">

**Class 01** Network Traffic Analysis

**Class 02** Network Enumeration

**Class 03** Network Segmentation

&shy;<!-- .element style="color: red;" -->**Class 04** Routing

**Class 05** VPN Tunnel


</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_02.png)
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 1 Challenges: Bash

<div>

<div align="left" style="font-size: 50px">


**Class 01** N/A

**Class 02** Append + Date and Time

**Class 03** File Permissions

&shy;<!-- .element style="color: red;" -->**Class 04** Conditionals in Menu Systems

**Class 05** Clearing Logs


</div>

<div>

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Network Design
  - Routing Protocols
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Network Design
  - Routing Protocols
- Demo

---

<!-- .element class="split-screen-with-title " -->
# Subnetting

<div>

<div>

- A subnet is a subnetwork, or a network inside of a larger network.
- A subnet mask or netmask indicates which bits in the octet are masked.
- A CIDR block represents a range of IP addresses using CIDR block notation, which consists of a forward slash then a number
- A network address represents the entire range of possible local IPs as a single IP address with a CIDR block at the end
  - 192.168.1.0/24 <!-- .element class="medium-text" -->
    - Addressable range 192.168.1.1-254

</div>

<div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/5_0.png)

</div>

</div>

NOTE:
What is a subnet?
A subnet is a subnetwork, or a network inside of a larger network.

What is a netmask?
A subnet mask or netmask indicates which bits in the octet are masked.
Example 255.255.255.0 explains the size of the network. This one is always associated with a CIDR block of /24.

What is a CIDR block?
A CIDR block represents a range of IP addresses using CIDR block notation, which consists of a forward slash then a number. This also serves to represent the size of a network.
Example /24 in most home routers

What is a network address?
A network address represents the entire range of possible local IPs as a single IP address with a CIDR block at the end.
Example: 192.168.1.0/24 represents the range 192.168.1.1-254.
We use network addresses in network diagrams to represent the breadth of a whole LAN or a subnet.

https://cidr.xyz/ can be demonstrated as a subnet calculation tool.
Source: NordVPN

---

<!-- .element class="split-screen-with-title" -->
# Network Segmentation

<div>

<div>

- Network segmentation divides a computer network into smaller parts to improve network performance and/or security
  - In logical segmentation we rely on software or packet header information to separate network traffic (Example: VLAN)
    - A virtual LAN (VLAN) is a subnetwork broadcast domain that is partitioned and isolated in a computer network at layer 2<!-- .element class="medium-text" -->
  - In physical segmentation we separate network traffic by ports and devices (Example: Air-gapping IT and OT networks)

</div>

<div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/6_0.png)<!-- .element style="width: 70%"-->

</div>

</div>

NOTE:
"Network segmentation is a way to isolate devices on separate networks to achieve better sharing of throughput or bandwidth to the Internet, securing systems with more sensitive data, and separating systems from people and other systems that don't have a need to connect to them."

Cisco: "What is an example of segmentation? Imagine a large bank with several branch offices. The bank's security policy restricts branch employees from accessing its financial reporting system. Network segmentation can enforce the security policy by preventing all branch traffic from reaching the financial system. And by reducing overall network traffic, the financial system will work better for the financial analysts who use it."

“VLANs allow network administrators to group hosts together even if the hosts are not directly connected to the same network switch. Because VLAN membership can be configured through software, this can greatly simplify network design and deployment.” -Wikipedia

Source: Delta Risk

---

<!-- .element class="main-title" -->
# Review: Lab


---

<!-- .element class="main-title" -->
# Review:

# Challenge


---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Network Design
  - Routing Protocols
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge 04:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Conditionals in Menu Systems**

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Network Design
  - Routing Protocols
- Demo

---

<!-- .element class="main-title" -->
# Network Design


NOTE:
- Network design is creating a blueprint for the architecture, infrastructure, and connectivity of computer networks.
- It involves careful consideration of factors like scalability, reliability, security, and performance to ensure efficient data flow and optimal user experience.
- A well-crafted network design forms the foundation for building robust and adaptable communication systems that cater to the needs of businesses and individuals.

---

<!-- .element class="split-screen " -->
<div>

# Network Design

- Network design's impact on an organization:
  - Performance
  - Security
  - Compliance
- Network diagramming
  - Demonstrate interdependencies
  - Identify visibility levels across network
  - Planning and proposals

</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/10_0.png)

NOTE:
## Network design's impact on an organization

- **Performance:** A well-executed network design influences an organization's digital infrastructure performance. It considers bandwidth, latency, and quality of service (QoS) for efficient data transmission and user experiences.

- **Security:** Network design establishes robust security with firewalls, access controls, encryption, and intrusion detection. It protects data and systems from cyber threats.

- **Compliance:** Network design ensures regulatory compliance by adhering to standards. It avoids legal issues and safeguards sensitive data.

## Network diagramming

- **Demonstrate interdependencies:** Diagrams show relationships among network components, aiding issue troubleshooting.

- **Identify visibility levels across the network:** Diagrams offer an overview of the network, identifying bottlenecks, vulnerabilities, or optimization areas.

- **Planning and proposals:** Diagrams serve as a foundation for expansion or improvements, aiding communication and decision-making.

Source: mcqquestions

---

<!-- .element class="split-screen " -->
<div>

# Network Design

- Generally performed by network designers, engineers and IT administrators before the implementation of a network infrastructure.
- Key aspects of network design:
  - Network requirements
  - Network topology
  - Hardware and software selection

</div>

> "Network design refers to the planning of the implementation of a computer network infrastructure.”
![Image](/ops-301-guide/curriculum/class-04/slides/assets/11_0.png)

NOTE:

- The following are some of the key aspects of network design:
  - Network requirements
    - The first step in network design is to identify the requirements of the network. This includes the number of users, the types of applications that will be used, the amount of data that will be transmitted, and the level of security required.
  - Network topology
    - The network topology is the physical layout of the network. There are many different network topologies, each with its own advantages and disadvantages. The best topology for a particular network will depend on the requirements of the network.
  - Hardware and software selection
    - The next step is to select the appropriate hardware and software for the network. This includes routers, switches, firewalls, servers, and workstations. The hardware and software must be compatible with each other and must meet the requirements of the network.

Source: mcqquestions

---

<!-- .element class="split-screen " -->
<div>

# Network Topologies

- How we choose to connect the devices determines the topology type:
  - Logical topology
    - Two main types of logical topologies:
      - Broadcast
      - Point-to-point
  - Physical topology
    - Cabling physically exists as depicted


</div>

> A network topology is the arrangement of the elements that form a communication network.
![Image](/ops-301-guide/curriculum/class-04/slides/assets/12_0.png)

NOTE:
- Logical
  - a logical topology refers to the way that data flows through the network, regardless of the physical layout of the devices.
  - There are two main types of logical topologies:
    - Broadcast: In a broadcast topology, all devices on the network can see all of the traffic on the network. This is the simplest type of logical topology, but it can also be the least efficient, as all devices must process all of the traffic, even if it is not intended for them.
    - Point-to-point: In a point-to-point topology, each device is only connected to one other device. This is the most efficient type of logical topology, as only the devices that are communicating with each other need to process the traffic.

- Physical
  - is when the cabling is literally as depicted
  - a physical network topology refers to the actual physical layout of the network devices and how they are connected to each other.
  - The physical topology is important for determining factors such as performance, scalability, and fault tolerance.
  - There are many different types of physical topologies.

- Note that CompTIA considers VLAN a form of virtual segmentation, not physical.
  > "In a virtually segmented network, VLANs identify separate segments. An admin may configure the VLANs in such a way that it achieves virtual system isolation.
  > In a physically segmented network, switches connect segments. The switches may connect in such a way that it achieves system isolation. This method is an approach that results in an air gap." - The Official CompTIA CySA+ Student Guide (Exam CS0-002)
  > You'll need to know all six network topologies to pass CompTIA Network+. Check the corresponding exam objectives.

Source: mcqquestions

---

<!-- .element class="split-screen " -->
<div>

# Wired Topologies

- Wired topologies break down into four types:
  - In a bus topology one cable runs from one end of the network to another
    - Affordable but single point of failure
    - Only half-duplex (one-way) network traffic is supported
    - Extremely rare, only in older facilities

</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/13_0.png)

NOTE:
A bus network topology is a type of network arrangement in which all devices are connected to a central cable, known as the "bus" or "backbone." This backbone serves as a single communication path through which data travels. Devices are linked to the backbone using connectors, and each device receives all the data transmitted on the network.

In a bus network:

- **Advantages:**
  - **Simplicity:** Bus topology is straightforward to set up and requires less cabling compared to other topologies.
  - **Cost-effective:** It requires minimal cable, making it cost-effective for smaller networks.
  - **Easy to expand:** Adding new devices involves connecting them to the central cable.
  - **Good for small networks:** Bus topology is suitable for smaller networks with limited traffic.

- **Disadvantages:**
  - **Only half-duplex network traffic is supported:** Half-duplex communication means that devices can either transmit or receive data on the network, but not both simultaneously. This limitation arises due to the nature of the shared central cable in a bus topology.
  - **Limited scalability:** As the network grows, the central cable can become a bottleneck, degrading performance.
  - **Single point of failure:** If the central cable fails, the entire network can go down.
  - **Collision risk:** Collisions can occur if multiple devices try to transmit data simultaneously, potentially causing data loss and retransmissions.
  - **Limited privacy and security:** Since all data is transmitted to all devices, privacy and security measures are more challenging to implement.

While bus topology was more common in the past, its limitations and vulnerabilities have led to more robust and flexible topologies like star, ring, and mesh in modern networking environments.

OLD NOTES:
- Bus
  - In a bus topology, there is a single cable that runs from one end of the network to another. Also known as "line topology."
  - Keeps the network cabling affordable and simple, but relies on a single point of failure. When designing computer systems architecture, we should always avoid SPOFs.
  - Half duplex, so data cannot be transmitted in two directions simultaneously. This is highly outdated in computer networks, and you're unlikely to encounter this.
> Think of truckers using CB radios. They often say "over" to let the other person know it's their turn to speak. This is an example of half-duplex communication. In full-duplex communication, we can communicate both directions at the same time, like when two people on cell phones accidentally speak at the same time.

Source: Wikimedia

---

<!-- .element class="split-screen " -->
<div>

# Wired Topologies

- Wired topologies (ctd.):
  - In a ring topology, computers are connected to each other in a circle.
    - Each device will have exactly two neighbors connected to it.
    - While common in the past, these are rare today.
    - Single ring is half-duplex
    - Affordable and high speed
    - Hard to scale
    - Needs all nodes up to function

</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/14_0.png)

NOTE:
A ring topology is a type of network arrangement in which each device is connected to exactly two other devices, forming a closed loop resembling a ring. Data travels in a unidirectional or bidirectional manner along the ring, passing through each device until it reaches its intended destination. Ring topologies are less common today due to advances in other topologies, but they still offer some unique advantages and challenges.

In a ring topology:

- **Advantages:**
  - **Equal access:** Each device in the network has equal access to the network's bandwidth since there's no central point of control.
  - **Predictable performance:** The structured nature of the ring topology can lead to consistent and predictable data transfer performance.
  - **Simple layout:** The physical layout is relatively straightforward, making it easy to understand and implement.

- **Disadvantages:**
  - **Single point of failure:** If a single device or connection in the ring fails, the entire network can be disrupted.
  - **Limited scalability:** Adding new devices to the ring can be challenging without interrupting the entire network.
  - **Maintenance difficulties:** Troubleshooting and reconfiguration might require disconnecting devices from the ring temporarily.
  - **Data collisions:** If not properly managed, bidirectional rings can still experience data collisions.

Ring topologies were more common in older networking technologies like Token Ring, but they've been largely replaced by star topologies in modern Ethernet networks. Despite their advantages, the single point of failure and scalability issues have made ring topologies less suitable for today's dynamic and expanding network environments.

OLD NOTES:
- Ring
  - In a ring topology, computers are connected to each other in a circle. Each device will have exactly two neighbors connected to it. While common in the past, these are rare today.
  - Typically half-duplex, if you add a second "ring" you can make the network full-duplex. This is called a dual ring topology.
  - High speed and low risk of packets colliding. Dual ring topologies have a layer of redundancy. Ring topologies are highly affordable.
  - Disadvantages include reliance on all nodes and the topology is not very scalable. To add or remove nodes, you need to shut down the whole network!

Source: tugurium

---

<!-- .element class="split-screen " -->
<div>

# Wired Topologies

- Wired topologies (ctd.):
  - A star topology mimics the client-server architecture with a central switch/hub as the server and all other hosts connect through it.
    - Centralized administration
    - Most commonly deployed today
    - Highly scalable, simple to deploy
    - Single point of failure/potential bottleneck in central appliance

</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/15_0.png)

NOTE:
A star topology is a type of network arrangement in which all devices are connected to a central hub or switch. Each device communicates directly with the central hub, and the hub manages the data traffic between devices. This topology resembles the spokes of a wheel radiating outward from a central point. Star topologies are widely used in modern networking due to their reliability, scalability, and ease of management.

In a star topology:

- **Advantages:**
  - **Reliability:** Failure of a single cable or device usually doesn't affect the rest of the network, making it more robust compared to other topologies.
  - **Easy troubleshooting:** Identifying and resolving issues is simplified, as faults are localized to the specific device or cable.
  - **Scalability:** Adding new devices is straightforward; they can be connected to the central hub without disrupting the existing network.
  - **High performance:** With proper cabling and network hardware, data traffic is directed efficiently through the central hub, reducing collisions.

- **Disadvantages:**
  - **Single point of failure:** The central hub itself becomes a single point of failure. If the hub fails, the entire network may go down.
  - **Hub performance:** The hub's capacity limits overall network performance. High data traffic might overload the hub.
  - **Cabling complexity:** Star topologies can require more cabling compared to some other topologies, especially as the network grows.

Star topologies are common in Ethernet networks, where a switch typically serves as the central hub. This topology's ability to isolate network problems and facilitate easy expansion has contributed to its widespread use in business, home, and industrial networking environments.

OLD NOTES:
- Star
  - This is your most common wired topology in today's enterprise. This topology mimics client-server architecture in that the central switch/hub acts as the server, and computers are the clients all connected individually to it.
  - You can manage the entire network centrally from the network appliances (switch, router). Star is highly scalable and generally simple to setup and manage.
  - Disadvantages include single point of failure at the switch/hub and performance bottleneck at the switch/hub.
  - Here's what a small business star topology might look like. Don't worry, we're starting out simple in our lab.

Source: imgur

---

<!-- .element class="split-screen " -->
<div>

# Wired Topologies

- Wired topologies (ctd.):
  - In a mesh topology, all nodes are connected to each other.
    - Data transmits via routing or flooding.
    - Subtypes partial and full mesh, based on how complete the mesh is
    - Highly resilient, no single point of failure
    - Costly and hard to manage

</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/16_0.png)

NOTE:
A mesh topology is a type of network arrangement where every device is directly connected to every other device. In this topology, multiple point-to-point connections are established between devices, creating a network where data can take multiple paths to reach its destination. Mesh topologies offer high reliability and fault tolerance due to the redundancy in connections, but they can be complex and resource-intensive to implement.

In a mesh topology:

- **Advantages:**
  - **Redundancy and fault tolerance:** Multiple connections ensure that if one link or device fails, data can still find alternative paths, minimizing network downtime.
  - **Reliability:** The redundancy in connections makes mesh networks highly reliable, as they are less vulnerable to single points of failure.
  - **Scalability:** Mesh topologies can be easily scaled by adding more devices and connections as needed.
  - **Efficient data transmission:** With numerous paths available, data can be transmitted through the shortest and least congested routes.

- **Disadvantages:**
  - **Complexity:** Establishing and managing a large number of point-to-point connections can be complex and resource-intensive.
  - **Cost:** The increased number of connections results in higher costs for cabling and network hardware.
  - **Configuration and maintenance:** Troubleshooting and managing a complex mesh network can be challenging due to the abundance of connections.

Mesh topologies are commonly found in wireless networks (like mesh Wi-Fi systems) and in critical infrastructure where reliability is paramount, such as military and industrial applications. While full mesh topologies with every device interconnected are rare due to their complexity, partial mesh topologies, where selected devices have redundant connections, offer a compromise between reliability and manageability.


OLD NOTES:
- In mesh topology, all nodes are connected to each other. Data is transmitted via routing (choosing shortest path or OSPF) or flooding (sending data packets to all nodes).
- Two types: partial and full mesh. Depends on how complete the meshed network is. A complete mesh is a full mesh.
- Deploy mesh when you need to design a highly resilient network. Interconnectivity means no single point of failure.
- Disadvantages include complex to configure and manage. This is the most complex and requires lots of wiring (costly).

Source: ianswer4u

---

<!-- .element class="split-screen " -->
<div>

# Wireless Topologies

- Mesh
  - Increase the range of the main network using satellite wi-fi hubs
  - Multiple hubs = cluster
- Ad hoc
  - Direct wireless connection between two devices. Many printers can do this.
- Infrastructure
  - Most wi-fi networks use this, where an access point broadcasts a SSID and you connect to it.


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/17_0.png)

NOTE:
A wireless topology refers to the layout or arrangement of wireless devices and their connections in a wireless network. Just like wired networks have different topologies (such as star, bus, ring, etc.), wireless networks also have various topologies that define how the wireless devices communicate and interact with each other. These topologies dictate the structure and communication patterns of the wireless network.

**Mesh:**
  - Mesh networks expand the coverage area of the primary network through satellite Wi-Fi hubs.
  - A collection of multiple hubs forms a cluster, enhancing network robustness.
  - Network devices, acting as nodes, communicate wirelessly among themselves, bypassing the need for a central access point.
  - Deployed in scenarios like sprawling outdoor locations (e.g., parks, campuses) where conventional wired or wireless setups are impractical or costly.

**Ad hoc:**
  - Ad hoc connections create direct wireless links between two devices, often seen in functions like wireless printing.
  - Devices establish communication without relying on a centralized infrastructure, such as a router.
  - Each device functions as both a sender and receiver, actively participating in routing data to other connected devices.

**Infrastructure:**
  - Most Wi-Fi networks utilize the infrastructure mode, where access points broadcast SSIDs for connection.
  - Devices connect to these access points, forming a network structure with centralized management and connectivity.

Source: superuser

---

<!-- .element class="main-title" -->
# Routing Protocols


NOTE:
- A routing protocol is a set of rules that routers use to exchange information about the networks they are connected to. This information includes the networks' addresses, subnets, and costs.
- Routers use this information to build routing tables, which they use to determine the best path for data to travel between any two points on the network.
- There are many different routing protocols, each with its own strengths and weaknesses. The best protocol for a particular network will depend on factors such as the size of the network, the number of routers, and the traffic volume.
- A comprehension of routing helps understand vulnerabilities like DDoS and therefore how to secure systems against malicious WAN based attacks.

---

<!-- .element class="split-screen " -->
<div>

# Routing Protocols

- Distributed denial of service (DDoS) is an attack technique whereby multiple hosts overwhelm a web server with a flood of requests.
- Network routing is the process of choosing a path across one or more networks
  - In static routing you set a predefined single path to the destination.
    - Saved to the router
    - Takes precedence over dynamic routes


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/19_0.png)

NOTE:
- Distributed Denial of Service (DDoS) is a cyber attack that involves overloading a system or network with a flood of traffic. This can cause the system or network to crash, making it unavailable to legitimate users.
  - In some cases, DDoS attacks can impact routing protocols. For instance, if a DDoS attack targets specific network segments or routers, it might result in routing instability or changes as routers attempt to reroute traffic to avoid affected areas.
- Network routing is the process of determining the best path for data packets to travel from their source to their destination. It is a critical function in any network, as it ensures that data is delivered efficiently and reliably.
  - Static routing is a type of routing in which the router is manually configured with a list of routes to the destinations. This is typically done in small networks, where the topology of the network does not change frequently.

##  Who is Cloudflare and how does their solution work?

Cloudflare is a content delivery network (CDN) and DDoS mitigation service. It provides a number of features to protect websites and applications from DDoS attacks, including:

  - Edge caching: Cloudflare caches static content, such as images and JavaScript files, at its edge nodes. This reduces the amount of traffic that needs to be sent to the origin server, which can help to mitigate DDoS attacks.
  - DDoS mitigation: Cloudflare uses a variety of techniques to mitigate DDoS attacks, including rate limiting, blackholing, and scrubbing.
  - Web application firewall (WAF): Cloudflare's WAF can be used to block malicious traffic, such as bots and scripts.
  - SSL/TLS offloading: Cloudflare can be used to offload SSL/TLS traffic from the origin server. This can help to improve performance and security.

Cloudflare's DDoS mitigation solution works by using its global network of edge nodes to detect and mitigate DDoS attacks. When an attack is detected, Cloudflare can take a number of measures to mitigate the attack, such as:

  - Rate limiting: Cloudflare can limit the rate at which traffic is sent to the origin server. This can help to prevent the origin server from being overwhelmed.
  - Blackholing: Cloudflare can block traffic from known malicious sources. This can help to prevent the attack from reaching the origin server.
  - Scrubbing: Cloudflare can scan traffic for malicious content and remove it before it reaches the origin server.

Source: superuser

---

<!-- .element class="split-screen " -->
<div>

# Routing Protocols

- Static routing: Having a predefined single path to the destination saved to your router that takes precedence over dynamic routes.
- Default Routing: Usually used in small networks, default is a manually defined path to take when no specific route can be determined.
- Dynamic routing: Most common method of routing that calculates what route to take.
  - Convergence
  - Accuracy


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/20_0.png)

NOTE:
## Static routing
  - Having a predefined single path to the destination saved to your router that takes precedence over dynamic routes.
  - In static routing, the router is manually configured with a list of routes to the destinations.
  - This is typically done in small networks, where the topology of the network does not change frequently.
  - Static routes are always preferred over dynamic routes, and they are also more secure.

## Default Routing
  - Usually used in small networks, default is a manually defined path to take when no specific route can be determined.
  - A default route is a route that is used when there is no specific route to the destination.
  - The default route is typically set to the gateway of last resort, which is the router that will forward the packet if there is no other route available.

## Dynamic routing: Most common method of routing that calculates what route to take.
  - In dynamic routing, the routers exchange routing information with each other to automatically determine the best paths to the destinations.
  - This is typically done in large networks, where the topology of the network changes frequently.
  - Dynamic routing protocols are more complex than static routing, but they are also more efficient and reliable.
    - Convergence: Time taken to update the routing table to reflect real topology. Fast convergence is good!
    - Accuracy: How accurate is the routing table, given convergence time?

Source: superuser

---

<!-- .element class="split-screen " -->
<div>

# Routing Protocols

- Routing mechanism
  - Autonomous System (AS)
    - Private AS used for internal networks <!-- .element class="medium-text" -->
    - Public AS used for external networks like internet backbone <!-- .element class="medium-text" -->
  - Interior gateway protocols:
    - RIPv1,RIPv2 (Routing Information Protocol) <!-- .element class="medium-text" -->
    - IGRP(Internet Gateway Routing Protocol) <!-- .element class="medium-text" -->
    - OSPF(open shortest path first) <!-- .element class="medium-text" -->
  - Exterior gateway protocols: BGP or Border Gateway Protocol


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/21_0.png)

NOTE:
## Autonomous System (AS)

An autonomous system (AS) is a collection of networks that are managed by a single organization. Each AS has its own routing policy, which determines how the AS exchanges routing information with other ASes.

The routing mechanism for autonomous systems is based on the Border Gateway Protocol (BGP). BGP is a dynamic routing protocol that allows ASes to exchange routing information with each other. BGP uses a path vector algorithm to determine the best path to a destination. A path vector algorithm considers the cost of each path to a destination, as well as the policies of the ASes that the path traverses.

**Private ASes and public ASes** are two types of autonomous systems. Private ASes are used by organizations to connect their internal networks, while public ASes are used by organizations to connect their networks to the Internet.

**Private ASes** use private IP addresses, which are not routable on the public Internet. This means that traffic from a private AS cannot be routed to the public Internet without going through a public AS.

**Public ASes** use public IP addresses, which are routable on the public Internet. This means that traffic from a public AS can be routed to any other AS on the Internet.

## Interior gateway protocols: RIPv1, RIPv2, IGRP, OSPF

Interior gateway protocols (IGPs) are routing protocols that are used to exchange routing information within an autonomous system (AS). IGPs are typically used in smaller networks, where the topology of the network does not change frequently.

The best IGP for a particular network will depend on its specific needs. If a network is small and has a simple topology, then RIP may be a good option. If a network is large or has a complex topology, then OSPF may be a good option.

  - **Routing Information Protocol (RIP)**: RIP is a simple and easy-to-implement IGP that is often used in small networks. RIP uses a distance vector algorithm to determine the best path to a destination.
  - **RIPv2**: RIPv2 is an enhanced version of RIP that supports subnetting and authentication. RIP is a good choice for small networks. RIP is not suitable for networks with a complex topology.
  - **Enhanced Interior Gateway Routing Protocol (EIGRP)**: EIGRP is a Cisco proprietary IGP that is more complex than RIP but provides better performance and scalability. EIGRP uses a composite metric to determine the best path to a destination. EIGRP is more secure than RIP and RIPv2.
  - **Open Shortest Path First (OSPF)**: OSPF is an open standard IGP that is more complex than RIP and EIGRP but provides the best performance and scalability. OSPF uses a link-state algorithm to determine the best path to a destination. OSPF is a good choice for large networks. OSPF is suitable for networks with a complex topology. OSPF is the most performant IGP.

## Exterior gateway protocols: BGP

Exterior gateway protocols (EGPs) are routing protocols that are used to exchange routing information between autonomous systems (ASes). EGPs are typically used in larger networks, where the topology of the network changes frequently.

The most common EGP is the Border Gateway Protocol (BGP). BGP is a path vector protocol that uses a variety of factors to determine the best path to a destination, including the cost of the path, the policies of the ASes that the path traverses, and the reliability of the path.

**Key features of BGP:**

  - It is a path vector protocol.
  - It uses a routing table to store the routes to destinations.
  - It uses a routing policy to determine which routes to use.
  - It uses a BGP session to exchange routing information with other ASes.
  - It uses a BGP community to exchange routing information with other ASes.
  - BGP is a critical part of the Internet routing infrastructure. It allows the Internet to scale to billions of devices and to route traffic efficiently and reliably.

**Advantages of using BGP:**

  - It is a scalable protocol that can be used to route traffic between large networks.
  - It is a reliable protocol that can be used to ensure that traffic is delivered even if there are failures in the network.
  - It is a secure protocol that can be used to protect against routing attacks.

**Disadvantages of using BGP:**

  - It is a complex protocol that can be difficult to configure and manage.
  - It can be a bandwidth-intensive protocol, as it requires a lot of traffic to be exchanged between ASes.
  - It can be a security risk, as it can be used to launch routing attacks.

OLD NOTES:
  - Routing mechanism
    - Autonomous System (AS)
        - The big networks that make up the internet
        - A large network or group of networks that has a unified routing policy
           - Private AS used for internal networks
           - Public AS used for external networks like internet backbone
      - Interior gateway protocols: RIPv1, RIPv2, IGRP, OSPF
      - Exterior gateway protocols: BGP or Border Gateway Protocol
      - Administrative Distance (AD):
      	- Level of reliability of routing updates received from neighboring router
      	- Used by routers to find out which route is better (lower number is better)

      - Metric: Tiebreaker for simultaneously equal ADs to choose a route (lower number is better)

Source: superuser

---

<!-- .element class="split-screen " -->
<div>

# Routing Protocols

- What are the routing protocol types?
  - Distance vector: Uses distance as the metric value.
    - RIP (Routing Information Protocol) <!-- .element class="medium-text" -->
  - Link state routing protocols: Works in a linked format and uses a complex metric table.
    - OSPF <!-- .element class="medium-text" -->
  - Hybrid routing protocol: Mix of distance vector and link state routing protocols.
    - EIGRP (enhanced interior gateway routing protocol) <!-- .element class="medium-text" -->


</div>

![Image](/ops-301-guide/curriculum/class-04/slides/assets/22_0.png)

NOTE:
## Distance vector:
  - Distance vector routing protocols are a type of routing protocol that uses a distance vector algorithm to determine the best path to a destination.
    - Distance vector algorithms work by sending routing updates to neighboring routers, which contain the distance to each destination.
      - Measures distance based on how many hops data has to pass to get to its destination
    - The routers then update their routing tables based on the received updates.
      - Number of hops = number of routers it takes to reach the destination
      - Routers send entire routing table to each other
    - Distance vector routing protocols are best suited for small networks with a simple topology. They are not recommended for large networks with a complex topology.
  - Examples:
    - **Routing Information Protocol (RIP)** is the simplest distance vector routing protocol. It uses a hop count as the metric to determine the best path to a destination. A hop count is the number of routers that a packet must pass through to reach its destination.
    - **Interior Gateway Protocol (IGRP)** is a more advanced distance vector routing protocol than RIP. It uses a composite metric to determine the best path to a destination. The composite metric is a combination of the hop count and the bandwidth of the links.
    - **Enhanced Interior Gateway Routing Protocol (EIGRP)** is a hybrid routing protocol that combines the features of distance vector routing protocols and link-state routing protocols. It uses a composite metric to determine the best path to a destination, but it also considers the entire network topology when making its decisions.

## Link state routing protocols:
  - Link-state routing protocols are a type of network routing protocol used in computer networks to determine the best paths for data to travel from a source to a destination.
    - These protocols focus on creating and maintaining an accurate representation of the network's topology by exchanging information about the state of network links.
    - This information is then used to calculate the shortest paths for routing data.
    - Usees an algorithm to find the best path based on the speed of the path to destination
    - Routers notify each other when route changes are detected
  - Examples:
    - **Open Shortest Path First (OSPF)**: Used in IP networks, OSPF is widely used within larger enterprise networks and ISPs. It supports multiple areas for scalability and uses various metrics to determine the path cost, such as bandwidth, delay, and reliability.
    - **Intermediate System to Intermediate System (IS-IS)**: Similar to OSPF, IS-IS is also used within larger networks and is commonly used in telecommunications networks. It's highly efficient and scalable.

## Hybrid routing protocol:
  - A hybrid routing protocol is a type of network routing protocol that combines characteristics of both distance-vector and link-state routing protocols.
  - Mix of distance vector and link state routing protocols.
  - These two types of routing protocols have their own advantages and limitations, and a hybrid approach aims to leverage the strengths of both while minimizing their weaknesses.
  - Examples:
    - **EIGRP (Enhanced Interior Gateway Routing Protocol)** incorporates distance-vector characteristics with aspects of link-state protocols.
      - Neighbor Discovery: Like distance-vector protocols, EIGRP routers establish neighbor relationships and exchange routing updates only with these neighbors. This reduces the amount of routing information exchange compared to full link-state protocols.
      - Feasible Distance and Reported Distance: EIGRP uses the concept of feasible distance and reported distance to make routing decisions. Feasible distance is the best metric a router knows to reach a destination, while reported distance is the metric advertised by a neighbor. These metrics are used to determine the best route.
      - Partial Link-State: EIGRP routers don't flood their entire link-state database across the network as in traditional link-state protocols. Instead, they use a limited set of information, reducing the overhead.
      - Fast Convergence: EIGRP provides faster convergence times compared to pure distance-vector protocols due to its use of feasible and reported distances and incremental updates.
      - Load Balancing: EIGRP allows for unequal-cost load balancing, meaning traffic can be distributed across multiple paths with different costs.

Source: superuser

---

<!-- .element class="main-title" -->
# Demo
