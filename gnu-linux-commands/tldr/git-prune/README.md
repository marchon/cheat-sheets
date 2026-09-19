# git-prune

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-prune/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansible pull
,
influx
,
hg update
.
git prune
Git command for pruning all unreachable objects from the object database.
This command is often not used directly but as an internal command that is used by Git gc.
More information:
https://git-scm.com/docs/git-prune
.
Report what would be removed by Git prune without removing it:
git prune --dry-run
Prune unreachable objects and display what has been pruned to stdout:
git prune --verbose
Prune unreachable objects while showing progress:
git prune --progress
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
