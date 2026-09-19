# gpgv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gpgv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh api
,
mutool
,
gixy
,
monop
,
ftp
.
gpgv
Verify OpenPGP signatures.
More information:
https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html
.
Verify a signed file:
gpgv {{path/to/file}}
Verify a signed file using a detached signature:
gpgv {{path/to/signature}} {{path/to/file}}
Add a file to the list of keyrings (a single exported key also counts as a keyring):
gpgv --keyring {{./alice.keyring}} {{path/to/signature}} {{path/to/file}}
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
