<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 06

NOTE:

Upcoming Career Assignments!
- Today! -- Behavioral Qs and Mock Interviews!
- Wednesday -- Another pitch video based assignment

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Network Address Translation
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

![Image](/ops-301-guide/curriculum/class-06/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 2 - Network Infrastructure Design and Implementation

<div>

<div align="left" style="font-size: 40px">

&shy;<!-- .element style="color: red;" -->**Class 06** Network Address Translation

**Class 07** Web Server Deployment

**Class 08** Network Access Controls

**Class 09** Traffic Mirroring

**Class 10** AWS VPC


</div>

<div>

![Image](/ops-301-guide/curriculum/class-06/slides/assets/0_02.png) 
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 2 Challenges: Python

<div>

<div align="left" style="font-size: 45.2px">


&shy;<!-- .element style="color: red;" -->**Class 06** Bash in Python

**Class 07** Directory Creation

**Class 08** Python Collections

**Class 09** Python Conditional Statements

**Class 10** Python File Handling


</div>

<div>

![Image](/ops-301-guide/curriculum/class-06/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Network Address Translation
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Network Address Translation
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 05


---

<!-- .element class="main-title" -->
# Review: 

- Virtual Private Networking
- Internet Protocol Security

NOTE:


---

<!-- .element class="split-screen-with-title" -->

# Virtual Private Networking

<div>

<div align="left" style="font-size: 35px">

- Use encryption to maintain confidentiality of data in motion<!-- .element: class="fragment" data-fragment-index="1" -->
- VPN use cases:<!-- .element: class="fragment" data-fragment-index="2" -->
  - Intersite connectivity<!-- .element: class="fragment" data-fragment-index="3" -->
  - Securely access a private cloud<!-- .element: class="fragment" data-fragment-index="4" -->
  - Confidentiality of data in motion<!-- .element: class="fragment" data-fragment-index="5" -->
  - Defensive security<!-- .element: class="fragment" data-fragment-index="6" -->
  - Offensive security<!-- .element: class="fragment" data-fragment-index="7" -->

</div>

<div align="left">

> **Virtual Private Network (VPN)**:
>
> A private network that is built over public infrastructure.

![Image](/ops-301-guide/curriculum/class-06/slides/assets/05_01.png
)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Michel Bakni, CC BY-SA 4.0</div>

<div>

<div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:VPN_overview-en.svg)

Intersite connectivity
- Securely access a private cloud
Confidentiality
- Confidentiality is one part of the CIA Triad. 
- The CIA Triad consists of Confidentiality, Integrity, and Availability of information. 
- Most information security processes facilitate one of these three pillars of the Triad.
Defensive security 
- Extending your private network geographically
Offensive security
- Evading detection
  - A VPN can be used aggressively to evade IDS/IPS detection by scrambling the traffic you're sending into the victim network.
 
David's Story: For one organization I worked for, we needed access to an AWS private cloud which hosted a critical piece of software used by many parts of the company. In order to establish secure access, we deployed a site-to-site VPN tunnel from our router to AWS. To forbid unauthorized access to the system, it was possible to restrict the AWS cloud server to users of the VPN tunnel. VPN tunnel was connected to the on-site router. Therefore, for an employee to work from home, they'd need to VPN into the on-site VPN server first. From there, they could hop over to AWS. What always amazed me is how many options there are in configuring a VPN. It felt overwhelming the first time! Once I understood encryption better, it made more sense why VPN tunnels always had a speed bottleneck to them.
 
Key takeaways:
 
- VPN Tunnels have LOTS of options, don't be intimidated by the complexity
- VPN Tunnels are great for establishing secure site-to-site communications
- VPN Tunnels can be a bottleneck, because each end must encrypt or decrypt traffic

---

<!-- .element class="split-screen-with-title" -->

# Virtual Private Networking

<div>

<div align="left" style="font-size: 36px">

- What traffic gets encrypted?<!-- .element: class="fragment" data-fragment-index="1" -->
  - Traffic in the tunnel between VPN client and VPN server gets encrypted<!-- .element: class="fragment" data-fragment-index="2" -->
  - Traffic extending beyond the VPN server (a “proxy”) does not get encrypted<!-- .element: class="fragment" data-fragment-index="3" -->
- MITM (man in the middle) attack would succeed against the latter, not the former<!-- .element: class="fragment" data-fragment-index="4" -->

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/05_02.drawio.png
)
<!-- .element style="width: 120%"-->

<div>

</div>

NOTE:

