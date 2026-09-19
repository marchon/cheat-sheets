# msmtp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/msmtp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
npm name
,
git format patch
.
msmtp
An SMTP client.
It reads text from standard input and sends it to an SMTP server.
More information:
https://marlam.de/msmtp
.
Send an email using the default account configured in
~/.msmtprc
:
echo "{{Hello world}}" | msmtp {{to@example.org}}
Send an email using a specific account configured in
~/.msmtprc
:
echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}
Send an email without a configured account. The password should be specified in the
~/.msmtprc
file:
echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}
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
