# git-config

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-config/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
logstash
,
zipinfo
,
ld
,
textql
,
spike
.
git config
Manage custom configuration options for Git repositories.
These configurations can be local (for the current repository) or global (for the current user).
More information:
https://git-scm.com/docs/git-config
.
List only local configuration entries (stored in
.git/config
in the current repository):
git config --list --local
List only global configuration entries (stored in
~/.gitconfig
):
git config --list --global
List all configuration entries that have been defined either locally or globally:
git config --list
Get the value of a given configuration entry:
git config alias.unstage
Set the global value of a given configuration entry:
git config --global alias.unstage "reset HEAD --"
Revert a global configuration entry to its default value:
git config --global --unset alias.unstage
Edit the Git configuration for the current repository in the default editor:
git config --edit
Edit the global Git configuration in the default editor:
git config --global --edit
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
