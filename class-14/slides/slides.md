<!-- .element class="main-title" -->
# Ops 301: Networking and Systems Administration

Class 14

NOTE:
Update the class number for each video recording

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Warmup
- Review
- Ops Challenge
- Lecture:
  - Group Policy
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

![Image](/ops-301-guide/curriculum/class-14/slides/assets/0_01.png)
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

**Class 13** Active Directory

&shy;<!-- .element style="color: red;" -->**Class 14** Group Policy

**Class 15** N/A: Project Kickoff


</div>

<div>

![Image](/ops-301-guide/curriculum/class-14/slides/assets/0_02.png) 
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

**Class 13** Powershell AD Automation

&shy;<!-- .element style="color: red;" -->**Class 14** Python Malware Analysis

**Class 15** N/A


</div>

<div>

![Image](/ops-301-guide/curriculum/class-14/slides/assets/0_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview
- Warmup <!-- .element style="color: red;" -->
- Review
- Ops Challenge
- Lecture:
  - Group Policy
- Demo

---

<!-- .element class="main-title" -->

# Warmup

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview
- Warmup
- Review <!-- .element style="color: red;" -->
- Ops Challenge
- Lecture:
  - Group Policy
- Demo

---

<!-- .element class="main-title" -->

# Review
- Previous Concepts <!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->
- Lab 13

---

<!-- .element class="main-title" -->
# Review: Active Directory

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

![Image](/ops-301-guide/curriculum/class-14/slides/assets/13_01.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- Microsoft Active Directory (AD) is a proprietary Microsoft product on Windows Server that is a database ("directory") that contains critical information about your environment, including users, computers, and their authorization levels. 
  - Active Directory Users and Computers (ADUC) is the traditional control panel for this system, see image
  - Active Directory Administrative Center (ADAC) is the modern app for identity administration

Image Source: include link to image source
Source: Wikipedia

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

![Image](/ops-301-guide/curriculum/class-14/slides/assets/13_03.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

- What is ADAC?
  - Active Directory Administrative Center (ADAC) is an administration control panel in Windows Server for identity management
    - User: Single user profile for a single individual
    - Groups:
      - A collection of AD objects that can include users, computers, other groups and other AD objects
      - Used to assign permissions to company resources
      - There are two types, Security and Distribution Groups
    - OU:
      - Organizational Units allow an administrator to implement role-based or group-based technical policies
      - Allow us to delegate admin tasks to users/groups without having to make them an admin

Image Source: include link to image source
Source: hmartinzobar

<div style="font-size: small">Title, Author, License Type</div>


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

![Image](/ops-301-guide/curriculum/class-14/slides/assets/13_06.png)
<!-- .element style="width: 100%"-->

</div>

</div>

NOTE:

Image Source: include link to image source
Source: hmartinzobar

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="main-title" -->

# Review:

## Lab 13

NOTE:

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview
- Warmup
- Review
- Ops Challenge <!-- .element style="color: red;" -->
- Lecture: 
  - Group Policy
- Demo

---

<!-- .element class="main-title" -->
# Ops Challenge:

- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="1" -->**Review Ops Challenge 13**
- &shy;<!-- .element: class="fragment highlight-current-red" data-fragment-index="2" -->**Ops Challenge 14** - Python Malware Analysis

NOTE:

### Review: Ops Challenge 13

### Introduce: Ops Challenge 14 - Python Malware Analysis

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: <!-- .element style="color: red;" -->
  - Group Policy
- Demo


---

<!-- .element class="main-title" -->

# Lecture:
### Class 14 - Group Policy

NOTE:
Is there a relevant Ch. in the Wiley Network+ (N10-008) Study Guide?

---

<!-- .element class="split-screen-with-title" -->


# Group Policy

<div>

<div align="left">

- Why is Group Policy used by sysadmins?
  - Need to standardize computer configurations across the org
  - Allows sysadmins implement custom configurations such as:
    - Folder redirection
    - Specialized security policies
  - Two policy menus to be aware of:
    - Local (gpedit.msc on endpoint)
    - Domain (managed from DC)

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-14/slides/assets/14_01.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

Does this relate to cyber security? Absolutely! An intruder who has made their way into the Administrator account over a domain can compromise the integrity of group policies and make massive changes across the enterprise. "Owning the domain" is a common objective for advanced threat actors for this reason.

Image Source: include link to image source
Source: securebydefault

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Group Policy

<div>

<div align="left">

- Group Policy is a proprietary Microsoft Windows infrastructure that specifies managed configurations for user and computers 
- A Group Policy Object (GPO) is a virtual collection of policy settings. Each GPO has a unique name and identifier
  - Settings that a GPO can include:
    - System Appearance
    - Security
    - Logging

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-14/slides/assets/14_01.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

Image Source: include link to image source
Source: securebydefault

<div style="font-size: small">Title, Author, License Type</div>



---

<!-- .element class="split-screen-with-title" -->


# Group Policy

<div>

<div align="left">

- Scope of GPO
  - Domain level, e.g. "globex.com"
  - OU level, e.g. "Accounting"
- Objects in the GPMC are often linked. Links symbolize relationships.
- Preferences will be set only upon initial startup of the computer or logon of the user
  - Not the same as a policy
- Why do we have preferences in addition to policy?
  - Different use cases!

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-14/slides/assets/14_01.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

Differences between preferences and policies 
- A policy disables its associated user interface item on the user's computer; a preference does not.
- A policy is removed when the GPO goes out of scope. A preference, however, remains configured for the targeted user or computer even when the GPO goes out of scope.
- When a policy is applied, the original registry settings on the client computer are not changed. With preferences, however, the original registry settings on the client are overwritten and removing the preference does not restore the original setting. In other words, a preference actually modifies the corresponding configuration setting in the user interface on the client. 
- Policies can be configured in both domain and local GPOs; preferences can be configured only in domain GPOs.
- A preference can be applied only once if desired; policies are always periodically refreshed.

Image Source: include link to image source
Source: securebydefault

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Group Policy Management

<div>

<div align="left">

- How is Group Policy managed?
  - A GPO is created using the Group Policy Object Editor
  - Group Policy Management Console (GPMC)
- How does Group Policy get applied to a computer?
  - Policy applied when the computer starts and when the user logs in
  - Default refresh takes place every 90 minutes + or - 30 minutes by default the interval can be modified

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-14/slides/assets/14_01.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

- How does Group Policy get applied to a computer?
  - Policy applied when the computer starts and when the user logs in
  - Default refresh takes place every 90 minutes, but this can be changed
  - If you're shelled into the computer needing a refresh, you can try `gpudate /force` command to initialize a policy check.

Image Source: include link to image source
Source: securebydefault

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="split-screen-with-title" -->


# Group Policy Management

<div>

<div align="left">

- Group Policy Hierarchy
  - By default, Group Policy is inherited and cumulative, and it affects all computers and users in an Active Directory container.
- GPOs are processed in the following order:
  - The local GPO is applied.
  - GPOs linked to sites are applied.
  - GPOs linked to domains are applied.
  - GPOs linked to organizational units are applied.

</div>

<div align="left">

![Image](/ops-301-guide/curriculum/class-14/slides/assets/14_01.png)
<!-- .element style="width: 120%"-->

</div>

</div>

NOTE:

- Group Policy Hierarchy
    - By default, Group Policy is inherited and cumulative, and it affects all computers and users in an Active Directory container.
    - GPOs are processed in the following order:
      - The local GPO is applied.
      - GPOs linked to sites are applied.
      - GPOs linked to domains are applied.
      - GPOs linked to organizational units are applied. For nested organizational units, GPOs linked to parent organizational units are applied before GPOs linked to child organizational units are applied.
  - "When applying policy, the system queries the directory service for a list of GPOs to process. Each GPO is linked to an Active Directory container in which the computer or user belongs. By default, the system processes the GPOs in the following order: local, site, domain, then organizational unit. Therefore, the computer or user receives the policy settings of the last Active Directory container processed." 
  - "When processing the GPO, the system checks the access-control list (ACL) associated with the GPO. If an access-control entry (ACE) denies the computer or user access to the GPO, the system does not apply the policy settings specified by the GPO. If the ACE allows access to the GPO, the system applies the policy settings specified by the GPO." 

Image Source: include link to image source
Source: securebydefault
Passcode: 08QiuADJUu

<div style="font-size: small">Title, Author, License Type</div>

---

<!-- .element class="title-and-subtitle" -->

# Agenda
## Class 14 - Group Policy
- Course Overview
- Warmup
- Review
- Ops Challenge
- Lecture: 
  - Group Policy
- Demo <!-- .element style="color: red;" -->

---

<!-- .element class="main-title" -->
# Demo & Lab

## Group Policy

NOTE:

### Import OVA File


### Demo: Group Policy

