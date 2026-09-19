# git-remote

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-remote/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clojure
,
rip
,
avo
,
dexdump
,
laravel zero
.
git remote
Manage set of tracked repositories ("remotes").
More information:
https://git-scm.com/docs/git-remote
.
Show a list of existing remotes, their names and URL:
git remote -v
Show information about a remote:
git remote show {{remote_name}}
Add a remote:
git remote add {{remote_name}} {{remote_url}}
Change the URL of a remote (use
--add
to keep the existing URL):
git remote set-url {{remote_name}} {{new_url}}
Remove a remote:
git remote remove {{remote_name}}
Rename a remote:
git remote rename {{old_name}} {{new_name}}
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
