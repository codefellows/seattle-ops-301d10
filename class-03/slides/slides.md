<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 03

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Network Segmentation
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

![Image](/ops-301-guide/curriculum/class-03/slides/assets/0_01.png)
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

&shy;<!-- .element style="color: red;" -->**Class 03** Network Segmentation

**Class 04** Routing

**Class 05** VPN Tunnel


</div>

<div>

![Image](/ops-301-guide/curriculum/class-03/slides/assets/0_02.png) 
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

&shy;<!-- .element style="color: red;" -->**Class 03** File Permissions

**Class 04** Conditionals in Menu Systems

**Class 05** Clearing Logs


</div>

<div>

![Image](/ops-301-guide/curriculum/class-03/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Network Segmentation
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Network Segmentation
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 02

---

<!-- .element class="split-screen-with-title" -->

# Ports and Protocols

<div>

<div align="left">

**Port Number**:
>
> A number assigned to uniquely identify a connection endpoint and to direct data to a specific service

**Network Protocol**:
>
> An established set of rules that determine how data is transmitted between different devices in the same network

</div>

<div align="left">

**Network Service**:
>
> An application running at Layer 7, providing data storage, manipulation, presentation, communication or other capability according to a **Protocol**

- **Ports only exist as a number** attached to incoming and outgoing packets
  - **Logical Ports** exist at **Layer 4**, and are ***not the same*** as **Layer 1 Physical Ports**
- Each port number is associated with a **Protocol**


</div>

</div>

NOTE:

Source:
- [Wikipedia: Port (computer networking)](https://en.wikipedia.org/wiki/Port_(computer_networking))
- [CompTIA: What Is a Network Protocol, and How Does It Work?](https://www.comptia.org/content/guides/what-is-a-network-protocol)
- [Wikipedia: Network Service](https://en.wikipedia.org/wiki/Network_service)

The whole purpose of port numbers is to facilitate the process of sorting network traffic which a computer receives so that the data is handled by the appropriate **Service**.

---

<!-- .element class="split-screen-with-title" -->

# Network Enumeration

<div>

<div align="left" style="font-size: 28px">

- **Port Scanning** involves sending crafted packets to remote ports, which tells us about:
  - IP addresses
  - Open ports
- **Network Enumeration** uses further information in the response packets to get a more ocmplete pictures, including retrieving:
  - Usernames
  - Group Information
  - Network Shares
  - Active services
  - Host OS

</div>

<div align="left">

>  **Network Enumeration**
>
> Using scanning tools to map out the structure of an unknown network as part of a pentest, or general site survey.

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_12.png)
<!-- .element style="width: 75%"-->

</div>

</div>

NOTE:

David Lee's story:
- Share a story to kick things off. Example: "I once hired a support technician who had a background in network  operations for the US Army. A part of his role was to contribute to team documentation. One of the first things he did on his own was run a Nmap scan of the entire network, in order to have an idea of how many computers he was dealing with on this network. While mildly effective, I would have preferred he notified me first; Nmap interacts with the network hosts quite aggressively to determine what ports are open."

---

<!-- .element class="split-screen-with-title" -->


# Network Enumeration

<div>

<div align="left">

- Protocol analyzers compliment packet sniffers by analyzing either a live capture or a .pcap file.
  - Filter traffic meeting criteria
  - Isolate problematic hosts
  - Identify malicious use of the network
  - Establish network activity baseline (what is normal)
- Protocol hierarchy tool in Wireshark
  -   Identify most recent active hosts
  -   Monitor bandwidth utilization

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_12.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Source: Wikimedia

We can use the *Protocol Hierarchy* tool in Wireshark to view the most active protocols on a network link and generate a baseline network activity report.
  Identify most recent active hosts
  Monitor bandwidth utilization

---

<!-- .element class="main-title" -->

# Review:

## Lab 02

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture: 
  - Network Segmentation
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 02**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 03** - File Permissions

NOTE:

### Review: Ops Challenge 02

### Introduce: Ops Challenge 03 - File Permissions

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Network Segmentation
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 03 - Network Segmentation

NOTE:
Is there a relevant Ch. in the Wiley Network+ (N10-008) Study Guide?

---

<!-- .element class="split-screen-with-title" -->

# Subnetting

<div>

<div align="left">

- A **Network** is a logical collection of contiguous IP addresses
- A **Subnet** is literally a "subnetwork," a network inside of a larger network
- An **IP Address** includes two parts:
  1) The **Network ID**
  2) The **Host ID**
- Subnetting involves *"borrowing"* bits from the **Host ID**  and adding them to the **Network ID**

</div>

<div align="left">

> **Subnetting**: logically breaking an addressable block of IP addresses into multiple, smaller addressable blocks.

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_10.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

### Why

- Why do networks use subnets?
  - Network design & planning will dictate the use of subnets.
  - DHCP ranges are a factor in planning subnets.
  - Segmentation needs.
 
### What

- What is a subnet?
  - A subnet is a sub-network, or a network inside of a larger network.
- What is a netmask?
  - A subnet mask or netmask indicates which bits in the octet are masked.
  - Explains the size of the network.
  - Example: 255.255.255.0 - This one is always associated with a CIDR block of /24.

Source: Trey Perry
Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Subnetting_Concept-en.svg)


