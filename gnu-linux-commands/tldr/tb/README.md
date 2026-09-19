# tb

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tb/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
firebase
,
gcal
,
zola
,
cabal
,
acme.sh dns
.
tb
CLI for managing tasks and notes across multiple boards.
More information:
https://github.com/klaussinani/taskbook
.
Add a new task to a board:
tb --task {{task_description}} @{{board_name}}
Add a new note to a board:
tb --note {{note_description}} @{{board_name}}
Edit item's priority:
tb --priority @{{item_id}} {{priority}}
Check/uncheck item:
tb --check {{item_id}}
Archive all checked items:
tb --clear
Move item to a board:
tb --move @{{item_id}} {{board_name}}
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
