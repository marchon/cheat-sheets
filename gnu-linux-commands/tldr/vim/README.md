# vim

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vim/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git show branch
,
git blame someone else
.
vim
Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
Pressing
i
enters insert mode.
enters normal mode, which enables the use of Vim commands.
More information:
https://www.vim.org
.
Open a file:
vim {{path/to/file}}
Open a file at a specified line number:
vim +{{line_number}} {{path/to/file}}
View Vim's help manual:
:help
Save and Quit:
:wq
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
Display the line numbers:
:set nu
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
