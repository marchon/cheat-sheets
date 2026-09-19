# qmv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qmv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rtl_sdr
,
git reauthor
,
lpass
.
qmv
Move files and directories using the default text editor to define the filenames.
More information:
https://www.nongnu.org/renameutils/
.
Move a single file (open an editor with the source filename on the left and the target filename on the right):
qmv {{source_file}}
Move multiple JPG files:
qmv {{*.jpg}}
Move multiple directories:
qmv -d {{path/to/directory1}} {{path/to/directory2}} {{path/to/directory3}}
Move all files and directories inside a directory:
qmv --recursive {{path/to/directory}}
Move files, but swap the positions of the source and the target filenames in the editor:
qmv --option swap {{*.jpg}}
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
