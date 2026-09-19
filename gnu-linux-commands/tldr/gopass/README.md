# gopass

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gopass/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hive
,
virsh pool info
,
dfc
,
tail
.
gopass
Standard Unix Password Manager for Teams. Written in Go.
More information:
https://www.gopass.pw
.
Initialize the configuration settings:
gopass init
Create a new entry:
gopass new
Show all stores:
gopass mounts
Mount a shared Git store:
gopass mounts add {{store_name}} {{git_repo_url}}
Search interactively using a keyword:
gopass show {{keyword}}
Search using a keyword:
gopass find {{keyword}}
Sync all mounted stores:
gopass sync
Show a particular password entry:
gopass {{store_name|path/to/directory|email@email.com}}
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
