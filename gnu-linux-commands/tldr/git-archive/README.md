# git-archive

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-archive/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
shc
,
gh formatting
,
pest
,
ranger
.
git archive
Create an archive of files from a named tree.
More information:
https://git-scm.com/docs/git-archive
.
Create a tar archive from the contents of the current HEAD and print it to standard output:
git archive --verbose HEAD
Create a zip archive from the current HEAD and print it to standard output:
git archive --verbose --format=zip HEAD
Same as above, but write the zip archive to file:
git archive --verbose --output={{path/to/file.zip}} HEAD
Create a tar archive from the contents of the latest commit on a specific branch:
git archive --output={{path/to/file.tar}} {{branch_name}}
Create a tar archive from the contents of a specific directory:
git archive --output={{path/to/file.tar}} HEAD:{{path/to/directory}}
Prepend a path to each file to archive it inside a specific directory:
git archive --output={{path/to/file.tar}} --prefix={{path/to/prepend}}/ HEAD
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
