# Class 05

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

The VPN protocol can be used in several ways; everyday computer users are likely familiar with client VPN services that claim to grant privacy to their customers. Another way to use VPN is to establish a private network connection between two computers (client-server VPN). Today you'll join two separate networks using IPsec Site-to-Site VPN Tunnelling via pfSense's built-in IPsec tunnelling capabilities.

## How does this topic fit?

**Where we've been**:
In the previous class we studied WANs and routing protocols.

**What are we focusing on today**:
Today, we'll be doing VPN configuration between two routers.

**Where we're headed**:
Next module's theme is "network infrastructure." Expect more pfSense tinkering.

## VPN Tunnel

### Why
- A VPN creates a secure encrypted tunnel between your device and the VPN server. This encryption ensures that your internet traffic, including sensitive information like passwords, credit card details, and personal communications, is protected from potential eavesdropping and cyberattacks, such as man-in-the-middle attacks.
- When using public Wi-Fi networks, your data is often transmitted over open channels, making it vulnerable to interception by hackers and cybercriminals. A VPN encrypts your connection, making it safer to use public Wi-Fi networks, such as those found in coffee shops, airports, and hotels.
- Some websites, streaming services, and online content might be restricted based on your geographical location. A VPN can allow you to connect to servers in different countries, effectively masking your IP address and granting you access to content that might otherwise be unavailable in your region.
- A VPN hides your real IP address by routing your traffic through a server located in a different location. This helps protect your online identity and browsing habits from advertisers, websites, and even your internet service provider (ISP), which may otherwise track and sell your data.
- In countries where internet access is restricted or heavily censored, a VPN can help users bypass these restrictions by tunneling their traffic through servers in more open regions. This allows users to access a freer and more open internet.
- For businesses, a VPN is often used to create secure connections for remote employees who need to access company resources and data from external locations. This ensures that sensitive business information remains protected even when accessed from outside the company network.
- Some ISPs may deliberately slow down (throttle) your internet connection when they detect certain types of traffic, such as streaming or downloading. Using a VPN can help bypass these restrictions, as your ISP won't be able to easily identify the type of traffic you're generating.

### What
- _______ is a technology that creates a secure, encrypted connection over a public network (usually the internet), allowing users to send and receive data as if they were directly connected to a private network.
- _______ is the process of converting data into a code to prevent unauthorized access. VPNs use encryption to secure the data transmitted between your device and the VPN server.
- _______ is a numerical label assigned to each device connected to a computer network. With a VPN, your original IP address is masked, making it harder to track your online activities.
- _______ is a computer or system that provides services or resources to other computers, known as clients. In the context of a VPN, servers are located in various geographic locations to allow users to connect and route their traffic through them.
- _______ is a device or software that connects to a server to access services or resources. In the case of a VPN, the software on your device that connects to the VPN server is the client.
- _______ is a set of rules and conventions that define how data is formatted and transmitted over a network. VPNs use different protocols to establish connections, such as OpenVPN, L2TP/IPsec, IKEv2, and more.
- _______ is the process of encapsulating one network protocol within another. VPNs use tunneling protocols to create a secure pathway for data transmission.
- _______ are the algorithms and methods used to encrypt and secure data transmitted over the VPN connection. Examples include AES (Advanced Encryption Standard) and RSA (Rivest-Shamir-Adleman).
- _______ is a company that provides internet access to customers. A VPN helps protect your data from being monitored or tracked by your ISP.
- _______ is the maximum data transfer rate of a network or internet connection. Using a VPN can slightly reduce your available bandwidth due to the overhead of encryption.
- _______ is the practice of recording and storing data about user activities on a network or service. It's important to choose a VPN provider with a strict no-logs policy to ensure your activities are not recorded.
- _______ is a feature in VPN software that automatically disconnects your internet connection if the VPN connection drops. This prevents your unencrypted data from being exposed.
- _______ are restrictions placed on internet content based on geographical location. VPNs can help bypass these restrictions by allowing you to connect to servers in different regions.
- _______ is a security process that requires users to provide two or more authentication factors to access an account. Some VPNs offer MFA to enhance account security.
- _______ is a network model where computers directly communicate and share resources without a central server. Some VPNs support P2P file sharing and torrenting.
- _______ is a feature that allows external devices or servers to access specific services on your device through the VPN tunnel.
- _______ is the state of being anonymous or unidentifiable online. While VPNs enhance anonymity, they don't provide complete anonymity.
- _______ is the suppression or restriction of information or communication. VPNs can help users bypass censorship by providing access to a more open internet.

