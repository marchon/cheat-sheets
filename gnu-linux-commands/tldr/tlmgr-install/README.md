# tlmgr-install

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-install/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
molecule
,
go env
,
git filter repo
.
tlmgr install
Install TeX Live packages.
More information:
https://www.tug.org/texlive/tlmgr.html
.
Install a package and its dependencies:
sudo tlmgr install {{package}}
Reinstall a package:
sudo tlmgr install --reinstall {{package}}
Simulate installing a package without making any changes:
tlmgr install --dry-run {{package}}
Install a package without its dependencies:
sudo tlmgr install --no-depends {{package}}
Install a package from a specific file:
sudo tlmgr install --file {{path/to/package}}
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
