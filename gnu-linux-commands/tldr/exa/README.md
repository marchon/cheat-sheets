# exa

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/exa/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
groups
,
who
,
ocrmypdf
,
go install
.
exa
A modern replacement for
ls
(List directory contents).
More information:
https://the.exa.website
.
List files one per line:
exa --oneline
List all files, including hidden files:
exa --all
Long format list (permissions, ownership, size and modification date) of all files:
exa --long --all
List files with the largest at the top:
exa --reverse --sort={{size}}
Display a tree of files, three levels deep:
exa --long --tree --level={{3}}
List files sorted by modification date (oldest first):
exa --long --sort={{modified}}
List files with their headers, icons, and Git statuses:
exa --long --header --icons --git
Don't list files mentioned in
.gitignore
:
exa --git-ignore
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
