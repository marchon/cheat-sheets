# zoxide

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zoxide/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
split
,
tlmgr paper
,
truffle
,
coffee
.
zoxide
Keep track of the most frequently used directories.
Uses a ranking algorithm to navigate to the best match.
More information:
https://github.com/ajeetdsouza/zoxide
.
Go to the highest-ranked directory that contains "foo" in the name:
zoxide query {{foo}}
Go to the highest-ranked directory that contains "foo" and then "bar":
zoxide query {{foo}} {{bar}}
Start an interactive directory search (requires
fzf
):
zoxide query --interactive
Add a directory or increment its rank:
zoxide add {{path/to/directory}}
Remove a directory from
zoxide
's database interactively:
zoxide remove {{path/to/directory}} --interactive
Generate shell configuration for command aliases (
z
,
za
,
zi
,
zq
,
zr
):
zoxide init {{bash|fish|zsh}}
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
