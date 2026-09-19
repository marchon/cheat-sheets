# git-mailinfo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-mailinfo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
parquet tools
,
pnpx
,
mosquitto_passwd
.
git mailinfo
Extract patch and authorship information from a single email message.
More information:
https://git-scm.com/docs/git-mailinfo
.
Extract the patch and author data from an email message:
git mailinfo {{message|patch}}
Extract but remove leading and trailing whitespace:
git mailinfo -k {{message|patch}}
Remove everything from the body before a scissors line (e.g. "-->* --") and retrieve the message or patch:
git mailinfo --scissors {{message|patch}}
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
