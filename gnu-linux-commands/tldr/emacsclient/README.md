# emacsclient

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/emacsclient/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mh_copyright
,
mp3info
,
odps func
.
emacsclient
Open files in an existing Emacs server.
See also
emacs
.
More information:
https://www.emacswiki.org/emacs/EmacsClient
.
Open a file in an existing Emacs server (using GUI if available):
emacsclient {{path/to/file}}
Open a file in console mode (without an X window):
emacsclient --no-window-system {{path/to/file}}
Open a file in a new Emacs window:
emacsclient --create-frame {{path/to/file}}
Evaluate a command, printing the output to stdout, and then quit:
emacsclient --eval '({{command}})'
Specify an alternative editor in case no Emacs server is running:
emacsclient --alternate-editor {{editor}} {{path/to/file}}
Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:
emacsclient --eval '(save-buffers-kill-emacs)'
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
