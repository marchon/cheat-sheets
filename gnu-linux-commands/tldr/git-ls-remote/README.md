# git-ls-remote

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-ls-remote/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
php artisan
,
pwsh
,
mosh
,
atom
,
csvcut
.
git ls-remote
Git command for listing references in a remote repository based on name or URL.
If no name or URL are given, then the configured upstream branch will be used, or remote origin if the former is not configured.
More information:
https://git-scm.com/docs/git-ls-remote
.
Show all references in the default remote repository:
git ls-remote
Show only heads references in the default remote repository:
git ls-remote --heads
Show only tags references in the default remote repository:
git ls-remote --tags
Show all references from a remote repository based on name or URL:
git ls-remote {{repository_url}}
Show references from a remote repository filtered by a pattern:
git ls-remote {{repository_name}} "{{pattern}}"
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
