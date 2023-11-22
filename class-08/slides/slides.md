<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 08

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Network Access Controls
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

![Image](/ops-301-guide/curriculum/class-08/slides/assets/0_01.png)
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

&shy;<!-- .element style="color: red;" -->**Class 08** Network Access Controls

**Class 09** Traffic Mirroring

**Class 10** AWS VPC


</div>

<div>

![Image](/ops-301-guide/curriculum/class-08/slides/assets/0_02.png)
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

&shy;<!-- .element style="color: red;" -->**Class 08** Python Collections

**Class 09** Python Conditional Statements

**Class 10** Python File Handling


</div>

<div>

![Image](/ops-301-guide/curriculum/class-08/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Network Access Controls
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Network Access Controls
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 07


---

<!-- .element class="main-title" -->
# Review Concepts:

- Switches and Hubs
- Web Server Deployment

NOTE:

---

<!-- .element class="split-screen" -->


<div align="left" style="font-size: 25px">

<div style="font-size: 55px"> Switches and Hubs</div>

# Collision Domain:

- A network segment where data packets can collide with each other if two or more devices transmit data simultaneously
- A **Hub** has a single collision domain
  - All traffic will go to all ports
  - Not secure
  - Does not scale well ("Hot Mic" on a radio)
- Each physical port of a **Switch** is its own collision domain
  - Traffic only goes to the port with the destination device
  - Switches use a **MAC Table** to match the **MAC Address** of a device with the **Port ID** it is connected to


</div>

<div align="left" style="font-size: 25px">

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_01.png)
<!-- .element style="width: 120%"-->

<div style="font-size: small">Mattias.Campe, CC BY-SA 4.0</div>

<br>

# Broadcast Domain:

- A Broadcast Domain contains all devices which can reach each other at the data link layer
- All physical ports on **Hubs** and unmodified **Switches** share a single Broadcast Domain per device
- **Routers** can break up Broadcast Domains with Subnets, as can **VLAN capable switches**

</div>

NOTE:

- What is a switch?
  - OSI Layer 2 device that connect devices together on a LAN using ethernet
  - Splits collision domains
  - Here Host A is trying to send a packet to Host C
  - Hosts B and D don't receive the packet from Host A

- What is a collision domain?
  - Where packets go on a switch.
  - If all ports on a device share a collision domain, then all traffic will go to all ports. This is a hub.
  - If each port has its own collision domain, then traffic only goes to the destined port. This is a switch.
  - Ask: Which is better for security and why?
    - Switches are harder to sniff traffic because traffic is routed specifically to destination ports. One port doesn't see all traffic.


MAC Tables (MAC address : Port ID) are similar to ARP Tables (IP Address : MAC Address)

Image Source: Mattias.Campe, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ethernet-broadcast-collision.svg)



---

<!-- .element class="split-screen-with-title" -->


# Web Server Hosting

<div>

<div align="left" style="font-size: 25px">

### &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Where and How do we host a web server?**

- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Locally (device)**: as software or a VM running on your machine
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->Accessible by the host device, but may not be accessible even over the LAN.
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**On-Prem**: the server is maintained on-site on the company's network.
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="5" -->Web servers on company **Intranet** are hosted within the organization's private network, and used for internal purposes
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->Web servers serving the company **Extranet** are accessible remotely *but only to authorized external users* like customers, partners, or suppliers.
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="7" -->Web servers meant to be accessible to the public are hosted on the **Internet**



</div>

<div align="left" style="font-size: 28px">

![Image](/ops-301-guide/curriculum/class-08/slides/assets/07_06.drawio.png)
<!-- .element style="width: 120%"-->

- &shy;<!-- .element: class="fragment" data-fragment-index="8" -->**Cloud Hosted Services**: often externally accessible via a public IP
  - Examples: AWS, Azure, etc.
  - Could be IaaS, PaaS, SaaS

</div>

</div>

NOTE:
**Locally (Device):**
- Hosting a web server locally means running the web server software or a virtual machine (VM) on your own machine, such as your personal computer.
- It's primarily accessible by the host device itself, which is useful for development and testing purposes.
- However, web servers hosted this way may not be accessible over the local area network (LAN) or the internet without additional configuration.

**On-Premises (On-Prem):**
- On-premises web servers are maintained and hosted within a company's physical location or data center.
- These servers are part of the organization's private network and are typically used for internal purposes, such as hosting company intranet sites.
- In some cases, on-premises web servers can also serve the company's extranet, allowing authorized external users like customers, partners, or suppliers to access specific resources remotely.
- Web servers meant to be accessible to the public are hosted on the internet, often in data centers managed by hosting providers.
  - These servers are publicly accessible via public IP addresses and domain names.
  - They are used for hosting websites, web applications, and services that need to reach a global audience.

