# hg-clone

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hg-clone/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nohup
,
csvstat
,
imapsync
,
ipsumdump
.
hg clone
Create a copy of an existing repository in a new directory.
More information:
https://www.mercurial-scm.org/doc/hg.1.html#clone
.
Clone a repository to a specified directory:
hg clone {{remote_repository_source}} {{destination_path}}
Clone a repository to the head of a specific branch, ignoring later commits:
hg clone --branch {{branch}} {{remote_repository_source}}
Clone a repository with only the
.hg
directory, without checking out files:
hg clone --noupdate {{remote_repository_source}}
Clone a repository to a specific revision, tag or branch, keeping the entire history:
hg clone --updaterev {{revision}} {{remote_repository_source}}
Clone a repository up to a specific revision without any newer history:
hg clone --rev {{revision}} {{remote_repository_source}}
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
