# multitail

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/multitail/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue enqueue
,
xml canonic
.
multitail
Extension of tail.
More information:
https://manned.org/multitail
.
Tail all files matching a pattern in a single stream:
multitail -Q 1 '{{pattern}}'
Tail all files in a directory in a single stream:
multitail -Q 1 '{{directory}}/*'
Automatically add new files to a window:
multitail -Q {{pattern}}
Show 5 logfiles while merging 2 and put them in 2 columns with only one in the left column:
multitail -s 2 -sn 1,3 {{mergefile}} -I {{file1}} {{file2}} {{file3}} {{file4}}
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
