# tlmgr-paper

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-paper/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gcal
,
pueue completions
,
pdfjoin
.
tlmgr paper
Manage paper size options of an TeX Live installation.
More information:
https://www.tug.org/texlive/tlmgr.html
.
Show the default paper size used by all TeX Live programs:
tlmgr paper
Set the default paper size for all TeX Live programs to A4:
sudo tlmgr paper {{a4}}
Show the default paper size used by a specific TeX Live program:
tlmgr {{pdftex}} paper
Set the default paper size for a specific TeX Live program to A4:
sudo tlmgr {{pdftex}} paper {{a4}}
List all available paper sizes for a specific TeX Live program:
tlmgr {{pdftex}} paper --list
Dump the default paper size used by all TeX Live programs in JSON format:
tlmgr paper --json
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