Do VPN services actually conceal my activities?
- Who do you trust more, your ISP or the VPN provider?
- Activities over VPN can still be traced by a determined investigator with adequate time/resources, especially if they can subpoena the VPN provider for data, like activity logs. VPN servers are ultimately proxies, and proxies can still point back to their originating IPs. 

---

<!-- .element class="split-screen-with-title" -->

# Internet Protocol Security (IPsec)

<div>

<div align="left">

IPsec consists of two key protocols:<!-- .element: class="fragment" data-fragment-index="1" -->&shy;<!-- .element: class="fragment" data-fragment-index="1" -->&shy;<!-- .element: class="fragment" data-fragment-index="1" -->&shy;<!-- .element: class="fragment" data-fragment-index="1" -->
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->**Authentication Header (AH)**: provides authenticity and integrity
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->**Encapsulating Security Payload (ESP)**: provides confidentiality in addition to authenticity and integrity

&shy;<!-- .element: class="fragment" data-fragment-index="4" -->Both **AH** and **ESP** can operate in either of two modes:
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="5" -->**Tunnel Mode**: used in *Client-to-Site* VPN connections (Remote Access VPN)
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->**Transport Mode**: used in *Site-to-Site* VPN connections

</div>

<div align="left">

> **Internet Protocol Security (IPsec)** encrypts the original payload and wraps it in a new header before transmission, ensuring **Confidentiality**, **Integrity**, and **Authenticity**.

![Image](/ops-301-guide/curriculum/class-06/slides/assets/05_05.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Cybjit, CC BY-SA 3.0</div>

<div>

<div>

NOTE:

Image Source: Cybjit, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:IP_in_IP_Encapsulation.svg)

Do VPN services actually conceal my activities?
- Who do you trust more, your ISP or the VPN provider?
- Activities over VPN can still be traced by a determined investigator with adequate time/resources, especially if they can subpoena the VPN provider for data, like activity logs. VPN servers are ultimately proxies, and proxies can still point back to their originating IPs. 

---

<!-- .element class="split-screen-with-title" -->

# Authentication Header (AH):

<div>

<div align="left" style="font-size: 25px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Purpose and Functionality:**
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->Establishes **Authentication** and **Integrity** for IP packets
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->*Does not* provide **Confidentiality** (encryption)
  - Packet contents are visible in plaintext

&shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Header Placement:**
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="5" -->Primarily used in Transport Mode: AH header inserted *before* the IP header
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->Assures **Authenticity** and **Integrity** for the entire IP packet, including the IP header

&shy;<!-- .element: class="fragment" data-fragment-index="7" -->**Use Case:**
- Encryption is not required<!-- .element: class="fragment" data-fragment-index="8" -->
- AH has greater interoperability and lower overhead than ESP<!-- .element: class="fragment" data-fragment-index="8" -->

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/05_04.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Mpk1024, CC BY-SA 4.0</div>

<div>

<div>

NOTE:

Image Source: Mpk1024, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ipsec-esp-tunnel-and-transport.svg)

Source: [ChatGPT](https://chat.openai.com/share/99d5945e-ab53-4409-af45-2bd66f065ed9)


---

<!-- .element class="split-screen-with-title" -->

# Encapsulating Security Payload (ESP):

<div>

<div align="left" style="font-size: 23px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Purpose and Functionality:**
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->ESP offers **Confidentiality** (encryption) services for IP packets by encrypting the payload
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->*ESP can also provide* **Authentication** and **Integrity** protection, similar to AH

&shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Header Placement:**
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="5" -->**Transport Mode**: encrypts and authenticates the payload (the data) of the IP packet while leaving the IP header untouched.
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->**Tunnel Mode**: encapsulates the entire original IP packet (header + payload) inside a new IP packet with its own header

&shy;<!-- .element: class="fragment" data-fragment-index="7" -->**Use Cases:**
- ESP is used when both data confidentiality and data integrity/authentication are crucial<!-- .element: class="fragment" data-fragment-index="7" -->
  - Such as with a VPN tunnel


</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/05_03.png)
<!-- .element style="width: 120%"-->

<div style="font-size: small">Mpk1024, CC BY-SA 4.0</div>

<div>

<div>

NOTE:

Image Source: Mpk1024, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ipsec-esp-tunnel-and-transport.svg)

