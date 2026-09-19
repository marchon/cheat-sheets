# locust

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/locust/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
latexmk
,
git effort
,
git contrib
.
locust
Load-testing tool to determine number of concurrent users a system can handle.
More information:
https://locust.io
.
Load-test "example.com" with web interface using locustfile.py:
locust --host={{http://example.com}}
Use a different test file:
locust --locustfile={{test_file.py}} --host={{http://example.com}}
Run test without web interface, spawning 1 user a second until there are 100 users:
locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}
Start locust in master mode:
locust --master --host={{http://example.com}}
Connect locust slave to master:
locust --slave --host={{http://example.com}}
Connect locust slave to master on a different machine:
locust --slave --master-host={{master_hostname}} --host={{http://example.com}}
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
