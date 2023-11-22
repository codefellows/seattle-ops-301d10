# Ops Challenge - Powershell AD Automation

PowerShell provides a dedicated module called **Active Directory Module for Windows PowerShell** (also known as AD PowerShell) that extends the PowerShell capabilities with a set of cmdlets specifically designed for AD administration.

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```powershell
Import-Module ActiveDirectory

New-ADUser -SamAccountName "CDavid" -Name "ChewDavid" -OtherAttributes @{'title'="director";'mail'="chewdavid@fabrikam.com"}

```
## Notes

- The AD module needs to be imported using the `Import-Module ActiveDirectory` command before using the AD-related cmdlets.
- The `New-ADUser` cmdlet creates an Active Directory user.
- When using PowerShell cmdlets, parameters are passed to the cmdlet using a `-ParameterName` syntax.
- You must specify the `SamAccountName` parameter to create a user.
  - `SamAccountName` stands for Security Account Manager Account Name
  - This value serves as the unique identifier and login name for the user.
  - It's worth noting that the `SamAccountName` must be unique within the domain, and it has some restrictions on the characters and length that can be used. It typically adheres to the NetBIOS naming conventions and can contain up to 20 characters.
- `-Name` sets the full name or display name for the user account.
- You can set property values that are not associated with cmdlet parameters by using the `OtherAttributes` parameter.
  - You make these up! Like "title" and "mail" from the demo.
  - When using this parameter, be sure to place single quotes around the attribute name.
  - You can set one or more custom parameters at the same time with this parameter. If an attribute takes more than one value, you can assign multiple values.
- All of the parameters available to the AD Module can be found in the [New-ADUser documentation](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps).
