<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 10

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - AWS VPC
- Demo

---

<!-- .element class="split-screen-with-title" -->

## Course Overview

<div>

<div align="left" style="font-size: 35px">

**Modules:**
- **Module 1** Networking Tools, Concepts, and Fundamentals
- &shy;<!-- .element style="color: red;" -->**Module 2** Network Infrastructure Design and Implementation
- **Module 3** Server Administration, Active Directory, and User Management
- **Module 4** Project

</div>

<div>

![Image](/ops-301-guide/curriculum/class-10/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 2 - Network Infrastructure Design and Implementation

<div>

<div align="left" style="font-size: 40px">

**Class 06** Network Address Translation

**Class 07** Web Server Deployment

**Class 08** Network Access Controls

**Class 09** Traffic Mirroring

&shy;<!-- .element style="color: red;" -->**Class 10** AWS VPC


</div>

<div>

![Image](/ops-301-guide/curriculum/class-10/slides/assets/0_02.png) 
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 2 Challenges: Python

<div>

<div align="left" style="font-size: 45.2px">


**Class 06** Bash in Python

**Class 07** Directory Creation

**Class 08** Python Collections

**Class 09** Python Conditional Statements

&shy;<!-- .element style="color: red;" -->**Class 10** Python File Handling


</div>

<div>

![Image](/ops-301-guide/curriculum/class-10/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - AWS VPC
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - AWS VPC
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 09


---

<!-- .element class="main-title" -->
# Review Concepts: 

- Traffic Mirroring

NOTE:


---

<!-- .element class="split-screen-with-title" -->


# Traffic Mirroring

<div>

<div align="left" style="font-size: 30px">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Traffic Mirroring** is done at **Layer 2** (on a **Switch**) by duplicating **Frames**, or on **Layer 3** appliances like **Routers**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->The physical port which mirrored traffic is directed to is called a **SPAN Port** (**Switched Port Analyzer**)
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->On **pfSense**, a **Bridge** connects the LAN port with the SPAN port, emulating the internal functions of a **Switch**
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->Because data is being copied before it is examined, mirroring **does not disrupt or affect network traffic**


</div>

<div align="left">

> **Traffic Mirroring**:
>
> The act of duplicating network traffic to a specific destination.

![Image](/ops-301-guide/curriculum/class-10/slides/assets/09_07.drawio.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

The topology on this slide is different from the ones yesterday: this one represents using a pfSense router instead of a switch, and includes representation of the bridge and also the routing mechanism within the router.

- What is traffic mirroring?
  - Also know as **Port Mirroring** or **Network Monitoring**
  - Traffic mirroring is the act of duplicating network traffic to a specific destination.
    - Think of it like "splitting coax" in highly conceptual terms
    - Also might be known as "tapping a line"
  - Draw the diagram for students to conceptually understand. Refer to the diagram at [How Traffic Mirroring Works](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html).
  - Include network adapters so students see that we are using dedicated sniffer interfaces.
  - Used by **Network Administrators** and **Security Professionals** for **analysis** and/or **monitoring**
  - Mirroring is mostly undetectable because it **does not disrupt or affect network traffic**


What is an interface bridge?
- In history, midway between Hubs and Switches, they had individual collision domains but only a couple of ports.
  - Separate collision domains: inspects each ethernet frame for det MAC and by that either filters or forwards.
  - They were used to bridge from one network to another on layer 2
  - Over time, more ports were added and their use case changed, and now we call them Switches
- Nowadays the word Bridge usually refers to a software element used to unite network segments
  - An interface bridge configuration causes multiple interfaces to share the same subnet, as if the ports were on a switch.
- Bridges are considered layer 2

Source: [ChatGPT](https://chat.openai.com/share/308eaae2-6b7b-4d67-8af0-985777bf7a67)

---

<!-- .element class="main-title" -->

# Review:

## Lab 09

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture: 
  - AWS VPC
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 09**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 10** - Python File Handling

NOTE:

### Review: Ops Challenge 09

### Introduce: Ops Challenge 10 - Python File Handling

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - AWS VPC
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 10 - AWS VPC

NOTE:
Is there a relevant Ch. in the Wiley Network+ (N10-008) Study Guide?

Ok, what's the deal with introducing VPCs, cause I clearly don't love how these slides are structured.
- One issue is that we haven't *really* built local network systems that mimic what we use a VPC for, cause we've focused on user-centered networks, rather than infrastructure-centered networks
- This would be a good place to introduce the Region + Availability Zone thing -- **but it's not necessary for MVP**
- They need to understand how many of the functions of a network which must be hosted on a router or another machine in an on-prem network (or in a virtual network meant to mimic an on-prem) can be partially abstracted in a fully virtualized network:
  - Things that don't need a responsible networked device in AWS:
	- IP Assignments/DHCP (handled automatically by subnets)
	- Subnet definition (defined within a VPC)
	- DNS (happens in the background)
	- Firewall/traffic filtering (Sec Groups attached to individual resources)
	- Routing (handled by routing tables within VPCs, which connect subnets and Internet Gateways)
	- Gateways (handled by Internet Gateways in a VPC)
	- Perimeter Network/DMZ (We call this a Public Subnet and define it in a VPC)
  - So all those things were handled but physical devices (or emulated devices) like routers, switches, firewalls, etc., which as devices must be managed and networked as well
  - In AWS, we can dispense with the need to have networked devices to run these things -- the "cloud" can handle abstract routing table and firewall rules which are attached to arbitrarily defined resources without the need for those rules or resources to *live* anywhere



- Cloud networking components
  - The network components in the cloud are very similar to the ones we would find in a data center
  - Components
    - VPC
    - Subnets
      - Public
      - Private
    - Internet Gateway
    - NAT Gateway
    - Security Groups

---

<!-- .element class="split-screen-with-title" -->


# Cloud Networking

<div>

<div align="left" style="font-size: 28px">

**On-prem networks** built from physical or emulated devices need devices to host critical features and roles of a network, and connections to be made between them with cables and wireless signals:
- Routers handle:
  - **IP Addressing** with DHCP
  - **Routing** between subnets
  - **Connecting** intranets and the internet
  - **Subnet Definition**
- Firewalls handle **Traffic filtering**
- Switches, cabling, and WAP **connect everything together**


</div>

<div align="left">

But in a **fully virtualized network environment** like AWS, **we don't need to be limited** by such material restrictions:

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_06a.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

You would find this structure in a data-center, not an *office* on-prem network. 
- Office on-prem networks are primarily about managing and serving users who are within the network
- Data-centers are generally built to host and regulate access to resources which are accessed from outside the local network environment, which is basically what we use the cloud for as well
  - "Cloud just means using someone else's hardware"

Image Source: include link to image source
Source: AWS

---

<!-- .element class="split-screen-with-title" -->


# Cloud Networking

<div>

<div align="left" style="font-size: 28px">

<br>

<br>

**Cloud Networks** require the **same features** as **on-prem networks** built from physical or emulated devices:
- Assignment schemes for **IP addressing**
- Tables of **routing information**
- Rules for **allowing and disallowing traffic**
- Gateways to **negotiate traffic between intranet and Internet**
- Shared IP addressing spaces to **define subnets**

</div>

<div align="left" style="font-size: 28px">

But **Cloud Networks leverage virtualization** to reduce network components to their simplest, most abstract parts:
- IP assignment is done automagically by subnets; **no DHCP server required**
- **Routing Tables** attached to an invisible, virtual router
- **Security Groups** are sets of traffic filtering rules; **no firewall needed**
- **Internet Gateways** let traffic pass in and out of a **VPC**
- **Subnets** and their shared **broadcast domains** are arbitrarily defined within a **VPC**

</div>

</div>

NOTE:

DNS servers are also handled abstractly

Each VPC is associated with a VPC router, which is a virtual router managed by AWS.
- The VPC Router is where Route Tables, Internet Gateways, Virtual Private Gateways (VPNs), and other network features actually live
- **However**: VPC routers are mostly invisible, in that we don't actually refer to them directly, we just define the features they contain
- N.B. Might want to expand on this concept

---

<!-- .element class="split-screen-with-title" -->


# Virtual Private Cloud:

<div>

<div align="left">

- **Closely resemble traditional networks** built in **data centers**
- **Logically isolated** from other virtual networks in the AWS Cloud
- **Contain** other AWS resources, such as EC2 instances
- A defined by a **large IP addressing space (address block)**
  - Support both IPv4 and IPv6 addressing
- Can contain both **publicly- and privately-accessible services**, when configured correctly

</div>

<div align="left">

> **Amazon Virtual Private Cloud (VPC)**:
>
> A virtual network dedicated to your AWS account

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_02.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: include link to image source

---

<!-- .element class="split-screen-with-title" data-visibility="hidden"-->


# Availability Zones

<div>

<div align="left">




</div>

<div align="left">

> **

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_00.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: include link to image source

---

<!-- .element class="split-screen-with-title" -->

# Subnets in AWS VPCs

<div>

<div align="left">

- **Public Subnets** host public-facing services like websites or file servers
  - These are analogous to a **Perimeter Network/DMZ**
- **Private Subnets** are meant for internal resources and disallow access to resources from outside the VPC
- An **Internet Gateway** is attached to your VPC to enable communication between your subnets and the internet

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_07b.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

You can use a **network address translation (NAT) gateway** to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances.
- NAT gateways will charge you.


Image Source: include link to image source
Source: PurpleBox

---

<!-- .element class="split-screen-with-title" -->

# Subnets in AWS VPCs

<div>

<div align="left"style="font-size: 32px">

- **VPCs are given a block of network addresses** at creation
  - Example: 10.0.0.0/16
- However, those addresses are not directly usable without defining a **Subnet**
- Example: a VPC with **`10.0.0.0/16`** block could contain: **`10.0.0.0/24`** subnet, a **`10.0.1.0/24`** subnet, and a **`10.0.2.0/24`** subnet

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_07b.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

Image Source: include link to image source
Source: PurpleBox

---

<!-- .element class="split-screen-with-title" -->


# Security Groups

<div>

<div align="left" style="font-size: 28.4px">

> A **Security Group (SG)** controls the incoming and outgoing traffic of any resource it is associated with
Security group basics
- They are **stateful** (aware of established sessions)
- **Inbound and outbound traffic rules** are defined by:
  - Protocol
  - Port Range
  - Source or Destination
  - ICMP type and code

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-10/slides/assets/10_07c.png)
<!-- .element style="width: 95%"-->

</div>

</div>

NOTE:

N.B.: we also see a **VPC Router** and **Routing Tables** in this topology:
- A **route table** is a set of rules, called routes, that are used to determine where network traffic is directed.

The **Firewalls** we have used are either:
- Defined individually on each device
- Defined on a **Network Appliance** (like a router or a standalone firewall), which then applies to traffic passing through it

**Security Groups** are like firewalls, except they are defined independently of any device or appliance and then **associated** with individual resources
- When associated with an EC2 instance, it controls inbound and outbound traffic to that instance

In our lab, we will define public and private subnets, and also public and private SGs
- **However**, we will associate the SGs with the EC2 **instances on the subnets**, but the SGs are **not associated with the subnets themselves**

**Essentially**, SGs operate like device firewalls, except we can define them once rather than individually configure them for each device

There are other **AWS services that mimic a traditional network firewall appliance**, but we do not use them today:
- Network ACLs
- AWS WAF (Web Application Firewall)
- AWS Firewall Manager
- AWS Network Firewall

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 10 - AWS VPC
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: 
  - AWS VPC
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## AWS VPC

NOTE:

### Demo: AWS VPC

