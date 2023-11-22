<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 09

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Traffic Mirroring
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

![Image](/ops-301-guide/curriculum/class-09/slides/assets/0_01.png)
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

&shy;<!-- .element style="color: red;" -->**Class 09** Traffic Mirroring

**Class 10** AWS VPC


</div>

<div>

![Image](/ops-301-guide/curriculum/class-09/slides/assets/0_02.png)
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

&shy;<!-- .element style="color: red;" -->**Class 09** Python Conditional Statements

**Class 10** Python File Handling


</div>

<div>

![Image](/ops-301-guide/curriculum/class-09/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>


---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Traffic Mirroring
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Traffic Mirroring
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 08


---

<!-- .element class="main-title" -->
# Review Concepts:

- Network Access Controls

NOTE:

---

<!-- .element class="split-screen-with-title" -->


# AAA Security

<div>

<div align="left" style="font-size: 34px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Authentication**:
- Uniquely identifying a user<!-- .element: class="fragment" data-fragment-index="1" -->

&shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Authorization**:
- Adding or denying individual user access to a computer network<!-- .element: class="fragment" data-fragment-index="2" -->

&shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Accounting**:
- Record-keeping and tracking of user activities on a computer network<!-- .element: class="fragment" data-fragment-index="3" -->

</div>

<div align="left">

> **Authentication**, **Authorization** and **Accounting** (**AAA**):
>
> A system for tracking user activities on an IP-based network and controlling their access to network resources

![Image](/ops-301-guide/curriculum/class-09/slides/assets/08_03.png)
<!-- .element style="width: 80%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:

Image Source: [Pixabay.com](https://pixabay.com/illustrations/access-control-authentication-4294692/)

---

<!-- .element class="split-screen-with-title" -->

# Network Access Controls

<div>

<div align="left">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**ACL** - Access Control List:
  - Control traffic in and out of one or more subnets
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**IAM** - Identity Access Management:
  - Policy and technology framework that facilitates the management of electronic or digital identities
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**MFA** - Multi-factor Authentication
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**SSO** - Single Sign-On
- &shy;<!-- .element: class="fragment" data-fragment-index="5" -->**Kerberos**:
  - Protocol for providing authentication over a non-secure network

</div>

<div align="left">

<br>

![Image](/ops-301-guide/curriculum/class-09/slides/assets/08_03.png)
<!-- .element style="width: 110%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:

Image Source: [Pixabay.com](https://pixabay.com/illustrations/access-control-authentication-4294692/)

---

<!-- .element class="split-screen-with-title" -->


# What is RADIUS?

<div>

<div align="left" style="font-size: 29px">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**RADIUS** is a **client/server protocol**
  - &shy;<!-- .element: class="fragment" data-fragment-index="2" -->The **Network Access Server (NAS)** is the **client**
  - &shy;<!-- .element: class="fragment" data-fragment-index="3" -->The **Authentication Server** is the **server**
	- Connected to the **User Database**
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->Runs in the **Application Layer**
- &shy;<!-- .element: class="fragment" data-fragment-index="5" -->Can use either **TCP** or **UDP**
- Ports:<!-- .element: class="fragment" data-fragment-index="6" -->
  - **1812** (Authentication)
  - **1813** (Authorization)
- &shy;<!-- .element: class="fragment" data-fragment-index="7" -->**FreeRADIUS** - open source RADIUS server software

</div>

<div align="left" style="font-size: 26px">

> **Remote Authentication Dial-In User Service**:
>
> A network management protocol that facilitates AAA management for network users

![Image](/ops-301-guide/curriculum/class-09/slides/assets/08_02.png)
<!-- .element style="width: 110%"-->

<div style="font-size: small">Buyanzayad, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

- What is RADIUS?
  - RADIUS (Remote Authentication Dial-In User Service) is a network management protocol facilitating AAA (Authentication, Authorization, and Accounting) management for network users. In this type of configuration, the **NAS (Network Access Server)** brokers authentication requests and acts as the network's gatekeeper.
  - Today we'll be using FreeRADIUS on pfSense
    - FreeRADIUS is an open source RADIUS server that we can deploy to pfSense in the form of a package
    	- *FreeRADIUS* authenticates over 1/3 of users on the internet
    	- Other RADIUS servers are *Cisco ACS* and *Microsoft IAS*

- What ports does RADIUS use?
  - Port 1812: Authentication
  - Port 1813: Authorization
  - Stick to using the default ports unless you have an explicit technical reason not to

- What is a captive portal?
  - When user intializes internet for first time, authentication page kicks in on their browser session
  - Similar to hotel wi-fi

- What might a RADIUS-integrated domain look like?

Image Source: Buyanzayad, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:RADIUS-Server.gif)

---

<!-- .element class="main-title" -->

# Review:

## Lab 08

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Traffic Mirroring
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 08**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 09** - Python Conditional Statements

NOTE:

### Review: Ops Challenge 08

### Introduce: Ops Challenge 09 - Python Conditional Statements

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Traffic Mirroring
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 09 - Traffic Mirroring

NOTE:
- Traffic mirroring, also known as packet mirroring, is a fundamental technique in modern network management and cybersecurity.
- It involves the duplication and redirection of network traffic to monitoring tools or devices, enabling organizations to gain insights into network performance, troubleshoot issues, and enhance security by analyzing the captured data.
- This essential process plays an important role in ensuring the integrity, efficiency, and security of today's complex computer networks.

---

<!-- .element class="split-screen-with-title" -->


# Traffic Mirroring

<div>

<div align="left">

- Also know as **Port Mirroring** or **Network Monitoring**
- Because data is being copied before it is examined, mirroring **does not disrupt or affect network traffic**
  - The behavior of traffic does not reveal that it has been mirrored
  - Impossible to tell without access to the network hardware
- Used by **Network Administrators** and **Security Professionals** for **analysis** and/or **monitoring**

</div>

<div align="left">

> **Traffic Mirroring**:
>
> The act of duplicating network traffic to a specific destination.

![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_04.drawio.png)
<!-- .element style="width: 120%"-->


</div>

</div>

NOTE:
- Also known as **Port Mirroring** or **Network Monitoring**, traffic mirroring allows for the monitoring and analysis of network traffic without impacting its normal flow.

- Because data is being copied before it is examined, mirroring **does not disrupt or affect network traffic** in any noticeable way. The behavior of mirrored traffic remains indistinguishable from regular network traffic, making it impossible to tell that mirroring is in progress without access to the network hardware.

- Used by **Network Administrators** and **Security Professionals** for **analysis** and/or **monitoring**, traffic mirroring serves as a vital tool for diagnosing network issues, optimizing network performance, and enhancing cybersecurity by detecting and responding to security threats.


OLD NOTES:
- What is traffic mirroring?
  - Traffic mirroring is the act of duplicating network traffic to a specific destination.
    - Think of it like "splitting coax" in highly conceptual terms
    - Also might be known as "tapping a line"
  - Draw the diagram for students to conceptually understand. Refer to the diagram at [How Traffic Mirroring Works](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html).
  - Include network adapters so students see that we are using dedicated sniffer interfaces.

Source: [ChatGPT](https://chat.openai.com/share/308eaae2-6b7b-4d67-8af0-985777bf7a67)

---

<!-- .element class="split-screen-with-title" -->


# Traffic Mirroring

<div>

<div align="left" style="font-size: 29px">

- **Traffic Mirroring** is usually done at **Layer 2** (on a **Switch**) by duplicating **Frames**
  - Layer 2 mirroring is ***simple*** and ***high-performance***, minimally effecting network performance
- However, **Layer 3** appliances like **Routers** are also capable of traffic mirroring
- **AWS** and other **Cloud Providers** implement their own mirroring methods
  - Non-cloud virtualized network systems may have mirroring tools as well

</div>

<div align="left">

> **Traffic Mirroring**:
>
> The act of duplicating network traffic to a specific destination.

![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_05.drawio.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:
- Traffic Mirroring is usually done at Layer 2 (on a Switch) by duplicating Frames, which allows for the capture of Ethernet frames without modifying the IP or TCP/UDP headers.
  - Layer 2 mirroring is simple and high-performance, minimally affecting network performance because it operates at the data link layer. It involves copying Ethernet frames directly from the source port to the destination port.

- However, Layer 3 appliances like Routers are also capable of traffic mirroring. In Layer 3 mirroring, packets are duplicated, allowing for the analysis of network traffic at the IP layer. This approach can be useful when more in-depth analysis of packet content is required.

- AWS and other Cloud Providers implement their own mirroring methods, enabling users to capture and analyze traffic within cloud-based environments. These cloud-native mirroring solutions are essential for monitoring and securing cloud resources.
  - Non-cloud virtualized network systems may have mirroring tools as well, providing virtual network administrators with the ability to capture and analyze traffic within virtualized environments, such as virtual machines (VMs) and containers. These tools are crucial for maintaining visibility and security in virtualized infrastructures.


OLD NOTES:
- Why monitor network traffic in the organization's cloud?
  - Threat detection with associated tools like IDS, DLP
  - Policy violation
  - Compliance
  - Logging
- Before IaaS providers matured their systems to provide native traffic mirroring, 3rd party solutions were bolted on (cumbersome).
  - Now, IaaS providers have native traffic mirroring:
    - [Azure Virtual Network TAP (vTAP)](https://www.extrahop.com/company/blog/2018/why-the-azure-virtual-network-tap-matters/)
    - AWS VPC Traffic Mirroring
  - Modern cloud capabilities save security teams a lot of tedious work in trying to observe network traffic in the cloud!

Source: [ChatGPT](https://chat.openai.com/share/308eaae2-6b7b-4d67-8af0-985777bf7a67)

---

<!-- .element class="split-screen-with-title" -->


# Traffic Mirroring

<div>

<div align="left" style="font-size: 32px">

- The physical port which mirrored traffic is directed to is called a **SPAN Port**
  - SPAN: **Switched Port Analyzer**

<br>

- **The mechanism of packet/frame duplication is often specific to the device model** or virtualization environment
  - On **pfSense**, a **Bridge** connects the LAN port with the SPAN port, emulating the internal functions of a **Switch**

</div>

<div align="left">

> **Traffic Mirroring**:
>
> The act of duplicating network traffic to a specific destination.

![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_06.drawio.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:
- The physical port to which mirrored traffic is directed is called a SPAN Port, which stands for **Switched Port Analyzer**. It is the designated destination port for duplicated network traffic.

- The mechanism of packet/frame duplication is often specific to the device model or virtualization environment. Different network devices and software platforms may implement traffic mirroring differently based on their capabilities and configurations.
  - On pfSense, a Bridge connects the LAN port with the SPAN port, emulating the internal functions of a Switch. This configuration allows traffic from the LAN interface to be mirrored to the SPAN port, where it can be captured and analyzed without disrupting the network flow.


OLD NOTES:
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

<!-- .element class="split-screen" -->

<div align="left">

# Traffic Mirroring

- On Jan 31, 2006, Electronic Frontier Foundation (EFF) filed class-action lawsuit against AT&T
  - Violation of law and customer privacy by collaborating with National Security Agency (NSA)
  - Wiretapped and data-mined US citizens in Room 641A of the AT&T building
  - US Supreme Court declined to hear the case

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_03.png)
<!-- .element style="width: 88%"-->

<div style="font-size: small" align="right">Roens, CC BY-SA 4.0</div>

| ![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_01.png)<!-- .element style="width: 200%"--> | ![Image](/ops-301-guide/curriculum/class-09/slides/assets/09_02.png)<!-- .element style="width: 100%"--> |
| - | - |



</div>

NOTE:
Hepting v. AT&T, also known as Hepting v. United States, was a significant legal case that revolved around the government's warrantless wiretapping program conducted by the National Security Agency (NSA) in the United States. The case raised important questions about privacy, surveillance, and the legality of government actions in the post-9/11 era. Here's a detailed explanation of the case:

**Background:**

1. **September 11, 2001, Attacks:** In the aftermath of the terrorist attacks on September 11, 2001, the U.S. government took various measures to enhance national security and prevent future attacks. One such measure was the authorization of secret surveillance programs aimed at monitoring electronic communications.

2. **Warrantless Wiretapping Program:** The NSA, under the Bush administration, initiated a program called the Terrorist Surveillance Program (TSP) shortly after 9/11. This program involved intercepting and monitoring international communications without obtaining warrants from the Foreign Intelligence Surveillance Court (FISC), as required by the Foreign Intelligence Surveillance Act (FISA).

**Facts of the Case:**

1. **Whistleblowers:** Mark Klein, a former AT&T technician, discovered that a secret room in an AT&T facility in San Francisco was used by the NSA for intercepting and collecting massive amounts of internet and telephone traffic. Klein believed that AT&T was collaborating with the NSA in conducting illegal surveillance on American citizens.

2. **Class Action Lawsuit:** In 2006, a class-action lawsuit was filed against AT&T by a group of individuals represented by the Electronic Frontier Foundation (EFF). The lead plaintiff in the case was Carolyn Jewel. The lawsuit alleged that AT&T had violated their privacy rights by participating in the NSA's warrantless wiretapping program.

**Legal Issues:**

1. **Fourth Amendment:** The central legal issue in Hepting v. AT&T was whether the warrantless wiretapping program violated the Fourth Amendment of the U.S. Constitution, which protects against unreasonable searches and seizures.

2. **State Secrets Privilege:** The government argued that the case should be dismissed based on the state secrets privilege, which allows the government to withhold evidence in court if its disclosure would harm national security.

**Court Proceedings:**

1. **District Court:** The case was initially dismissed by a federal district court in 2006. The court cited the state secrets privilege and the government's argument that national security would be compromised if the case proceeded.

2. **Ninth Circuit Court of Appeals:** The plaintiffs appealed the district court's decision. In 2007, the Ninth Circuit Court of Appeals ruled that the state secrets privilege did not warrant the dismissal of the case and sent it back to the district court for further review.

3. **Congressional Action:** During the course of the litigation, Congress passed the FISA Amendments Act of 2008, which provided retroactive immunity to telecommunications companies like AT&T that had participated in warrantless surveillance programs. This immunity provision posed a significant challenge to the plaintiffs' case.

4. **Settlement:** In 2009, after the FISA Amendments Act was enacted, the case was settled out of court. The terms of the settlement were not disclosed, and the case did not result in a definitive legal ruling on the constitutionality of the NSA's warrantless wiretapping program.

**Impact:**

Hepting v. AT&T raised important questions about the balance between national security and civil liberties in the context of modern surveillance technology. While the case did not result in a legal precedent, it contributed to public awareness of government surveillance programs and the ongoing debate over the scope of government surveillance and the protection of individual privacy.

Additionally, it highlighted the challenges of pursuing legal action against government surveillance programs when the government claims that national security concerns justify secrecy and immunity for the companies involved.

source: https://chat.openai.com/share/6844ea31-34d0-4f92-8ce6-7f260aaf9633

OLD NOTES:
- Discuss how this was being done by the NSA.
  - Ensure students understand the term "wiretapping."
  - Show the splitter diagram at [Wikipedia - Room 641a](https://en.wikipedia.org/w/index.php?title=File:SER_marcus_decl.djvu&page=17).
  - NSA used a splitter to copy the network traffic to NSA monitoring system. Compare it to a coaxial splitter for copper cable service; anyone ever used that at home?
    - Downside: signal degradation
  - Show what a [fiber optic tap](https://en.wikipedia.org/wiki/Room_641A#/media/File:Fiber_optic_tap.png) looks like.

Image Source: U.S. government, Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Seal_of_the_U.S._National_Security_Agency.svg)

Image Source: AT&T, Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AT%26T_logo_2016.svg)

Image Source: Roens, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Fiber_optic_tap.png)

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 09 - Traffic Mirroring
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Traffic Mirroring
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Traffic Mirroring

NOTE:

### Demo: Traffic Mirroring

LAN port can be changed to Promiscuous, I don't remember if that's necessary or not ~Ethan
