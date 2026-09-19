# jc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc unfreeze
,
gcc
,
terragrunt
.
jc
A utility to convert the output of multiple commands to JSON.
More information:
https://github.com/kellyjonbrazil/jc
.
Convert command output to JSON via pipe:
{{ifconfig}} | jc {{--ifconfig}}
Convert command output to JSON via magic syntax:
jc {{ifconfig}}
Output pretty JSON via pipe:
{{ifconfig}} | jc {{--ifconfig}} -p
Output pretty JSON via magic syntax:
jc -p {{ifconfig}}
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
