# sendmail

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sendmail/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
influx
,
xml escape
,
ivpn
,
dog
,
dolt config
.
sendmail
Send email from the command-line.
More information:
https://manned.org/sendmail
.
Send a message with the content of
message.txt
to the mail directory of local user
username
:
sendmail {{username}} < {{message.txt}}
Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the message in
message.txt
:
sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}
Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the file
file.zip
:
sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}
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
