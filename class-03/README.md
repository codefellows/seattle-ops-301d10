# Class 03

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

By designing a network to control how traffic flows among its parts, we can achieve network segmentation. Benefits of segmentation include improvements to operational performance, reduction of cyber attack surface, additional protection for vulnerable devices, and a reduction in scope of regulatory compliance. Today you will practice designing a network to achieve a specified segmentation requirement.

## How does this topic fit?

**Where we've been**:
In the previous class we worked with the network mapping tool Nmap.

**What are we focusing on today**:
Today, we'll be exploring network segmentation.

**Where we're headed**:
Next class we will be exploring routing protocols.

## Network Segmentation

### Why
- If a breach or compromise occurs, network segmentation limits the lateral movement of attackers. This containment prevents them from easily accessing other parts of the network.
- By restricting communication paths, you reduce the attack surface available to potential threats. This makes it harder for attackers to exploit vulnerabilities across the entire network.
- Network segmentation allows you to enforce specific access controls based on user roles, device types, or other criteria. This ensures that users and devices only access the resources they are authorized for.
- Segmentation can help allocate bandwidth more effectively, ensuring critical applications have the necessary resources without being affected by non-essential traffic.
- Segmentation allows for separate environments for development, testing, and production. This prevents testing activities from impacting production systems and vice versa.
- In environments that require guest access, segmentation provides a secure way to isolate guest traffic from internal systems.
- Smaller segments are easier to manage and monitor, leading to improved network performance and easier troubleshooting.
- Many IoT devices have limited security features. Segmenting these devices from critical parts of the network can prevent compromised IoT devices from affecting the rest of the infrastructure.
- In the event of a network breach or failure, segmented backup networks can ensure that critical data remains isolated and accessible for disaster recovery.

### What
- _______ is the practice of dividing a larger network into smaller, isolated segments to enhance security, access control, and network management.
- _______ is a distinct and isolated portion of a network with its own set of security policies, access controls, and communication boundaries.
- _______ are rules or lists of permissions that dictate which users, devices, or applications are allowed or denied access to specific network resources.
- _______ is a logical network segment created within a physical network, allowing devices to communicate as if they are on the same physical network even if they are not.
- _______ is a range of IP addresses within a larger network that are grouped together based on a common subnet mask.
- _______ is a network segment that is isolated from the internal network and is used to host public-facing services, such as web servers, to reduce exposure to potential threats.
- _______ is a more granular form of network segmentation where each individual workload or device is isolated from others, enhancing security within the same segment.
- _______ is the practice of separating devices, applications, or services from one another to prevent unintended or unauthorized communication.
- _______ is network communication that occurs between devices within the same segment, as opposed to traffic flowing from external sources (north-south traffic).
- _______ is network communication that occurs between devices in different network segments, often involving external sources like the internet.

### How
- The lab involves designing and configuring a network with network segmentation using VLANs (Virtual LANs) to achieve several objectives. These objectives include improving operational performance, reducing the attack surface for cyber attacks, protecting vulnerable devices, and complying with regulatory requirements.
- Some major concepts that need to be tackled in this lab include:
  - **Network Segmentation:** This involves dividing the network into separate segments using VLANs to control traffic flow and enhance security.
  - **VLANs:** Understanding what VLANs are and how they work is crucial. VLANs are used to separate broadcast domains and logically group devices within a network.
  - **Trunking:** Configuring trunk interfaces between switches to allow VLAN traffic to pass between them.
  - **IP Addressing and Subnetting:** Setting up IP addresses and subnet masks on devices, including configuring default gateways for communication.
  - **Basic Network Configuration:** Initializing devices, attaching them in the network topology, and configuring initial settings.
- In the demo and lab, we will be working with Cisco Packet Tracer, a network simulation tool, to create a network topology that involves switches and PCs.

### Experimentation and Discovery Ideas
- Imagine you're responsible for designing a network for a company with sensitive financial data. How could network segmentation play a role in protecting this data from both external and internal threats? What specific measures might you take?
- What are the potential drawbacks or challenges of network segmentation? How might it impact the user experience, and what strategies could you employ to mitigate these challenges?
- Consider the scenario mentioned in the lab text, where VLANs are used to create network segments. How do VLANs contribute to achieving network segmentation goals? Can you think of any other methods that could achieve similar results?
- In the lab, why is it important to manually configure the trunk interface settings after using Dynamic Trunk Protocol (DTP)? What potential risks or benefits does this manual configuration offer?
- How does microsegmentation differ from traditional network segmentation? What benefits might it provide, especially in modern, complex network environments?
- Often, regulatory compliance is mentioned as a reason for implementing network segmentation. How does network segmentation help organizations meet compliance requirements? Can you think of specific industries or regulations where this might be particularly important?
- In the stretch goals of the lab, you're asked to introduce a router for inter-VLAN routing. Why might inter-VLAN routing be necessary, and how does it impact network design and communication between segments?
- Let's explore a hypothetical scenario. You're managing a network for a large hospital. How could network segmentation be employed to balance the need for medical devices to communicate while maintaining strict security for patient data?

## Learning Objectives

### Students will be able to

#### Describe and Define

- Subnet
- Subnet mask/netmask
- CIDR
- CIDR block notation
- Network address
- Network segmentation
  - Logical
  - Physical
- Interface
- Microsegmentation
- Virtual LANs (VLANs)

#### Execute
- **Build a network and configure basic device settings**
  - Deploy switches and PCs according to a topology diagram.
  - Initialize switches and configure basic settings.
  - Configure IP addresses on PC hosts.
- **Create VLANs and assign switch ports**
  - Create VLANs on the switches.
  - Assign VLANs to the correct switch interfaces.
  - Assign PCs to specific VLANs based on the IP addressing table.
- **Configure an 802.1Q Trunk between switches**
  - Use Dynamic Trunk Protocol (DTP) to enable trunking on a specific interface.
  - Manually configure trunk interface settings, including switchport modes, to allow VLAN traffic to pass between switches.

## Helpful Resources

- [Subnet Practice](https://subnetipv4.com/){:target="_blank"}
- [Subnetting Implementation in Cisco Packet Tracer](https://www.geeksforgeeks.org/subnetting-implementation-in-cisco-packet-tracer/){:target="_blank"}
- [What is VLAN?](https://www.guru99.com/vlan-definition-types-advantages.html#9){:target="_blank"}
- [Configuring VLANs and Trunking](https://sites.radford.edu/~hlee3/classes/backup/itec451_spring2017/Cisco/CCNA2_RSE_spring2017/Lab%20Source%20Files_solutions/6.2.2.5%20Lab%20-%20Configuring%20VLANs%20and%20Trunking%20-%20solution.pdf){:target="_blank"}
- [Basic VLAN Configuration](https://courses.cs.ut.ee/2012/NT/juh/3_1.pdf){:target="_blank"}

## Notes

- What does the final digit after the “/” represent in an IPv4 address?
