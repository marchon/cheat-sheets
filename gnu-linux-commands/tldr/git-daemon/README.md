# git-daemon

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-daemon/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nu
,
tsc
,
adscript
,
acyclic
,
pfetch
.
git daemon
A really simple server for Git repositories.
More information:
https://git-scm.com/docs/git-daemon
.
Launch a Git daemon with a whitelisted set of directories:
git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}
Launch a Git daemon with a specific base directory and allow pulling from all sub-directories that look like Git repositories:
git daemon --base-path={{path/to/directory}} --export-all --reuseaddr
Launch a Git daemon for the specified directory, verbosely printing log messages and allowing Git clients to write to it:
git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose
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
