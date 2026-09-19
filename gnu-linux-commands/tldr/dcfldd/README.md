# dcfldd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dcfldd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
while
,
buku
,
bshell
,
virsh pool undefine
.
dcfldd
Enhanced version of dd for forensics and security.
More information:
http://dcfldd.sourceforge.net/
.
Copy a disk to a raw image file and hash the image using SHA256:
dcfldd if=/dev/{{disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}
Copy a disk to a raw image file, hashing each 1 GB chunk:
dcfldd if=/dev/{{disk_device}} of={{file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{file.hash}} hashwindow={{1G}}
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
