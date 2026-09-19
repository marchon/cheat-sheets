# glab-alias

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glab-alias/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
grex
,
pax
,
expose
,
git branch
,
git coauthor
.
glab alias
Manage GitLab CLI command aliases from the command-line.
More information:
https://glab.readthedocs.io/en/latest/alias
.
Display the subcommand help:
glab alias
List all the aliases
glab
is configured to use:
glab alias list
Create a
glab
subcommand alias:
glab alias set {{mrv}} '{{mr view}}'
Set a shell command as a
glab
subcommand:
glab alias set --shell {{alias_name}} {{command}}
Delete a command shortcut:
glab alias delete {{alias_name}}
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
