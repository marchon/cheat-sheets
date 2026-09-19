# oathtool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/oathtool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gacutil
,
choose
,
py spy
,
ls
,
git archive
.
oathtool
OATH one-time password tool.
More information:
https://www.nongnu.org/oath-toolkit/oathtool.1.html
.
Generate TOTP token (behaves like Google Authenticator):
oathtool --totp --base32 "{{secret}}"
Generate a TOTP token for a specific time:
oathtool --totp --now "{{2004-02-29 16:21:42}}" --base32 "{{secret}}"
Validate a TOTP token:
oathtool --totp --base32 "{{secret}}" "{{token}}"
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
