<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 01

---

<!-- .element class="main-title" -->
## Ops 301
# Agenda

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation <!-- .element: class="fragment" data-fragment-index="1" -->
- Course Overview <!-- .element: class="fragment" data-fragment-index="2" -->
- Tools used in Ops 301 <!-- .element: class="fragment" data-fragment-index="3" -->
- Career Outcomes <!-- .element: class="fragment" data-fragment-index="4" -->
- Lecture: <!-- .element: class="fragment" data-fragment-index="5" -->
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo <!-- .element: class="fragment" data-fragment-index="6" -->

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation <!-- .element style="color: red;"-->
- Course Overview
- Tools used in Ops 301
- Career Outcomes
- Lecture:
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation
- Course Overview <!-- .element style="color: red;"-->
- Tools used in Ops 301
- Career Outcomes
- Lecture:
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo

---

<!-- .element class="main-title" -->
## Ops 301
# Course Overview

---

<!-- .element class="split-screen-with-title" -->

## Course Overview

<div>

<div align="left" style="font-size: 35px">

**Modules:**
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="1" -->**Module 1** Networking Tools, Concepts, and Fundamentals
- &shy;<!-- .element class="fragment fade-in-then-semi-out" data-fragment-index="2" -->**Module 2** Network Infrastructure Design and Implementation
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="3" -->**Module 3** Server Administration, Active Directory, and User Management
- &shy;<!-- .element: class="fragment fade-in-then-semi-out" data-fragment-index="4" -->**Module 4** Project Week and Presentations

</div>

<div>

![Image](/ops-301-guide/curriculum/class-01/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-text" -->

# Course Overview: Topics / Labs (15%)

| Module 01 <!-- .element width="30%" class="fragment" data-fragment-index="1" --> | Module 02 <!-- .element width="30%" class="fragment" data-fragment-index="3" --> | Module 03 <!-- .element width="30%" class="fragment" data-fragment-index="5" --> |
| ------------------- | ------------------- | ------------------- |
| Class 01: <br> &nbsp; &nbsp; Network Traffic Analysis <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 06: <br> &nbsp; &nbsp; &nbsp; Network Address Translation <!-- .element class="fragment" data-fragment-index="4" -->| Class 11: <br> &nbsp; &nbsp; Windows Server <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 02: <br> &nbsp; &nbsp; Network Enumeration <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 07: <br> &nbsp; &nbsp; Web Server Deployment <!-- .element class="fragment" data-fragment-index="4" --> | Class 12: <br> &nbsp; &nbsp; Domain Controller <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 03: <br> &nbsp; &nbsp; Network Segmentation <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 08: <br> &nbsp; &nbsp; Network Access Controls <!-- .element class="fragment" data-fragment-index="4" --> | Class 13: <br> &nbsp; &nbsp; Active Directory <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 04: <br> &nbsp; &nbsp; Routing <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 09: <br> &nbsp; &nbsp; Traffic Mirroring <!-- .element class="fragment" data-fragment-index="4" --> | Class 14: <br> &nbsp; &nbsp; Group Policy <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 05: <br> &nbsp; &nbsp; VPN Tunnel <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 10: <br> &nbsp; &nbsp; AWS VPC <!-- .element class="fragment" data-fragment-index="4" --> | Class 15: <br> &nbsp; &nbsp; N/A: Project Kickoff <!-- .element class="fragment" data-fragment-index="6" --> |


<!-- .element class="medium-text" -->

NOTE:
**Class 01: Network Traffic Analysis**
Use Wireshark on Kali Linux to capture CERN website traffic.

**Class 02: Ports and Protocols**
Learn Nmap, configure DNS, analyze with Wireshark and `netstat`.

**Class 03: Network Segmentation**
Set up networks, VLANs, and trunking in Cisco's Packet Tracer.

**Class 04: Routing**
Continuing in Cisco's Packet Tracer, we will configure routers, establish BGP, update the network topology.

**Class 05: VPN Tunnel**
Create VPNs in pfSense, test connectivity, draw the topology.

**Class 06: Network Address Translation**
Share folders on Windows, configure NAT rules.

**Class 07: Web Server Deployment**
Deploy NGINX on pfSense, test, update the topology.

**Class 08: RADIUS Authentication**
Configure portals with Captive Portal, use FreeRADIUS.

**Class 09: Traffic Mirroring**
Mirror LAN traffic, use Kali Linux and Wireshark.

**Class 10: AWS VPC**
Set up AWS VPCs, deploy instances, create Internet Gateway.

**Class 11: Windows Server**
Deploy Windows Server, connect to pfSense.

**Class 12: Domain Control**
Configure domains, add DC, establish DNS.

**Class 13: Active Directory**
Join systems to domain, configure user accounts.

**Class 14: Group Policy**
Use Group Policy to manage user settings.

**Class 15: Project Kickoff**
Review, overview 401 content, form teams, assign projects.

---

<!-- .element class="title-and-text" -->

# Course Overview: Challenges (10%)

| Module 01: Bash &nbsp;&nbsp;&nbsp;<!-- .element width="30%" class="fragment" data-fragment-index="1" --> | Module 02: Python <!-- .element width="30%" class="fragment" data-fragment-index="3" --> | Module 03: Python + PowerShell <!-- .element width="30%" class="fragment" data-fragment-index="5" --> |
| ------------------- | ------------------- | ------------------- |
| Class 01: <br> &nbsp; &nbsp; N/A <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 06: <br> &nbsp; &nbsp; Bash in Python <!-- .element class="fragment" data-fragment-index="4" -->| Class 11: <br> &nbsp; &nbsp; Psutil <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 02: <br> &nbsp; &nbsp; Append + Date and Time <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 07: <br> &nbsp; &nbsp; Directory Creation <!-- .element class="fragment" data-fragment-index="4" --> | Class 12: <br> &nbsp; &nbsp; Python Requests Library <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 03: <br> &nbsp; &nbsp; File Permissions <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 08: <br> &nbsp; &nbsp; Python Collections <!-- .element class="fragment" data-fragment-index="4" --> | Class 13: <br> &nbsp; &nbsp; Powershell AD Automation <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 04: <br> &nbsp; &nbsp; Conditionals in Menu Systems <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 09: <br> &nbsp; &nbsp; Python Conditional Statements <!-- .element class="fragment" data-fragment-index="4" --> | Class 14: <br> &nbsp; &nbsp; Python Malware Analysis <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 05: <br> &nbsp; &nbsp; Clearing Logs <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 10: <br> &nbsp; &nbsp; Python File Handling <!-- .element class="fragment" data-fragment-index="4" --> | Class 15: <br> &nbsp; &nbsp; N/A <!-- .element class="fragment" data-fragment-index="6" --> |

<!-- .element class="medium-text" -->

NOTE:
**Class 01 None**

**Class 02 Append; Date and Time**
Craft a script to copy logs with timestamps, enhancing recordkeeping.

**Class 03 File Permissions**
Build an interactive script for modifying file permissions based on user input.

**Class 04 Conditionals in Menu Systems**
Develop a menu-driven script with options, incorporating conditional logic for user choices.

**Class 05  Clearing Logs**
Write a log clearing bash script.

**Class 06 Bash in Python**
Use Python to execute Bash commands and display results.

**Class 07 Directory Creation**
Create a script that generates folders and files in a specified path.

**Class 08 Python Collections**
Script for modifying and displaying elements within a Python list.

**Class 09 Python Conditional Statements**
Learn Python conditionals, including secondary conditions and catch-all cases.

**Class 10 Python File Handling**
Develop a script for creating, writing, reading, and deleting text files in Python.

**Class 11 Psutil**
Explore process execution times and virtual CPU usage using Psutil in Python.

**Class 12 Python Requests Library**
Use Python's requests library for user-directed HTTP interactions.

**Class 13 Powershell AD Automation**
Learn Active Directory user addition in Windows Server using Powershell.

**Class 14 Python Malware Analysis**
Analyze a malicious script and create comments.

**Class 15 None**

---

<!-- .element class="title-and-text" -->

# Course Overview: Career (10%)

| Module 01 &nbsp;&nbsp;&nbsp;<!-- .element width="30%" class="fragment" data-fragment-index="1" --> | Module 02 <!-- .element width="30%" class="fragment" data-fragment-index="3" --> | Module 03 <!-- .element width="30%" class="fragment" data-fragment-index="5" --> |
| ------------------- | ------------------- | ------------------- |
| Class 01: <br> &nbsp; &nbsp; Accountability Partners <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 06: <br> &nbsp; &nbsp; Behavioral Questions & Mock <br> &nbsp; &nbsp; Interviews <!-- .element class="fragment" data-fragment-index="4" -->| Class 11: <br> &nbsp; &nbsp; Targeted Job Search <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 02: <br> &nbsp; &nbsp; --- <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 07: <br> &nbsp; &nbsp; --- <!-- .element class="fragment" data-fragment-index="4" --> | Class 12: <br> &nbsp; &nbsp; --- <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 03: <br> &nbsp; &nbsp; Networking Opportunities <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 08: <br> &nbsp; &nbsp; Professional Pitch & Introduction <!-- .element class="fragment" data-fragment-index="4" --> | Class 13: <br> &nbsp; &nbsp; Coffee Meeting <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 04: <br> &nbsp; &nbsp; --- <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 09: <br> &nbsp; &nbsp; --- <!-- .element class="fragment" data-fragment-index="4" --> | Class 14: <br> &nbsp; &nbsp; Attend A Networking Event <!-- .element class="fragment" data-fragment-index="6" --> |
| Class 05: <br> &nbsp; &nbsp; Partner Power Hour #1 <!-- .element height="100" class="fragment" data-fragment-index="2" --> | Class 10: <br> &nbsp; &nbsp; Partner Power Hour #2 <!-- .element class="fragment" data-fragment-index="4" --> | Class 15: <br> &nbsp; &nbsp; Partner Power Hour #3 <!-- .element class="fragment" data-fragment-index="6" --> |

<!-- .element class="medium-text" -->

NOTE:
**Class 01 Accountability Partners**
Stay motivated by seeking assistance and being transparent about your progress and responsibilities.

**Class 03 Networking Opportunities**
Explore local tech events via GeekWire, Meetup, and more to enhance job connections. Share 5 unique off-campus networking options with classmates.

**Class 05 Partner Power Hour #1**
Participate in industry-oriented presentations, share insights, and connect on LinkedIn.

**Class 06 Behavioral Questions & Mock Interviews**
Practice behavioral interviews, collaborate with partners, summarize insights, and personal growth.

**Class 08 Professional Pitch & Introduction**
Revise your professional pitch video, seek feedback, and submit for assessment.

**Class 10 Partner Power Hour #2**
Engage with professionals, share insights, and network effectively.

**Class 11 Targeted Job Search**
Explore companies, fill Google Spreadsheet with job postings' info, and share link for evaluation.

**Class 13 Coffee Meeting**
Learn through 1:1 meetings, share insights, and allocate 40 minutes for the task.

**Class 14 Attend A Networking Event**
Attend a meetup, meet new contacts, converse meaningfully, and share experiences.

**Class 15 Partner Power Hour #3**
Participate in industry presentations, share insights, and network actively.

---

<!-- .element class="split-screen-with-title" -->

# Course Overview: 401 Entrance Exam (10%)

<div>

<div align="left">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Must pass in order to complete 301 and progress to 401**


&shy;<!-- .element: class="fragment" data-fragment-index="2" --> <br>
&shy;<!-- .element: class="fragment" data-fragment-index="2" --> Details:
- Taken at the end of Module 3 <!-- .element: class="fragment" data-fragment-index="3" -->
- 25 questions <!-- .element: class="fragment" data-fragment-index="3" -->
- 80% or higher required to pass <!-- .element: class="fragment" data-fragment-index="3" -->
- Open-book: <!-- .element: class="fragment" data-fragment-index="3" -->
  - Google == yes <!-- .element: class="fragment" data-fragment-index="4" -->
  - ChatGPT == no <!-- .element: class="fragment" data-fragment-index="4" -->


</div>

<div>

![Image](/ops-301-guide/curriculum/class-01/slides/assets/0_05.png)

</div>

</div>


<!-- .element class="normal-text" -->

---

<!-- .element class="split-screen-with-title" -->

# Course Overview: CompTIA Exam + Project Week (25%)

### (320 available points)

<div>

<div>

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**CompTIA Net+ N10-008**<br>(100 points)
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->*Taking* the exam is required to complete 301
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->*Passing* the exam is not a requirement
  - 720 or higher = 100 points <!-- .element: class="fragment" data-fragment-index="4" -->
  - Lower than 720 = <90 points <!-- .element: class="fragment" data-fragment-index="4" -->
- Take the exam before the end of Module 4 <!-- .element: class="fragment" data-fragment-index="5" -->

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_02.png) <!-- .element style="width: 70%"-->
</div>

