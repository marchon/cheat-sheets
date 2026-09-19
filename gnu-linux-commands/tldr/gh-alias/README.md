# gh-alias

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-alias/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stolonctl
,
gh reference
,
docker rmi
.
gh alias
Manage GitHub CLI command aliases from the command-line.
More information:
https://cli.github.com/manual/gh_alias
.
Display the subcommand help:
gh alias
List all the aliases
gh
is configured to use:
gh alias list
Create a
gh
subcommand alias:
gh alias set {{pv}} '{{pr view}}'
Set a shell command as a
gh
subcommand:
gh alias set --shell {{alias_name}} {{command}}
Delete a command shortcut:
gh alias delete {{alias_name}}
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