Source: [ChatGPT](https://chat.openai.com/share/99d5945e-ab53-4409-af45-2bd66f065ed9)

---

<!-- .element class="main-title" -->

# Review:

## Lab 05

NOTE:

Make note of students to didn't get their VPN working -- they need it in order to start lab06.

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture: 
  - Network Address Translation
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 05**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 06** - System Commands in Python

NOTE:

### Review: Ops Challenge 05

### Introduce: Ops Challenge 06 - System Commands in Python

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Network Address Translation
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 06 - Network Address Translation

- Types of Networks
- Addressing: IPv4 vs. IPv6
- NAT (Network Address Translation)


NOTE:
Is there a relevant Ch. in the Wiley Network+ (N10-008) Study Guide?

---

<!-- .element class="main-title" -->
# Types of Networks


---

<!-- .element class="split-screen-with-title" -->


# Access Models

<div>

<div align="left" style="font-size: 28px">

&shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->**Open Access**:
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->On the **Internet**, network resources available to the general public at large via ISP

&shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->**Controlled Access**:
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->An **Extranet** consists of controlled private network resources only made available by hosting company to its partners, vendors/suppliers, or set of customers

&shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="1" -->**Closed Access**: 
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="1" -->In an **Intranet** network resources are available only to internal employees

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_01.drawio.png)
<!-- .element style="width: 75%"-->

</div>

</div>

NOTE:

---

<!-- .element class="split-screen-with-title" -->


# Geographical Networks Types:

<div>

<div align="left">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->The **Internet** is a type of **Wide Area Network (WAN)** that spans across the entire earth 
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Radio Area Network (RAN)** resides between a device such as a mobile phone, a computer, or any remotely controlled machine and provides connection with its core network
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->A **Metropolitan Area Network (MAN)** spans across several LANS over a city or metropolitan area

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small" align="left">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Data_Networks_classification_by_spatial_scope.svg)

Network types include:
- LAN: Local Area Network
- VPN: Virtual Private Network
- WAN: Wide Area Network
- MAN: Metropolitan Area Network
  - Example: Joining buildings together in San Francisco, Oakland, and San Jose via microwave transmission or fiber optic cabling.
- CAN: Campus Area Network
  - Join multiple adjacent LANs in a limited geographic area
- PAN: Personal Area Network
  - Example: Anything scoped to your room. Wireless PAN is Bluetooth. Wired PAN is USB.

---

<!-- .element class="split-screen-with-title" -->


# Geographical Networks Types:

<div>

<div align="left">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->A network infrastructure covering the school, university, or a corporate premises can be classified as a **Campus Area Network (CAN)**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Local Area Network (LAN)** is the home or workplace network we're all familiar with
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**A Personal Area Network (PAN)** is intended for personal use within a range of under ten meters with usually wireless devices

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small" align="left">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Data_Networks_classification_by_spatial_scope.svg)

Network types include:
- LAN: Local Area Network
- VPN: Virtual Private Network
- WAN: Wide Area Network
- MAN: Metropolitan Area Network
  - Example: Joining buildings together in San Francisco, Oakland, and San Jose via microwave transmission or fiber optic cabling.
- CAN: Campus Area Network
  - Join multiple adjacent LANs in a limited geographic area
- PAN: Personal Area Network
  - Example: Anything scoped to your room. Wireless PAN is Bluetooth. Wired PAN is USB.

---

<!-- .element class="split-screen-with-title" -->


# Geographical Networks Types

<div>

<div align="left">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Body Area Networks (BANs)** include a body area of wearable devices like smartwatches, fitness bands, biometric RFID implants, and medical devices placed inside the body like pacemakers
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Near-Me Network (NAN)** encompasses networked devices not necessarily connected on the same LAN but are in close proximity, e.g. two friends on Twitter in the same living room.

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small" align="left">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Data_Networks_classification_by_spatial_scope.svg)

Network types include:
- LAN: Local Area Network
- VPN: Virtual Private Network
- WAN: Wide Area Network
- MAN: Metropolitan Area Network
  - Example: Joining buildings together in San Francisco, Oakland, and San Jose via microwave transmission or fiber optic cabling.
- CAN: Campus Area Network
  - Join multiple adjacent LANs in a limited geographic area
- PAN: Personal Area Network
  - Example: Anything scoped to your room. Wireless PAN is Bluetooth. Wired PAN is USB.

---

<!-- .element class="main-title" -->
# Addressing: 
# IPv4 vs. IPv6

---

<!-- .element class="split-screen-with-title" -->


# IPv4 vs. IPv6

<div>

