# lpass

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lpass/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
linkchecker
,
glab auth
,
apm
,
dotnet tool
.
lpass
Command-line interface for the LastPass password manager.
More information:
https://github.com/lastpass/lastpass-cli
.
Log in to your LastPass account, by entering your master password when prompted:
lpass login {{username}}
Show login status:
lpass status
List all sites grouped by category:
lpass ls
Generate a new password for gmail.com with the identifier
myinbox
and add to LastPass:
lpass generate --username {{username}} --url {{gmail.com}} {{myinbox}} {{password_length}}
Show password for a specified entry:
lpass show {{myinbox}} --password
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
