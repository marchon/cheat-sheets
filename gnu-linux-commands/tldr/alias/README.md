# alias

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/alias/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc unfreeze
,
cronic
,
git lock
.
alias
Creates aliases -- words that are replaced by a command string.
Aliases expire with the current shell session unless defined in the shell's configuration file, e.g.
~/.bashrc
.
More information:
https://tldp.org/LDP/abs/html/aliases.html
.
List all aliases:
alias
Create a generic alias:
alias {{word}}="{{command}}"
View the command associated to a given alias:
alias {{word}}
Remove an aliased command:
unalias {{word}}
Turn
rm
into an interactive command:
alias {{rm}}="{{rm --interactive}}"
Create
la
as a shortcut for
ls --all
:
alias {{la}}="{{ls --all}}"
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
