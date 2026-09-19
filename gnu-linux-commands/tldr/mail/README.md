# mail

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mail/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
unalias
,
fc
,
docker machine
,
tailscale
.
mail
The command operates on the user's mailbox if no argument is given.
To send an email the message body is built from standard input.
More information:
https://manned.org/mail
.
Send a typed email message. The command-line below continues after pressing Enter key. Input CC email-id (optional) press Enter key. Input message text (can be multiline). Press Ctrl-D key to complete the message text:
mail --subject="{{subject line}}" {{to_user@example.com}}
Send an email that contains file content:
mail --subject="{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}
Send a
tar.gz
file as an attachment:
tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject="{{subject_line}}" {{to_user@example.com}}
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
