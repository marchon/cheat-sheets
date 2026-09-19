# gh-pr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-pr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
drush
,
nim
,
go fix
,
expand
,
ssh
,
hg clone
.
gh pr
Manage GitHub pull requests from the command-line.
More information:
https://cli.github.com/manual/gh_pr
.
Create a pull request:
gh pr create
Check out a specific pull request locally:
gh pr checkout {{pr_number}}
View the changes made in the pull request for the current branch:
gh pr diff
Approve the pull request for the current branch:
gh pr review --approve
Merge the pull request associated with the current branch interactively:
gh pr merge
Edit a pull request interactively:
gh pr edit
Edit the base branch of a pull request:
gh pr edit --base {{branch_name}}
Check the status of the current repository's pull requests:
gh pr status
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
