# direnv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/direnv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
info
,
jupyter
,
git format patch
.
direnv
Shell extension to load and unload environment variables depending on the current directory.
More information:
https://github.com/direnv/direnv
.
Grant direnv permission to load the
.envrc
present in the current directory:
direnv allow {{.}}
Revoke the authorization to load the
.envrc
present in the current directory:
direnv deny {{.}}
Edit the
.envrc
file in the default text editor and reload the environment on exit:
direnv edit {{.}}
Trigger a reload of the environment:
direnv reload
Print some debug status information:
direnv status
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
