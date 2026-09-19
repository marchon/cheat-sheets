# gpg-zip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gpg-zip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mongorestore
,
turbo
,
enca
,
ifconfig
.
gpg-zip
Encrypt files and directories in an archive using GPG.
More information:
https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html
.
Encrypt a directory into
archive.gpg
using a passphrase:
gpg-zip --symmetric --output {{archive.gpg}} {{path/to/directory}}
Decrypt
archive.gpg
into a directory of the same name:
gpg-zip --decrypt {{path/to/archive.gpg}}
List the contents of the encrypted
archive.gpg
:
gpg-zip --list-archive {{path/to/archive.gpg}}
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
