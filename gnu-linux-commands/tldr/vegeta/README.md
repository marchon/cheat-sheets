# vegeta

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vegeta/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
where
,
vegeta
,
shred
,
sshpass
,
bison
.
vegeta
A command-line utility and a library for HTTP load testing.
See also
ab
.
More information:
https://github.com/tsenart/vegeta
.
Launch an attack lasting 30 seconds:
echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}
Launch an attack on a server with a self-signed HTTPS certificate:
echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}
Launch an attack with a rate of 10 requests per second:
echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}
Launch an attack and display a report:
echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report
Launch an attack and plot the results on a graph (latency over time):
echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}
Launch an attack against multiple URLs from a file:
vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report
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
