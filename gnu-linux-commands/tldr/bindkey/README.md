# bindkey

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bindkey/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
minetest
,
github label sync
.
bindkey
Add keybindings to Z-Shell.
More information:
https://zsh.sourceforge.io/Guide/zshguide04.html
.
Bind a hotkey to a specific command:
bindkey "{{^k}}" {{kill-line}}
Bind a hotkey to a specific key sequence:
bindkey -s '^o' 'cd ..\n'
View keymaps:
bindkey -l
View the hotkey in a keymap:
bindkey -M main
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
