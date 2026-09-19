# mutt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mutt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aapt
,
kosmorro
,
docker cp
,
jupyter
.
mutt
Command-line email client.
More information:
http://mutt.org
.
Open the specified mailbox:
mutt -f {{mailbox}}
Send an email and specify a subject and a cc recipient:
mutt -s {{subject}} -c {{cc@example.com}} {{recipient@example.com}}
Send an email with files attached:
mutt -a {{file1}} {{file2}} -- {{recipient@example.com}}
Specify a file to include as the message body:
mutt -i {{file}} {{recipient@example.com}}
Specify a draft file containing the header and the body of the message, in RFC 5322 format:
mutt -H {{file}} {{recipient@example.com}}
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
