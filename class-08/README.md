# Class 08

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

RADIUS (Remote Authentication Dial-In User Service) is a network management protocol facilitating AAA (Authentication, Authorization, and Accounting) management for network users. In this type of configuration, the NAS (Network Access Server) brokers authentication requests and acts as the network's gatekeeper.

## How does this topic fit?

**Where we've been**:
In the previous class we spun up our own Linux-based web server.

**What are we focusing on today**:
Today we'll be studying Network Access Control (NAC) systems and the RADIUS network management protocol.

**Where we're headed**:
Next class we'll be configuring traffic mirroring, which is how to duplicate packets from one interface to another.

## RADIUS Authentication

### Why
- Network access control (NAC) systems use RADIUS and AAA to enforce policies that dictate which users or devices are allowed on the network and what resources they can access. This is crucial for maintaining a secure and well-managed network environment.
- Many industries and organizations are subject to regulatory compliance requirements that mandate strong authentication and access control. Implementing RADIUS, NAC, and AAA helps meet these compliance requirements, avoiding potential legal issues and penalties.
- RADIUS and AAA systems centralize user authentication and authorization, making it easier to manage access control policies across a network. This simplifies administration and reduces the risk of configuration errors.
- These technologies are scalable, making it feasible to manage access for large numbers of users and devices. This scalability is essential for organizations with diverse and growing networks.
- AAA systems provide real-time monitoring and reporting capabilities, allowing administrators to quickly identify and respond to network anomalies, suspicious activities, or policy violations.
- RADIUS and NAC can facilitate secure guest access to networks, ensuring that visitors have limited, controlled access without compromising security.
- AAA's accounting component keeps a record of user activities, which can be valuable for auditing purposes and attributing actions to specific users or devices.
- RADIUS servers can be configured for redundancy and high availability, ensuring that authentication and authorization services remain accessible even in the event of server failures.
- RADIUS, NAC, and AAA systems can be integrated with other network security technologies like firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS), creating a layered security approach.

### What
- _______ is a framework that encompasses three key security processes: Authentication, Authorization, and Accounting.
- _______ is the process of verifying the identity of a user, device, or entity attempting to access a system or network.
  - _______ is a set of rules and procedures used to validate the identity of a user or device.
  - _______ are methods or elements used to verify a user's identity. Common factors include something you know (like a password), something you have (like a smart card), and something you are (e.g., biometrics).
  - _______ is a server responsible for verifying the identity of users or devices during the authentication process.
- _______ is the process of determining what actions or resources an authenticated user or device is permitted to access based on their permissions and privileges.
  - _______ is a set of rules and conditions that dictate who is allowed to access specific network resources and what actions they can perform.
  - _______ is the practice of regulating access to resources based on user permissions and policies.
  - _______ is a server responsible for determining and enforcing access permissions and policies for authenticated users or devices.
- _______ is the process of recording and monitoring the activities of authenticated users or devices for auditing or billing purposes.
  - _______ are logs or records that track user actions and network usage.
  - _______ is a server that collects and records data about user or device activities for auditing or billing purposes.
- _______ is a networking protocol and system used for centralized authentication, authorization, and accounting for users attempting to access a network.
- _______ is a security technology that enforces policies to control and restrict access to a network, ensuring that only authorized devices and users connect.
- _______ is a security method that requires two separate authentication factors for user verification, enhancing security compared to a single-factor method.
- _______ is a mechanism that allows users to log in once and access multiple applications or services without needing to enter separate credentials.
- _______ is the process of monitoring and controlling user sessions to ensure security and appropriate access.
- _______ is a set of guidelines and rules that define the organization's approach to security, including access control policies.

### How
RADIUS authentication, network access control, and AAA work together to ensure secure and controlled access to a network. Here's a step-by-step overview of how these components work together:
- **User Authentication**
  - The process begins when a user or device attempts to connect to the network. This could be through wired or wireless connections, VPN access, or any other network access point.
  - The first step is user authentication, where the user or device provides credentials to prove their identity. These credentials can include a username and password, a digital certificate, or other authentication factors.
- **RADIUS Authentication**
  - Once the credentials are provided, they are sent to a RADIUS server for authentication. RADIUS stands for Remote Authentication Dial-In User Service and is a commonly used protocol for this purpose.
  - The RADIUS server receives the authentication request and validates the credentials against its authentication database, which may contain user account information, passwords, and authentication policies.
- **Authentication Response**
  - The RADIUS server responds to the authentication request with a success or failure message. If the provided credentials are valid, the user or device is authenticated. If not, access is denied.
- **Network Access Control (NAC)**
  - If authentication is successful, the process moves to the authorization phase, which involves network access control (NAC).
  - The NAC system evaluates the authenticated user's or device's attributes and checks them against predefined access policies. These policies determine what resources, services, and actions the user or device is allowed to access.
  - NAC may involve endpoint security checks to ensure the device meets security requirements, such as having up-to-date antivirus software or operating system patches.
