# core-validate-commit

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/core-validate-commit/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jhsdb
,
az bicep
,
sdkmanager
,
transmission cli
.
core-validate-commit
Validate commit messages for Node.js core.
More information:
https://github.com/nodejs/core-validate-commit
.
Validate the current commit:
core-validate-commit
Validate a specific commit:
core-validate-commit {{commit_hash}}
Validate a range of commits:
git rev-list {{commit_hash}}..HEAD | xargs core-validate-commit
List all validation rules:
core-validate-commit --list
List all valid Node.js subsystems:
core-validate-commit --list-subsystem
Validate the current commit formatting the output in tap format:
core-validate-commit --tap
Display help:
core-validate-commit --help
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
