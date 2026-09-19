# spfquery

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/spfquery/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
task
,
kotlin
,
git fetch
,
mat2
,
electrum
.
spfquery
Query Sender Policy Framework records to validate e-mail senders.
More information:
https://www.libspf2.org/
.
Check if an IP address is allowed to send an e-mail from the specified e-mail address:
spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}}
Turn on debugging output:
spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}} --debug
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
