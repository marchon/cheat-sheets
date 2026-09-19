# chezmoi

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/chezmoi/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
scheme
,
git fork
,
base32
,
textql
.
Chezmoi
A multi-machine dotfile manager, written in Go.
More information:
https://chezmoi.io
.
Initialize chezmoi on your machine:
chezmoi init
Tell chezmoi to manage a dotfile:
chezmoi add {{path/to/file}}
Edit the source state of a tracked dotfile:
chezmoi edit {{path/to/file}}
See changes chezmoi would make:
chezmoi diff
Apply the changes:
chezmoi -v apply
Set chezmoi up on another machine by downloading existing dotfiles from a Git repository:
chezmoi init {{https://example.com/path/to/repository.git}}
Fetch the latest changes from a remote repository:
chezmoi update
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