**Cloud Hosted Services:**
- Cloud hosting involves using third-party cloud service providers, such as AWS (Amazon Web Services) or Azure (Microsoft Azure), to host web servers and related infrastructure.
- These cloud-hosted services can be externally accessible via public IPs and domain names.
- Cloud hosting options include Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS), each offering different levels of management and control.

---

<!-- .element class="split-screen-with-title" -->


# Perimeter Network

<div>

<div align="left" style="font-size: 26px">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->Also called a **Screened Subnet** or a **Demilitarized Zone (DMZ)**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->Uses **firewall rules designed to permit traffic** to specific ports and devices that host **public services**, such as a web server
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->A **private LAN zone** typically contains remaining non-public devices

![Image](/ops-301-guide/curriculum/class-08/slides/assets/07_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Dgondim, CC BY-SA 4.0</div>

</div>

<div align="left" style="font-size: 26px">

> A **Perimeter Network** is a segregated network segment within an organization's infrastructure:

![Image](/ops-301-guide/curriculum/class-08/slides/assets/07_07.drawio.png)
<!-- .element style="width: 115%"-->

</div>

</div>

NOTE:
**Demilitarized Zone (DMZ):**
- A Demilitarized Zone, commonly referred to as a DMZ, is a network segment that acts as an intermediary zone between a trusted, private network (typically the internal LAN) and an untrusted, public network (usually the internet).
- The DMZ is also known as a "Screened Subnet" because it screens or filters network traffic between the private LAN and the public internet.
- The primary purpose of a DMZ is to enhance network security by isolating publicly accessible services (e.g., web servers, email servers) from the internal network. This isolation helps protect sensitive internal resources from direct exposure to external threats.

**Firewall Rules and Public Services:**
- In a DMZ, firewall rules are designed and implemented to permit or restrict traffic based on specific criteria, such as source and destination IP addresses, ports, and protocols.
- These rules are carefully configured to allow traffic to reach and interact with devices that host public services, such as a web server, email server, or DNS server, located within the DMZ.
- The firewall acts as a security barrier between the DMZ and the internal LAN, controlling which types of traffic are allowed to pass through and which are blocked. This ensures that only authorized and necessary traffic can access the services hosted in the DMZ.

**Private LAN Zone:**
- Alongside the DMZ, the private LAN zone is the trusted, internal network where an organization's non-public devices and resources reside.
- This private LAN zone typically contains devices like workstations, internal servers, databases, and other assets that are not intended to be directly accessible from the public internet.
- By separating the DMZ from the private LAN, an organization can maintain a clear security boundary, reducing the risk of unauthorized access to internal resources.

Image Source: Dgondim, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Traditional_Single_Layer_DMZ_with_two_flanking_firewalls.png)