<div>

&shy;<!-- .element: class="fragment" data-fragment-index="6" -->**Project Week (Module 4)**<br>(220 points)
- Project: <!-- .element: class="fragment" data-fragment-index="7" -->
  - Grouped into teams of 3-5
  - Given a scenario and requirements
  - Plan project, organize team, build systems, write documentation
- At the end of Module 4: <!-- .element: class="fragment" data-fragment-index="8" -->
  - Deliver professional presentation to instructors, family, peers
  - Deliver a professional compilation of written documentation
- Add this project to your resume! <!-- .element: class="fragment" style="font-size: 40px; color: red" data-fragment-index="9" -->

</div>

</div><!-- .element class="medium-text" -->

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation
- Course Overview
- Tools used in Ops 301 <!-- .element style="color: red;"-->
- Career Outcomes
- Lecture:
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo

---

<!-- .element class="main-title" -->
## Ops 301
# Tools

---

<!-- .element class="split-screen-with-title" -->

# Course Tools

<div>

<div align="left">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Canvas**
- Syllabus / Course Details <!-- .element: class="fragment" data-fragment-index="2" -->
- Modules <!-- .element: class="fragment" data-fragment-index="3" -->
- Assignments and Due Dates <!-- .element: class="fragment" data-fragment-index="4" -->
- Assignment Submission <!-- .element: class="fragment" data-fragment-index="5" -->
- Grading <!-- .element: class="fragment" data-fragment-index="6" -->

&shy; <!-- .element: class="fragment" data-fragment-index="7" -->**GitHub Class Repo**
- Course README <!-- .element: class="fragment" data-fragment-index="8" -->
  - Course Schedule & Downloads <!-- .element: class="fragment" data-fragment-index="9" -->