### How
- The lab involves setting up a VPN tunnel between two separate networks using pfSense's built-in IPsec tunneling capabilities. This will allow the networks to communicate securely over the internet as if they were part of the same private network. We will need to configure the pfSense devices on both networks, establish the VPN tunnel with specific encryption settings, and troubleshoot any connectivity issues that may arise.
- The major concepts covered include:
  - Understanding VPN protocols, specifically IPsec and its components like Phase 1 and Phase 2 settings.
  - Configuring VPN parameters such as encryption methods, key exchange methods, and lifetimes.
  - Working with network address translation (NAT) to simulate an over-internet connection.
  - Adjusting firewall rules to permit traffic through the VPN tunnel.
  - Troubleshooting connectivity issues using logs and diagnostic tools.
  - Creating a network topology diagram to visualize the interconnected devices.
- In the demo and lab, we will be performing hands-on configurations related to setting up a VPN tunnel using pfSense as the platform for implementation.

### Experimentation and Discovery Ideas
- Can you think of any real-world scenarios where VPN tunneling could be beneficial?
- Imagine you're sending sensitive information over the internet. How could VPN tunneling's encryption help protect that information from potential eavesdropping?
- What encryption methods have you heard of, and how might they be used in VPN tunneling to ensure data security?
- VPNs are known to slightly reduce internet speed due to encryption. Why might users still choose to use a VPN despite this trade-off?
- What are some potential downsides of using a VPN? How might VPNs impact your online experience in terms of access to region-specific content or services?
- Why might different VPN protocols exist? What factors could influence someone's choice of protocol?
- What does it mean to "mask" your IP address using a VPN? Can VPNs truly provide complete online anonymity?
- Reflect on the statement that VPN providers can potentially see your activities. What implications does this have for privacy?
- Can you think of any ethical considerations related to using a VPN to bypass region-based content restrictions?
- In what scenarios might businesses use VPN tunneling? How could it enhance security for remote employees accessing company resources?
- Why might a business choose to set up a site-to-site VPN, as opposed to a client-server VPN?
- If you were tasked with creating a topology diagram to represent a VPN network setup, what key components and connections would you include?

## Learning Objectives

### Students will be able to

#### Describe and Define

- VPN Tunnel
- Site-to-site VPN tunnel
- Split tunnel
- Client-server VPN
- IPsec VPN protocols
  - AH
  - ESP
  - SA
  - IKE

#### Execute

- Configuring pfSense devices to handle the VPN connection, including adjusting settings for logging, interfaces, and security.
- Defining encryption settings for Phase 1 and Phase 2 of the VPN connection.
- Creating firewall rules to allow traffic through the VPN tunnel.
- Verifying connectivity status and troubleshooting any issues using pfSense's IPsec status indicators and system logs.
- Performing a ping test from pfSense and a host computer to ensure successful communication across the VPN tunnel.
- Creating a network topology diagram using a tool like [Draw.io](https://app.diagrams.net/){:target="_blank"} to visualize the setup.

## Helpful Resources

- [Configuring a Site-to-Site IPsec VPN](https://docs.netgate.com/pfsense/en/latest/recipes/ipsec-s2s-psk.html){:target="_blank"}
- [Troubleshooting IPsec VPNs](https://docs.netgate.com/pfsense/en/latest/troubleshooting/ipsec.html){:target="_blank"}
- [Draw.io](https://app.diagrams.net/){:target="_blank"}

## Notes

### Legal Considerations

**Copyright and Piracy:**
  - Legal Use: VPNs can be used for legitimate purposes like securing online transactions and accessing region-specific content. Some countries have more lenient copyright laws.
  - Illegal Use: Using a VPN for downloading copyrighted content without proper authorization or licenses is illegal and considered piracy in many jurisdictions.

**Cybercrime and Hacking:**
  - Legal Use: Using a VPN for securing communications and protecting personal information from cyber threats is legal.
  - Illegal Use: Engaging in hacking, cyberattacks, or any illegal online activities while using a VPN is illegal and subject to criminal prosecution.

**Export Restrictions:**
  - Some countries have restrictions on using VPNs or exporting encryption-related technologies.
  - Illegal Use: Violating export regulations related to VPN technologies can lead to legal penalties.
