# Ops Challenge: File Permissions

## Overview

Linux tracks file permissions using a text and digit system that is associated with each file. In today's challenge you will learn how to automate the manipulation of file permissions in a bash script. Use the resources below to ensure you comprehend Linux file permissions before manipulating them in today's challenge.

## `chmod`

The `chmod` command in Unix operating systems is used to change the permissions of files and directories. "chmod" stands for "change mode," and it allows you to control who can read, write, and execute a file or directory. It is a fundamental command for managing access control in a Unix environment, where security and user permissions are important.

The basic syntax of the `chmod` command is as follows:

```
chmod [options] mode file(s)
```

Here, "mode" represents the new permissions you want to assign, and "file(s)" specifies the file or files you want to modify. There are two common ways to specify the mode:

1. **Symbolic Mode:** This is a more human-readable way to represent permissions. It involves using letters and symbols to specify who gets which permissions. The basic symbols are:
   - `+` to add permissions.
   - `-` to remove permissions.
   - `=` to set permissions explicitly.

   The permission letters are:
   - `r`: Read permission.
   - `w`: Write permission.
   - `x`: Execute permission.

   For example:
   - `chmod +r file.txt`: Adds read permission to "file.txt."
   - `chmod -w file.txt`: Removes write permission from "file.txt."
   - `chmod u+x script.sh`: Adds execute permission to the owner of "script.sh."

2. **Numeric Mode:** This involves using three digits to represent the permissions in octal (base-8) format. Each digit corresponds to a different user category:
   - The first digit represents the owner's permissions.
   - The second digit represents the group's permissions.
   - The third digit represents others' permissions.

   The permission values are:
   - `4`: Read permission.
   - `2`: Write permission.
   - `1`: Execute permission.
   - `0`: No permission.

   You calculate the numeric value by adding the values for the desired permissions. For example:
   - `chmod 755 script.sh`: Gives read, write, and execute permissions to the owner, and read and execute permissions to the group and others.

Some common `chmod` options include:
- `-R` or `--recursive`: Applies the permission change recursively to all files and directories within a directory.
- `--reference=file`: Sets the permissions of the target file to match those of the reference file.

> It's important to use the `chmod` command carefully, as incorrect permissions can affect the security and functionality of your system. Always ensure that you understand the implications of the permission changes you make.

Keep in mind that you might need administrative privileges (root or sudo) to change permissions on certain files and directories, like system files. Instead, you should only perform this operation in user-created files and directories. Changing permissions in system files is not advised, as this can cause malfunctions in the OS.

## Resources

- [Linux Commands Cheat Sheet](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/) (Focus on Section 7)
- [Linux Handbook chmod Command](https://linuxhandbook.com/chmod-command/)
- [Linux Training Academy File Permissions](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/#7_8211_FILE_PERMISSIONS)
- [chmod calculator](https://chmod-calculator.com/)

## Demonstration

Refer to [DEMO.md](DEMO.md)
