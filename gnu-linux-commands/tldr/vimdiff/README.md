# vimdiff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vimdiff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sha512sum
,
virsh list
,
tslint
.
vimdiff
Open up two or more files in vim and show the differences between them.
See also
vim
.
More information:
https://www.vim.org
.
Open two files and show the differences:
vimdiff {{file1}} {{file2}}
Move the cursor to the window on the left|right:
Ctrl + w {{h|l}}
Jump to the next difference:
[c
Jump to the previous difference:
]c
Copy the highlighted difference from the other window to the current window:
do
Copy the highlighted difference from the current window to the other window:
dp
Update all highlights and folds:
:diffupdate
Toggle the highlighted code fold:
za
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
