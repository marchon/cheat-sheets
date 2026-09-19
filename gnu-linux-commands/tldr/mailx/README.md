# mailx

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mailx/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
roll
,
uname
,
openssl s_client
.
mailx
Send and receive mail.
More information:
https://manned.org/mailx
.
Send mail (the content should be typed after the command, and ended with
Ctrl+D
):
mailx -s "{{subject}}" {{to_addr}}
Send mail with content passed from another command:
echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}
Send mail with content read from a file:
mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}
Send mail to a recipient and CC to another address:
mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}
Send mail specifying the sender address:
mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}
Send mail with an attachment:
mailx -a {{file}} -s "{{subject}}" {{to_addr}}
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
