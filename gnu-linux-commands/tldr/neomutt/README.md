# neomutt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/neomutt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gcloud
,
fossa
,
shc
,
mullvad
,
az appconfig
.
neomutt
NeoMutt command line email client.
More information:
https://neomutt.org
.
Open the specified mailbox:
neomutt -f {{path/to/mailbox}}
Start writing an email and specify a subject and a
cc
recipient:
neomutt -s "{{subject}}" -c {{cc@example.com}} {{recipient@example.com}}
Send an email with files attached:
neomutt -a {{path/to/file1 path/to/file2 ...}} -- {{recipient@example.com}}
Specify a file to include as the message body:
neomutt -i {{path/to/file}} {{recipient@example.com}}
Specify a draft file containing the header and the body of the message, in RFC 5322 format:
neomutt -H {{path/to/file}} {{recipient@example.com}}
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
