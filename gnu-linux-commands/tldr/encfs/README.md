# encfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/encfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lynx
,
doctum
,
rsstail
,
git annotate
.
encfs
Mounts or creates encrypted virtual filesystems.
See also
fusermount
, which can unmount filesystems mounted by this command.
More information:
https://github.com/vgough/encfs
.
Initialize or mount an encrypted filesystem:
encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}
Initialize an encrypted filesystem with standard settings:
encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}
Run encfs in the foreground instead of spawning a daemon:
encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}
Mount an encrypted snapshot of a plain directory:
encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}
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
