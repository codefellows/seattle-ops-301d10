# Lab: Network Address Translation

## Overview

NAT (Network address translation) is a technique performed by routers whereby the IP address in a packet header is altered in transit so that the destination interprets the packet as coming from the new IP instead of the actual originating IP. One-to-many NAT has played a vital role globally in delaying [IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion){:target="_blank"}, greatly reducing the need to transition at a large scale to IPv6.

In network administration, you may encounter sub-optimal situations where two LANs share the same network addressing scheme. For example, the 192.168.1.1/24 network address is extremely common amongst consumer grade routers. 1:1 NAT can offer a workaround for this kind of issue.

## Scenario

GlobeX has made a strategic acquisition and needs to share resources over a VPN tunnel. However, your manager wishes to obfuscate the corporate network architecture for security reasons. You've been tasked with working up a proof of concept as to how GlobeX can conceal the IP addresses of critical resources such as file servers.

## Prerequisites

- Two networks with pfSense at the edge, connected via IPsec VPN
- Windows 10 in the Corporate network
- Windows 10 in the External network

## Objectives

- Share a folder from the Windows 10 VM on the Corporate network and test normal accessibility both from same LAN and from External network.
- Create a 1:1 NAT rule that alters the IP address of the Corporate Windows 10 for hosts accessing it from over the VPN tunnel.
- Use 1:1 NAT to access the Corporate Windows 10 shared folder from External Windows 10  without using Coporate Windows 10's real local IP address.

## Resources

- [Netgate Docs - 1:1 NAT](https://docs.netgate.com/pfsense/en/latest/nat/1-1.html){:target="_blank"}
- [Troubleshooting NAT](https://docs.netgate.com/pfsense/en/latest/troubleshooting/nat.html){:target="_blank"}
- [Troubleshooting NAT 1:1](https://docs.netgate.com/pfsense/en/latest/troubleshooting/nat-1-1.html){:target="_blank"}
- [Troubleshooting NAT Port Forwards](https://docs.netgate.com/pfsense/en/latest/troubleshooting/nat-port-forwards.html){:target="_blank"}

## Tasks

### Part 1: Topology 1/2

Read through the entire lab and use Draw.io to create an appropriate topology of the network you expect to construct. Include as many details as you can such as computer names, OS types, IP addresses, etc. Include a screenshot of this initial topology.

### Part 2: Staging the Networks

This lab requires that you've established a VPN tunnel between two pfSense networks in VirtualBox.

- Share a folder on the Corporate Windows 10.
- From another VM on the Corporate (internal) network, access the shared folder. Create a file. Include a screenshot of this operation.
- From External Windows 10, access the shared folder via VPN. Create a file. Include a screenshot of this operation.
- On each Windows 10, [create a firewall rule to allow ICMP traffic](https://www.how2shout.com/how-to/allow-windows-10-ping-through-firewall-gui-powershell-netsh-command.html). This will make testing your network easier, and will help you diagnose problems with you network vs problems with the fileshare.
> Hint: if you are having trouble accessing the shared folder, try disabling Windows Firewall.

### Part 3: Configuring the Networks

Now that we have established normal comms between the networks, and know that the file share is working, let's start experimenting with NAT. We can use a 1:1 NAT rule in pfSense to convert the IP address of our Corporate Windows 10 for VPN users.

- In pfSense, utilize 1:1 NAT to convert the file server IP to a different IP if accessed via VPN tunnel.
- To accomplish this, you can use the 1:1 NAT features built into IPsec VPN in pfSense.
- Include a screenshot of your configuration.

### Part 4: Testing

Now let's test and verify that the NAT is translating the IP address correctly and that we can access the shared folder from the External Windows 10.

- Mount the file share on the External Windows 10.
- Include a screenshot of successfully accessing the file share in Windows Explorer.

### Part 5: Topology 2/2

When the other tasks are complete, review the topology and update, revise, extend, or add details as necessary.

Was your initial topology accurate to the finished product? Why or why not?

## Submission Instructions

1. Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
1. Name the document according to your course code and assignment.
   - i.e. `seattle-ops-201d1: Lab 04`.
1. Add your name & date at the top of the Google Doc.
1. Share your Google Doc so that "Anyone with the link can view".
1. Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
