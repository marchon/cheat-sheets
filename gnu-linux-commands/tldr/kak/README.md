# kak

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kak/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fg
,
asar
,
tlmgr platform
,
ed
,
git cherry
.
kak
Kakoune is a mode-based code editor implementing the "multiple selections" paradigm.
Data can be selected and simultaneously edited in different locations, using multiple selections; users can also connect to the same session for collaborative editing.
More information:
https://kakoune.org
.
Open a file and enter normal mode, to execute commands:
kak {{path/to/file}}
Enter insert mode from normal mode, to write text into the file:
i
Escape insert mode, to go back to normal mode:
Replace all instances of "foo" in the current file with "bar":
%s{{foo}}
c{{bar}}
Unselect all secondary selections, and keep only the main one:
Search for numbers and select the first two:
/\d+
N
Insert the contents of a file:
!cat {{path/to/file}}
Save the current file:
:w
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
