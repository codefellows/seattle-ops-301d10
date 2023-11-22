<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 11

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Windows Server
- Demo

---

<!-- .element class="split-screen-with-title" -->

## Course Overview

<div>

<div align="left" style="font-size: 35px">

**Modules:**
- **Module 1** Networking Tools, Concepts, and Fundamentals
- **Module 2** Network Infrastructure Design and Implementation
- &shy;<!-- .element style="color: red;" -->**Module 3** Server Administration, Active Directory, and User Management
- **Module 4** Project

</div>

<div>

![Image](/ops-301-guide/curriculum/class-11/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 3 - Server Administration, Active Directory, and User Management

<div>

<div align="left" style="font-size: 40px">

&shy;<!-- .element style="color: red;" -->**Class 11** Windows Server

**Class 12** Domain Controller

**Class 13** Active Directory

**Class 14** Group Policy

**Class 15** N/A: Project Kickoff


</div>

<div>

![Image](/ops-301-guide/curriculum/class-11/slides/assets/0_02.png)
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 3 Challenges: Python + PowerShell

<div>

<div align="left" style="font-size: 50px">


&shy;<!-- .element style="color: red;" -->**Class 11** Psutil

**Class 12** Python Requests Library

**Class 13** Powershell AD Automation

**Class 14** Python Malware Analysis

**Class 15** N/A


</div>

<div>

![Image](/ops-301-guide/curriculum/class-11/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Windows Server
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Windows Server
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 10

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

![Image](/ops-301-guide/curriculum/class-11/slides/assets/10_02a.png)
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

![Image](/ops-301-guide/curriculum/class-11/slides/assets/10_00.png)
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

![Image](/ops-301-guide/curriculum/class-11/slides/assets/10_07b.png)
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

![Image](/ops-301-guide/curriculum/class-11/slides/assets/10_07b.png)
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

![Image](/ops-301-guide/curriculum/class-11/slides/assets/10_07c.png)
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

Image Source: Firewall free icon, by Those Icons, [Flaticon License](https://www.freepikcompany.com/legal#nav-flaticon-agreement), via [Flaticon](https://www.flaticon.com/free-icon/firewall_811683)

---

<!-- .element class="main-title" -->

# Review:

## Lab 10

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Windows Server
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 10**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 11** - Psutil

NOTE:

### Review: Ops Challenge 10

### Introduce: Ops Challenge 11 - Psutil

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Windows Server
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 11 - Windows Server

NOTE:
- Windows Server is a powerful and versatile operating system developed by Microsoft, designed to serve as the backbone of modern IT infrastructures.
- It provides a robust platform for organizations to manage, store, and secure data, host applications, and facilitate network services.
- With a range of editions and features tailored to diverse business needs, Windows Server is a cornerstone of enterprise computing, offering scalability, reliability, and extensive management tools to support businesses of all sizes.

---

<!-- .element class="split-screen-with-title" -->


# Servers

<div>

<div align="left">

- Definition of a server depends on context
  - Hardware
    - HP Proliant
    - Dell PowerEdge
    - NAS file server
  - OS
    - Windows Server 2019
    - Ubuntu Linux Server
  - Software
    - File server
    - nginx Web server running Linux

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_01.png)
<!-- .element style="width: 100%"-->


</div>

</div>

NOTE:
**Definition of a Server Depends on Context:**
A server is a computer or system designed to provide specific services, resources, or functions to clients or other devices over a network. The exact definition and purpose of a server can vary widely depending on the context and the specific role it plays in a networked environment.

**Hardware:**
Servers come in various hardware configurations, and two common examples are:

- **HP Proliant:** HP Proliant servers are a line of enterprise-grade hardware known for their reliability and performance. They are often used for a wide range of server applications, including database hosting and virtualization.
- **Dell PowerEdge:** Dell PowerEdge servers are another popular choice among businesses for their robust hardware and scalability. They are commonly used for tasks such as web hosting and data storage.
- **NAS File Server:**
A Network-Attached Storage (NAS) file server is a specialized server that is primarily used for storing and sharing files over a network. NAS devices are dedicated to this purpose and often include multiple hard drives configured for data redundancy and access control.

**Operating Systems (OS):**
Servers require an operating system to manage hardware resources and run server software. Examples of server operating systems include:

- **Windows Server 2019:** Microsoft's server operating system designed for enterprise applications, offering features like Active Directory, virtualization, and robust security.
- **Ubuntu Linux Server:** A popular Linux distribution often used for server environments due to its stability, security, and extensive software repositories.

**Software:**
Server software defines the specific role or service a server provides. Examples include:

- **File Server:** A file server is dedicated to storing and sharing files with users or other systems within a network, facilitating centralized file management and access control.
- **nginx Web Server (Running on Linux):** Nginx is a high-performance web server and reverse proxy server. When combined with Linux, it provides a powerful platform for hosting websites, web applications, and web services.

OLD NOTES:
- What is a server?
  - Can mean many things depending on context
    - OS. "Windows Server 2019 is an OS."
      - Can be virtualized and often is!
    - Hardware. "I had to go into the tech room and plug a network cable into the server."
    - Software running a critical service. "The DHCP server is malfunctioning."
  - Computer that is the dedicated provider of a particular service
    - A NAS device is an example of a file server
    - A website is dependent on a web server for hosting

Source: AandEnterprise

---

<!-- .element class="split-screen-with-title" -->


# Servers

<div>

<div align="left">

- What do hardware servers look like and where are they stored?
  - Data Centers are buildings dedicated to powering many servers 24/7
  - Blade-style servers rack-mounted for optimal maintenance
  - Loud!
  - Example use cases
    - AWS availability zones
    - Crypto-mining facilities
    - Rackspace web hosting

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
**Data Centers:** Data centers are specialized facilities designed to house and operate large numbers of servers and networking equipment. They provide a controlled environment with temperature and humidity regulation, redundant power supplies, and security measures. Servers in data centers are maintained around the clock to ensure high availability.

**Blade-Style Servers:** Blade servers are compact, modular servers that are often rack-mounted for efficient use of space. They share common resources, such as power and cooling, making them easier to manage and maintain. Their design optimizes scalability and maintenance.

**Loud:** Servers can be noisy due to cooling fans and the constant operation of hardware components. This noise level can be challenging in data center environments and may require specialized soundproofing and cooling solutions.

**Example Use Cases:**

  - **AWS Availability Zones:** Amazon Web Services (AWS) divides its infrastructure into availability zones (AZs), each comprising one or more data centers. These AZs provide redundancy and fault tolerance, ensuring that AWS services remain available even in the event of hardware or data center failures.

  - **Crypto-Mining Facilities:** Cryptocurrency mining operations often rely on extensive server farms to solve complex cryptographic puzzles. These servers work collaboratively to validate and record cryptocurrency transactions, and they require significant computational power and cooling.

  - **Rackspace Web Hosting:** Rackspace is a managed cloud hosting provider that offers a range of hosting services, including web hosting. Their servers are hosted in data centers, providing businesses with reliable and scalable web hosting solutions to ensure websites and applications remain accessible to users.


OLD NOTES:
- What do hardware servers look like and where are they stored?
  - Data Centers
  - Rackmount (look at pictures for reference)
  - Size of rack mount designated by "#U"
  - Commonly paired with other rack mounted and related appliances
    - UPS for power
    - Switches for networking
    - Firewalls
    - Routers
    - NAS
  - Tend to be loud
    - Share [Dell PowerEdge R720XD Noise Level](https://www.youtube.com/watch?v=YVfbxv6VGdI&ab_channel=123aznbeast2)
    - Why so loud on startup? Fans are testing.
  - Consumer power
  - Designed for 24/7 uptime

Source: AandEnterprise

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**
<!-- .element style="color: red"-->

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_02.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**Server:** This is the fundamental unit in this context, representing the hardware and software responsible for providing specific services or resources.

**Rackmount:** A "rackmount" server refers to the physical form factor of a server designed to be mounted in a standard server rack. These servers are typically compact and fit into standard-sized racks for efficient use of space.

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**
<!-- .element style="color: red"-->

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_03.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**Server Racks**: Servers are often mounted in server racks, which are metal frames or enclosures designed to hold multiple servers in a standardized form factor. These racks come in different sizes, with 19-inch racks being the most common. Rack-mounted servers are secured in these racks using mounting rails or brackets.

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**
<!-- .element style="color: red"-->

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_04.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**What do you call multiple servers, stacked on top of each other in multiple racks?**

When multiple servers are stacked on top of each other in multiple racks, this configuration is often referred to as a "server farm," "server cluster," or "server room."

These terms describe a collection of servers organized within a data center or dedicated server room environment. The servers may be housed in individual racks or cabinets, with each rack containing multiple servers.

**Server Farm:** A server farm typically refers to a large grouping of servers used to provide computing power and services, often for hosting websites, applications, or data processing. It may consist of multiple racks or cabinets of servers, and the term implies a significant scale of server deployment.

**Server Cluster:** A server cluster is a closely interconnected group of servers working together to perform specific tasks or provide high availability and redundancy. These servers are often organized in racks or cabinets within a data center.

The specific term used may vary depending on the context and the scale of the server deployment.

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**
<!-- .element style="color: red"-->

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_05.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**Server Room:** A server room is a dedicated space within a facility that houses servers and networking equipment. In larger organizations, multiple racks or cabinets may be installed in the server room to accommodate the server infrastructure.

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**
<!-- .element style="color: red"-->

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_06.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**Data Centers:** Servers racks are housed in data centers, which are specialized facilities designed to provide an optimal environment for server storage and operation. Data centers offer:
  - Climate Control: Precise temperature and humidity control to maintain server hardware within specified operating conditions.
  - Redundant Power: Multiple power sources and backup generators to ensure uninterrupted server operation.
  - Security: Access control, surveillance, and physical security measures to protect servers from unauthorized access and potential threats.
  - Fire Suppression: Advanced fire detection and suppression systems to safeguard against fire-related hazards.
  - Structured Cabling: Neat and organized cabling systems for data transmission and power distribution.
  - Monitoring: Continuous monitoring of server health, environmental conditions, and security.

---

<!-- .element class="image-full-bleed" -->


# **Servers - Zoom Out**


![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_07.png)
<!-- .element style="width: 86.5%"-->


NOTE:
**Why do we need data centers all over the world?**

Data centers are strategically distributed all over the world for several important reasons:

**Reduced Latency:** Placing data centers in various geographic locations helps reduce network latency. When users access online services or data hosted in a data center that is physically closer to them, data travels shorter distances over the internet, leading to faster response times and improved user experiences.

**Redundancy and High Availability:** Data centers are designed with redundancy in mind. Having multiple data centers ensures that if one experiences a failure or disruption (such as power outages, hardware failures, or natural disasters), services can quickly fail over to other locations, minimizing downtime and ensuring high availability.

**Disaster Recovery:** Data centers are distributed to different regions or even continents to mitigate the risk of natural disasters, such as earthquakes, floods, hurricanes, or wildfires. Redundant data centers allow for disaster recovery and business continuity planning to safeguard data and services.

**Compliance and Data Sovereignty:** Many countries and regions have specific regulations and compliance requirements regarding data storage and processing. Distributing data centers globally allows organizations to comply with local data protection laws and maintain data sovereignty, which may require data to be stored within specific geographic boundaries.

**Load Balancing:** By distributing workloads across multiple data centers, organizations can balance the computational load more efficiently. This helps optimize resource usage and ensures that services can handle fluctuations in demand without performance degradation.

**Content Delivery:** Content delivery networks (CDNs) use distributed data centers to cache and serve content, such as web pages, videos, and images, from servers geographically close to end-users. This accelerates content delivery and minimizes bandwidth consumption.

**Global Reach:** Organizations with a global user base or international operations benefit from having data centers in various regions to cater to users' local needs. It improves the responsiveness of applications and services for users worldwide.

**Scalability:** Distributed data centers support scalability. As an organization's computing and storage needs grow, they can expand their infrastructure by adding additional data center locations or resources within existing centers.

**Geopolitical Considerations:** Geopolitical factors, including international trade agreements and political stability, can influence the location of data centers. Organizations may establish data centers in regions with favorable economic and political conditions.

**What are "hops" in this context?**

Refers to the number of intermediate devices, such as routers or switches, that data packets must traverse as they move from one network node (e.g., a computer) to another. Each time data passes through one of these intermediate devices, it is considered to have completed one "hop."

Hops are a measure of the complexity and distance data must travel within a network. They can impact factors like latency, network congestion, and overall data transmission speed. In general:

- Fewer hops typically result in lower latency and faster data transfer because data travels a more direct path.
- More hops may introduce additional latency and increase the potential for network congestion or packet loss, especially if there are bottlenecks at certain network points.

Reducing the number of hops between network nodes is often a goal in network optimization to improve performance and reliability. Efficient routing algorithms and network infrastructure design aim to minimize hops and maximize data transmission efficiency.

The location of data centers can significantly affect the number of "hops" that data packets need to traverse.

**Proximity to End-Users:** When a data center is located closer to the end-users or clients who are accessing its services, it reduces the number of hops. Data packets can take a more direct route from the user to the nearby data center, resulting in lower latency and faster response times.

**Content Delivery:** Content delivery networks (CDNs) strategically place data centers and caching servers in various geographic locations. These distributed data centers help reduce hops by serving content from a server that is physically closer to the user. This minimizes the number of hops data must travel to reach the user, improving content delivery speed.

**Global Network Architecture:** Large organizations or cloud service providers often have a global network presence with multiple data centers in various regions. These data centers are interconnected through high-speed, low-latency links. When users access services hosted in these data centers, the network infrastructure can intelligently route traffic to the nearest data center, minimizing hops and optimizing performance.

**Data Replication and Redundancy:** To ensure high availability and disaster recovery, data centers may replicate data to other geographically dispersed data centers. When a user accesses data, the network can route them to the nearest data center with a copy of the requested data. This can reduce hops and improve redundancy.

**Regional Data Localization:** Data privacy regulations in some regions require certain types of data to be stored within the country's borders. In such cases, organizations establish data centers in those regions to comply with local laws. This localization can reduce hops for users within the region.

**Load Balancing:** Data centers often employ load balancing techniques to distribute user requests evenly across multiple server instances or data centers. Load balancers can make routing decisions based on factors like server load and network proximity, optimizing the number of hops for each request.

---

<!-- .element class="split-screen-with-title" -->


# RAID
Increase data redundancy and/or improve performance

<div>

<div align="left" style="font-size: 27px">

**RAID** (**Redundant Array of Independent Disks**):
- A **data storage virtualization technology** that maps multiple physical disks to a single "drive"
- **Mirrored disks** are **failover real-time copies** of each other
  - Creates redundancy
- **Striped disks** depend on each other for optimal performance but aren't clones
- Learn RAID 0, 1, and 5 for starters -- Study!
- **RAID provides High Availability (HA), but is NOT a backup!**

</div>

<div align="left">


![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_08.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Title, Author, License Type</div>

</div>

</div>

NOTE:
**RAID (Redundant Array of Independent Disks):**
- RAID is a technology that combines multiple physical disks into a single logical unit, appearing as a single "drive" to the operating system. It is used to enhance data storage and provide various levels of redundancy and performance.

**Mirrored Disks (RAID 1):**
- In RAID 1, also known as disk mirroring, data is duplicated across two or more disks. These mirrored disks are real-time copies of each other, providing redundancy. If one disk fails, the data remains accessible from the mirrored copy, ensuring data integrity and availability.

**Striped Disks (RAID 0):**
- RAID 0, also known as disk striping, does not provide redundancy but aims to improve performance. Data is divided into blocks and written across multiple disks. While this striping enhances read/write speeds, if one disk fails, data loss occurs, as there are no redundant copies.

**RAID Levels to Learn:**
- For starters, it's essential to understand RAID 0, RAID 1, and RAID 5:
  - **RAID 0:** Improves performance through striping but offers no redundancy.
  - **RAID 1:** Provides redundancy through mirroring but doesn't improve performance.
  - **RAID 5:** Offers both performance improvement and redundancy by striping data across multiple disks and using parity for fault tolerance.

**High Availability (HA) vs. Backup:**
- RAID provides High Availability (HA) by ensuring data remains accessible even if a disk fails. However, it's crucial to note that RAID is not a substitute for proper backups. Backups involve regularly copying data to separate media or locations, protecting against data loss due to various factors, including accidental deletion, corruption, or catastrophic failures.

OLD NOTES:
- RAID (Redundant Array of Independent Disks) is a data storage virtualization technology that utilizes multiple physical disk drives to increase data redundancy and/or improve performance.
  - View the raid chart at [RAID LEVELS INTRO FOR BEGINNERS: PROS, CONS, AND
    TECHNIQUES](https://ttrdatarecovery.com/raid-levels/) for a visual comparison of the RAID types
  - RAID Types
      - RAID 0 - stripes data across multiple drives
      - RAID 1 - takes all data and mirrors it to a second drive
      - RAID 5 - uses parity to provide redundancy, can rebuild data if one drive fails
- More CPU and RAM storage on deck per server blade
- In a business, tend to be stored in a dedicated fireproofed electrical room
- In a home, somewhere cool and separated like a closet or garage

- What hardware specs should I look for in a server?
  - Similar to desktop components
  - Look for high CPU and RAM; redundant drives great to find
  - Depends on the purpose

> Yes you can totally deploy enterprise-grade equipment at home, just keep an eye on that power bill!

- How can we transition from workgroup P2P to client-server architecture?
  - Need to deploy Windows Server 2019 to the LAN
  - This server will host authoritative services that "take charge" of the Windows 10 computers

Source: TRR Data Recovery
Image Source: include link to image source

---

<!-- .element class="main-title" -->
# IT Project Management


NOTE:
- IT Project Management is a critical discipline within the realm of information technology, responsible for the planning, execution, and successful delivery of IT projects.
- These projects encompass a wide range of initiatives, from software development and system implementations to network upgrades and cybersecurity enhancements.
- Effective IT project management ensures that resources are allocated efficiently, timelines are met, and project objectives align with the organization's strategic goals, ultimately driving innovation and success in the technology-driven world.

---

<!-- .element class="image-with-title" -->
# IT Project Management

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_09.png)

NOTE:
The choice between Waterfall and Agile project management depends on the project's nature, requirements, and the organization's culture. Waterfall is often used for projects with well-defined, stable requirements, while Agile is favored for projects with evolving or uncertain needs that benefit from rapid adaptation and customer involvement.

**Waterfall IT Project Management:**

Waterfall is a traditional and linear project management methodology that follows a sequential, step-by-step approach. In waterfall project management, each phase of the project is completed before moving on to the next one. The key characteristics of the waterfall model include:

1. **Phases:** Waterfall projects typically consist of distinct phases such as requirements gathering, design, implementation, testing, deployment, and maintenance.

2. **Sequential:** Phases follow a fixed order, and progress flows in one direction, making it challenging to revisit previous phases once they are completed.

3. **Detailed Planning:** Extensive planning is done upfront to define project requirements, scope, and deliverables in detail.

4. **Documentation:** Comprehensive documentation is generated at each phase, serving as a reference for project progress and outcomes.

5. **Rigidity:** Waterfall projects are less adaptable to changes in requirements or unexpected issues, as adjustments are cumbersome after the project begins.

**Agile IT Project Management:**

Agile is a flexible and iterative project management methodology that focuses on collaboration, adaptability, and delivering value incrementally. Agile projects break the work into smaller, manageable increments, and the key characteristics of Agile include:

1. **Iterations:** Agile projects are divided into short iterations or sprints, typically lasting two to four weeks, where a specific set of features or tasks is completed.

2. **Collaboration:** Cross-functional teams collaborate closely with stakeholders, allowing for continuous feedback and adjustments.

3. **Customer-Centric:** Agile prioritizes delivering value to the customer quickly, allowing for evolving requirements and changes based on customer feedback.

4. **Adaptability:** Agile embraces change and welcomes evolving requirements, making it well-suited for projects with uncertain or changing needs.

5. **Minimal Documentation:** While Agile projects maintain documentation, the focus is on working software or deliverables over comprehensive documentation.

6. **Testing and Feedback:** Testing is conducted continuously throughout the project, and feedback from testing is used to refine and improve the product.

**Comparison:**

- **Approach:** Waterfall is a sequential, plan-driven approach, while Agile is an iterative and adaptable approach.
- **Flexibility:** Waterfall is less flexible in accommodating changes after project initiation, whereas Agile embraces change.
- **Risk:** Waterfall attempts to mitigate risks upfront through detailed planning, while Agile manages risk through continuous testing, feedback, and adaptation.
- **Customer Involvement:** Agile involves customers and stakeholders throughout the project, while Waterfall typically involves them at the beginning and end.
- **Delivery:** Waterfall delivers the entire project at the end, while Agile delivers functional increments at the end of each iteration.
- **Documentation:** Waterfall places a strong emphasis on documentation, whereas Agile prioritizes working software or deliverables.


OLD NOTES:
- Why do we care about project management in an Ops class?
  - These ideas may help your team stay organized as you enter project week
  - If you're looking at any kind of systems administration role, you should consider picking up qualifications and experience
    related to project management. This can be a competitive edge in the job hunt!

- What frameworks allow IT teams to operate effectively and at scale?
  - ITIL framework
    - Good resource for reference: Wiki IT Process Maps
    - Four dimensions model
      - ITIL 4 defines four dimensions that should be considered to ensure a holistic approach to service management:
        - Organizations and people
        - Information and technology
        - Partners and suppliers
        - Value streams and processes

    - Service value system
      - The service value System (SVS) represents "how all the components and activities of an organization work together to
        facilitate value creation". The ITIL 4 SVS includes several elements:
        - Guiding principles
          - Recommendations that guide an organization in all circumstances, regardless of changes in its goals, strategies, type
            of work or management structure
        - Governance
          - The means by which an organization is directed and controlled
        - Service value chain
          - A set of interconnected activities that an organization performs to deliver a valuable product/service to its customers
        - Continual improvement practices
          - Recurring organizational activity that takes place at all levels to make sure that stakeholders' expectations are met

- What is Agile project management?
    - Agile is a philosophy that advocates for the incremental and evolutionary delivery of outputs instead of revolutionary one
      and encourages the iterative revisiting of project stages.
      - Benefits
        - Faster deployment life cycle
        - Predictable schedule (sprints)
        - Customer-focused approach
        - Flexibility
        - Team empowerment
        - Promotes effective communication

    - Waterfall is the traditional project management approach where stages are marked complete and not revisited.

- CompTIA Project+
- Agile-related credentials and experience
- PMP (advanced, experienced PMs only)

Source: DevTeam.space

---

<!-- .element class="split-screen-with-title" data-visibility="hidden"-->


# IT Project Management

<div>

<div align="left">



</div>

<div align="left">

> **

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_00.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Title, Author, License Type</div>

</div>

</div>

NOTE:

Image Source: include link to image source


---

<!-- .element class="main-title" -->
# IT Infrastructure

NOTE:
- IT infrastructure forms the technological backbone of modern organizations, encompassing all the hardware, software, networks, and resources necessary to support the information technology needs of a business.
- This intricate ecosystem of components provides the foundation for data storage, communication, computing, and the delivery of IT services.
- IT infrastructure plays a pivotal role in enabling businesses to operate efficiently, innovate, and remain competitive in the digital age.

---

<!-- .element class="split-screen-with-title" -->


# IT Infrastructure

<div>

<div align="left">

- Servers are computers that host services for clients to access
  - Service delivery
  - Scalable
  - Mission-critical asset
    - Targeted by threat actors
    - Allows sysadmins to oversee network at scale
- You've been promoted!

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_10.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
- **Servers** are specialized computers designed to host and deliver various services that clients can access over a network. They are the workhorses of IT infrastructure, providing essential functions for organizations of all sizes.

- **Service Delivery:** Servers are dedicated to delivering specific services, such as web hosting, email, database management, and file sharing, making them indispensable for business operations.

- **Scalability:** Servers can be scaled vertically (by upgrading hardware components) or horizontally (by adding more servers) to accommodate growing demands. This scalability ensures that IT infrastructure can adapt to changing needs.

- **Mission-Critical Asset:** Servers often host mission-critical applications and services that are essential for daily operations. Any downtime can result in significant disruptions and financial losses.

- **Targeted by Threat Actors:** Servers are prime targets for cyber threat actors due to their critical role in service delivery. Protecting servers against security threats is a top priority for IT teams.

- **Network Oversight:** Servers enable system administrators (sysadmins) to oversee and manage a network at scale. They provide centralized control and monitoring, facilitating efficient network administration.

Servers are the backbone of IT infrastructure, supporting a wide range of services and applications critical to business success. Their security, reliability, and scalability are of paramount importance in modern IT environments.

OLD NOTES:
- Why are we studying servers?
  - Predominant way services are delivered, computers configured, and user identities managed
  - Facilitates computing at larger scales, e.g. "enterprise-grade server"
  - Often a mission-critical asset in a company requiring specialized skill set to administer
    - Attractive target for hackers seeking to access company secrets or simply seeking to cause outages
    - Primary way a systems administrator can oversee a network at scale
  - In this course, you'll be promoted from level one support technician to a network and systems administrator. That's a lot of
    responsibility!

Image Source: Yanni Davros, [Prolific Pen Comics](https://prolificpencomics.net/comic/tech-support-raph-comics-collab/1tps://prolificpencomics.net/comic/tech-support-raph-comics-collab/)

---

<!-- .element class="split-screen-with-title" -->


# IT Infrastructure

<div>

<div align="left">

- In client-server architecture, clients access a server to provide the given service
  - **Thin clients** are lightweight, low-spec computers meant to remote into s server which does the majority of the processing
  - **Thick clients** perform the majority of the processing on their own hardware

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_11.png)
<!-- .element style="width: 120%"-->

<div style="font-size: small">Carl Sack, CC BY-SA 3.0</div>

</div>

</div>

NOTE:
- In **client-server architecture**, clients are devices or software applications that access a central server to obtain services or resources. This model is fundamental to networked computing and is used for various purposes, including web hosting, database management, and file sharing.

- **Thin clients** are lightweight computing devices or software applications that rely on a server to perform the majority of processing tasks. These clients are often used in situations where processing power, storage, and software capabilities are offloaded to a central server. Thin clients are cost-effective, easy to manage, and well-suited for tasks like remote desktop access and virtualization.

- **Thick clients**, also known as "fat clients" or "rich clients," have substantial processing power and resources of their own. They perform a significant portion of data processing and application execution on their local hardware. Thick clients are commonly used for software applications that require substantial computing capabilities, such as video editing or computer-aided design (CAD) software.

The choice between thin and thick clients depends on factors like the specific computing needs of the organization, cost considerations, and the desired level of centralization and control. Thin clients are often favored for their ease of management and cost savings, while thick clients provide more processing power and autonomy but may require higher maintenance and resource allocation.

Image Source: Carl Sack, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Thin_Client-Thick_Client.jpg)

---

<!-- .element class="split-screen-with-title" -->


# IT Infrastructure

<div>

<div align="left">

- A workgroup is decentralized and does not answer to a singular authority
  - Peer-to-peer (P2P)
  - Default of Win 10 out the box
  - Easy to deploy but config varies
- A domain is a network of computers that all answer to a singular authority
  - A domain style network is a form of client-server architecture
  - Standard best practice design
  - …but potentially single point of failure

</div>

<div align="left">


![Image](/ops-301-guide/curriculum/class-11/slides/assets/11_12d.png)
<!-- .element style="width: 85%"-->


</div>

</div>

NOTE:
**Workgroup:**
- A **workgroup** is a decentralized network configuration in which individual computers or devices connect to each other in a peer-to-peer (P2P) manner. In a workgroup, there is no central authority or server that manages user accounts and resources. Key characteristics include:
  - **Peer-to-Peer (P2P):** Workgroup computers communicate directly with each other without relying on a centralized server.
  - **Default of Win 10:** In a Windows-based environment, Windows 10 and earlier versions default to a workgroup configuration.
  - **Easy to Deploy but Config Varies:** Workgroups are easy to set up, making them suitable for small networks, home environments, or temporary setups. However, configuration and management can vary between devices, leading to challenges in maintaining consistency and security.

**Domain:**
- A **domain** is a network architecture in which all connected computers and devices answer to a central authority known as a domain controller. A domain follows a client-server model, where the server manages user accounts, access permissions, and network resources. Key characteristics include:
  - **Client-Server Architecture:** A domain network operates on a client-server model, where the domain controller centrally manages user authentication and resource access.
  - **Standard Best Practice Design:** Domains are considered a best practice for medium to large organizations as they offer centralized control, security, and scalability.
  - **Single Point of Failure:** While domains provide centralized control, they can be vulnerable to a single point of failure if the domain controller experiences issues. Redundancy and backup measures are crucial to mitigate this risk.

The choice between a workgroup and a domain network depends on factors such as the size of the organization, security requirements, ease of management, and scalability needs. Workgroups are simpler to set up but may lack centralized control, while domains offer greater control and security but require more complex configuration and maintenance.


---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 11 - Windows Server
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Windows Server
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Windows Server

NOTE:

### Import OVA File


### Demo: Windows Server

