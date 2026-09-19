# git-for-each-repo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-for-each-repo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
web ext
,
git lfs
,
zless
,
flac
,
xml
.
git for-each-repo
Run a Git command on a list of repositories.
Note: this command is experimental and may change.
More information:
https://git-scm.com/docs/git-for-each-repo
.
Run maintenance on each of a list of repositories stored in the
maintenance.repo
user configuration variable:
git for-each-repo --config={{maintenance.repo}} {{maintenance run}}
Run
git pull
on each repository listed in a global configuration variable:
git for-each-repo --config={{global_configuration_variable}} {{pull}}
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
