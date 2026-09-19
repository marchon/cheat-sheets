# emacs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/emacs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg update
,
kubectl rollout
.
emacs
The extensible, customizable, self-documenting, real-time display editor.
See also
emacsclient
.
More information:
https://www.gnu.org/software/emacs
.
Start Emacs and open a file:
emacs {{path/to/file}}
Open a file at a specified line number:
emacs +{{line_number}} {{path/to/file}}
Start Emacs in console mode (without an X window):
emacs --no-window-system
Start an Emacs server in the background (accessible via
emacsclient
):
emacs --daemon
Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:
emacsclient --eval '(save-buffers-kill-emacs)'
Save a file in Emacs:
Ctrl + X, Ctrl + S
Quit Emacs:
Ctrl + X, Ctrl + C
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
