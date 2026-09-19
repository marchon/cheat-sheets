# histexpand

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/histexpand/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tokei
,
git branch
,
nvm.fish
,
http server upload
.
history expansion
Reuse and expand the shell history in
sh
,
bash
,
zsh
,
rbash
and
ksh
.
More information:
https://www.gnu.org/software/bash/manual/html_node/History-Interaction
.
Run the previous command as root (
!!
is replaced by the previous command):
sudo !!
Run a command with the last argument of the previous command:
{{command}} !$
Run a command with the first argument of the previous command:
{{command}} !^
Run the Nth command of the history:
!{{n}}
Run the command
n
lines back in the history:
!-{{n}}
Run the most recent command containing
string
:
!?{{string}}?
Run the previous command, replacing
string1
with
string2
:
^{{string1}}^{{string2}}^
Perform a history expansion, but print the command that would be run instead of actually running it:
{{!-n}}:p
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
