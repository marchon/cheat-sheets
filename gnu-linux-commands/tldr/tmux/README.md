# tmux

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tmux/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
micro
,
odps func
,
sudo
,
asdf
,
mosquitto_pub
.
tmux
Terminal multiplexer. It allows multiple sessions with windows, panes, and more.
See also
zellij
and
screen
.
More information:
https://github.com/tmux/tmux
.
Start a new session:
tmux
Start a new named session:
tmux new -s {{name}}
List existing sessions:
tmux ls
Attach to the most recently used session:
tmux attach
Detach from the current session (inside a tmux session):
Ctrl-B d
Create a new window (inside a tmux session):
Ctrl-B c
Switch between sessions and windows (inside a tmux session):
Ctrl-B w
Kill a session by name:
tmux kill-session -t {{name}}
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
