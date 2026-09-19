# tlmgr-info

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-info/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sails
,
ptargrep
,
leave
,
figlet
.
tlmgr info
Show information about TeX Live packages.
More information:
https://www.tug.org/texlive/tlmgr.html
.
List all available TeX Live packages, prefexing installed ones with
i
:
tlmgr info
List all available collections:
tlmgr info collections
List all available schemes:
tlmgr info scheme
Show information about a specific package:
tlmgr info {{package_name}}
List all files contained in a specific package:
tlmgr info {{package_name}} --list
List all installed packages:
tlmgr info --only-installed
Show only specific information about a package:
tlmgr info {{package_name}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},..."
Print all available packages as JSON encoded array:
tlmgr info --json
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