- Daily README <!-- .element: class="fragment" data-fragment-index="10" -->
- Demo material <!-- .element: class="fragment" data-fragment-index="11" -->



</div>

<div align="left">

&shy; <!-- .element: class="fragment" data-fragment-index="12" -->**Remo Shared Workspace**
- TA help queue <!-- .element: class="fragment" data-fragment-index="13" -->
- Partner Power Hour recordings  <!-- .element: class="fragment" data-fragment-index="14" -->

**Student Tool**  <!-- .element: class="fragment" data-fragment-index="15" -->
- Google Docs  <!-- .element: class="fragment" data-fragment-index="16" -->
- Personal Github Repos  <!-- .element: class="fragment" data-fragment-index="17" -->
- Reading Notes Repo  <!-- .element: class="fragment" data-fragment-index="18" -->
- Challenge Repo for scripts  <!-- .element: class="fragment" data-fragment-index="19" -->

</div>

</div>
NOTE:
- **Course Mechanics**
  - Walk students through each of the key tools and platforms we'll be using in class
  - Introduce Canvas
  - Show the modules page
  - Show the assignments page
  - Show the discussions page
  - Explain how assignments are submitted
    - **GitHub Repo**
      - Students will create their own public GitHub repo and push to it, then link for submission
      - Demo how this is done
        - Cloning
        - Add, commit, push workflow
    - **Google Docs**
      - Create an example Google Doc and show students how to submit written/screenshot assignments
      - Demo how to insert a screenshot using Snipping Tool (Windows)
  - Grading expectations (90%) and criteria
  - Getting Help
    - Ops sequence contains its own curriculum, so students will need to contact Ops sequence TAs and not Code TAs
  - Projects
  - 301 Readiness

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation
- Course Overview
- Tools used in Ops 301
- Career Outcomes <!-- .element style="color: red;"-->
- Lecture:
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo

---

<!-- .element class="main-title" -->

## Ops 301
# Career Outcomes

---

<!-- .element class="split-screen-with-title" -->

# Career Outcomes

<div>

<div align="left" style="font-size: 28px">

### What kind of jobs can an Ops 301 graduate do?
- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Jr. Systems Administrator**
  - Startup and Small/Medium business space
  - Expect to handle day-to-day operations
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**MSP Technician**
  - Support multiple client companies
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**IT Specialist**
  - A tier above Support Technician in seniority
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Network Specialist or Support**



</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_01.png
)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Ann Fandrey, CC0, via Wikimedia Commons</div>


<div>

<div>

NOTE:
**Jr. Systems Administrator:**
  - This role involves managing and maintaining an organization's computer systems, servers, and networks under the guidance of senior administrators.
  - Responsibilities might include installing and configuring hardware and software, troubleshooting technical issues, performing system updates and backups, and ensuring the overall health and functionality of IT infrastructure.
  - Junior Systems Administrators often work in collaboration with other IT professionals to ensure smooth operations.

**MSP Technician (Managed Service Provider Technician):**
  - Working for a managed service provider, an MSP Technician supports multiple client companies by providing IT services remotely or on-site.
  - They may handle a wide range of tasks, including troubleshooting hardware and software problems, setting up and maintaining networks, managing security protocols, and offering technical support to clients.
  - The role requires good communication skills to interact effectively with clients and resolve their IT issues.

**IT Specialist:**
  - An IT Specialist typically holds a higher seniority level than a Support Technician and is responsible for more complex tasks.
  - This role could involve specialization in areas like network administration, cybersecurity, database management, or cloud computing.
  - IT Specialists might be involved in planning and implementing IT projects, managing advanced troubleshooting, and assisting in the development of IT strategies for the organization.

**Network Specialist or Support:**
  - A Network Specialist is responsible for the design, implementation, and management of an organization's network infrastructure.
  - This could include tasks such as configuring routers, switches, firewalls, and other networking devices, optimizing network performance, and ensuring network security.
  - Network Support might involve providing assistance to end-users facing network connectivity issues, diagnosing network problems, and maintaining network documentation.

Image Source: [The Noun Project](https://thenounproject.com/icon/22612,), by way of [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=67123537)

Sr. Sysadmins oversee IT architecture and design

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation
- Course Overview
- Tools used in Ops 301
- Career Outcomes
- Lecture: <!-- .element style="color: red;"-->
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo

---

<!-- .element class="main-title" -->

# Lecture:
### Class 01 - Network Traffic Analysis

- OSI Model
- Packet Capture
- Traffic Analysis

---

<!-- .element class="title-with-text" -->

## Review from 201: First 4 Layers of the OSI model:

| Layer &emsp; &emsp; &emsp; &emsp; <!-- .element: class="fragment" data-fragment-index="1" --> | Address Type <!-- .element: class="fragment" data-fragment-index="6" --> | Data Type <!-- .element: class="fragment" data-fragment-index="11" --> | Devices/Protocols <!-- .element: class="fragment" data-fragment-index="16" --> |
| ----- | ------------ | --------- | ----------------- |
| 4) Transport <!-- .element: class="fragment" data-fragment-index="5" --> | Logical Port Number <!-- .element: class="fragment" data-fragment-index="10" --> | Segments <!-- .element: class="fragment" data-fragment-index="15" --> | TCP, UDP, Gateway, Load Balancer <!-- .element: class="fragment" data-fragment-index="20" --> |
| 3) Network <!-- .element: class="fragment" data-fragment-index="4" --> | IP Address <!-- .element: class="fragment" data-fragment-index="9" --> | Packets  <!-- .element: class="fragment" data-fragment-index="14" --> | Router, Layer 3 Switch (VLAN) <!-- .element: class="fragment" data-fragment-index="19" --> |
| 2) Data Link <!-- .element: class="fragment" data-fragment-index="3" --> | MAC Address <!-- .element: class="fragment" data-fragment-index="8" --> | Frame <!-- .element: class="fragment" data-fragment-index="13" --> | L2 Switch, Bridge <!-- .element: class="fragment" data-fragment-index="18" --> |
| 1) Physical <!-- .element: class="fragment" data-fragment-index="2" --> | Physical Port ID <!-- .element: class="fragment" data-fragment-index="7" --> | Bits <!-- .element: class="fragment" data-fragment-index="12" --> | Cables, Hub, Repeater <!-- .element: class="fragment" data-fragment-index="17" --> |

<br>

<div align="center">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_07.png)
<!-- .element style="width: 50%"-->

</div>

NOTE:
Do you remember the **Hierarchy or Abstraction** we learned about in 102?
- Well the OSI model is that concept applied to networks.

| Layer | Address Type | Data Type | Devices/Protocols |
| ----- | ------------ | --------- | ----------------- |
| 4) Transport | Logical Port Number | Segments | TCP, UDP |
| 3) Network | IP Address | Packets | Router, Layer 3 Switch (VLAN) |
| 2) Data Link | MAC Address | Frame | L2 Switch, Bridge |
| 1) Physical | Physical Port ID | Bits | Cables, Hub, Repeater |

**Careful!** The word *Port* does double duty here:
- **Physical ports** are what you plug ethernet cables into
- **Logical ports** are used by protocols and services (i.e. SSH on port 22, RDP on port 3389, etc.)

# First 4 OSI layers:

