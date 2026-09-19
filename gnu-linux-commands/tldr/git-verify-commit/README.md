# git-verify-commit

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-verify-commit/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dcode
,
gcloud
,
dotnet restore
.
git verify-commit
Check for GPG verification of commits.
If no commits are verified, nothing will be printed, regardless of options specified.
More information:
https://git-scm.com/docs/git-verify-commit
.
Check commits for a GPG signature:
git verify-commit {{commit_hash1 optional_commit_hash2 ...}}
Check commits for a GPG signature and show details of each commit:
git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --verbose
Check commits for a GPG signature and print the raw details:
git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw
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
