# git-push

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-push/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clang format
,
scc
,
which
,
pwd
,
mkfifo
.
git push
Push commits to a remote repository.
More information:
https://git-scm.com/docs/git-push
.
Send local changes in the current branch to its default remote counterpart:
git push
Send changes from a specific local branch to its remote counterpart:
git push {{remote_name}} {{local_branch}}
Send changes from a specific local branch to its remote counterpart, and set the remote one as the default push/pull target of the local one:
git push -u {{remote_name}} {{local_branch}}
Send changes from a specific local branch to a specific remote branch:
git push {{remote_name}} {{local_branch}}:{{remote_branch}}
Send changes on all local branches to their counterparts in a given remote repository:
git push --all {{remote_name}}
Delete a branch in a remote repository:
git push {{remote_name}} --delete {{remote_branch}}
Remove remote branches that don't have a local counterpart:
git push --prune {{remote_name}}
Publish tags that aren't yet in the remote repository:
git push --tags
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
