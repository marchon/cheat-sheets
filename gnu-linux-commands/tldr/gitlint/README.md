# gitlint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gitlint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ssh agent
,
f3write
,
xpdf
,
ctest
.
gitlint
Git commit message linter checks your commit messages for style.
More information:
https://jorisroovers.com/gitlint/
.
Check the last commit message:
gitlint
The range of commits to lint:
gitlint --commits {{single_refspec_argument}}
Path to a directory or python module with extra user-defined rules:
gitlint --extra-path {{path/to/directory}}
Start a specific CI job:
gitlint --target {{path/to/target_directory}}
Path to a file containing a commit-msg:
gitlint --msg-filename {{path/to/filename}}
Read staged commit meta-info from the local repository:
gitlint --staged
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