---

<!-- .element class="split-screen-with-title" -->

# Subnetting

<div>

<div align="left">
  
A **Subnet Mask** or **Netmask** indicates which bits are "masked" to find the **Host ID**
- Example: 255.255.255.0 in Decimal, or 1111111.11111111.11111111.0 in Binary

Similarly, **CIDR Block Notation** represents the number of binary bits (counted from left to right) which belong to the **Network ID**
  - Example /24 in most home routers


</div>

<div align="left">

> *What portion of an IP address belongs to the **Network ID** and what belongs to the **Host ID**?*

A **Network Address** represents the entire range of possible local IPs as a single IP address with a CIDR block at the end
- Example: 192.168.1.0/24 represents the range 192.168.1.1-254

</div>

</div>

NOTE:

- What is a CIDR block?
  - A CIDR block represents a range of IP addresses using CIDR block notation, which consists of a forward slash then a number. This also serves to represent the size of a network.
  - Example: /24 in most home routers
 
- What is a network address?
  - A network address represents the entire range of possible local IPs as a single IP address with a CIDR block at the end.
  - Example: 192.168.1.0/24 represents the range 192.168.1.1-254.
  - We use network addresses in network diagrams to represent the breadth of a whole LAN or a subnet.

Source: Wikimedia
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="title-with-text" -->

# How to calculate a subnet


![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_12.png)
<!-- .element style="width: 100%"-->
<div style="font-size: small">Dario Lanza, CC BY-SA 3.0</div>


NOTE:

### How

- How is a subnet calculated?
  - Practice calculating a subnet value by hand

Image Source: Dario Lanza, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Tabella_Subnet_con_notazione_CIDR.png)
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="main-title" -->
# Network Segmentation


NOTE:

---

<!-- .element class="split-screen-with-title" -->

# Network Segmentation

<div>

<div align="left">

Reasons to implement network segmentation
- Performance
- Security
- Regulatory compliance
  - NIST SP 800-53
  - NIST SP 800-171
  - NIST Cybersecurity Framework (CSF)
  - Cybersecurity Maturity Model Certification (CMMC)

</div>

<div align="left">

> *Dividing a computer network into smaller, isolated segments or subnetworks to enhance security by controlling and limiting the flow of network traffic between these segments*

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_05.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Why perform network segmentation?
 
  > "Network segmentation is a way to isolate devices on separate networks to achieve better sharing of throughput or bandwidth to the Internet, securing systems with more sensitive data, and separating systems from people and other systems that don't have a need to connect to them." - [blog article](https://www.ckd3.com/blog/2018/10/15/home-network-segmentation-a-must-in-the-iot-era)
 
  - Performance: Efficient use of bandwidth means smoother performance
  - Security: Isolation of problems and incidents
 
  > Example: Separating IT systems from OT systems in an industrial plant.
 
  - Regulatory compliance
    - NIST SP 800-53
    - NIST SP 800-171
    - NIST Cybersecurity Framework (CSF)
    - Cybersecurity Maturity Model Certification (CMMC)
    - International Traffic in Arms Regulations (ITAR)
    - Defense Federal Acquisition Regulation Supplement (DFARS)
    - Health Insurance Portability and Accountability Act (HIPAA)
    - Payment Card Industry Data Security Standard (PCI DSS)

Source: Trey Perry
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Network Segmentation

<div>

<div align="left">

Reasons to implement network segmentation
- Regulatory compliance
  - International Traffic in Arms Regulations (**ITAR**)
  - Defense Federal Acquisition Regulation Supplement (**DFARS**)
  - Health Insurance Portability and Accountability Act (**HIPAA**)
  - Payment Card Industry Data Security Standard (**PCI DSS**)

</div>

<div align="left">

> *Dividing a computer network into smaller, isolated segments or subnetworks to enhance security by controlling and limiting the flow of network traffic between these segments*

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_06.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Why perform network segmentation?
 
  - Regulatory compliance
    - International Traffic in Arms Regulations (ITAR)
    - Defense Federal Acquisition Regulation Supplement (DFARS)
    - Health Insurance Portability and Accountability Act (HIPAA)
    - Payment Card Industry Data Security Standard (PCI DSS)

Source: Trey Perry
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Network Segmentation

<div>

<div align="left">

**Interfaces** can be the physical ethernet ports on a router, but can also be represented virtually.
- Commonly the lowest number is WAN, the rest tend to be LAN. Configurable.
- x0, x1, x2, etc. or ens0, ens1, ens2, etc.
- We can use these interfaces to divide up the network using different subnets and DHCP pools. We'll take a look at this today.

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_07.png)
<!-- .element style="width: 110%"-->

