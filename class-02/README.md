# Class 02

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

The network mapping tool Nmap is an open source, command line utility commonly used in network discovery ("enumeration" in offensive terms), security auditing, and pentesting. Nmap can audit whether ports are open or closed on a target host.

Today you will perform a series of basic scanning operations using Nmap and learning more about network ports and protocols.

## How does this topic fit?

**Where we've been**:
Previously we studied network traffic analysis using Wireshark.

**What are we focusing on today**:
Today, we'll be using Nmap to scan for network ports.

**Where we're headed**:
In the next class we'll be exploring network segmentation.

## Network Scanning with NMAP

### Why
- Nmap helps in discovering devices and hosts on a network. This is crucial for network administrators to maintain an up-to-date inventory of all devices connected to the network. It aids in identifying unauthorized or rogue devices, as well as potential security vulnerabilities that might be present in the network.
- Nmap can be used to perform security assessments of networks, identifying open ports, services, and potential vulnerabilities. By understanding what services are running on network devices, administrators can take proactive steps to secure and patch vulnerable systems.
- Nmap can be used to test the effectiveness of firewalls and intrusion detection systems. By simulating various scan types and techniques, administrators can evaluate how well their network defenses are holding up against potential attackers.
- Nmap can assist in ongoing network monitoring by providing insights into the status of network devices, services, and ports. This helps administrators detect any changes or anomalies that might indicate a security breach or system malfunction.
- Ethical hackers and penetration testers often use Nmap to gather information about a target network before attempting to exploit vulnerabilities. This helps them understand potential attack vectors and plan their strategies accordingly.
- Understanding the services and ports that are active on devices can help network administrators optimize network traffic and resource allocation. Unnecessary or insecure services can be disabled or reconfigured for better performance and security.
- In the event of a security incident, Nmap can be used to quickly assess the extent of the compromise and identify affected systems. This information is crucial for timely and effective incident response.

### What
- _______ is the process of systematically investigating a network to discover active hosts, open ports, and services running on those hosts.
- _______ is a logical endpoint for communication on a network device. Ports are numbered and associated with specific protocols (e.g., port 80 for HTTP).
- _______ is a controlled and authorized attempt to exploit vulnerabilities in a system to identify security weaknesses. Also known as ethical hacking.
- _______ is a person who uses hacking techniques to identify and fix security vulnerabilities, rather than exploiting them for malicious purposes.
- _______ is the act of sending packets to a range of port numbers on a target system to determine which ports are open and potentially vulnerable.
- _______ is the process of gathering information about hosts on a network, including their IP addresses, open ports, and services.
- _______ stands for Transmission Control Protocol/Internet Protocol. A suite of networking protocols that defines how data is sent and received over the internet.
- _______ is a connectionless protocol that operates at the transport layer of the TCP/IP model. It's often used for tasks that require quick data transmission, such as real-time video streaming.
- _______ is a network protocol used to send error messages and operational information about network conditions.
- _______ is adhering to industry-specific regulations and standards related to security and data protection.
- _______ is a record of all devices and resources (hardware, software, and data) within a network.
- _______ is the process of identifying and evaluating potential risks and vulnerabilities in a system or network.
- _______ is dividing a network into smaller segments to improve security and manageability.

### How
- Prepare a network environment and stage Kali Linux
- Port scanning with Nmap
- Reporting Nmap findings
- Explore some protocol-related capabilities of Wireshark
- Run a `netstat` command to show all active ports

### Experimentation and Discovery Ideas
- Imagine you're responsible for managing the security of a network. What are some potential reasons you might want to conduct a network scan? How might such scans help you identify vulnerabilities or weaknesses?
- Before diving into the technical details, let's consider the ethical aspects. What ethical considerations should be taken into account when conducting network scans, especially on systems you don't own? How might you balance the need for security with respecting the privacy of others?
- Imagine you want to scan a network for open ports. What might be the significance of identifying open ports on a target system? How might this information be useful to an attacker? Conversely, how might it be useful to a system administrator trying to secure their network?
- NMAP provides different scanning options, such as TCP, UDP, and SYN scans. Can you think of situations where one scan might be more suitable than the others? What are the advantages and disadvantages of these scan types?
- Let's talk about "fingerprinting" in the context of NMAP. What is OS fingerprinting, and why might someone want to determine the operating system of a target system? How might OS fingerprinting be accomplished using NMAP?
- NMAP scripting engine (NSE) allows for custom scripts to be run during scans. Why do you think this feature might be valuable? Can you think of any scenarios where custom scripts could provide insights beyond what standard scans offer?
- As you explore NMAP, you might encounter difficulties or unexpected results. What's your plan for troubleshooting and resolving issues as you experiment with different scanning techniques and options? How might a growth mindset play a role in overcoming challenges?
- Imagine you've gained a deep understanding of NMAP and its capabilities. How might you leverage this knowledge to enhance your career prospects, contribute to cybersecurity efforts, or even educate others?

## Learning Objectives

### Students will be able to

#### Describe and Define

- Network Enumeration
- Nmap
- Service Fingerprinting
- Network ports
- Port scanning

#### Execute

- Perform port scans using Nmap.

## Helpful Resources

- [Wireshark Docs on the "Protocol Hierarchy" Window](https://www.wireshark.org/docs/wsug_html_chunked/ChStatHierarchy.html#:~:text=This%20is%20a%20tree%20of,be%20shown%20at%20the%20bottom.){:target="blank"}

## Notes

- What ports and protocols do I need to know to pass CompTIA Net+?
- What types of Transport Layer (Layer 4) protocols are there?
- What types of Network Layer (Layer 3) protocols are there?