- **Layer 1 (Physical):** Deals with physical transmission of data over the medium.
- **Layer 2 (Data Link):** Manages data frames within a local network segment using MAC addresses.
- **Layer 3 (Network):** Uses IP addresses to route data between different networks.
- **Layer 4 (Transport):** Manages data exchange between applications on different devices using port numbers.

## Addresses:
- **Physical Port ID (Layer 1):**
  - This is the ID value used internally by a device to differentiate between its physical ports
  - Examples: "Ethernet 1/1," "GigabitEthernet0/1," "FastEthernet0/1," or "eth0"
- **MAC Address (Layer 2):**
  - A unique ID assigned to a Network Interface Card (NIC), usually during manufacturing
    - Think of it the Social Security number of physical networking component
    - Not usually changed, but can be spoofed
  - Comes as a 48-bit/6-byte hexadecimal number
    - Example: "00:1A:2B:3C:4D:5E", or "00-1A-2B-3C-4D-5E"
    - First half: Organizational Unique Identifier (OUI) which is the manufacturer's ID
    - Second half: unique device ID
  - Windows: the output of `ipconfig /all` includes the MAC address: `Physical Address. . . . . . . . . : 00-1A-2B-3C-4D-5E`
  - Ubuntu: the output of `ip a` includes the MAC address: `link/ether 00:1A:2B:3C:4D:5E`
- **IP Address (Layer 3):**
  - Internet Protocol Address - a variable ID assigned to a network device when it connects to a network
	- A Network Device can receive multiple IP addresses, can change addresses, and can have different addresses on different networks
      - An IP Address is like a temporary ID given to you when you enter a building
    - Used by devices to identify themselves in the network
    - Usually mapped to a hostname
  - Two types:
    - IPv4:
      - 32-bit addresses, usually represented in 4x8-bit decimals
	    - Ex: 192.168.1.1
    - IPv6:
      - Less common
      - We don't really use them in this course
      - 128-bit addresses, usually represented in 8x16-bit hexadecimals
        - Ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- **Logical Port Number (Layer 4):**
  - Logical port addresses, or port numbers, allow network devices to direct incoming traffic to the correct application or service running on the device
  - Port numbers range from 1024 to 65535
    - Well-Known: 0-1023
    - Registered: 1024-49151
      - Used for applications and services that have been registered with the Internet Assigned Numbers Authority (IANA)
    - Dynamic (Private): 49152-65535
	  - Available for temporary or private use by applications and services

## Data Types:
- **Bits (Layer 1)**
  - A bit, short for "binary digit," is the smallest unit of digital information in computing and networking. It can represent one of two values: 0 or 1. All data in a computer or network is ultimately represented using combinations of bits. Bits are the building blocks of digital communication and storage.

- **Frame (Layer 2)**
  - In networking, a frame is a structured unit of data that is transmitted over a data link layer (usually Ethernet) of a network. A frame contains both control information, such as source and destination MAC addresses, as well as the actual data payload. Frames are used for local communication within a network segment, and they help ensure data integrity and proper delivery.

- **Packets (Layer 3)**
  - A packet is a unit of data that is transmitted over a network and contains both the actual data being sent and various control information. Unlike frames, which operate at the data link layer, packets operate at the network layer (Layer 3) of the networking stack. They include source and destination IP addresses, as well as other information needed for routing and delivery across different networks.

- **Segments (Layer 4)**
  - Segments are units of data that are transmitted over a transport layer (Layer 4) protocol, such as TCP (Transmission Control Protocol). In the context of networking, segments are part of a larger data stream, and they help manage the flow of data between devices by breaking it into smaller, manageable chunks. Segmentation is particularly important for reliable communication, as it allows for error correction and retransmission of lost data.

## Devices/Protocols:
- Network Devices
  - Hubs
    - Operate at the physical layer
    - Connects multiple devices together
    - Acts as a repeater of sorts.
  - Routers
    - These devices efficiently direct traffic on the network
    - Work as gateways to other networks (like the Internet)
  - Switches
    - Distributes messages from one computer to another
    - Difference from router, it doesn't work as a gateway to other networks
  - Firewalls
    - Sometimes standalone devices but sometimes integrated into routers
    - Protects network from unwanted incoming or outgoing network traffic
    - Firewalls can be applied at layers 2, 3, 4, or even higher

# Important Network Services:
DHCP
DNS

Source: [ChatGPT](https://chat.openai.com/share/c035bdb2-e129-48bb-aef2-dba8d5a7da49)
Image Source 12_05.png: [Wikipedia: Computer Network Diagram](https://en.wikipedia.org/wiki/Computer_network_diagram)
Image Source 12_03.png: [Rhyno.io](https://rhyno.io/what-is-the-open-systems-interconnection-osi-model/)

---

<!-- .element class="title-with-text" -->

# All 7 Layers of the OSI model:

| Layer &emsp; &emsp; &emsp; &emsp; | Address Type | Data Type | Devices/Protocols |
| ----- | ------------ | --------- | ----------------- |
| 7) Application <!-- .element: class="fragment" data-fragment-index="3" --> | --- <!-- .element: class="fragment" data-fragment-index="3" --> | --- <!-- .element: class="fragment" data-fragment-index="3" --> | HTTP, FTP, DNS, DHCP, Computer <!-- .element: class="fragment" data-fragment-index="3" --> |
| 6) Presentation <!-- .element: class="fragment" data-fragment-index="2" --> | --- <!-- .element: class="fragment" data-fragment-index="2" --> | --- <!-- .element: class="fragment" data-fragment-index="2" --> | ASCII, JPEG/GIF/PNG, Computer <!-- .element: class="fragment" data-fragment-index="2" --> |
| 5) Session <!-- .element: class="fragment" data-fragment-index="1" --> | --- <!-- .element: class="fragment" data-fragment-index="1" --> | --- <!-- .element: class="fragment" data-fragment-index="1" --> | SMB, SIP, Computer <!-- .element: class="fragment" data-fragment-index="1" --> |
| 4) Transport <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Logical Port Number <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Segments <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | TCP, UDP, Gateway, Load Balancer <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> |
| 3) Network <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | IP Address <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Packets  <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Router, Layer 3 Switch (VLAN) <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> |
| 2) Data Link <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | MAC Address <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Frame <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | L2 Switch, Bridge <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> |
| 1) Physical <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Physical Port ID <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Bits <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> | Cables, Hub, Repeater <!-- .element: class="fragment semi-fade-out" data-fragment-index="1" --> |

<br>

<div align="center" style="font-size: 40px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->Layers 5, 6 and 7 do not have specific **Address**

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->or **Data Types** associated with them

</div>

NOTE:
Layers 5, 6, and 7 of the OSI model are the upper layers that focus on application-level communication and user interactions.

**Layer 5: Session Layer:**
- The Session Layer is responsible for establishing, managing, and terminating communication sessions between two devices.
- It ensures that data exchange between applications is organized and synchronized, allowing for proper sequencing and error recovery.
- This layer also manages dialogue control, allowing applications to start, pause, resume, and end communication sessions.

**Layer 6: Presentation Layer:**
- The Presentation Layer is responsible for data translation, encryption, and compression to ensure that data from the application layer of one system can be understood by the application layer of another.
- It takes care of data formatting, character encoding, and data encryption/decryption to provide secure and efficient communication.
- This layer helps to provide a common format for data exchange between different systems with varying data representations.

