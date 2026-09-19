# tlmgr-update

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-update/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
qmv
,
ng
,
yank
,
arch
,
hg push
,
radare2
.
tlmgr update
Update TeX Live packages.
More information:
https://www.tug.org/texlive/tlmgr.html
.
Update all TeX Live packages:
sudo tlmgr update --all
Update tlmgr itself:
sudo tlmgr update --self
Update a specific package:
sudo tlmgr update {{package}}
Update all except a specific package:
sudo tlmgr update --all --exclude {{package}}
Update all packages, making a backup of the current packages:
sudo tlmgr update --all --backup
Update a specific package without updating its dependencies:
sudo tlmgr update --no-depends {{package}}
Simulate updating all packages without making any changes:
sudo tlmgr update --all --dry-run
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
