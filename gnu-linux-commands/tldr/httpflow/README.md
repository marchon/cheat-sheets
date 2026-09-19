# httpflow

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/httpflow/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cryfs
,
script
,
amass db
,
az tag
.
httpflow
A command-line utility to capture and dump HTTP streams.
More information:
https://github.com/six-ddc/httpflow
.
Capture traffic on all interfaces:
httpflow -i {{any}}
Use a bpf-style capture to filter the results:
httpflow {{host httpbin.org or host baidu.com}}
Use a regular expression to filter requests by URLs:
httpflow -u '{{regular_expression}}'
Read packets from pcap format binary file:
httpflow -r {{out.cap}}
Write the output to a directory:
httpflow -w {{path/to/directory}}
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
