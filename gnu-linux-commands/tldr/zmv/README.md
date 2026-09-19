# zmv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zmv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio team
,
amass viz
,
youtube viewer
.
zmv
Move or rename files matching a specified extended glob pattern.
See also
zcp
and
zln
.
More information:
http://zsh.sourceforge.net/Doc/Release/User-Contributions.html
.
Move files using a regular expression-like pattern:
zmv '{{(*).log}}' '{{$1.txt}}'
Preview the result of a move, without making any actual changes:
zmv -n '{{(*).log}}' '{{$1.txt}}'
Interactively move files, with a prompt before every change:
zmv -i '{{(*).log}}' '{{$1.txt}}'
Verbosely print each action as it's being executed:
zmv -v '{{(*).log}}' '{{$1.txt}}'
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
