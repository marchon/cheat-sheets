# bw

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bw/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sops
,
swig
,
git unlock
,
unzip
,
phing
.
bw
A CLI to access and manage a Bitwarden vault.
More information:
https://help.bitwarden.com/article/cli/
.
Log in to a Bitwarden user account:
bw login
Log out of a Bitwarden user account:
bw logout
Search and display items from Bitwarden vault:
bw list items --search {{github}}
Display a particular item from Bitwarden vault:
bw get item {{github}}
Create a folder in Bitwarden vault:
{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder
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