- **Authorization**
  - After successful authentication and NAC checks, the user or device is authorized for specific network access based on their role, group membership, and the policies defined by the organization.
  - Authorization may involve assigning VLANs, firewall rules, or other network attributes to the user or device to enforce access control.
- **Access Granted or Denied**
  - Depending on the results of the authorization process, access is either granted or denied to the network resources. Users or devices are allowed to connect to the network and access authorized services, or they are blocked from accessing certain areas or services.
- **Accounting**
  - The AAA system continuously monitors and records user or device activities while connected to the network. This accounting data includes information on who accessed the network, what they accessed, and when they accessed it.
  - Accounting records are crucial for auditing, billing, and security incident investigations.
- **Session Management**
  - Throughout the user's or device's session on the network, session management ensures that the user remains authenticated and authorized. It may also involve periodic reauthentication or reauthorization checks.
- **Logging and Reporting**
  - Throughout the entire process, logs and reports are generated to track and document authentication, authorization, and accounting events. These logs can be used for security analysis and compliance reporting.

### Experimentation and Discovery Ideas
- Why do you think RADIUS authentication is widely used in network security? What benefits does it offer that other authentication methods might not?
- Imagine you're responsible for designing a network access control (NAC) system for a university campus. What factors would you consider in determining the access policies for students, faculty, and guests?
- How might you experiment with different authentication factors, like biometrics or smart cards, to enhance network security while minimizing user inconvenience?
- Considering the importance of accounting in AAA, can you brainstorm some creative ways to use the accounting data collected from network activities for improving network management or security?
- What ethical considerations should be taken into account when implementing network access control, especially in regard to user privacy and monitoring?
- Can you think of scenarios in which AAA systems might face challenges or vulnerabilities, and what measures could be taken to mitigate these risks through experimentation and discovery?
- How could the principles of zero trust security be integrated into a network access control strategy, and what experiments might you conduct to evaluate its effectiveness?

## Learning Objectives

### Students will be able to

#### Describe and Define

- TACACS+
- RADIUS
- FreeRADIUS
- Captive Portal
- AAA
- NAS
- NAC
- Network level authentication

#### Execute
- Students will be able to set up a Captive Portal in pfSense, including the selection of the interface and authentication method.
- They will deploy the FreeRADIUS package on pfSense, encompassing essential configurations like user creation, client setup, and interface configuration.
- Students will demonstrate the capability to integrate FreeRADIUS with pfSense's Captive Portal, modify the authentication server settings and verify login functionality.
- Students will develop understanding in accessing and interpreting system logs associated with FreeRADIUS and the Captive Portal, enabling them to recognize authentication events and potential issues effectively.
- Students will achieve a comprehensive understanding of AAA management within the context of RADIUS configuration, recognizing its role in enhancing network security.

## Helpful Resources

- [How to Set Up a Radius Server on pfSense](https://turbofuture.com/internet/How-to-Set-Up-a-Radius-Server-on-pfSense-Using-the-FreeRadius-Package){:target="blank"}
- Professor Messer:
  - [TACACS and RADIUS](https://www.professormesser.com/network-plus/n10-006/tacacs-and-radius/){:target="blank"}
  - [Authorization, Authentication, and Accounting](https://www.professormesser.com/network-plus/n10-007/authorization-authentication-and-accounting/){:target="blank"}
  - [Access Control](https://www.professormesser.com/network-plus/n10-007/access-control/){:target="blank"}
- pfSense Documentation:
  - [pfSense RADIUS Authentication Servers](https://docs.netgate.com/pfsense/en/latest/usermanager/radius.html){:target="blank"}
  - [pfSense Captive Portal Configuration](https://docs.netgate.com/pfsense/en/latest/captiveportal/index.html){:target="blank"}
- [FreeRADIUS Documentation](http://wiki.freeradius.org/){:target="blank"}

## Notes

- How does Single Sign-On (SSO) relate to RADIUS and AAA, and what benefits does it offer in terms of user authentication and access control?
- Can you explain the concept of "failover" in the context of RADIUS servers? How do organizations ensure high availability and redundancy in their authentication systems?
- What are the common security challenges associated with RADIUS authentication, and what measures can be taken to mitigate these challenges?
- How does Network Access Control (NAC) differ from traditional perimeter security measures like firewalls and intrusion detection systems (IDS)? What unique advantages does NAC provide?
- What role does RADIUS play in securing remote access to corporate networks, especially in the context of telecommuting and remote work?
- Can you explain the differences between RADIUS and TACACS+ (Terminal Access Controller Access Control System Plus)? When might one be preferred over the other?
- What is the impact of Bring Your Own Device (BYOD) policies on network access control, and how can organizations effectively implement NAC solutions to accommodate BYOD while maintaining security?
- How does the concept of "Zero Trust" apply to network access control and security? What principles and technologies are associated with the Zero Trust model?
- How do emerging technologies like Software-Defined Networking (SDN) and cloud-based services influence network access control and authentication methods, and what challenges do they introduce?
- What are the privacy implications of collecting and storing user activity data for accounting purposes, and how can organizations balance the need for security with user privacy concerns?
