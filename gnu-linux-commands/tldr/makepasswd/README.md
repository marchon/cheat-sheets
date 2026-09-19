# makepasswd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/makepasswd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm gcc
,
qutebrowser
,
ptpython
.
makepasswd
Generate and encrypt passwords.
More information:
https://manpages.debian.org/stretch/makepasswd/makepasswd.1.en.html
.
Generate a random password (8 to 10 characters long, containing letters and numbers):
makepasswd
Generate a 10 characters long password:
makepasswd --chars {{10}}
Generate a 5 to 10 characters long password:
makepasswd --minchars {{5}} --maxchars {{10}}
Generate a password containing only the characters "b", "a" or "r":
makepasswd --string {{bar}}
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
