# httprobe

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/httprobe/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue kill
,
imapsync
,
transmission create
.
httprobe
Take a list of domains and probe for working HTTP and HTTPS servers.
More information:
https://github.com/tomnomnom/httprobe
.
Probe a list of domains from a text file:
cat {{input_file}} | httprobe
Only check for HTTP if HTTPS is not working:
cat {{input_file}} | httprobe --prefer-https
Probe additional ports with a given protocol:
cat {{input_file}} | httprobe -p {{https:2222}}
Output all available options:
httprobe --help
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
