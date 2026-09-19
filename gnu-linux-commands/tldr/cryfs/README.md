# cryfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cryfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git delete branch
,
dirsearch
.
cryfs
A cryptographic filesystem for the cloud.
More information:
https://www.cryfs.org/
.
Mount an encrypted filesystem. The initialization wizard will be started on the first execution:
cryfs {{path/to/cipher_dir}} {{path/to/mount_point}}
Unmount an encrypted filesystem:
cryfs-unmount {{path/to/mount_point}}
Automatically unmount after ten minutes of inactivity:
cryfs --unmount-idle {{10}} {{path/to/cipher_dir}} {{path/to/mount_point}}
Show a list of supported ciphers:
cryfs --show-ciphers
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
