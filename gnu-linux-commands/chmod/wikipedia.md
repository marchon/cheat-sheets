# Chmod

Cloned from https://en.wikipedia.org/wiki/Chmod.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 50623.

chmod is a shell command for changing access permissions and special mode flags of files (including special files such as directories). The name is short for change mode where mode refers to the permissions and flags collectively.
The command originated in AT&T Unix version 1 and was exclusive to Unix and Unix-like operating systems until it was ported to other operating systems such as Windows (in UnxUtils) and IBM i.
In Unix and Unix-like operating systems, a system call with the same name as the command, chmod(), provides access to the underlying access control data. The command exposes the capabilities of the system call to a shell user.
As the need for enhanced file-system permissions grew, access-control lists were added to many file systems to augment the modes controlled via chmod.
The implementation of chmod bundled in GNU coreutils was written by David MacKenzie and Jim Meyering. 


== Use ==
Although the syntax of the command varies somewhat by implementation, it generally accepts either a single octal value (which specifies all the mode bits on each file), or a comma-delimited list of symbolic specifiers (which describes how to change the existing mode bits of each file). The remaining arguments are a list of paths to files to be modified.
Changing permissions is only allowed for the superuser (root) and the owner of a file. 
If a symbolic link is specified, the target of the link has its mode bits adjusted. Permissions directly associated with a symbolic link file system entry are typically not used.


=== Options ===
Optional, command-line options may include:

-R recursive; include contained files and subdirectories of specified directories
-v verbose; log changed file names


=== Octal notation ===
Given a numeric permissions argument, the chmod command treats it as an octal number, and replaces all  the mode bits for each file. (Although four digits are specified, leading 0 digits can be elided.)
There are twelve standard mode bits, comprising three special bits (setuid, setgid, and sticky), and three permission groups (controlling access by user, group, and other) of 3 bits each (read, write, and exec/scan); each permission bit grants access if set (1) or denies access if clear (0).
As an octal digit represents a 3-bit value, the twelve mode bits can be represented as four octal digits. chmod accepts up to four digits and uses 0 for left digits not specified (as is normal for numeric representation). In practice, three digits are commonly specified since the special modes are rarely used and the user class is usually specified. 
In the context of an octal digit, each operation bit represents a numeric value: read: 4, write: 2 and execute: 1. The following table relates octal digit values to a class operations value.

The command stat can report a file's permissions as octal. For example:

The reported value, 754 indicates the following permissions:

user class: read, write, and execute; 7 => (4 + 2 + 1)
group class: read and execute; 5 => (4 + 1)
others class: read only; (4)
A code permits execution if and only if it is odd (i.e. 1, 3, 5, or 7). A code permits read if and only if it is greater than or equal to 4 (i.e. 4, 5, 6, or 7). A code permits write if and only if it is 2, 3, 6, or 7.


=== Symbolic notation ===
The chmod command accepts symbolic notation that specifies how to modify the existing permissions. The command accepts a comma-separate list of specifiers like: [classes]+|-|=operations
Classes map permissions to users. A change specifier can select one class by including its symbol, multiple by including each class's symbol with no delimiter, or all classes by not specifying a symbol; when using the last method, the bits of the umask mask will remain unchanged. Class specifiers include:

As ownership is key to access control, and since the symbolic specification uses the abbreviation o, some incorrectly think that it means owner, when, in fact, it is short for others.
The change operators include:

Operations can be specified as follows:

Most chmod implementations support the specification of the special modes in octal, but some do not which requires using the symbolic notation.
The ls command can report file permissions in a symbolic notation that is similar to the notation used with chmod. ls -l reports permissions in a notation that consists of 10 letters. The first indicates the type of the file system entry, such as dash for regular file and 'd' for directory. Following that are three sets of three letters that indicate read, write and execute permissions grouped by user, group and others classes. Each position is either dash to indicate lack of permission or the single-letter abbreviation for the permission to indicate that it's granted. For example:

The permission specifier -rwxr-xr-- starts with a dash, which indicates that findPhoneNumbers.sh is a regular file, not a directory. The next three letters rwx indicate that the file can be read, written, and executed by the owning user dgerman. The next three letters r-x indicate that the file can be read and executed by members of the staff group. And the last three letters r-- indicate that the file is read-only for other users.


== Examples ==
Add write permission to the group class of a directory, allowing users in the same group to add files:

Remove write permission for all classes, preventing anyone from writing to the file:

Set the permissions for the user and group classes to read and execute only, with no write permission, preventing anyone from adding files:

Enable read and write for the user class while making it read-only for group and others:

To recursively set access for the directory docs/ and its contained files:
chmod -R u+w docs/
To set user and group for read and write only and set others for read only:
chmod 664 file
To set user for read, write, and execute only and group and others for read only:
chmod 744 file
To set the sticky bit in addition to user, group and others permissions:
chmod 1755 file
To set UID in addition to user, group and others permissions:
chmod 4755 file
To set GID in addition to user, group and others permissions:
chmod 2755 file


== See also ==
attrib
cacls, modifies access control lists
chattr, changes the attributes of a file
chgrp, changes the group of a file
chown, changes the owner of a file
Group identifier – Unix/POSIX system account group number; numeric value used to represent a specific group
List of POSIX commands
User identifier – Value identifying a user account in Unix and Unix-like operating systems
umask, restricts permissions at file creation


== Notes ==


== References ==


== External links ==

chmod(1): change file modes – FreeBSD General Commands Manual
chmod(1) – Plan 9 Programmer's Manual, Volume 1
chmod(1) – Inferno General commands Manual
chmod — manual page from GNU coreutils.
GNU "Setting Permissions" manual
CHMOD-Win 3.0 — Freeware Windows' ACL ↔ CHMOD converter.
Beginners tutorial with on-line "live" example
