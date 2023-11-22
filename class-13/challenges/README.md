# Ops Challenge: Powershell AD Automation

## Overview

Powershell can be a powerful tool in administering Active Directory (AD) users and computers. Today you'll write a Powershell script to add a new user to AD.

## Resources

- You will need a Windows Server with AD DS installed and the server promoted to Domain Controller
- [Microsoft Documentation: New-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps)

## Demonstration

Refer to [DEMO.md](DEMO.md)

## Notes

- PowerShell AD Automation refers to the use of PowerShell scripting to automate tasks and operations related to Active Directory (AD).
- PowerShell provides a dedicated module called **Active Directory Module for Windows PowerShell** (also known as AD PowerShell) that extends the PowerShell capabilities with a set of cmdlets specifically designed for AD administration.
  - This module needs to be imported using the `Import-Module ActiveDirectory` command before using the AD-related cmdlets.
  - This command is typically placed at the top of your PowerShell script or executed in the PowerShell console before running any AD related commands.
- PowerShell scripts can be created, tested, and executed using PowerShell Integrated Scripting Environment (ISE) or directly in the PowerShell console.
- With PowerShell AD Automation, you can perform a wide range of tasks, including:
  - User Management
    - Create, modify, and delete user accounts, set properties such as name, password, group membership, and organizational unit.
  - Group Management
    - Create, modify, and delete security groups and distribution lists, add or remove members, manage group properties.
  - Computer Management
    - Create, join, and remove computers from the domain, manage computer properties and attributes.
  - OU Management
    - Create, modify, and delete organizational units, move objects between OUs, manage OU properties.
  - GPO Management
    - Create, modify, and delete group policy objects, configure GPO settings, link GPOs to OUs.
  - Query and Reporting
    - Retrieve information from AD, perform searches based on various criteria, generate reports.
  - Automation and Bulk Operations
    - Perform bulk user creation, modification, or deletion, automate repetitive tasks, schedule scripts.
- Review file permissions and the [chmod command](../../class-03/challenges/)
