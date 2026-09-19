# gh-pr-create

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-pr-create/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git ignore
,
pio home
,
bzip2
,
pnpm
.
gh pr create
Manage GitHub pull requests from the command-line.
More information:
https://cli.github.com/manual/gh_pr_create
.
Interactively create a pull request:
gh pr create
Create a pull request, determining the title and description from the commit messages of the current branch:
gh pr create --fill
Create a draft pull request:
gh pr create --draft
Create a pull request specifying the base branch, title, and description:
gh pr create --base {{base_branch}} --title "{{title}}" --body "{{body}}"
Start opening a pull request in the default web browser:
gh pr create --web
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
