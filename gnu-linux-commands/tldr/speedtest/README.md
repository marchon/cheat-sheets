# speedtest

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/speedtest/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc fetch
,
mlr
,
piodebuggdb
,
sc im
.
speedtest
Official command-line interface for testing internet bandwidth using https://speedtest.net.
Note: some platforms link
speedtest
to
speedtest-cli
. If some of the examples in this page don't work, see
speedtest-cli
.
More information:
https://www.speedtest.net/apps/cli
.
Run a speed test:
speedtest
Run a speed test and specify the unit of the output:
speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}
Run a speed test and specify the output format:
speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}
Run a speed test and specify the number of decimal points to use (0 to 8, defaults to 2):
speedtest --precision={{precision}}
Run a speed test and print its progress (only available for output format
human-readable
and
json
):
speedtest --progress={{yes|no}}
List all
speedtest.net
servers, sorted by distance:
speedtest --servers
Run a speed test to a specific
speedtest.net
server:
speedtest --server-id={{server_id}}
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