</div>

</div>

NOTE:

### What (10 min) 
- What are router interfaces?
  - Interfaces can be the physical ethernet ports on a router, but can also be represented virtually.
  - Commonly the lowest number is WAN, the rest tend to be LAN. Configurable.
  - x0, x1, x2, etc. or ens0, ens1, ens2, etc.
  - We can use these interfaces to divide up the network using different subnets and DHCP pools. We'll take a look at this today.

Source: Superuser
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Network Segmentation

<div>

<div align="left">

> “**Network Segmentation** divides a computer network into smaller parts. The purpose is to improve network performance and security. Other terms that often mean the same thing are **Network Segregation**, **Network Partitioning**, and **Network Isolation**." 
>
> ~Cisco

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_08.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
- What is network segmentation?
 
  - Cisco: "Network Segmentation divides a computer network into smaller parts. The purpose is to improve network performance and security. Other terms that often mean the same thing are network segregation, network partitioning, and network isolation."
 
  - Cisco: "What is an example of segmentation? Imagine a large bank with several branch offices. The bank's security policy restricts branch employees from accessing its financial reporting system. Network segmentation can enforce the security policy by preventing all branch traffic from reaching the financial system. And by reducing overall network traffic, the financial system will work better for the financial analysts who use it."


Source: Stackexchange
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Network Segmentation

<div>

<div align="left">

> “**Microsegmentation** uses much more information in segmentation policies like application-layer information. It enables policies that are more granular and flexible to meet the highly-specific needs of an organization or business application."
>
> ~Cisco

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_09.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- What is **Microsegmentation**?
  - "**Microsegmentation** uses much more information in segmentation policies like application-layer information. It enables policies that are more granular and flexible to meet the highly-specific needs of an organization or business application."

Source: Wikimedia
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Segmentation Methods

<div>

<div align="left">

In **Logical Segmentation** we rely on software or packet header information to separate network traffic.
- Examples: 
  - Software Defined Segmentation such as **Cisco TrustSec** and **Guardicore** 
  - **VLANs**

In **Physical Segmentation**, hardware interfaces are used

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_08.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Segmentation methods
  - Logical segmentation = VLANs and Zones used
    - In logical segmentation we rely on software or packet header information to separate network traffic.
    - Example:
      - Software Defined Segmentation such as Cisco TrustSec and Guardicore
      - VLANs
  - Physical segmentation = Interfaces used
    - In physical segmentation we separate network traffic by ports and devices.
    - Example: Airgapping OT network from IT network
  - Note that CompTIA considers VLAN a form of virtual segmentation, not physical.
    > "In a virtually segmented network, VLANs identify separate segments. An admin may configure the VLANs in such a way that it achieves virtual system isolation.
    > In a physically segmented network, switches connect segments. The switches may connect in such a way that it achieves system isolation. This method is an approach that results in an air gap." - The Official CompTIA CySA+ Student Guide (Exam CS0-002)

Source: Stackexchange
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->

# Segmentation Policies and Configurations

<div>

<div align="left">

Traditional Technologies:
- Internal firewalls
- ACLs
- VLANs
- Networking equipment

Software-defined Networking:
- Grouping and tagging network traffic
- Enforce segmentation on the network equipment

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-03/slides/assets/03_08.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
- How are segmentation policies/configurations enforced?
 
  - Some traditional technologies for segmentation included internal firewalls, and Access Control List (ACL) and Virtual Local Area Network (VLAN) configurations on networking equipment. However, these approaches are costly and difficult.
 
  - Today, software-defined access technology simplifies segmentation by grouping and tagging network traffic. It then uses traffic tags to enforce segmentation policy directly on the network equipment, yet without the complexity of traditional approaches.
  
Source: Stackexchange
Image Source: include link to image source
<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 03 - Network Segmentation
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: 
  - Network Segmentation
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

### Network Segmentation with Cisco Packet Tracer

NOTE:

### Import OVA File


### Demo: Network Segmentation with Cisco Packet Tracer