Source:
- [ChatGPT](https://chat.openai.com/share/756e485f-368e-4d41-a275-857d1760d656)
- [Reddit](https://www.reddit.com/r/networking/comments/10903k/dmz_design_dual_or_threelegged/c6bfa7r/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

Old Note:
- What is a DMZ?
  - A demilitarized zone is a part of your network that is more open to the public using firewall rules designed to permit traffic to specific ports and devices in the DMZ that host public services, such as a web server

  - Different ways to create a DMZ
    - Two firewalls of different models
    - One firewall with the DMZ outside of it

> A word on obfuscation of ports; you can move your SSH or RDP ports to non-well-known port numbers, but any human attacker will find it with a port scanner. This may however help you avoid bot scanners. Obscurity is not security (hiding key under rug). "Security through obscurity" is a known fallacy.

---

<!-- .element class="main-title" -->

# Review:

## Lab 07

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Network Access Controls
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 07**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 08** - Python Collections

NOTE:

### Review: Ops Challenge 07

### Introduce: Ops Challenge 08 - Python Collections

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Network Access Controls
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 08 - Network Access Controls

NOTE:
- Network Access Control (NAC) is an important component of modern network security strategies.
- It serves as a gatekeeper, ensuring that only authorized users and devices gain access to a network while also enforcing security policies and compliance measures.
- Today, we will introduce the core concepts of NAC, its significance in safeguarding network resources, and the technologies and practices that underpin its effective implementation.

---

<!-- .element class="split-screen-with-title" -->


# Managing Network Access

<div>

<div align="left" style="font-size: 32px">

### Most large companies have diverse authentication needs:<!-- .element: class="fragment" data-fragment-index="1" -->

- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Manage network access** for:
  - Guests/contractors
  - BYOD
  - IOT
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Incident response**
- Third party software, devices, and services:<!-- .element: class="fragment" data-fragment-index="4" -->
  - Medical devices

</div>

<div align="left">

> How do we keep the right people/machines using the network in the right way?

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_03.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:
Most large companies have diverse authentication needs, encompassing various aspects of network access management.

They must:

**Manage network access for:**
  - **Guests/contractors:** Providing temporary access to visitors or external contractors while ensuring security.
  - **BYOD (Bring Your Own Device):** Facilitating secure connections for employees using personal devices.
  - **IoT (Internet of Things):** Controlling and monitoring access for a multitude of connected devices.

**Incident response:** Being prepared to swiftly adjust access permissions during security incidents or breaches to contain threats and mitigate risks.

**Third-party software, devices, and services:** Safely integrating and authorizing external systems, applications, or services, such as medical devices in healthcare settings, within the corporate network.

Image Source: [Pixabay.com](https://pixabay.com/illustrations/access-control-authentication-4294692/)

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

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_03.png)
<!-- .element style="width: 80%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:
**Authentication** is the process of uniquely identifying a user by verifying their identity through various means, such as passwords, biometrics, or smart cards. It serves as the initial gatekeeper for network access.

**Authorization** involves determining whether to grant or deny an individual user access to a computer network based on their authenticated identity. It defines what resources, services, or actions the user is allowed to access or perform.

**Accounting**, also known as auditing or logging, is the practice of recording and tracking user activities on a computer network. It provides a detailed record of who accessed the network, what they accessed, and when they accessed it, which is crucial for security monitoring, compliance, and troubleshooting purposes.

Image Source: [Pixabay.com](https://pixabay.com/illustrations/access-control-authentication-4294692/)

---

<!-- .element class="split-screen-with-title" -->


# Network Access Controls

<div>

<div align="left" style="font-size: 32px">

### Applications of Network Access Controls:<!-- .element: class="fragment" data-fragment-index="1" -->
- Policy lifecycle management<!-- .element: class="fragment" data-fragment-index="2" -->
- Profiling and visibility<!-- .element: class="fragment" data-fragment-index="3" -->
- Guest networking access<!-- .element: class="fragment" data-fragment-index="4" -->
- Security posture check<!-- .element: class="fragment" data-fragment-index="5" -->
- Incident response<!-- .element: class="fragment" data-fragment-index="6" -->
- Bidirectional integration<!-- .element: class="fragment" data-fragment-index="7" -->

</div>

<div align="left">

> **Network Access Controls**:
>
> Authentication systems that protect network access from unauthorized usage

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_03.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:
Applications of Network Access Controls encompass a wide range of functions:

**Policy lifecycle management** NAC systems assist in defining, implementing, and updating network access policies. They facilitate the entire lifecycle of access control rules, ensuring they align with security and compliance requirements.

**Profiling and visibility** NAC solutions provide visibility into devices and users accessing the network, profiling them based on characteristics like device type, operating system, and behavior. This insight aids in making informed access decisions.

**Guest networking access** NAC enables secure onboarding for guest users, allowing temporary and controlled access to network resources while maintaining separation from critical assets.

**Security posture check** NAC conducts assessments of connected devices to ensure they meet security and compliance standards. Non-compliant devices may be restricted or quarantined until remediation occurs.

**Incident response** NAC plays a crucial role in incident response by quickly adjusting access permissions when security incidents or breaches occur, limiting potential damage and containing threats.

**Bidirectional integration** NAC systems often integrate bidirectionally with other security solutions, such as firewalls, SIEM (Security Information and Event Management) systems, and endpoint security tools, to enhance network protection and incident response capabilities.

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

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_03.png)
<!-- .element style="width: 110%"-->

<div style="font-size: small">by Mohamed Hassan via Pixabay</div>

</div>

</div>

NOTE:
**ACL - Access Control List:** ACLs are used to control the flow of network traffic by specifying rules that permit or deny access to resources based on source or destination IP addresses, ports, or other criteria. They are commonly used in routers, switches, and firewalls to manage access to subnets or network segments.

**IAM - Identity Access Management:** IAM is a comprehensive policy and technology framework designed to streamline the management of electronic or digital identities within an organization. It encompasses user provisioning, access control, authentication, and authorization to ensure secure and efficient identity management.

**MFA - Multi-factor Authentication:** MFA enhances security by requiring users to provide multiple forms of authentication before granting access. This typically includes something the user knows (e.g., a password) and something the user has (e.g., a smartphone app or a hardware token).

**SSO - Single Sign-On:** SSO enables users to access multiple applications or services with a single set of credentials (usually a username and password). It simplifies user authentication by eliminating the need to remember multiple login credentials for various systems.

**Kerberos:** Kerberos is a network authentication protocol that provides strong authentication over potentially insecure networks. It uses secret-key cryptography to securely authenticate users and services, ensuring the confidentiality and integrity of communications. It's commonly used in Windows Active Directory environments for authentication.

Image Source: [Pixabay.com](https://pixabay.com/illustrations/access-control-authentication-4294692/)

---

<!-- .element class="main-title" -->
# RADIUS

NOTE:
- RADIUS (Remote Authentication Dial-In User Service) is a pivotal protocol in the realm of Network Access Controls (NAC).
- It serves as a central authentication, authorization, and accounting mechanism, enabling organizations to securely manage and regulate user access to network resources.
- Today, we will explore the core functions of RADIUS and its role in enforcing access policies, enhancing network security, and facilitating seamless authentication within diverse network environments.

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

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_02.png)
<!-- .element style="width: 110%"-->

<div style="font-size: small">Buyanzayad, CC BY-SA 4.0</div>

</div>

</div>

NOTE:
**RADIUS is a client/server protocol:** RADIUS operates as a client/server protocol where the Network Access Server (NAS) serves as the client, and the Authentication Server takes on the role of the server. It facilitates authentication, authorization, and accounting processes.
  - **Connected to the User Database:** RADIUS is closely tied to a User Database, which holds user credentials and information, allowing the Authentication Server to verify user identities during authentication.

**Runs in the Application Layer:** RADIUS functions within the Application Layer of the OSI model, providing a standardized framework for managing user access to network resources.

**Can use either TCP or UDP:** RADIUS is transport-agnostic and can operate over both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol), providing flexibility in network configurations.

**Ports:**
  - Port 1812 is reserved for Authentication purposes, enabling the exchange of authentication requests and responses.
  - Port 1813 is designated for Authorization activities, allowing the server to grant or deny access based on the received information.

**FreeRADIUS - open source RADIUS server software:** FreeRADIUS stands out as a prominent open-source RADIUS server software solution, offering organizations a cost-effective and customizable option for deploying RADIUS-based authentication and access control.

OLD NOTES:
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

<!-- .element class="split-screen-with-title" -->


# Key Features of RADIUS

<div>

<div align="left">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Centralized Authentication**:
  - &shy;<!-- .element: class="fragment" data-fragment-index="2" -->Simplifies user management in large network environments
  - &shy;<!-- .element: class="fragment" data-fragment-index="3" -->This makes RADIUS **easily scalable**
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Accounting**:
  - &shy;<!-- .element: class="fragment" data-fragment-index="5" -->Tracks and **logs user activities**
  - &shy;<!-- .element: class="fragment" data-fragment-index="6" -->Useful for **monitoring**, **billing**, and **security**
- &shy;<!-- .element: class="fragment" data-fragment-index="7" -->**Interoperability**:
  - &shy;<!-- .element: class="fragment" data-fragment-index="8" -->An **industry-standard** protocol
  - &shy;<!-- .element: class="fragment" data-fragment-index="9" -->Supported on many devices and software across various vendors

</div>

<div align="left" style="font-size: 26px">

> **Remote Authentication Dial-In User Service**:
>
> A network management protocol that facilitates AAA management for network users

![Image](/ops-301-guide/curriculum/class-08/slides/assets/08_02.png)
<!-- .element style="width: 110%"-->

<div style="font-size: small">Buyanzayad, CC BY-SA 4.0</div>

</div>

</div>

NOTE:
**Centralized Authentication**, a hallmark of RADIUS, offers significant advantages in large network environments by simplifying user management. This centralized approach makes RADIUS highly scalable, enabling organizations to efficiently accommodate a growing number of users and devices.

RADIUS's **Accounting** functionality plays a crucial role by meticulously tracking and logging user activities. This feature proves invaluable for activities such as network monitoring, billing, and security auditing.

Furthermore, RADIUS boasts remarkable **interoperability**, as it adheres to industry-standard protocols. This means it is supported across a wide range of devices and software from various vendors, fostering compatibility and flexibility in network access control implementations.

OLD NOTES:
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

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 08 - Network Access Controls
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Network Access Controls
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## RADIUS Athentication

NOTE:

### Demo: RADIUS Athentication

When you first create a group on pfSense, you have to save it, then re-enter its config in order to grant it privileges.
- You want to assign it "User - Services: Captive Portal login"

When testing, you may need to clear your browser cache!
