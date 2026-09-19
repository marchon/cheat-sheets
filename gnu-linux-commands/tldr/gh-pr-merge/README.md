# gh-pr-merge

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-pr-merge/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pyflakes
,
openssl s_client
.
gh pr merge
Merge GitHub pull requests.
More information:
https://cli.github.com/manual/gh_pr_merge
.
Merge the pull request associated with the current branch interactively:
gh pr merge
Merge the specified pull request, interactively:
gh pr merge {{pr_number}}
Merge the pull request, removing the branch on both the local and the remote:
gh pr merge --delete-branch
Merge the current pull request with the specified merge strategy:
gh pr merge --{{merge|squash|rebase}}
Merge the current pull request with the specified merge strategy and commit message:
gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}
Squash the current pull request into one commit with the message body and merge:
gh pr merge --squash --body="{{commit_message_body}}"
Display help:
gh pr merge --help
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