<div align="left" style="font-size: 27.8px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Address Exhaustion**:
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**IPv4** has a **large but exhaustible** number of addresses
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->Not enough addresses for every device
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="4" -->Addresses must be reused and masked
- &shy;<!-- .element: class="fragment" data-fragment-index="5" -->**IPv6** has a sufficiently large name-space that **we will never run out**
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->Every device can have a unique address
- &shy;<!-- .element: class="fragment" data-fragment-index="7" -->**Subnetting** and **Network Address Translation** are also attempts to address the limited number of available IPv4 addresses

</div>

<div align="left" style="font-size: 27px">

> **Internet Protocol version 4 (IPv4)** and **Internet Protocol version 6 (IPv6)** are two different addressing schemes used to identify and route data packets in computer networks

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_06.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Tmthetom, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Tmthetom, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:IPv4-vs-IPv6-graphic.png)

Source: [ChatGPT](https://chat.openai.com/share/009ac8af-5bf0-4975-bd48-52995114fbae)

---

<!-- .element class="split-screen-with-title" -->


# IPv4 vs. IPv6

<div>

<div align="left" style="font-size: 27px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->In addition to an increased address-space, **IPv6 offers several improvements of IPv4**:
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Better support** for end-to-end connectivity
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Simplified** network management
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Built-in security features**
  - &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="5" -->Fully **integrated with IPsec** from the start (natively supports AH and ESP)
  - Improved Routing Security<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="6" -->
  - Simplified NAT<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="7" -->
- &shy;<!-- .element: class="fragment" data-fragment-index="8" -->**Support** for **mobile networks** and **auto-configuration of devices**
- &shy;<!-- .element: class="fragment" data-fragment-index="9" -->**However**: IPv6 and IPv4 operate at the **same speed**

</div>

<div align="left" style="font-size: 27px">

> **Internet Protocol version 4 (IPv4)** and **Internet Protocol version 6 (IPv6)** are two different addressing schemes used to identify and route data packets in computer networks

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_06.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Tmthetom, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Tmthetom, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:IPv4-vs-IPv6-graphic.png)

Source: [ChatGPT](https://chat.openai.com/share/009ac8af-5bf0-4975-bd48-52995114fbae)


---

<!-- .element class="main-title" -->
# Network Address Translation

---

<!-- .element class="split-screen-with-title" -->

# Network Address Translation

<div>

<div align="left">

- **Network address translation (NAT)** is a performed by routers (Layer 3) so that the destination interprets the packet as coming from the translated IP instead of the actual originating IP.
- This allows us to **re-use the same address-spaces** (**192.168.x.x** and **10.x.x.x**, for example) over and over without creating address conflicts.
- **NAT** has played a vital role globally in delaying **IPv4 address exhaustion**, reducing the need to transition at a large scale to IPv6.

</div>

<div align="left" style="font-size: 25px">

> **Network address translation (NAT)**:
>
> Altering the IP address in a packet header in transit so that the destination interprets the packet as coming from the new IP instead of the actual originating IP.

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_03.png)
<!-- .element style="width: 120%"-->

<div style="font-size: small">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:NAT_Concept-en.svg)

- What is NAT?
  - NAT (Network address translation) is a technique performed by routers whereby the IP address in a packet header is altered in transit so that the destination interprets the packet as coming from the new IP instead of the actual originating IP. NAT has played a vital role globally in delaying, greatly reducing the need to transition at a large scale to IPv6.

---

<!-- .element class="split-screen-with-title" -->


# Types of Network Address Translation

<div>

<div align="left" style="font-size: 24px">

- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="1" -->**One-to-One**: When one address gets translated to one new address
  - This method obscures addresses, but does not conserve the address-space
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="2" -->**One-to-Many**: Entire networks can be hidden behind a single public-facing IP address
  - This is what delayed IPv4 address exhaustion
  - Takes place on our home routers
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->**NAT traversal**: When two endpoints use different NATs
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="4" -->**Double NAT**: When a network's router is behind another router, each of which is performing NAT.
  - The IP gets translated twice instead of just once
  - Can cause problems with VPNs and other protocols

</div>

<div align="left" style="font-size: 25px">

> **Network address translation (NAT)**:
>
> Altering the IP address in a packet header in transit so that the destination interprets the packet as coming from the new IP instead of the actual originating IP.

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_03.png)
<!-- .element style="width: 120%"-->

<div style="font-size: small">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:NAT_Concept-en.svg)