**Layer 7: Application Layer:**
- The Application Layer is the topmost layer and is the one closest to the end-users or applications.
- It provides a direct interface for user interaction and supports various application services, protocols, and APIs.
- This layer encompasses a wide range of functions, including email services, file transfers, remote access, web browsing, and more. It's where end-user applications and network services reside.

---

<!-- .element class="split-screen" -->

<div align="left">

# Layer 1: Physical

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Hardware**
  - Hubs
  - Repeaters
  - NIC (Network Interface Cards)
  - Ethernet Cables
  - Optical Fibers
  - Radio transceivers (Wi-Fi)
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Protocols**
  - USB
  - Bluetooth
  - RJ45
  - IEEE 802.11/Wi-Fi (also Layer 2)

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 1: Physical

**Layer 1**, the **Physical layer**, is the lowest layer of the OSI model. It deals with the actual physical connection and transmission of raw binary data (bits) between devices on a network. This layer is responsible for the fundamental aspects of communication that involve converting digital data into electrical, optical, or radio signals for transmission over the physical medium.

### Functions of the Physical Layer:

- **Bit Synchronization:** Ensures that sender and receiver devices are synchronized in terms of bit timing, allowing for accurate data transmission and reception.
- **Bit Rate Control:** Manages the rate at which bits are transmitted over the medium to prevent data loss due to different speeds between sender and receiver.
- **Physical Topologies:** Describes how devices are physically connected to each other, such as in bus, star, ring, or mesh topologies.
- **Transmission Mode:** Defines how data is transmitted, including simplex (one-way), half-duplex (both directions but not simultaneously), and full-duplex (both directions simultaneously).

### Devices and Components:

- **Hubs:** Basic networking devices that operate at Layer 1, connecting multiple devices in a star topology. They amplify and broadcast incoming signals to all connected devices.
- **Repeater:** Amplifies and regenerates signals to extend the reach of a network by preventing signal degradation.
- **Network Interface Card (NIC):** Hardware component in devices that connects them to a network medium (e.g., Ethernet cable or wireless).
- **Ethernet Cables:** Physical cables used to transmit data signals between devices. They come in various categories, such as Cat 5, Cat 6, etc.
- **Optical Fibers:** High-speed transmission medium that uses light signals to carry data over long distances with minimal signal loss.

### Wiring Standards:

- **TIA/EIA 568A and 568B Wiring Standards:** These are standards used for wiring Ethernet cables, specifying the arrangement of the wires within the cable connectors (RJ-45 connectors).
- **Straight-Through Cable:** Used to connect devices that have different functions, such as a switch to a router or a hub to a PC.
- **Crossover Cable:** Used to connect devices of the same type, such as switch to switch, switch to hub, or router to router.

Understanding the Physical layer is crucial as it forms the foundation for all network communication. It ensures that bits are transmitted reliably and accurately over the physical medium, enabling data exchange across the network.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left" style="font-size: 32px">

# Layer 2: Data Link

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Encode** and **Decode** electrical signals into **Bits**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Manages data errors** from physical layer
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->Convert electrical signals to **Frames**
- Includes two sub-layers: <!-- .element: class="fragment" data-fragment-index="4" -->
  - Media Access Control (**MAC**) layer
  - Logical Link Control (**LLC**) layer
- Example: <!-- .element: class="fragment" data-fragment-index="5" -->
  - **Layer 2 Switch**

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 2: Data Link Layer:

The **Data Link Layer** is the second layer of the OSI (Open Systems Interconnection) model. It serves as a bridge between the physical layer (Layer 1) and the network layer (Layer 3). Its primary functions revolve around providing a reliable link between two directly connected nodes (devices) in a network.

- **Encode and Decode Electrical Signals into Bits:**
  The Data Link layer takes the raw stream of electrical signals from the physical layer and converts them into a series of bits, organizing them into meaningful units known as **frames**. This process involves both encoding data into a format suitable for transmission and decoding received bits back into meaningful data.

- **Manages Data Errors from Physical Layer:**
  As data is transmitted over physical media, there's always a possibility of errors due to factors like signal interference, attenuation, and noise. The Data Link layer detects and sometimes corrects these errors to ensure reliable data transmission.

- **Convert Electrical Signals to Frames:**
  The Data Link layer adds a header and a trailer to the raw data received from the network layer. These headers and trailers create the structure of a **frame**, which includes control information, source and destination addresses, and error-checking information.

- **Includes Two Sub-Layers:**
  The Data Link layer is divided into two sub-layers:
  - **Media Access Control (MAC) Layer:** This sub-layer is responsible for managing access to the physical medium (such as Ethernet cables or wireless channels) to avoid data collisions in shared network environments. It assigns unique addresses, known as MAC addresses, to network interface cards (NICs) to identify devices on the same network.
  - **Logical Link Control (LLC) Layer:** The LLC sub-layer controls the flow of data between devices over the link. It provides error control and flow control mechanisms to ensure that data is delivered reliably and efficiently.

## Example: Layer 2 Switch:

A **Layer 2 switch** is a networking device that operates primarily at the Data Link layer. It functions as an intelligent bridge, forwarding data frames based on MAC addresses. When a switch receives a frame, it examines the destination MAC address and then makes a decision about which port to forward the frame to. This allows for more efficient data transmission within a local area network (LAN) as compared to a hub or a simple bridge.

In summary, the OSI Layer 2, or Data Link layer, plays a critical role in managing data communication within a local network segment. It ensures error-free transmission of data frames, manages access to the physical medium, and provides addressing and control mechanisms. Devices like Layer 2 switches operate at this layer to facilitate efficient data forwarding based on MAC addresses.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left" style="font-size: 30px">

# Layer 3: Network

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->Handles **Switching** and **Routing**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Establish logical paths** between hosts
  - Route data packets to destination
  - Forward data packets
  - Internetworking
  - Error Handling
  - Congestion Control
  - Packet Sequencing
- Example: <!-- .element: class="fragment" data-fragment-index="3" -->
  - **Routers**
  - **TCP/IP** works at layer 3

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 3: Network Layer:

The **Network Layer** is the third layer of the OSI (Open Systems Interconnection) model. It plays a critical role in facilitating communication across different networks by establishing logical paths and determining how data packets should be forwarded from source to destination.

**Functions of the Network Layer:**

- **Switching and Routing:** The Network Layer decides the best path for data packets to travel from the source to the destination. This involves making routing decisions based on factors such as network topology, network policies, and routing algorithms.

- **Establishing Logical Paths:** The Network Layer establishes logical paths, also known as routes or paths, between hosts or devices. These paths are essential for guiding data packets through the network.

- **Routing Data Packets:** The Network Layer is responsible for forwarding data packets from one node (host or router) to another along the established logical paths. This process involves making decisions about the most efficient route for packet delivery.

- **Internetworking:** The Network Layer enables communication between different networks, allowing data to traverse different types of networks and protocols. It facilitates interconnectivity and interoperability across diverse network technologies.

- **Error Handling:** The Network Layer may provide mechanisms for error detection and correction, ensuring that data packets are delivered accurately. Error detection is crucial to maintain data integrity during transmission.

- **Congestion Control:** The Network Layer monitors network traffic and helps prevent congestion by managing the flow of data packets. It can use techniques like traffic shaping and quality of service (QoS) to prioritize certain types of traffic.

