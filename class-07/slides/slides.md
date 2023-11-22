<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 07

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Web Server Deployment
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

![Image](/ops-301-guide/curriculum/class-07/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 2 - Network Infrastructure Design and Implementation

<div>

<div align="left" style="font-size: 40px">

**Class 06** Network Address Translation

&shy;<!-- .element style="color: red;" -->**Class 07** Web Server Deployment

**Class 08** Network Access Controls

**Class 09** Traffic Mirroring

**Class 10** AWS VPC


</div>

<div>

![Image](/ops-301-guide/curriculum/class-07/slides/assets/0_02.png)
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 2 Challenges: Python

<div>

<div align="left" style="font-size: 45.2px">


**Class 06** Bash in Python

&shy;<!-- .element style="color: red;" -->**Class 07** Directory Creation

**Class 08** Python Collections

**Class 09** Python Conditional Statements

**Class 10** Python File Handling


</div>

<div>

![Image](/ops-301-guide/curriculum/class-07/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Web Server Deployment
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Web Server Deployment
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 06


---

<!-- .element class="main-title" -->
# Review Concepts:

- Types of Networks
- NAT

NOTE:

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

![Image](/ops-301-guide/curriculum/class-07/slides/assets/06_01.drawio.png)
<!-- .element style="width: 75%"-->

</div>

</div>

NOTE:

---

<!-- .element class="split-screen-with-title" -->


# Geographical Networks Types:

<div>

<div align="left" style="font-size: 35px">

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Wide Area Network (WAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Radio Area Network (RAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="3" -->**Metropolitan Area Network (MAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="4" -->**Campus Area Network (CAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="5" -->**Local Area Network (LAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="6" -->**Personal Area Network (PAN)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="7" -->**Body Area Networks (BANs)**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="8" -->**Near-Me Network (NAN)**

</div>

<div align="center">

![Image](/ops-301-guide/curriculum/class-07/slides/assets/06_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small" align="left">Michel Bakni, CC BY-SA 4.0</div>

</div>

</div>

NOTE:

Image Source: Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Data_Networks_classification_by_spatial_scope.svg)

Network types include:

- VPN: Virtual Private Network
- WAN: Wide Area Network
- RAN: Radio Area Network
  - Connects mobile or remote devices to their core network
- MAN: Metropolitan Area Network
  - Example: Joining buildings together in San Francisco, Oakland, and San Jose via microwave transmission or fiber optic cabling.
- CAN: Campus Area Network
  - Join multiple adjacent LANs in a limited geographic area
- LAN: Local Area Network
- PAN: Personal Area Network
  - Example: Anything scoped to your room. Wireless PAN is Bluetooth. Wired PAN is USB.
- BAN: Body Area Networks
  - Example: Wearable devices like smartwatches, fitness bands, biometric RFID implants, and medical devices
- NAN: Near-Me Network
  - Networked devices not necessarily connected on the same LAN but are in close proximity

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

<!-- .element class="main-title" -->

# Review:

## Lab 06

NOTE:

Some problems people had:
- LAN and WAN had the same addressing scheme
- Both LANs had the same addressing scheme, but NAT was not applied to both sides
- Missing firewall rule
- Not turning your VPN off and on again
  - People can end up with multiple p2s on top of the same p1

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Web Server Deployment
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 06**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 07** - Directory Creation

NOTE:

### Review: Ops Challenge 06

### Introduce: Ops Challenge 07 - Directory Creation

This assignment introduces `os.walk()`, `for` loops because of `os.walk()`, introduces lists because of the looping, and of course functions and argument passing
- That's a lot of concepts in one thing

Show them:
- How to make a function
- How to pass arguments
- WHY to use functions and arguments
- How and why to use the structural template

Extra:
- Start showing them =None=, =False=, =0=, =""=, =[]=, etc.

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Web Server Deployment
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 07 - Web Server Deployment

NOTE:
- Web server deployment is the process of making web apps and websites accessible to users on the internet.
- It involves configuring servers, setting up security measures, and optimizing performance to ensure reliable delivery of web content.
- Successful web server deployment is important for organizations and developers looking to reach a global audience and deliver web services effectively.

---

<!-- .element class="split-screen-with-title" -->


# Web Server Deployment

<div>

<div align="left" style="font-size: 30px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->The primary Function of a web server is to handle **HTTP Methods**:
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**GET** - request a representation of the target
  - Typically used for retrieving web pages, images, etc.
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**POST**: submit an entity to the server
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**PUT**: replaces a file on the server with a new one
- &shy;<!-- .element: class="fragment" data-fragment-index="5" -->**DELETE**: request the webserver to destroy something


</div>

<div align="left">

> **Web Server**:
>
> An application or device that hosts and delivers web content (web pages, images, videos, web applications) to networked clients.

<br>

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_05.drawio.png)
<!-- .element style="width: 110%"-->

</div>

</div>

NOTE:
HTTP methods, also known as HTTP request methods, are part of the Hypertext Transfer Protocol (HTTP), which is the foundation of data communication on the World Wide Web. These methods define the actions that a client (typically a web browser) can request from a web server. Each HTTP method specifies a particular operation to be performed on a resource identified by a URL.

**GET**
- The GET method is primarily used for retrieving resources from the web server.
- It is the most commonly used method and is employed when you want to request a representation of a resource (e.g., a web page, an image, a document) from the server.
- GET requests are typically read-only operations, meaning they should not have any side effects on the server or the resource being retrieved.
- This method is ideal for browsing websites and fetching data without causing any modifications or updates.

**POST**
- The POST method is used to submit data to the web server for processing.
- It is commonly employed for actions such as form submissions, where user input is sent to the server for further processing, like submitting a contact form or creating a new record in a database.
- Unlike GET, POST requests can have side effects on the server, as they often lead to data being created, modified, or stored.

**PUT**
- The PUT method is utilized to replace or update a resource on the web server with a new representation.
- It is less commonly used in web applications compared to GET and POST.
- When a client sends a PUT request, it typically includes the updated representation of the resource. The server then replaces the existing resource with the provided data.
- PUT requests are idempotent, meaning sending the same request multiple times will have the same result as sending it once.

**DELETE**
- The DELETE method is used to request the removal or deletion of a resource on the web server.
- It allows clients to instruct the server to delete the specified resource.
- Like PUT, DELETE requests are also idempotent, meaning multiple requests to delete the same resource will not have any additional effect beyond the first request.
- DELETE requests should be used with caution, as they permanently remove data from the server.

OLD NOTES:
- What ports need opened and forwarded to the web server?
  - 80 HTTP
  - 443 HTTPS
  - Any port you will use to remotely administer the web server
    - SSH 22
    - RDP 3389

Common Web Server ports and protocols:
- **443 HTTPS**: uses SSL/certificates
  - **80 HTTP: unsecured,** and should never be avoided in most cases
- **22 SSH**: if needed for remote administration

**A word on obfuscation of ports**:
- You can move your SSH or RDP ports to a random unused port, but any sophisticated or persistent attacker will find it with a port scanner
  - Remember Nmap??
- ***Obscurity is not security*** (hiding key under rug). "Security through obscurity" is a known fallacy.

- "Nginx (pronounced as “Engine-X”) is an open source web server that is often used as reverse proxy or HTTP cache. It is available for Linux for free." -Canonical

Image Source: Virtualmv, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2013vmvClientServer.png)

Source: [ChatGPT](https://chat.openai.com/share/756e485f-368e-4d41-a275-857d1760d656)

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

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_06.drawio.png)
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

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_02.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Dgondim, CC BY-SA 4.0</div>

</div>

<div align="left" style="font-size: 26px">

> A **Perimeter Network** is a segregated network segment within an organization's infrastructure:

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_07.drawio.png)
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

<!-- .element class="split-screen-with-title" -->


# Further Security Considerations

<div>

<div align="left" style="font-size: 35px">

Security issues to consider when deploying a web server:<!-- .element: class="fragment" data-fragment-index="1" -->
- DDoS mitigation<!-- .element: class="fragment" data-fragment-index="2" -->
- Secure configuration<!-- .element: class="fragment" data-fragment-index="3" -->
- SSL certificate<!-- .element: class="fragment" data-fragment-index="4" -->
- Vulnerabilities<!-- .element: class="fragment" data-fragment-index="5" -->
- Connections to private systems (database)<!-- .element: class="fragment" data-fragment-index="6" -->
- Network design<!-- .element: class="fragment" data-fragment-index="7" -->

</div>

<div align="left">

<br>

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_04.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:
**DDoS Mitigation**:
  - Distributed Denial of Service (DDoS) attacks are malicious attempts to overwhelm a web server with a flood of traffic, rendering it inaccessible to legitimate users.
  - DDoS mitigation strategies involve implementing measures to detect, block, or absorb the attack traffic, ensuring the web server remains available and responsive.

**Secure Configuration**:
  - Ensuring the web server is securely configured is crucial. This includes hardening the server's operating system, web server software, and other components.
  - Secure configuration practices involve disabling unnecessary services, limiting access privileges, and regularly patching and updating software to mitigate known vulnerabilities.

**SSL Certificate**:
  - Secure Sockets Layer (SSL) certificates, now known as Transport Layer Security (TLS) certificates, are essential for encrypting data in transit between the client and the server.
  - Deploying an SSL/TLS certificate ensures secure and encrypted communication, safeguarding sensitive data, such as login credentials and payment information.

**Vulnerabilities**:
  - Web servers can be susceptible to various vulnerabilities, including software bugs, misconfigurations, and zero-day vulnerabilities.
  - Continuous vulnerability assessment, patch management, and security testing are essential to identify and remediate vulnerabilities promptly.

**Connections to Private Systems (Database)**:
  - Web servers often connect to private systems, such as databases, to retrieve or store data. Securing these connections is crucial.
  - Best practices include implementing strong authentication, access controls, encryption for database connections, and regularly auditing and monitoring database access.

**Network Design**:
  - Proper network design is essential for web server security. Considerations include network segmentation, firewall rules, and access control lists.
  - Network design should isolate the web server from sensitive internal systems and apply security measures to control inbound and outbound traffic.

Image Source: Virtualmv, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2013vmvClientServer.png)

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 07 - Web Server Deployment
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Web Server Deployment
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Web Services with

![Image](/ops-301-guide/curriculum/class-07/slides/assets/07_01.png)
<!-- .element style="width: 150%"-->

NOTE:

### Demo: Web Services with Nginx

Start with a fresh pfSense!

You can just make a clone of your devbox!

May need to restart NGINX for step 5 -- =sudo systemctl restart nginx=
