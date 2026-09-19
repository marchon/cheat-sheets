# nvim

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nvim/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go fmt
,
pwgen
,
trawl
,
lpstat
,
ffprobe
.
nvim
Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation.
Pressing
i
enters edit mode.
goes back to normal mode, which doesn't allow regular text insertion.
More information:
https://neovim.io
.
Open a file:
nvim {{file}}
Enter text editing mode (insert mode):
i
Copy ("yank") or cut ("delete") the current line (paste it with
P
):
{{yy|dd}}
Undo the last operation:
u
Search for a pattern in the file (press
n
/
N
to go to next/previous match):
/{{search_pattern}}
Perform a regular expression substitution in the whole file:
:%s/{{regular_expression}}/{{replacement}}/g
Save (write) the file, and quit:
:wq
Quit without saving:
:q!
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
