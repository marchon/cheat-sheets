# shc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/shc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kubectl describe
,
httprobe
.
shc
Generic shell script compiler.
More information:
https://manned.org/shc
.
Compile a shell script:
shc -f {{script}}
Compile a shell script and specify an output binary file:
shc -f {{script}} -o {{binary}}
Compile a shell script and set an expiration date for the executable:
shc -f {{script}} -e {{dd/mm/yyyy}}
Compile a shell script and set a message to display upon expiration:
shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{Please contact your provider}}"
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
