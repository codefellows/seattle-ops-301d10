<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 13

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Active Directory
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

![Image](/ops-301-guide/curriculum/class-13/slides/assets/0_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->

## Module 3 - Server Administration, Active Directory, and User Management

<div>

<div align="left" style="font-size: 40px">

**Class 11** Windows Server

**Class 12** Domain Controller

&shy;<!-- .element style="color: red;" -->**Class 13** Active Directory

**Class 14** Group Policy

**Class 15** N/A: Project Kickoff


</div>

<div>

![Image](/ops-301-guide/curriculum/class-13/slides/assets/0_02.png)
<!-- .element style="width: 70%"-->

</div>

</div>

---

<!-- .element class="split-screen-with-title" -->


## Module 3 Challenges: Python + PowerShell

<div>

<div align="left" style="font-size: 50px">


**Class 11** Psutil

**Class 12** Python Requests Library

&shy;<!-- .element style="color: red;" -->**Class 13** Powershell AD Automation

**Class 14** Python Malware Analysis

**Class 15** N/A


</div>

<div>

![Image](/ops-301-guide/curriculum/class-13/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Active Directory
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Active Directory
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 12




---

<!-- .element class="main-title" -->
# Review: DNS


NOTE:
- Concepts to review
  - DNS Hierarchy
  - DNS Resolution Process
  - DNS Resolution Components
    - DNS Resolver
    - Root Server
    - TLD Server
    - Authoritative Name Server
  - DNS Record Types

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
- DC's commonly run Windows Server OS
  - Can also be non-Windows, e.g. Samba or Red Hat FreeIPA

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/12_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

### WHAT

- What is a DC?
  - A network server responsible for host access to domain resources
  - Oversees the whole domain
  - Authenticates users
  - Stores account information
  - Enforces security policy across devices

- Can run on Windows Server or Linux

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
  - NTP
  - Kerberos
  - DNS

Image Source: include link to image source
Source: Blogspot

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

![Image](/ops-301-guide/curriculum/class-13/slides/assets/12_02.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

### WHAT

- What is a DNS Server?
  - Domain Name System (DNS)
  - Maintains a local database of IP addresses associated with domain names
  - Acts in hierarchy with other DNS servers, all the way up to root DNS

### Draw

- Draw out the DNS hierarchy of forest, tree, domain and OU

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
Source: OpenSource

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="main-title" -->

# Review:

## Lab 12

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture:
  - Active Directory
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 12**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 13** - PowerShell AD Automation

NOTE:

### Review: Ops Challenge 12

### Introduce: Ops Challenge 13 - PowerShell AD Automation

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Active Directory
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 13 - Active Directory

NOTE:
- Active Directory (AD) is a foundational component of Microsoft Windows-based network environments.
- It serves as a centralized directory and identity management system, facilitating the organization, authentication, and authorization of users, computers, and resources within a network.
- AD plays a pivotal role in simplifying administrative tasks, enhancing security, and enabling efficient access control in complex enterprise IT ecosystems.

---

<!-- .element class="split-screen-with-title" -->


# Identity Management

<div>

<div align="left">

- Why is identity management critical to understand for systems administrators and security professionals?
  - Granting privileges
  - Transcends any single system
  - Core topic in cybersecurity as 1/8 of the CISSP CBK Domains.
- Why is AD so popular?
  - Scalability
  - Central identity authority
  - Central administration

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
Identity management is critical for systems administrators and security professionals because it forms the foundation of secure and efficient network operations.

- **Granting Privileges**: Identity management involves controlling who has access to what resources. Understanding this process is crucial for administrators to ensure that users are granted the right privileges, minimizing security risks associated with unauthorized access or privilege escalation.

- **Transcends Any Single System**: Identity management isn't limited to a single system or application. It encompasses the entire network, allowing administrators to manage user access consistently across multiple systems, applications, and services.

- **Core Topic in Cybersecurity**: Identity management is one of the core domains in the Certified Information Systems Security Professional (CISSP) Common Body of Knowledge (CBK). This highlights its importance in the field of cybersecurity, emphasizing its role in protecting sensitive information and maintaining data integrity.

- **Why is Active Directory (AD) So Popular?**:
  - **Scalability**: AD's ability to scale seamlessly makes it popular for organizations of all sizes. It can accommodate the growth of user accounts, devices, and resources within a network without compromising performance or security.
  - **Central Identity Authority**: AD serves as a central identity authority, providing a unified and consistent way to manage user identities and access privileges. This centralization simplifies administration and ensures consistency.
  - **Central Administration**: AD's centralized management console and Group Policy features allow administrators to efficiently control user authentication, authorization, and resource access policies, reducing administrative overhead and ensuring security policies are consistently enforced.

OLD NOTES:
- Why is identity management critical to understand for systems administrators and security professionals?
  - Granting privileges
- How attackers commonly expose a system is privilege escalation, so we need to get this right
  - Transcends any single system. Most computers systems have a central identity management control panel.
  - Core topic in cybersecurity as 1/8 of the CISSP CBK Domains. Show students the [8 domains](https://cisspdomain.com/) or draw them out.

Image Source: include link to image source
Source: Wikipedia

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Identity Management

<div>

<div align="left">

- Microsoft Active Directory (AD) is a proprietary Microsoft product on Windows Server that is a database ("directory") that contains critical information about your environment, including users, computers, and their authorization levels.
  - Active Directory Users and Computers (ADUC) is the traditional control panel for this system, see image
  - Active Directory Administrative Center (ADAC) is the modern app for identity administration

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
- **Microsoft Active Directory (AD)** is a proprietary Microsoft product designed to function as a centralized identity and access management system within Windows Server environments. It serves as a database, often referred to as a "directory," housing essential information about entities within your network, such as user accounts, computer accounts, and their associated authorization levels.

- **Active Directory Users and Computers (ADUC)** is the traditional control panel used for managing user accounts, computer accounts, and various aspects of the Active Directory environment. It provides a familiar interface for administrators to perform tasks related to identity and access management.

- **Active Directory Administrative Center (ADAC)** is a modern, web-based application developed by Microsoft for identity administration within Active Directory. It offers a more user-friendly and feature-rich alternative to ADUC, making it easier for administrators to perform tasks related to user management, group management, and access control. ADAC is designed to simplify the administration of Active Directory resources and enhance overall efficiency.

Image Source: include link to image source
Source: Wikipedia

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Identity Management

<div>

<div align="left">

- AD facilitates authentication and authorization
  - Authentication takes place when users log in to their profiles a computer system, in this case using a domain profile
    - Example: CORP\s.wilkins
  - Authorization is what users or computers are allowed to do
    - Groups and OUs determine user privilege

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
- **Active Directory (AD)** serves as the core framework for facilitating both authentication and authorization in a Windows-based network environment.

- **Authentication** is the process through which users prove their identity to the system, typically by entering their credentials (e.g., username and password). In the context of Active Directory, authentication occurs when users log in to their computer systems using a domain profile. For instance, a user might log in as "CORP\s.wilkins," where "CORP" is the domain name, and "s.wilkins" is the username.

- **Authorization** is the subsequent step that determines what actions and resources users or computers are allowed to access or perform within the network. In Active Directory, authorization is managed through the use of groups and Organizational Units (OUs). Groups help define user privileges by specifying what resources and permissions group members have access to, while OUs help organize objects within AD, providing a structure for applying security policies and permissions.

Image Source: include link to image source
Source: Wikipedia

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# RSAT

<div>

<div align="left">

- Remote Server Administration Tools (RSAT) is a software package for Windows 10 that includes:
  - Server Manager
  - Microsoft Management Console (MMC) snap-ins
  - Consoles
  - Windows PowerShell cmdlets and providers
  - Command-line tools for managing roles and features that run on Windows Server

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_02.png)
<!-- .element style="width: 90%"-->

</div>

</div>

NOTE:
**Remote Server Administration Tools (RSAT)** is a valuable software package designed for Windows 10 that empowers administrators to manage and administer Windows servers remotely. It encompasses a variety of tools and utilities, including:

- **Server Manager**: Server Manager provides a centralized interface for managing and configuring Windows servers. It enables administrators to oversee server roles, features, and system properties, making it easier to monitor and maintain server health.

- **Microsoft Management Console (MMC) Snap-ins**: RSAT includes various MMC snap-ins that allow administrators to create custom management consoles tailored to their specific needs. These snap-ins provide access to a wide range of administrative functions and tools.

- **Consoles**: RSAT facilitates the creation and customization of administrative consoles. Administrators can build consoles that focus on specific tasks or server roles, streamlining their management efforts.

- **Windows PowerShell Cmdlets and Providers**: RSAT extends Windows PowerShell capabilities by including cmdlets and providers specifically designed for server administration. PowerShell automation scripts can be used to manage server roles and features remotely.

- **Command-Line Tools**: RSAT incorporates a suite of command-line tools that enable administrators to perform various tasks related to managing roles and features running on Windows Server. These tools provide flexibility and efficiency in server administration tasks.

Image Source: include link to image source
Source: Superuser

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# ADAC

<div>

<div align="left">

- Active Directory Administrative Center (ADAC) is an administration control panel in Windows Server for identity management
- User: Single user profile for a single individual
- Group: Security groups, usually departments or functional roles if RBAC
- Organizational Units (OUs) allow a administers to implement role-based or group-based technical policies

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
**Active Directory Administrative Center (ADAC)** serves as a powerful administration control panel within Windows Server, offering an intuitive interface for effective identity management and Active Directory (AD) administration. It simplifies various tasks related to user and group management:

- **User**: In ADAC, a "User" represents a single user profile for an individual within the AD environment. Administrators can create, modify, and manage user accounts, including specifying attributes such as username, password policies, group memberships, and access permissions.

- **Group**: ADAC allows administrators to work with security groups, which are often organized based on departments or functional roles to implement Role-Based Access Control (RBAC). Security groups enable efficient access management by granting specific permissions and access rights to group members, streamlining user privilege assignments.

- **Organizational Units (OUs)**: OUs are a fundamental component of ADAC, providing a hierarchical structure for organizing and managing objects within Active Directory. They allow administrators to implement role-based or group-based technical policies by grouping related resources, users, and computers together. OUs are instrumental in applying Group Policy Objects (GPOs) to enforce specific configurations and security settings.


Image Source: include link to image source
Source: hmartinzobar

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Provisioning

<div>

<div align="left">

- Provisioning is the process applied to new hires.
  - During the enrollment or registration process, HR will send IT details on what the new user will be doing, who they report to, what department, etc.
  - Sysadmin will create new user and assign OU according to the role provided.

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_07.png)
<!-- .element style="width: 100%"-->

<div style="font-size: small">Management icons created by surang - Flaticon</div>

</div>

</div>

NOTE:
**Provisioning** is a critical process in IT administration, particularly when onboarding new employees. It involves setting up user accounts, access permissions, and resources for new hires to ensure they can perform their job roles effectively within the organization. Here's how provisioning typically works:

- **New Hire Enrollment**: The provisioning process begins with HR collecting essential information about new employees during the enrollment or registration process. HR gathers details such as the employee's name, job title, department, reporting structure, and specific access requirements.

- **Information Transfer to IT**: HR collaborates with the IT department to relay the collected information. This data includes details about what the new user will be doing, who they report to, which department they belong to, and any unique access needs or resource requirements.

- **User Account Creation**: IT, often with the involvement of system administrators or network administrators, then proceeds to create a new user account for the new employee. This involves generating login credentials (username and password) and establishing the user's identity within the organization's identity management system, which may include Active Directory (AD) or similar systems.

- **Assignment of Organizational Unit (OU)**: The sysadmin or IT team assigns the user to a specific Organizational Unit (OU) based on the role and department provided by HR. OUs help organize users and resources within AD or other directory services, allowing for efficient application of group policies and security settings.

Provisioning ensures that new employees have the necessary tools, access permissions, and resources to fulfill their job responsibilities from day one. It plays a crucial role in maintaining security and operational efficiency while facilitating a smooth onboarding process for new staff members.

Image Source: Management free icon, by surang, [Flaticon License](https://www.freepikcompany.com/legal#nav-flaticon-agreement), via [Flaticon](https://www.flaticon.com/free-icon/management_762699)

---

<!-- .element class="split-screen-with-title" -->


# Account Review

<div>

<div align="left">

- Admins should regularly review user accounts for irregularities to proactively thwart security problems.
  - Remove inactive accounts
  - Remove excessive privilege
- Privilege creep occurs when users switch roles and keep their old authorization unnecessarily.
- When an employee quits or is terminated, revoke their account using prearranged SOP. This is called account revocation.

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-13/slides/assets/13_06.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:
**Account Review** is a vital practice in IT and cybersecurity that involves regularly assessing and managing user accounts within an organization's network. It is crucial for maintaining security and efficiency. Here are key points about account review:

- **Proactive Security**: Regular account reviews are essential for administrators to proactively identify and address irregularities that may pose security risks. By doing so, they can prevent potential security breaches before they occur.

- **Removing Inactive Accounts**: Part of the account review process involves identifying and removing inactive accounts. These are accounts that belong to users who are no longer active employees or users who haven't logged in for an extended period. Removing these accounts reduces the attack surface and mitigates the risk of unauthorized access.

- **Removing Excessive Privileges**: Account reviews also focus on identifying and rectifying excessive privilege issues. Privilege creep can occur when users switch roles within an organization but retain their old authorizations unnecessarily. Account reviews help administrators ensure that users have only the privileges they need for their current roles, reducing the risk of privilege abuse.

- **Account Revocation**: When an employee resigns or is terminated, it's essential to follow a predefined Standard Operating Procedure (SOP) for account revocation. This process involves promptly revoking the user's access rights, including disabling or deleting their account, to prevent unauthorized access to company resources after their departure.

Regular account reviews are a crucial component of an organization's security posture, as they help maintain a lean and secure user account environment. By proactively managing accounts, organizations can reduce the likelihood of security incidents and data breaches.

Image Source: include link to image source
Source: hmartinzobar

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 13 - Active Directory
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Active Directory
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Active Directory

NOTE:

### Import OVA File


### Demo: Active Directory

