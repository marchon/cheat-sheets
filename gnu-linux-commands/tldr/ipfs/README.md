# ipfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ipfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pretty bytes
,
cabal
,
view
,
calibredb
.
ipfs
Inter Planetary File System.
A peer-to-peer hypermedia protocol. Aims to make the web more open.
More information:
https://ipfs.io
.
Add a file from local to the filesystem, pin it and print the relative hash:
ipfs add {{filename}}
Add a directory and its files recursively from local to the filesystem and print the relative hash:
ipfs add -r {{directory}}
Save a remote file and give it a name but not pin it:
ipfs get {{hash}} -o {{filename}}
Pin a remote file locally:
ipfs pin add {{hash}}
Display pinned files:
ipfs pin ls
Unpin a file from the local storage:
ipfs pin rm {{hash}}
Remove unpinned files from local storage:
ipfs repo gc
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