- **Packet Sequencing:** The Network Layer can include mechanisms to ensure that data packets are delivered in the correct order at the destination, even if they take different paths through the network.

**Example: Routers:**
Routers are devices that operate at the Network Layer. They play a central role in routing data packets between different networks. Routers make intelligent decisions about packet forwarding based on information in their routing tables and the destination IP address of the packet.

**TCP/IP at Layer 3:**
The TCP/IP protocol suite, which is commonly used in networking and the internet, operates at the Network Layer. The Internet Protocol (IP), a fundamental component of TCP/IP, is responsible for addressing and routing data packets across networks.

In summary, the Network Layer (Layer 3) of the OSI model is responsible for establishing logical paths between hosts and devices, forwarding data packets, routing decisions, internetworking, error handling, congestion control, and more. It is a critical layer that enables communication across diverse networks and ensures efficient and reliable data transmission.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left" style="font-size: 25px">

# Layer 4: Transport

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Sequencing**: a connection-oriented service that takes TCP segments that are received out of order and place them in the right order
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Error Control**: error control mechanisms ensure reliable delivery of data
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Layer-4 Addressing** (also called Process Level Addressing): allows a computer to use multiple network layer protocols simultaneously
- Protocols: <!-- .element: class="fragment" data-fragment-index="4" -->
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)
- Hardware: <!-- .element: class="fragment" data-fragment-index="5" -->
  - Firewalls
  - Gateways
  - Load Balancers


</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 4: Transport Layer:

The **Transport Layer** is responsible for managing end-to-end communication between devices and ensuring reliable data delivery across a network. It takes data segments from the Session Layer (Layer 5) and breaks them into smaller units for transmission. This layer also handles flow control, error detection and correction, and reordering of out-of-sequence data.

**Sequencing:**
- The Transport Layer provides **sequencing** to ensure that data segments received out of order are arranged in the correct order before passing them to the upper layers.
- This feature is particularly important for connection-oriented protocols like TCP, which guarantees the orderly and reliable delivery of data.

**Error Control:**
- **Error control mechanisms** in the Transport Layer ensure that data is delivered accurately and reliably to the receiving device.
- Error detection and correction mechanisms help identify and correct errors that might occur during data transmission.

**Layer-4 Addressing (Process Level Addressing):**
- **Layer-4 Addressing**, also known as **Process Level Addressing**, allows a single device to use multiple network layer protocols simultaneously.
- It enables a device to distinguish between different processes or services running on the same host and facilitates the delivery of data to the appropriate process.

## Protocols:

**TCP (Transmission Control Protocol):**
- TCP is a connection-oriented protocol that provides reliable and ordered delivery of data.
- It establishes a connection between sender and receiver through a three-way handshake and maintains the connection until the data exchange is complete.
- TCP features flow control, error detection and correction, and acknowledgment mechanisms.

**UDP (User Datagram Protocol):**
- UDP is a connectionless protocol that offers a simple, lightweight alternative to TCP.
- It lacks the reliability and ordering guarantees of TCP but is preferred in scenarios where speed and low overhead are more critical than error recovery.
- UDP is commonly used for real-time applications like video streaming and online gaming.

## Hardware:

**Firewalls:**
- Firewalls are hardware or software devices used to control the flow of traffic between networks, typically between a private network and the internet.
- They can operate at the Transport Layer to filter and inspect traffic based on rules defined by administrators.

**Gateways:**
- Gateways are devices that connect networks with different protocols or technologies.
- They can perform protocol translation, allowing data to flow smoothly between networks with differing Transport Layer protocols.

**Load Balancers:**
- Load balancers distribute incoming network traffic across multiple servers to ensure efficient utilization and prevent overload on any single server.
- They often work at the Transport Layer to distribute data packets based on factors like server health and load.

In summary, the Transport Layer (Layer 4) is responsible for ensuring reliable, orderly, and efficient data transmission between devices. It handles sequencing, error control, and process-level addressing. Protocols like TCP and UDP define how data is managed at this layer, and hardware components such as firewalls, gateways, and load balancers contribute to the functionality and security of the Transport Layer.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left" style="font-size: 25px">

# Layer 5: Session

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Sessions Management**: responsible for establishing, managing and ending sessions & connections between end user applications
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Duplex Control**: controls that whether both sender/receiver of a session will communicate at same time (**Full-Duplex**) or one will speak & other will listen (**Half-Duplex**)
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Authentication** and **Authorization**
- Protocols: <!-- .element: class="fragment" data-fragment-index="4" -->
  - SIP (Session Initiation Protocol)
  - SMB (Server Message Block)
- Hardware: <!-- .element: class="fragment" data-fragment-index="5" -->
  - End Devices: Computers, Smart Phones, Servers
  - Firewalls, Gateways, Load Balancers


</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 5: Session

The Session Layer is the fifth layer of the OSI model, responsible for managing the communication sessions between end-user applications. It provides a framework for establishing, managing, and ending sessions or connections between devices.

### Sessions Management:
The **Session Layer** oversees the establishment, maintenance, and termination of communication sessions between applications on different devices. It ensures that data exchange is organized, synchronized, and reliable. This involves managing dialogues, controlling session initiation and closure, and handling session-specific data.

### Duplex Control:
The Session Layer controls the **duplex communication** mode for sessions. It determines whether both the sender and receiver can communicate simultaneously (**Full-Duplex**) or if one can send while the other can only receive (**Half-Duplex**). Full-Duplex communication is common for most modern networks, enabling efficient bidirectional data exchange.

### Authentication and Authorization:
The Session Layer is also involved in aspects of **authentication** and **authorization**. It verifies the identities of devices and users participating in the session and ensures that only authorized entities can establish connections and exchange data. This contributes to maintaining a secure and controlled communication environment.

## Protocols:

### SIP (Session Initiation Protocol):
SIP is a protocol used for initiating, modifying, and terminating communication sessions, primarily in VoIP (Voice over Internet Protocol) systems. It's used to set up voice and video calls, multimedia conferences, and other real-time communication sessions over IP networks.

### SMB (Server Message Block):
SMB is a network file-sharing protocol that operates at the Session Layer. It enables devices to share files, printers, and other resources over a network. SMB is used in Microsoft Windows networks and facilitates seamless file and printer sharing among networked computers.

## Hardware:

### End Devices: Computers, Smart Phones, Servers:
End devices such as computers, smartphones, and servers participate in communication sessions facilitated by the Session Layer. These devices run applications that require session management, such as web browsers, video conferencing software, and file-sharing applications.

### Firewalls, Gateways, Load Balancers:
Network devices like firewalls, gateways, and load balancers play a role in managing sessions and connections as they traverse the network. They can inspect and control session-related parameters, ensuring that communication adheres to security policies and optimizing network performance.

In summary, the Session Layer (Layer 5) of the OSI model is responsible for managing communication sessions between end-user applications. It handles the establishment, synchronization, and termination of sessions, controls the communication mode (Full-Duplex or Half-Duplex), manages authentication and authorization, and supports protocols like SIP and SMB. This layer ensures organized and reliable data exchange while contributing to security and efficiency in network communication.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left">

# Layer 6: Presentation

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Data Formatting & Representation**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Data Encryption/Decryption**
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Data Compression/Decompression**
- Protocols: <!-- .element: class="fragment" data-fragment-index="4" -->
  - ASCII
  - SSL and TLS
  - JPEG/GIF/PNG/TIFF
