# gocryptfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gocryptfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rekor cli
,
kube capacity
,
mat2
.
gocryptfs
Encrypted overlay filesystem written in Go.
More information:
https://github.com/rfjakob/gocryptfs
.
Initialize an encrypted filesystem:
gocryptfs -init {{path/to/cipher_dir}}
Mount an encrypted filesystem:
gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}
Mount with the explicit master key instead of password:
gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}
Change the password:
gocryptfs --passwd {{path/to/cipher_dir}}
Make an encrypted snapshot of a plain directory:
gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}
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
