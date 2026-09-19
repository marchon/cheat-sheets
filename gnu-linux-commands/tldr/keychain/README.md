# keychain

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/keychain/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
plesk
,
ffplay
,
standard
,
grumphp
.
keychain
Re-use ssh-agent and/or gpg-agent between logins.
More information:
http://funtoo.org/Keychain
.
Check for a running ssh-agent, and start one if needed:
keychain
Also check for gpg-agent:
keychain --agents "{{gpg,ssh}}"
List signatures of all active keys:
keychain --list
List fingerprints of all active keys:
keychain --list-fp
Add a timeout for identities added to the agent, in minutes:
keychain --timeout {{minutes}}
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
