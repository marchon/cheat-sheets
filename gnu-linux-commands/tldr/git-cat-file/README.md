# git-cat-file

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-cat-file/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arduino
,
glances
,
lpstat
,
joe
,
docker run
.
git cat-file
Provide content or type and size information for Git repository objects.
More information:
https://git-scm.com/docs/git-cat-file
.
Get the [s]ize of the HEAD commit in bytes:
git cat-file -s HEAD
Get the [t]ype (blob, tree, commit, tag) of a given Git object:
git cat-file -t {{8c442dc3}}
Pretty-[p]rint the contents of a given Git object based on its type:
git cat-file -p {{HEAD~2}}
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