Source: [ChatGPT](https://chat.openai.com/share/fea7f1c2-6ab3-458a-983b-c56c9a45eb82)

### How One-to-Many NAT

A router uses a combination of the source IP address, source port, destination IP address, and destination port to determine which host on the internal network incoming traffic should be routed to.

Also known as Port Address Translation (PAT) or Network Address Port Translation (NAPT)

Here's how it works:

1. **Outgoing Traffic Translation**: When an internal device sends a packet to an external destination, **the router translates** the **source IP** address ***and*** the **source port** of the internal device to its own public IP address **and assigns it a unique source port number**.
  - This mapping is stored in a **NAT translation table**, which keeps track of which internal device made the request and which external port was assigned.

2. **Incoming Traffic Routing**: When a response packet or incoming traffic arrives at the router's public IP address, **the router checks the destination IP address and destination port against the NAT translation table**.
  - Once the correct internal device is identified, the router forwards the incoming traffic to that internal device using the private IP address and port number it originally used when making the outgoing request.

3. **Tracking Connections**: The NAT translation table keeps track of the translations for established connections, and entries in the table typically have a timeout mechanism. 
  - When the connection is no longer active or times out, the translation entry is removed from the table to free up resources.

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 06 - Network Address Translation
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: 
  - Network Address Translation
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Sharing and Accessibility

NOTE:

### Import OVA File


### Demo: Sharing and Accessibility

---

<!-- .element class="split-screen-with-title" -->

# Lab Topology

<div>

<div align="left" style="font-size: 32px">

### &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**NAT 1:1 (One-to-One):**

- Maps every IP address in one network to another subnet of same size:<!-- .element: class="fragment" data-fragment-index="2" -->
  - All outgoing traffic will have its origin address translated to the external IP<!-- .element: class="fragment" data-fragment-index="3" -->
  - All incoming traffic will have the destination address translated to the internal IP<!-- .element: class="fragment" data-fragment-index="4" -->



</div>

<div align="left" style="font-size: 26px">


![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_04.drawio.png)
<!-- .element style="width: 120%"-->

<br>


|          | Internal IP           |    | External IP           |
| -------- | --------------------  | -- | --------------------- |
| Network: | **`192.168.10.0/24`** | <> | **`192.168.30.0/24`** |
| Host:    | **`192.168.10.5`**    | <> | **`192.168.30.5`**    |
<!-- .element: class="fragment" data-fragment-index="5" -->

</div>

</div>

NOTE:

Part 1:
- Share a directory path without spaces! It makes your life easier.
- If you need to test if you can ping across the VPN, then be very confident that your win10 box is configured to respond to pings (it is not by default), or just use a linux machine (kali or an ubuntu server)
  - (Turning the win10 firewall completely off should do the trick)
- If you cloned your win10 machine, or imported from the save OVA, you may need to change the computer's name.

Part 2:
- pfSense has 1:1 NAT built into IPsec VPN:
  - VPN / IPsec / Tunnels / Edit Phase 2: Networks:
    - Local Network: LAN subnet (no change)
    - NAT/BINAT Translation:
      - Network: network address this router is using to perform NAT
    - Remote Network:
      - Network: network address this router expects to see on the other side (should reflect the other router's NAT)
  - [OPNSense resource](https://docs.opnsense.org/manual/how-tos/ipsec-s2s-binat.html) (most helpful to me)
  - [pfSense docs example](https://docs.netgate.com/pfsense/en/latest/vpn/ipsec/phase-2-nat.html)
  - [Another resource](https://www.provya.com/blog/pfsense-site-to-site-ipsec-vpn-with-overlapping-subnets/)

At this point, consider mucking around:
- Show them both translation of one side only, and mutual translation

---

<!-- .element class="split-screen-with-title" -->

# Lab Topology

<div>

<div align="left" style="font-size: 32px">

### &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**NAT 1:1 (One-to-One):**

-  &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**IPsec** has a built-in feature for doing 1:1 NAT
-  &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Binat** stands for **Bidirectional NAT**

<br><br>

 &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Don't forget!**
- You will also need to tell the remote router what network addressing it should expect to see, now that we've implemented this NAT/BINAT translation! <!-- .element: class="fragment" data-fragment-index="5" -->

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-06/slides/assets/06_05.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

Image Source: include link to image source

- What kind of NAT are we using today?
  - We'll need to apply our settings over the IPsec tunnel.

---

<!-- .element class="main-title" -->
# Wrap Up


NOTE:
- Review today's assignments in Canvas
  - SAY: This week I'll be meeting with you 1:1, please submit that assignment in advance of our meeting.
    - Student-instructor 1:1
- Deliver any helpful reminders regarding due dates
- Any last questions before we end lecture time?
- Good luck on labs!
 