- Hardware: <!-- .element: class="fragment" data-fragment-index="5" -->
  - End Devices: Computers, Smart Phones, Servers
  - Firewalls, Gateways, Load Balancers


</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 6: Presentation Layer:

The Presentation Layer is the sixth layer of the OSI model and plays a crucial role in ensuring that data from the application layer of one system can be properly understood by the application layer of another system. This layer is responsible for data formatting, encoding, encryption, and compression.

### Data Formatting & Representation:

The Presentation Layer handles data **formatting and representation**. It takes care of converting the data from its native format into a standardized format that can be understood by both the sender and the receiver. This involves handling differences in data representation, such as character sets, data structures, and integer formats.

### Data Encryption/Decryption:

**Data encryption and decryption** are important functions of the Presentation Layer, contributing to data security. Encryption involves converting data into a secure and unreadable format to prevent unauthorized access during transmission. Decryption reverses this process to restore the original data at the receiving end. Secure protocols like SSL (Secure Sockets Layer) and its successor TLS (Transport Layer Security) operate at this layer to provide encryption for sensitive data during communication.

### Data Compression/Decompression:

Data compression is the process of reducing the size of data for efficient storage and transmission, while decompression restores the data to its original format. This is particularly useful for optimizing bandwidth usage and improving overall network efficiency. Image formats like JPEG, GIF, PNG, and multimedia formats often use compression techniques to reduce file sizes without significant loss of quality.

## Protocols:

### ASCII (American Standard Code for Information Interchange):

ASCII is a character encoding standard that assigns numerical codes to represent characters, symbols, and control characters. It's widely used for representing text in computers and communication devices. The Presentation Layer handles the translation between ASCII characters and their binary representations.

### SSL and TLS (Secure Sockets Layer and Transport Layer Security):

SSL and TLS are cryptographic protocols that provide secure communication over a network, ensuring data confidentiality and integrity. These protocols establish encrypted connections between two devices, making it difficult for unauthorized parties to intercept or manipulate the data being transmitted. They are commonly used for securing online transactions, email communication, and sensitive data transfers.

### Image Formats: JPEG, GIF, PNG, TIFF:

The Presentation Layer is responsible for managing the compression and decompression of image formats like JPEG (Joint Photographic Experts Group), GIF (Graphics Interchange Format), PNG (Portable Network Graphics), and TIFF (Tagged Image File Format). These formats use different compression algorithms and techniques to store and transmit images efficiently while maintaining acceptable quality.

## Hardware:

### End Devices: Computers, Smart Phones, Servers:

End devices, such as computers, smartphones, and servers, interact directly with users and applications. The Presentation Layer ensures that data exchanged between these devices is correctly formatted and can be displayed or processed by the respective applications.

### Firewalls, Gateways, Load Balancers:

Infrastructure devices like firewalls, gateways, and load balancers can also interact with the Presentation Layer. For example, a firewall might inspect data at this layer to detect potential security threats. Gateways may perform protocol translation or encryption/decryption to enable communication between networks with different protocols or security requirements. Load balancers can optimize network traffic by compressing or decompressing data before distributing it to different servers.

In summary, the Presentation Layer of the OSI model focuses on making data understandable between different systems by handling data formatting, encryption, compression, and character encoding. It plays a vital role in ensuring secure and efficient communication across diverse network environments.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen" -->

<div align="left">

# Layer 7: Application

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Manages Applications**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Supplies Network Services** to End User
- Protocols: <!-- .element: class="fragment" data-fragment-index="3" -->
  - HTTP
  - DNS
  - DHCP
  - FTP
- Hardware: <!-- .element: class="fragment" data-fragment-index="4" -->
  - *End Devices: Computers, Smart Phones, Servers*
  - Firewalls, Gateways, Load Balancers

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_06.png)
<!-- .element style="width: 95%"-->

<div style="font-size: small">CultureDuQ, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</div>

</div>

NOTE:
## Layer 7: Application

The **Application Layer (Layer 7)** is the topmost layer of the OSI model and is the closest layer to end-users and applications. It directly interacts with software applications and provides services to enable effective communication and data exchange between different devices over a network.

### Manages Applications:

The Application Layer **manages applications** and provides a platform for different software programs to communicate with each other across a network. It defines the protocols and conventions that applications must follow for seamless data exchange.

### Supplies Network Services to End User:

This layer **supplies network services to end-users**. It means that the Application Layer is responsible for providing services like file transfers, email, web browsing, and more to the end-users of the network. It abstracts the complexity of lower-level network operations, allowing applications to focus on their specific tasks.

### Protocols:

Several **protocols** operate at the Application Layer, each serving a specific purpose:

- **HTTP (Hypertext Transfer Protocol):** Used for transmitting web pages and other resources over the internet. It's the protocol behind web browsing.
- **DNS (Domain Name System):** Translates human-readable domain names (like www.example.com) into IP addresses, facilitating internet navigation.
- **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses and network configuration settings to devices joining a network.
- **FTP (File Transfer Protocol):** Enables the transfer of files between computers on a network, commonly used for uploading/downloading files to/from servers.

### Hardware:

Hardware at the Application Layer includes both **end devices** (computers, smartphones, servers) and network infrastructure components like **firewalls, gateways, and load balancers**. While these components might not directly process application-specific data, they can still impact the functioning and security of applications and services running on the network.

In summary, the OSI Layer 7, the Application Layer, plays a vital role in enabling communication between software applications and end-users. It defines protocols and services that facilitate tasks like web browsing, email communication, and file transfers. The layer abstracts the complexities of network operations, allowing applications to function without worrying about lower-level details. The protocols and services at this layer are integral to the modern internet's functionality and the seamless interaction between users and applications.

> It's vital to recognize this is a *theoretical* model. It doesn't always translate perfectly to real-world operations, so be wary of over-analyzing a network system's OSI categorization.

Image Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:OSI_Model_v2.svg)

---

<!-- .element class="split-screen-with-title" -->


# Packet Capture

<div>

<div align="left" style="font-size: 40px">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->What is a **Packet**?
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->Why perform **Packet Analysis**?
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->What is **Packet Sniffing**?
  - Offensive
  - Defensive
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->What is involved in **Analyzing a Packet**?
- &shy;<!-- .element: class="fragment" data-fragment-index="5" -->The **TCP Handshake**

</div>

<div align="left">

> **Packet**:
>
> A unit of data transmitted over a network
>
> Contains both the actual data being sent and control information needed for its successful transmission and delivery to its destination

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_04.png)
<!-- .element style="width: 90%"-->

</div>

</div>

NOTE:

