# tlmgr-remove

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-remove/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git missing
,
hsw cli
,
smbmap
.
tlmgr remove
Uninstall TeX Live packages.
By default, removed packages will be backed up to
./tlpkg/backups
under the TL installation directory.
More information:
https://www.tug.org/texlive/tlmgr.html
.
Uninstall a TeX Live package:
sudo tlmgr remove {{package}}
Simulate uninstalling a package without making any changes:
tlmgr remove --dry-run {{package}}
Uninstall a package without its dependencies:
sudo tlmgr remove --no-depends {{package}}
Uninstall a package and back it up to a specific directory:
sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}
Uninstall all of TeX Live, asking for confirmation:
sudo tlmgr remove --all
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
