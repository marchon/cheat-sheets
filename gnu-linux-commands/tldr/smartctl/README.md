# smartctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/smartctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
c99
,
git whatchanged
,
in toto run
.
smartctl
View a disk's SMART data and other information.
More information:
https://en.wikipedia.org/wiki/S.M.A.R.T.
.
View SMART health summary:
sudo smartctl --health {{/dev/sdX}}
View device information:
sudo smartctl --info {{/dev/sdX}}
Begin a short self-test:
sudo smartctl --test short {{/dev/sdX}}
View current/last self-test status and other SMART capabilities:
sudo smartctl --capabilities {{/dev/sdX}}
View SMART self-test log (if supported):
sudo smartctl --log selftest {{/dev/sdX}}
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
