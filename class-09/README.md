# Class 09

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

Configuring the network for optimal visibility by security tools is essential in the modern era. One method involves duplicating or "mirroring" network traffic to a sniffing tool. This allows the tool to see all traffic passing through the mirrored interface.

## How does this topic fit?

**Where we've been**:
In the previous class we deployed a network access control system in the form of FreeRADIUS.

**What are we focusing on today**:
Today we'll be duplicating packets by bridging an interface in pfSense.

**Where we're headed**:
In the next class, we'll be working doing cloud computing with AWS.

## Traffic Mirroring

### Why
- Network traffic mirroring allows network administrators and IT professionals to capture and analyze network traffic in real-time or retrospectively. This capability is invaluable for diagnosing and troubleshooting network issues. By inspecting the mirrored traffic, they can identify the root causes of network slowdowns, outages, or abnormal behavior.
- Network traffic mirroring is a fundamental tool for cybersecurity. Security teams can use it to monitor network traffic for signs of malicious activity, such as intrusion attempts, malware infections, and data exfiltration. By analyzing mirrored traffic, they can detect and respond to security threats more effectively.
- In the event of a security breach or incident, network traffic mirroring provides a valuable source of evidence for digital forensics. It allows investigators to reconstruct the timeline of events, identify the attack vectors, and determine the extent of the breach. This information is crucial for incident response and legal proceedings.
- Understanding network traffic patterns through mirroring can help organizations optimize their network infrastructure. By analyzing the volume and nature of traffic, administrators can make informed decisions about network capacity, load balancing, and resource allocation. This can lead to better overall network performance and cost savings.
- Network traffic mirroring can be used to monitor the quality of service provided to network applications and users. It helps ensure that critical applications receive the necessary network resources and that QoS policies are enforced effectively.
- Network traffic mirroring allows organizations to enforce network usage policies and monitor compliance with internal policies. It helps ensure that employees or users are not engaging in activities that violate company rules or introduce security risks.

### What
- _______ is the process of copying and forwarding network traffic from one network segment or device to another for analysis and monitoring.
- _______ is a network interface mode that allows a network card to capture all traffic on a network segment, not just traffic destined for its own MAC address.
- _______ is a hardware device that provides a passive way to capture network traffic by physically tapping into a network cable.
- _______ is a feature on network switches that allows traffic from one or more ports to be mirrored to a designated monitoring port for analysis.
- _______ is the specific port on a network switch or router where mirrored traffic is sent for monitoring and analysis.
- _______ is a set of rules or criteria used to filter which network packets are captured and analyzed by a packet sniffer or network analyzer.
- _______ is the storage area or memory allocated for temporarily storing captured network packets for analysis.
- _______ is the practice of monitoring and analyzing network traffic to assess the performance of applications and services running on a network.

### How
Network traffic mirroring involves duplicating and redirecting network traffic from one part of a network to another. Here's a step-by-step breakdown of how traffic mirroring works:
- **Identify the Need for Traffic Mirroring**
  - The process begins by identifying the specific need for traffic mirroring. This could be for troubleshooting network issues, monitoring network performance, or enhancing cybersecurity.
- **Configure the Mirroring Source**
  - Determine which network segment or device's traffic you want to mirror. This could be a specific network switch port, a segment of the network, or an entire network device, depending on your objectives.
- **Identify the Mirroring Target**
  - Choose where you want to send the duplicated traffic for analysis. This is typically referred to as the "monitoring port" or "mirror port." It's a separate network port or device where the mirrored traffic will be sent.
- **Set Up the Mirroring Session**
  - Configure the network device responsible for traffic mirroring, such as a network switch or router. This involves specifying the source and target ports for the mirroring session. In Cisco terminology, this feature is known as SPAN (Switched Port Analyzer).
- **Mirroring Configuration**
  - Define the specific traffic to be mirrored. You can set up filters or rules to determine which packets should be copied to the monitoring port. This helps reduce the volume of traffic sent to the monitoring tool and ensures that you capture only the relevant data.
