<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 12

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Domain Controller
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

![Image](/ops-301-guide/curriculum/class-12/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 3 - Server Administration, Active Directory, and User Management

<div>

<div align="left" style="font-size: 40px">

**Class 11** Windows Server

&shy;<!-- .element style="color: red;" -->**Class 12** Domain Controller

**Class 13** Active Directory

**Class 14** Group Policy

**Class 15** N/A: Project Kickoff


</div>

<div>

![Image](/ops-301-guide/curriculum/class-12/slides/assets/0_02.png) 
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 3 Challenges: Python + PowerShell

<div>

<div align="left" style="font-size: 50px">


**Class 11** Psutil

&shy;<!-- .element style="color: red;" -->**Class 12** Python Requests Library

**Class 13** Powershell AD Automation

**Class 14** Python Malware Analysis

**Class 15** N/A


</div>

<div>

![Image](/ops-301-guide/curriculum/class-12/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Domain Controller
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Domain Controller
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 11


---

<!-- .element class="image-with-title" -->
# IT Project Management

![Image](/ops-301-guide/curriculum/class-12/slides/assets/11_09.png)

NOTE:

### Why

- Why do we care about project management in an Ops class?
  - These ideas may help your team stay organized as you enter project week
  - If you're looking at any kind of systems administration role, you should consider picking up qualifications and experience 
    related to project management. This can be a competitive edge in the job hunt!
 
### What


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
 
### How

- CompTIA Project+
- Agile-related credentials and experience
- PMP (advanced, experienced PMs only)

Source: DevTeam.space

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


![Image](/ops-301-guide/curriculum/class-12/slides/assets/11_12d.png)
<!-- .element style="width: 85%"-->


</div>

</div>

NOTE:

 What infrastructure designs are scalable and centrally administered?

### Workgroup vs Domain
- A workgroup is decentralized and does not answer to a singular authority
  - This style of network is P2P (peer-to-peer)
  - This is the default configuration of a Windows 10 PC out of box
  - Quick and easy to deploy, but configurations between computers will vary greatly
- A domain is a network of computers that all answer to a singular authority
  - A domain style network is a form of client-server architecture
  - To be joined to a domain, a Windows 10 PC must not be Home edition; typically, Pro is recommended
  - More work to setup and deploy, but configurations will be consistent across computers
  - Domain is recommended for most businesses more than a handful of computers
  - Support for centralized management of user profiles and computer configurations
  - Disadvantage: Single point of failure from a security perspective. Discuss why.

---

<!-- .element class="split-screen-with-title" -->


# RAID
Increase data redundancy and/or improve performance

<div>

<div align="left" style="font-size: 27px">

**RAID** (**Redundant Array of Inexpensive Disks**):
- A **data storage virtualization technology** that maps multiple physical disks to a single "drive"
- **Mirrored disks** are **failover real-time copies** of each other
  - Creates redundancy
- **Striped disks** depend on each other for optimal performance but aren't clones
- Learn RAID 0, 1, and 5 for starters -- Study!
- **RAID provides High Availability (HA), but is NOT a backup!**

</div>

<div align="left">


![Image](/ops-301-guide/curriculum/class-12/slides/assets/11_08.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- RAID (Redundant Array of Inexpensive Disks) is a data storage virtualization technology that utilizes multiple physical disk drives to increase data redundancy and/or improve performance.
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
 
# HOW

 
- How can we transition from workgroup P2P to client-server architecture?
  - Need to deploy Windows Server 2019 to the LAN
  - This server will host authoritative services that "take charge" of the Windows 10 computers

Source: TRR Data Recovery
Image Source: include link to image source

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="main-title" -->

# Review:

## Lab 11

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture: 
  - Domain Controller
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 11**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 12** - Python Requests Library

NOTE:

### Review: Ops Challenge 11

### Introduce: Ops Challenge 12 - Python Requests Library

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Domain Controller
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 11 - Domain Controller

NOTE:
Is there a relevant Ch. in the Wiley Network+ (N10-008) Study Guide?

---

<!-- .element class="split-screen-with-title" -->


# Domain Controller

<div>

<div align="left">

- Why study domains and DCs in 301?
  - Systems administrator VS adversaries can use the same tools to achieve objectives
    - Adversary: Why reinvent the wheel? I'll just take over the DC
    - Admin: I need these tools to do my job
  - DCs are essential to managing endpoints at scale

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Why does a domain need a DC? 
  - Authorization to domain resources 
  - Issue configurations to endpoints

Image Source: include link to image source
Source: Blogspot

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# Domain Controller

<div>

<div align="left">

- A Domain Controller (DC) is a network server responsible for host access to domain resources
  - Oversees the whole domain
  - Authenticates users
  - Stores user account information
  - Enforces security policy across devices
- Directory Servers commonly run Windows Server OS there are alternatives
  - OKTA
  - Linux LDAP

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

# WHAT 

- What is a DC? 
  - A network server responsible for host access to domain resources 
  - Oversees the whole domain 
  - Authenticates users 
  - Stores account information 
  - Enforces security policy across devices 
 
- Can run on Windows Server or Linux 

Image Source: include link to image source
Source: Blogspot

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# Domain Controller

<div>

<div align="left">

- DC components
  - Supported OS
  - Lightweight Directory Access Protocol (LDAP) is the standard protocol behind systems such as AD
  - Active Directory (AD) is a proprietary Microsoft software that uses LDAP to manage computers and user identities

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- What are the components of a DC? 
  - Supported OS 
    - Windows 
    - Linux 
  - LDAP Service 
    - Standard protocol behind systems like AD 
    - Facilitates the authentication and authorization of users to servers, files, networking equipment and applications. 
    - Default on TCP and UDP port 389
    - Stores objects (users and computers) as X500 objects or Distinguished Names which contain three values
      - DC (Domain)
      - OU (Organization Unit)
      - CN (anything else)

Image Source: include link to image source
Source: Blogspot

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# Domain Controller

<div>

<div align="left">

- DC components (ctd.)
  - Network time protocol (NTP)
  - Kerberos on port 88 encrypts the authentication traffic for AD
  - DNS
    - The DC traditionally acts as the Domain Name System (DNS) server
  - Public key infrastructure
    - Certificates

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Network Time Protocol 
- Kerberos 
  - Port 88 
  - Ticket-based network authentication protocol used by AD 
  - Named after Cerberus, mythological three-headed dog, who guards the gates of Hades 
  - Designed to travel over unsecured networks, uses encryption to protect against eavesdropping and relay attacks

Image Source: include link to image source
Source: Blogspot

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="main-title" -->
# DNS


NOTE:
Update the class number for each video recording

---

<!-- .element class="split-screen-with-title" -->


# DNS at Internet Level

<div>

<div align="left" style="font-size: 28px">

- A DNS Server maintains a local database of IP addresses associated with domain names
  - Acts in hierarchy with other DNS servers, all the way up to root DNS
  - Top level domains (TLDs) are domains in the DNS root zone of the internet's DNS
    - Example: *.com
    - Maintained by the Internet Assigned Numbers Authority (IANA)
  - Public DNS, e.g. Google DNS at 8.8.8.8
  - Private DNS, e.g. your LAN's DC

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_02.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

# WHAT 

- What is a DNS Server? 
  - Domain Name System (DNS) 
  - Maintains a local database of IP addresses associated with domain names 
  - Acts in hierarchy with other DNS servers, all the way up to root DNS 
 
# Draw 

- Draw out the DNS hierarchy of forest, tree, domain and OU 

Image Source: include link to image source
Source: OpenSource

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# DNS at Local Level

<div>

<div align="left">

- A domain is composed of various parts:
  - Forest is composed of multiple trees but may also only have one tree
  - Tree is composed of multiple domains
  - Domain is represented as a triangle
  - Organizational Unit (OU) is represented as a circle
- Image depicts a domain forest with two trees

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: include link to image source
Source: ServerFault

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# DNS Resolution Process

<div>

<div align="left">

- A DNS forward lookup zone converts a domain name to an IP address or another name
- A DNS reverse lookup zone converts an IP address to a domain name
- A fully-qualified domain name (FQDN) is written with the host name, the domain name, then the TLD name. Examples:
  - www.microsoft.com
  - en.wikipedia.org
  - p301srv03.timandtombreadco.us

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_04.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

# WHAT 

- What are the components of the DNS resolution process? 
  - DNS Resolver 
    - Receives the request to resolve the domain name with the IP address 
    - This server does the grunt work in figuring out where the site you want to go actually resides on the internet 
  - Root Server 
    - Receives the first request and returns a result to let the DNS resolver know what the address of the TLD server that stores the information about the site 
    - TLD is the equivalent of the .com or .net portion of the domain name 
  - TLD Server
    - Dns resolver then queries this server, which returns the Authoritative Name Server where the site is actually returned 
  - Authoritative Name Server 
    - Finally, the DNS resolver queries this server to learn the actual IP address of the website you are trying to deliver 
 
# Draw 

- Draw out the DNS hierarchy and the process 

Image Source: include link to image source
Source: StackOverflow

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="split-screen-with-title" -->


# DNS Resolution Order

<div>

<div align="left">

- Client makes a lookup request for Server1 DNS Suffix is appended to the request IF a FQDN is not used, in this instance a short name is used and the suffix MyDomain.Net is appended then sent to the clients DNS Server
- DNS Server checks to see if it hosts a primary forward lookup zone for MyDomain.Net if it does not have a record it will check its Conditional Forwarders.

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/12_05.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Walk the class through the resolution order 

### WHAT 

- What are the components of the DNS resolution process? 
  - DNS Resolver 
    - Receives the request to resolve the domain name with the IP address 
    - This server does the grunt work in figuring out where the site you want to go actually resides on the internet 
  - Root Server 
    - Receives the first request and returns a result to let the DNS resolver know what the address of the TLD server that stores the information about the site 
    - TLD is the equivalent of the .com or .net portion of the domain name 
  - TLD Server
    - Dns resolver then queries this server, which returns the Authoritative Name Server where the site is actually returned 
  - Authoritative Name Server 
    - Finally, the DNS resolver queries this server to learn the actual IP address of the website you are trying to deliver 
 
### Draw 

- Draw out the DNS hierarchy and the process

Image Source: include link to image source
Source: Devopedia

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# DNS Resolution Order

<div>

<div align="left">


- If the Conditional Forwarder is found it will send the request to that DNS Server that's specified.
- If the DNS Server specified in the conditional forwarder does not respond then the DNS Server will send the request for its Forwarder
- The request hits the DNS server specified in the forwarders tab of the DNS server, the request hits 8.8.8.8 which then replies with the IP address

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/12_05.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Walk the class through the resolution order 

### WHAT 

- What are the components of the DNS resolution process? 
  - DNS Resolver 
    - Receives the request to resolve the domain name with the IP address 
    - This server does the grunt work in figuring out where the site you want to go actually resides on the internet 
  - Root Server 
    - Receives the first request and returns a result to let the DNS resolver know what the address of the TLD server that stores the information about the site 
    - TLD is the equivalent of the .com or .net portion of the domain name 
  - TLD Server
    - Dns resolver then queries this server, which returns the Authoritative Name Server where the site is actually returned 
  - Authoritative Name Server 
    - Finally, the DNS resolver queries this server to learn the actual IP address of the website you are trying to deliver 
 
### Draw 

- Draw out the DNS hierarchy and the process

Image Source: include link to image source
Source: Devopedia

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# DNS Record Types

<div>

<div align="left">

- DNS servers use records to track configuration
  - A, AAAA
  - TXT (SPF, DKIM)
  - SRV
  - MX
  - CNAME
  - NS
  - PTR

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-12/slides/assets/12_04.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- DNS Record Types 
  - A
    - Holds the IP address of a domain
  - AAAA 
    - Holds the IPv6 address for a domain 
  - TXT (SPF, DKIM)
    - Lets an admin store text notes in the records 
    - SPF and DKIM are used for email security 
  - SRV 
    - Specifies a port for specific services 
  - MX 
    - Directs mail to an email server 
  - CNAME 
    - Forwards one domain or subdomain to another domain 
    - Does NOT provide an IP address
  - NS 
    - Stores the name server for a DNS entry 
  - PTR 
    - Provides a domain name in reverse-lookups

Image Source: include link to image source
Source: StackOverflow

<div style="font-size: small">Title, Author, License Type</div>


---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 12 - Domain Controller
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: 
  - Domain Controller
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Domain Controller

NOTE:

### Import OVA File


### Demo: Domain Controller

