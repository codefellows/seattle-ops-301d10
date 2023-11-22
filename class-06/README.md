# Class 06

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

NAT (Network address translation) is a technique performed by routers whereby the IP address in a packet header is altered in transit so that the destination interprets the packet as coming from the new IP instead of the actual originating IP. NAT has played a vital role globally in delaying [IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion){:target="blank"}, greatly reducing the need to transition at a large scale to IPv6.

## How does this topic fit?

**Where we've been**:
In the previous class we established a VPN tunnel between two sites.

**What are we focusing on today**:
Today we'll be continuing from that setup and using NAT to translate IPs between the sites.

**Where we're headed**:
Next class we'll be spinning up our own Linux-based web server.

## Network Address Translation

### Why
- NAT allows multiple devices on a local network to share a single public IP address. This is crucial due to the limited availability of IPv4 addresses. With NAT, organizations and households can connect multiple devices to the internet without needing a unique public IP address for each one.
- NAT provides a level of security by acting as a barrier between the public internet and the private local network. Inbound traffic from the internet is typically blocked or restricted, only allowing responses to outgoing requests initiated from within the local network. This helps in preventing unsolicited incoming connections and potential attacks.
- NAT helps isolate the devices on a local network from the outside world. Devices within the local network are not directly reachable from the public internet, adding an extra layer of protection against external threats.
- NAT allows an organization to use private IP addresses on its local network, which aren't globally unique. This simplifies internal network configuration and management. Only the NAT gateway needs a public IP address, while devices within the network can use private IP addresses that don't need to be registered globally.
- As the world transitions from IPv4 to IPv6 (which offers a vastly larger address space), NAT can serve as a transitional mechanism. It allows IPv4 devices to coexist with IPv6 devices by providing a method to connect between the two address types.
- NAT enables the design of complex networks with different segments using private IP addresses. This design flexibility is particularly useful for larger organizations that need to segregate and control their internal network traffic effectively.
- In cases where different organizations or networks might be using the same private IP address ranges, NAT helps prevent address collisions by allowing these overlapping networks to communicate with the external world using a shared public IP address.
- NAT can be used for load balancing across multiple servers or services within a network. By mapping requests to different internal servers, NAT can distribute the load effectively.
- NAT devices can keep logs of the traffic passing through them, aiding in troubleshooting, monitoring network activity, and analyzing potential security breaches.

### What
- _______ is an IP address used within a private network that is not globally routable on the public internet. Examples include addresses from ranges like 192.168.0.0/16 and 10.0.0.0/8.
- _______ is an IP address that is globally routable on the public internet and used to identify a device or network on the internet.
- _______ is the device responsible for translating private IP addresses to a single public IP address and vice versa, enabling communication between devices in a private network and the public internet.
- _______ is the private IP address assigned to a device within the local network.
- _______ is the public IP address assigned to a device within the local network after translation by the NAT gateway.
- _______ is the private IP address of a remote device on the internet.
- _______ is the public IP address of a remote device on the internet after translation by the NAT gateway.
- _______ is a type of NAT where a one-to-one mapping is created between an inside local address and an inside global address. It's often used for servers that need to be directly accessible from the internet.
- _______ is a type of NAT where multiple inside local addresses are mapped to a pool of inside global addresses, allowing many devices to share a limited number of public IP addresses.
- _______ is also known as NAT Overload, it's a variation of dynamic NAT where both IP addresses and port numbers are used to map multiple devices to a single public IP address.
- _______ is the process of sharing a single public IP address among multiple devices using port-based differentiation, as in PAT.
- _______ is a network segment that sits between the internal network and the external internet, often used to host publicly accessible services while protecting the internal network.
- _______ traffic flows from the external network to the internal network, while _______ traffic flows from the internal network to the external network.
- _______ is a firewall or NAT router's ability to keep track of the state of active connections and allow only legitimate traffic.

### How
- The lab involves setting up and configuring Network Address Translation (NAT) using pfSense routers.
- The major concepts covered in this lab include:
  - **Network Address Translation (NAT)**: Understanding how NAT works, its role in altering IP addresses in packet headers, and the types of NAT rules that can be created.
  - **VPN Tunneling**: Understanding the concept of a Virtual Private Network (VPN) tunnel and how it enables secure communication between two networks.
  - **1:1 NAT Rule**: Understanding the concept of one-to-one NAT, where a specific internal IP address is mapped to a unique external IP address.
  - **Firewall Rules**: Learning how to create firewall rules to control traffic and ensure proper communication between devices.
  - **IPsec VPN Configuration**: Configuring a secure VPN tunnel between two pfSense networks.
  - **File Sharing**: Setting up and testing shared folders between Windows 10 machines.
  - **Network Topology Design**: Designing and representing the network topology using tools like [Draw.io](https://app.diagrams.net/){:target="_blank"}.
- In the demo, using our preconfigured a VPN tunnel, we will learn how to set up shared folders on Windows 10 VMs, and understand the principles of altering IP addresses using NAT rules.

### Experimentation and Discovery Ideas
- Imagine you're responsible for managing a network where multiple devices need to access a public server using the same public IP address. How might you implement NAT to enable these devices to communicate with the server while sharing that single IP address?
- In the lab scenario, why do you think the manager wants to conceal the IP addresses of critical resources over the VPN tunnel? What potential security advantages might this approach offer?
- The lab mentions creating a 1:1 NAT rule. Can you explain why such a rule might be necessary and how it differs from other NAT configurations? How does this rule address the issue of IP address conflicts?
- While setting up the shared folder, one of the tasks involves creating a firewall rule to allow ICMP traffic. Why is this important, and how might it help in diagnosing issues related to network communication?
- The lab highlights the concept of "obfuscating the corporate network architecture for security reasons." What are some potential risks associated with this approach, and how can network administrators balance the need for security with the need for efficient and accessible network resources?
- As we transition to IPv6, what challenges might arise in the context of NAT? Will NAT still be relevant, and if so, how might its role change in the face of the expanded address space offered by IPv6?
- In the lab, students are asked to update their initial network topology based on the completed tasks. Why is this step important, and what insights can you gain from comparing the initial design with the final configuration? How might this process help identify areas for improvement in network planning and implementation?

## Learning Objectives

### Students will be able to

#### Describe and Define

- Network types
- Network access models
- NAT
- IPv4 vs IPv6
- IP address exhaustion

#### Execute

- Sharing a folder from a Windows 10 VM on the Corporate network.
- Testing accessibility of the shared folder both within the same LAN and from the External network.
- Creating a 1:1 NAT rule to alter the IP address of the Corporate Windows 10 for hosts accessing it over the VPN tunnel.
- Using 1:1 NAT to access the shared folder from External Windows 10 without using the real local IP address of Corporate Windows 10.

## Helpful Resources

- [Netgate Docs - 1:1 NAT](https://docs.netgate.com/pfsense/en/latest/nat/1-1.html){:target="blank"}
- [AWS VPC - NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html){:target="blank"}

## Notes

- At what layer of the OSI model does NAT operate?
- What happens to packets when NAT runs out of addresses in the pool of available IPs?