- **Duplicate and Redirect Traffic**
  - As network traffic flows through the source port, the network device copies the packets based on the configured rules and forwards them to the monitoring port. The original traffic continues its normal path through the network.
- **Analyze the Mirrored Traffic**
  - At the monitoring port, you have a network analyzer or packet capture tool (like Wireshark) connected. This tool receives the duplicated traffic and captures it for analysis.
- **Data Storage and Analysis**
  - The captured network packets can be stored in a file for further analysis. This data can be used for real-time monitoring, historical analysis, or forensics, depending on the goals of the mirroring session.
- **Interpretation and Action**
  - Network administrators or security analysts review the captured data to gain insights into network performance or security incidents. Depending on what they find, they may take corrective actions, configure network settings, or investigate security breaches further.
- **Monitoring and Maintenance**
  - Traffic mirroring is an ongoing process. Network administrators may continuously monitor network traffic or set up periodic mirroring sessions to keep an eye on network performance and security.

### Experimentation and Discovery Ideas
- Imagine you're a network administrator responsible for maintaining a large corporate network. What challenges or issues might you encounter that could lead you to consider implementing traffic mirroring?
- How do you think network administrators decide which traffic to mirror and analyze? What factors might influence their choices?
- Suppose you've set up a traffic mirroring session to monitor network traffic for security purposes. What specific types of security threats or suspicious activities might you be looking for in the mirrored traffic?
- How might traffic mirroring be used beyond troubleshooting and security monitoring? Can you think of other potential applications or scenarios where mirroring network traffic could be beneficial?
- Traffic mirroring can generate a significant volume of data for analysis. How could data storage and management become a challenge in this context? What strategies might you employ to handle and store the captured traffic data effectively?
- Consider the ethical implications of traffic mirroring. When is it appropriate to monitor and mirror network traffic, and are there situations where it might raise concerns about privacy or consent?

## Learning Objectives

### Students will be able to

#### Describe and Define

- Span port
- Interface bridge
- Traffic mirroring
- Sniffing

#### Execute

- Students should be able to configure pfSense to mirror LAN traffic to a specific interface, create bridge configurations, and associate the bridge with the LAN interface.
- Students should be able to use Wireshark on Kali to capture network traffic on the designated "span" connection.

## Helpful Resources

- [pfSense Docs - Interface Bridges](https://pfsense-docs.readthedocs.io/en/latest/interfaces/interface-bridges.html){:target="blank"}
- Professor Messer:
  - [Port Mirroring](https://www.professormesser.com/network-plus/n10-005/port-mirroring-2/){:target="blank"}
  - [Interface Configurations](https://www.professormesser.com/network-plus/n10-008/n10-008-video/interface-configurations-n10-008/){:target="blank"}

## Notes

- What are the key differences between passive and active network monitoring, and when might you choose one approach over the other for traffic analysis?
- What are the potential security risks associated with traffic mirroring, and how can these risks be mitigated to protect sensitive data and privacy?
- How does network traffic encryption (e.g., HTTPS) impact the effectiveness of traffic mirroring and packet analysis for security monitoring? Are there ways to inspect encrypted traffic?
- What role does network bandwidth play in traffic mirroring, and how can you ensure that the mirroring process does not negatively impact network performance?
- Are there legal or compliance considerations when implementing traffic mirroring, particularly in industries with strict data protection regulations? How can organizations ensure they are in compliance?
- How can you use captured network traffic data to identify and respond to specific security threats, such as Distributed Denial of Service (DDoS) attacks or malware infections?
- Are there emerging technologies or trends in network traffic analysis that professionals in this field should be aware of, such as the integration of artificial intelligence or machine learning? Explain your reasoning.
- Can you explain the concept of "packet loss" in the context of traffic mirroring and how it can affect the accuracy of network monitoring and analysis?
- What are some common challenges and best practices when it comes to scaling traffic mirroring for large, complex networks with multiple segments and high traffic volumes?
