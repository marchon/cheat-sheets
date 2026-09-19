# speedtest-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/speedtest-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ebook convert
,
mr
,
cradle
,
expr
.
speedtest-cli
Unofficial command-line interface for testing internet bandwidth using https://speedtest.net.
See also
speedtest
for the official CLI.
More information:
https://github.com/sivel/speedtest-cli
.
Run a speed test:
speedtest-cli
Run a speed test and display values in bytes, instead of bits:
speedtest-cli --bytes
Run a speed test using
HTTPS
, instead of
HTTP
:
speedtest-cli --secure
Run a speed test without performing download tests:
speedtest-cli --no-download
Run a speed test and generate an image of the results:
speedtest-cli --share
List all
speedtest.net
servers, sorted by distance:
speedtest-cli --list
Run a speed test to a specific speedtest.net server:
speedtest-cli --server {{server_id}}
Run a speed test and display the results as JSON (suppresses progress information):
speedtest-cli --json
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
