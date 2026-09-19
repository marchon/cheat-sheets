# p4

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/p4/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
date
,
tlmgr
,
syncthing
,
ocaml
,
rails destroy
.
p4
Perforce Version Control System.
More information:
https://www.perforce.com/manuals/cmdref
.
Log in to the Perforce service:
p4 login -a
Create a client:
p4 client
Copy files from depot into the client workspace:
p4 sync
Create or edit changelist description:
p4 change
Open a file to edit:
p4 edit -c {{changelist_number}} {{filename}}
Open a new file to add it to the depot:
p4 add
Display list of files modified by changelist:
p4 describe -c {{changelist_number}}
Submit a changelist to the depot:
p4 submit -c {{changelist_number}}
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
