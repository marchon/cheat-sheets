# git-reauthor

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-reauthor/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm nm
,
gh alias
,
apg
,
vlc
,
redis cli
.
git reauthor
Change details about an author identity. Since this command rewrites the Git history,
--force
will be needed when pushing next time.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor
.
Change an author's email and name across the whole Git repository:
git reauthor --old-email {{old@example.com}} --correct-email {{new@example.com}} --correct-name "{{name}}"
Change the email and name to the ones defined in the Git config:
git reauthor --old-email {{old@example.com}} --use-config
Change the email and name of all commits, regardless of their original author:
git reauthor --all --correct-email {{name@example.com}} --correct-name {{name}}
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
