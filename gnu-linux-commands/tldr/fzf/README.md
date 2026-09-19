# fzf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fzf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdftocairo
,
kiwi ng
,
ncc
,
clamscan
.
fzf
Command-line fuzzy finder.
Similar to
sk
.
More information:
https://github.com/junegunn/fzf
.
Start fzf on all files in the specified directory:
find {{path/to/directory}} -type f | fzf
Start fzf for running processes:
ps aux | fzf
Select multiple files with
Shift + Tab
and write to a file:
find {{path/to/directory}} -type f | fzf --multi > {{filename}}
Start fzf with a specified query:
fzf --query "{{query}}"
Start fzf on entries that start with core and end with either go, rb, or py:
fzf --query "^core go$ | rb$ | py$"
Start fzf on entries that not match pyc and match exactly travis:
fzf --query "!pyc 'travis"
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
