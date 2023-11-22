<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 02

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Ports and Protocols
  - Port Scanning
  - Nmap
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

&shy;<!-- .element style="color: red;" -->**Class 02** Network Enumeration

**Class 03** Network Segmentation

**Class 04** Routing

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

&shy;<!-- .element style="color: red;" -->**Class 02** Append + Date and Time

**Class 03** File Permissions

**Class 04** Conditionals in Menu Systems

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
  - Ports and Protocols
  - Port Scanning
  - Nmap
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
  - Ports and Protocols
  - Port Scanning
  - Nmap
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 01


---

<!-- .element class="main-title" -->
# Review:

- OSI Model
- Packet Capture
- Traffic Analysis

NOTE:

---

<!-- .element class="title-with-text" -->

# All 7 Layers of the OSI model:

| Layer &emsp; &emsp; &emsp; &emsp; | Address Type | Data Type | Devices/Protocols |
| ----- | ------------ | --------- | ----------------- |
| 7) Application | --- | --- | HTTP, FTP, DNS, DHCP, Computer |
| 6) Presentation | --- | --- | ASCII, JPEG/GIF/PNG, Computer |
| 5) Session | --- | --- | SMB, SIP, Computer |
| 4) Transport | Logical Port Number | Segments | TCP, UDP, Gateway, Load Balancer |
| 3) Network | IP Address | Packets  | Router, Layer 3 Switch (VLAN) |
| 2) Data Link | MAC Address | Frame | L2 Switch, Bridge |
| 1) Physical | Physical Port ID | Bits | Cables, Hub, Repeater |

<br>

<div align="center" style="font-size: 35px">

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->Layers 5, 6 and 7 do not have specific **Address**

&shy;<!-- .element: class="fragment" data-fragment-index="1" -->or **Data Types** associated with them

</div>

NOTE:

### First 4 OSI layers:

- **Layer 1 (Physical):** Deals with physical transmission of data over the medium.
- **Layer 2 (Data Link):** Manages data frames within a local network segment using MAC addresses.
- **Layer 3 (Network):** Uses IP addresses to route data between different networks.
- **Layer 4 (Transport):** Manages data exchange between applications on different devices using port numbers.

### Layers 5, 6, and 7:

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

![Image](/ops-301-guide/curriculum/class-02/slides/assets/01_04.png)
<!-- .element style="width: 90%"-->

</div>

</div>

NOTE:

Image Source: [ScientDirect.com](https://www.sciencedirect.com/topics/computer-science/three-way-handshake) (inherited from old slides; omay not be licensable)

Source: [ChatGPT](https://chat.openai.com/share/18572832-bb05-484e-a9d5-8035cbddb1fa)

What is a packet?
- A packet is a segment of data sent from one computer or device to another over a network
- Remember a package or a letter -- information about sender, destination, etc., attached to a segment of data

What is a packet composed of?
- Header:
  - Source IP Address
  - Destination IP Address
  - Protocol
  - Length
  - Packet Numbers
  - etc.
  - Header data is always un-encrypted
- Payload:
  - Data
  - Payload may be encypted

Three-way handshake:
- TCP protocols use a three-way handshake to establish a session
- SYN > SYN/ACK > ACK

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

![Image](/ops-301-guide/curriculum/class-02/slides/assets/01_05.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: [NetworkManagementSoftware.com](https://www.networkmanagementsoftware.com/review-solarwinds-netflow-traffic-analyzer-3-10-0/) (inherited from old slides; omay not be licensable)



---

<!-- .element class="main-title" -->

# Review:

## Lab 01

NOTE:

---

<!-- .element class="main-title" -->
# Review: Lab


NOTE:
# Review: Previous Lab


- Prompt class for specific questions or areas they'd like covered
- Demonstrate `getmac /s 127.0.0.1` to fetch the MAC address of the Win2019 network adapter.
  - Show IP reservation process on pfSense
  - Show how to clear the "IP is not static" error in Windows Server via manual IP assignment on the network adapter
  - This might be a good time to show what an IP address conflict log looks like, in case they get a system with inconsistent network connectivity and need to look up the log. Symptom was yellow exclamation cycling to normal connectivity.
  - Demonstrate turning off enhanced security in Server Manager > Local Server

HTTP post codes
- GET
  - Show students how navigating to a website performs HTTP GET
- POST
- Sends data to the server
- PUT
- HEAD
- DELETE
- PATCH
- OPTIONS

What is “promiscuous mode”
- Promiscous mode means the NIC/device will pass frames with unicast destination MAC addresses other than its own to the OS.
- In normal mode the NIC will just drop these.
- WiFi is encrypted, so you won’t be able to decode traffic to the other machine. You should be able to see management frames however.
- [source](https://www.reddit.com/r/networking/comments/hhjvrg/promiscuous_mode_am_i_understanding_this_right/)


- Unicast: from one source to one destination i.e. One-to-One
- Broadcast: from one source to all possible destinations i.e. One-to-All
- Multicast: from one source to multiple destinations stating an interest in receiving the traffic i.e. One-to-Many
- [source](https://www.esds.co.in/blog/difference-between-unicast-broadcast-and-multicast/)
- [geeks-for-geeks](https://www.geeksforgeeks.org/difference-between-unicast-broadcast-and-multicast-in-computer-network/)
- [illustration](https://www.esds.co.in/blog/wp-content/uploads/2016/04/Difference-between-unicast-broadcast-and-multicast-diagram.png)


Wireshark default setting - Captures everything
FTP vs SFTP

SFTP (SSH File Transfer Protocol) that sends files over an SSH connection
How (30 min)

How do we use Wireshark to analyze a packet?

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Ports and Protocols
  - Port Scanning
  - Nmap
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 02** - Append + Date and Time

NOTE:

### Review: Ops Challenge 01

### Introduce: Ops Challenge 02 - Append + Date and Time

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Ports and Protocols
  - Port Scanning
  - Nmap
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 02 - Network Enumeration

- Ports and Protocols
- Port Scanning
- Nmap

NOTE:
- Network enumeration is a crucial phase in cybersecurity assessment, aimed at identifying active hosts, open ports, and services running on a network.
- Ports and protocols serve as communication endpoints, each associated with specific services.
- Port scanning, a technique commonly employed in network enumeration, involves systematically probing these ports to unveil potential entry points.
- Nmap, a versatile and widely-used tool, stands out for its ability to conduct comprehensive port scans, providing valuable insights into network topology and potential vulnerabilities.

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


# Ports and Protocols

<div>

<div align="left">

- What ports and protocols do I need to know to pass **CompTIA Network+**?
  - See your study guide for a complete list!
- What types of protocol are there?
  - ICMP
  - UDP
  - TCP
  - IP
  - Connection-oriented vs. connectionless

</div>

<div align="center" style="font-size: 24px">

### Common Ports and Protocols:

| Protocol	| Port Number |
| --------- | ----------- |
| FTP		| 20, 21 |
| SSH		| 22 |
| SFTP		| 22 |
| TELNET	| 23 |
| SMTP		| 25 |
| DNS		| 53 |
| DHCP		| 67, 68 |
| HTTP		| 80 |
| NTP		| 123 |
| HTTPS	    | 443 |
| SMB		| 445 |
| RDP		| 3389 |


</div>

</div>

NOTE:
Indeed, there are various types of network protocols that serve different purposes in data communication. Here are the ones you mentioned:

**ICMP (Internet Control Message Protocol):** ICMP is used for diagnostic and control purposes in IP networks. It's commonly employed for tasks like sending error messages, network testing, and troubleshooting.

**UDP (User Datagram Protocol):** UDP is a connectionless and lightweight protocol that offers low-latency communication. It's often used for tasks that require quick data transmission, such as streaming media or online gaming.

**TCP (Transmission Control Protocol):** TCP is a connection-oriented protocol that ensures reliable data delivery by establishing a connection, acknowledging received data, and retransmitting lost packets. It's used for applications where data integrity is crucial, like web browsing and file transfers.

**IP (Internet Protocol):** IP is the fundamental protocol for routing and addressing packets across networks. It's responsible for the logical addressing and routing of data packets between devices.

**Connection-oriented vs. connectionless:**
- **Connection-oriented:** This refers to protocols like TCP, where a connection is established before data transfer. This ensures reliable and ordered data delivery but might introduce some latency due to the connection setup process.
- **Connectionless:** This refers to protocols like UDP, where data packets are sent without establishing a dedicated connection. While this offers lower latency, it doesn't guarantee the same level of reliability as connection-oriented protocols.

## Common Ports and Protocols:

**FTP (File Transfer Protocol) - 20, 21:** FTP is used for transferring files over a network. Port 21 is used for control commands, while port 20 is used for data transfer.

**SSH (Secure Shell) - 22:** SSH provides secure remote access to systems. It encrypts data during transmission and is widely used for secure command-line access and file transfers.

**SFTP (SSH File Transfer Protocol) - 22:** SFTP is an extension of SSH that provides secure file transfer capabilities, ensuring data integrity and confidentiality.

**TELNET - 23:** TELNET allows remote terminal access to a device over a network. However, it's considered insecure due to transmitting data in plaintext.

**SMTP (Simple Mail Transfer Protocol) - 25:** SMTP is used for sending and relaying email messages between email servers.

**DNS (Domain Name System) - 53:** DNS translates human-readable domain names into IP addresses, enabling users to access websites using easy-to-remember names.

**DHCP (Dynamic Host Configuration Protocol) - 67, 68:** DHCP dynamically assigns IP addresses to devices on a network (server uses port 67, client uses port 68).

**HTTP (Hypertext Transfer Protocol) - 80:** HTTP is the foundation of data communication on the World Wide Web, used to retrieve and display web content.

**NTP (Network Time Protocol) - 123:** NTP synchronizes the clocks of devices on a network to a common time reference, ensuring accurate timekeeping.

**HTTPS (Hypertext Transfer Protocol Secure) - 443:** HTTPS is a secure version of HTTP, encrypting data transmitted between a user's browser and a website.

**SMB (Server Message Block) - 445:** SMB is used for sharing files, printers, and other resources on a network, commonly associated with Windows file sharing.

**RDP (Remote Desktop Protocol) - 3389:** RDP allows remote access and control of a computer's desktop, often used for remote administration.

---

<!-- .element class="split-screen-with-title" -->


# Port Scanning

<div>

<div align="left" style="font-size: 34px">

A port scanner reveals open ports on a target host by sending specially crafter packets and waiting for a response.
- Example: The **`netstat`** command lets you check port states on the local host
- Try **`netstat -an`** to display all connections in numerical format.
- **`netstat -r`** should display the routing table

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_12.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- A port scanner reveals open ports on a target host
  - Example: The `netstat` command lets you check port states on the local host
  - Try netstat -an to display all connections in numerical format.
  - netstat -r should display the routing table

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

- The Nmap Security Scanner is used for scanning remote hosts and networks, either for auditing or pentesting
- Nmap can:
  - Enumerate hosts on a network
  - Enumerate ports open on a host
  - Operate more discreetly or aggressively
  - Perform service fingerprinting to determine what software (OS or applications) might be running on the target host

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-02/slides/assets/0_12.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

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

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 02 - Network Enumeration
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Ports and Protocols
  - Port Scanning
  - Nmap
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Basic Scanning with Nmap

NOTE:

### Import OVA File


### Demo: Basic Scanning with Nmap

