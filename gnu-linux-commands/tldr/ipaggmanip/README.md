# ipaggmanip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ipaggmanip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az lock
,
matlab
,
mosquitto_passwd
.
ipaggmanip
Manipulate aggregate statistics produced by
ipaggcreate
.
More information:
https://manned.org/ipaggmanip
.
Combine labels equal in their high-order bits:
ipaggmanip --prefix {{16}} {{path/to/file}}
Remove labels with a count smaller than a given number of bytes and output a random sample of such labels:
ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{path/to/file}}
Replace each label's count with 1 if it is non-zero:
ipaggmanip --posterize {{path/to/file}}
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