Image Source: [ScientDirect.com](https://www.sciencedirect.com/topics/computer-science/three-way-handshake) (inherited from old slides; omay not be licensable)

Source: [ChatGPT](https://chat.openai.com/share/18572832-bb05-484e-a9d5-8035cbddb1fa)

## What is a packet?

A **packet** is a fundamental unit of data used for communication across networks. It's a small segment of data that carries information from one computer or device to another. Packets are used to transmit data efficiently over a network, as they can be individually routed and managed.

## What is a packet composed of?

A **packet** is composed of several key elements that provide the necessary information for successful transmission and routing:

- **Source IP Address:** This is the IP address of the sender or the source of the packet.
- **Destination IP Address:** This is the IP address of the intended recipient or the destination of the packet.
- **Protocol:** This indicates the protocol to be used for handling the packet's data at the destination. It defines how the data should be processed and interpreted.
- **Packet Numbers:** These are sequence numbers or identifiers assigned to packets to ensure proper ordering and reconstruction of data at the receiving end.

## Why perform network packet analysis?

**Network packet analysis** involves capturing and examining the data packets flowing through a network. It serves various purposes:

- **Sniffing Traffic:**
  - **Defensive Security:** Analyzing packets helps security professionals detect and respond to potential threats or anomalies on a network. It's a key component of intrusion detection systems (IDS) and intrusion prevention systems (IPS).
  - **Offensive Security:** Ethical hackers and penetration testers use packet analysis to identify vulnerabilities and potential attack vectors that malicious actors could exploit.

## What is packet sniffing?

**Packet sniffing** refers to the process of capturing and analyzing data packets as they traverse a network. It can be done for both defensive and offensive purposes:

- **Defensive Context:** In the context of network security, packet sniffing helps identify unusual or suspicious network activity, which can aid in detecting unauthorized access attempts, malware infections, and other security breaches.
- **Offensive Context:** In an offensive context, packet sniffing can be used by hackers to intercept sensitive information, such as passwords or confidential data, from unencrypted network traffic.

## What is involved in analyzing a packet?

Analyzing a packet involves dissecting its contents to extract valuable information. For instance, in the context of Transmission Control Protocol (TCP), a common protocol used for reliable data transmission, the **TCP handshake** is a crucial part of packet analysis:

- **TCP Handshake:** The TCP handshake is a process used to establish a connection between two devices before they start exchanging data. It involves three steps:
  1. **SYN (Synchronize):** The initiating device sends a SYN packet to the receiving device, indicating its desire to establish a connection.
  2. **SYN/ACK (Synchronize/Acknowledge):** The receiving device responds with a SYN/ACK packet, acknowledging the request and indicating its willingness to establish the connection.
  3. **ACK (Acknowledge):** The initiating device sends an ACK packet back, confirming the establishment of the connection.

This handshake ensures that both devices are ready and willing to communicate before data transmission begins, contributing to the reliability and integrity of the communication process.

---

<!-- .element class="split-screen-with-title" -->


# Network Traffic Analysis (NTA)

<div>

<div align="left" style="font-size: 35px">

- &shy;<!-- .element: class="fragment" data-fragment-index="1" -->**Real-Time Monitoring** of what's happening on your network
  - Save records as **logs**
- &shy;<!-- .element: class="fragment" data-fragment-index="2" -->**Detect**:
  - Traces of malware
  - The use of vulnerable protocols and ciphers
- &shy;<!-- .element: class="fragment" data-fragment-index="3" -->**Troubleshoot** a slow network
- &shy;<!-- .element: class="fragment" data-fragment-index="4" -->**Improve internal visibility** and eliminate blind spots

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-01/slides/assets/01_05.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: [NetworkManagementSoftware.com](https://www.networkmanagementsoftware.com/review-solarwinds-netflow-traffic-analyzer-3-10-0/) (inherited from old slides; omay not be licensable)

## Real-Time Monitoring of What's Happening on Your Network:

**Real-time monitoring** involves continuously observing network activities as they occur. This proactive approach helps organizations stay vigilant and responsive to potential issues or threats. By monitoring in real time, you can identify abnormal behavior and take immediate action to mitigate risks. Real-time monitoring can encompass:

- **Network Traffic Analysis:** Tracking the volume and types of data flowing through the network to detect unusual spikes or patterns.
- **Intrusion Detection:** Identifying unauthorized access attempts, malware activity, or other suspicious behavior.
- **Application Performance Monitoring:** Monitoring the performance of critical applications to ensure they're running smoothly.

## Save Records as Logs:

**Logging** refers to the practice of recording events, actions, and activities on a network in the form of logs. These logs are invaluable for analysis, troubleshooting, and compliance. Logs can contain information about:

- **User Activities:** Who accessed what resources and when.
- **System Events:** Errors, warnings, and successful operations.
- **Security Incidents:** Any detected anomalies, potential breaches, or unauthorized access attempts.

## Detect Traces of Malware:

Real-time monitoring and logging help in **detecting traces of malware** by observing unusual behavior that might indicate an infection. This could include unexpected network connections, file modifications, or communication with known malicious servers. By detecting malware early, organizations can prevent its spread and minimize damage.

## Detect the Use of Vulnerable Protocols and Ciphers:

Real-time monitoring allows you to identify the **use of vulnerable protocols and ciphers** in network communication. These vulnerabilities can be exploited by attackers to compromise security. Detecting their usage helps administrators take remedial actions such as disabling weak protocols or enforcing secure encryption methods.

## Troubleshoot a Slow Network:

When facing **network performance issues**, real-time monitoring provides insights into the factors causing slowdowns. By analyzing network traffic and identifying bottlenecks, administrators can pinpoint the root causes of slow performance. This could be due to heavy bandwidth usage, misconfigured devices, or inefficient routing.

## Improve Internal Visibility and Eliminate Blind Spots:

**Internal visibility** refers to a clear understanding of what is happening within your network infrastructure. Real-time monitoring offers insights into internal network traffic and activities that might otherwise remain unnoticed. This helps **eliminate blind spots**—areas of the network that lack monitoring coverage. Improved visibility enhances security, facilitates efficient resource allocation, and supports compliance efforts.


OLD NOTES:
- What is NTA used for?
  - Collecting a real-time and historical record of what’s happening on your network
  - Detecting malware such as ransomware activity
  - Detecting the use of vulnerable protocols and ciphers
  - Troubleshooting a slow network
  - Improving internal visibility and eliminating blind spots

## Network Profiling

  - “Profiling” takes a 1-3 month “snapshot” of network activity.
  - This snapshot is then compared to current activity to detect anomalies.
  - For instance, say your ICMP traffic suddenly increases 1000x on a network segment.
  - The profiler would note that is is unusual an generate an alert.
  - This could indicate a ping sweep being executed (early stage attacker discovery technique)

---

<!-- .element class="title-and-subtitle" -->

# Agenda

- Campus Orientation
- Course Overview
- Tools used in Ops 301
- Career Outcomes
- Lecture:
  - OSI Model
  - Packet Capture
  - Traffic Analysis
- Demo <!-- .element style="color: red;"-->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Packet Capture and Filtering with Wireshark

NOTE:

### Import OVA File


### Demo: Packet Capture and Filtering with Wireshark

- What is “promiscuous mode”
    - In a network, promiscuous mode allows a network device, like Wireshark to intercept and read each network packet that arrives to your computer.
    - Wireshark default setting - Captures everything
  - FTP vs SFTP
    - FTP is the traditional file transfer protocol. It's a basic way of using the Internet to share files. SFTP (or Secure File Transfer Protocol) is an alternative to FTP that also allows you to transfer files, but adds a layer of security to the process.
    - The key difference between FTP vs SFTP is that SFTP uses a secure channel to transfer files while FTP doesn't.
    - SFTP (SSH File Transfer Protocol) that sends files over an SSH connection

- **How** (30 min)
TODO: We don't install Wireshark, we install Kali Linux and launch it from there
 How do we use Wireshark to analyze a packet?
  - Install Wireshark
  - View current connections
- Refer to [DEMO.md](DEMO.md)
