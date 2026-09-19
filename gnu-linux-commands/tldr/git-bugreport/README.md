# git-bugreport

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-bugreport/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vi
,
npx
,
xephyr
,
write
,
tsort
,
cd
.
git bugreport
Captures debug information from the system and user, generating a text file to aid in the reporting of a bug in Git.
More information:
https://git-scm.com/docs/git-bugreport
.
Create a new bug report file in the current directory:
git bugreport
Create a new bug report file in the specified directory, creating it if it does not exist:
git bugreport --output-directory {{path/to/directory}}
Create a new bug report file with the specified filename suffix in
strftime
format:
git bugreport --suffix {{%m%d%y}}
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
