# git-check-ignore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-check-ignore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
maestral
,
deluged
,
jhsdb
,
tcpdump
.
git check-ignore
Analyze and debug Git ignore / exclude (".gitignore") files.
More information:
https://git-scm.com/docs/git-check-ignore
.
Check whether a file or directory is ignored:
git check-ignore {{path/to/file_or_directory}}
Check whether multiple files or directories are ignored:
git check-ignore {{path/to/file}} {{path/to/directory}}
Use pathnames, one per line, from stdin:
git check-ignore --stdin < {{path/to/file_list}}
Do not check the index (used to debug why paths were tracked and not ignored):
git check-ignore --no-index {{path/to/files_or_directories}}
Include details about the matching pattern for each path:
git check-ignore --verbose {{path/to/files_or_directories}}
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
