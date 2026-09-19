# umask

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/umask/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
opam
,
pio debug
,
fusermount
,
tlmgr info
.
umask
Manage the read/write/execute permissions that are masked out (i.e. restricted) for newly created files by the user.
More information:
https://manned.org/umask
.
Display the current mask in octal notation:
umask
Display the current mask in symbolic (human-readable) mode:
umask -S
Change the mask symbolically to allow read permission for all users (the rest of the mask bits are unchanged):
umask {{a+r}}
Set the mask (using octal) to restrict no permissions for the file's owner, and restrict all permissions for everyone else:
umask {{077}}
This is a
tldr pages
(
source
, CC BY 4.0) web wrapper for
cheat-sheets.org
.
All commands
,
popular commands
,
most used linux commands
.
Referrals
.
Progressive Web Application (PWA) version to install on your device
.
