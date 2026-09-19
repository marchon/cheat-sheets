# k6

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/k6/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
autossh
,
s3cmd
,
yes
,
doctum
,
colordiff
.
k6
Open source load testing tool and SaaS for engineering teams.
More information:
https://k6.io
.
Run load test locally:
k6 run {{script.js}}
Run load test locally with a given number of virtual users and duration:
k6 run --vus {{10}} --duration {{30s}} {{script.js}}
Run load test locally with a given environment variable:
k6 run -e {{HOSTNAME=example.com}} {{script.js}}
Run load test locally using InfluxDB to store results:
k6 run --out influxdb={{http://localhost:8086/k6db}} {{script.js}}
Run load test locally and discard response bodies (significantly faster):
k6 run --discard-response-bodies {{script.js}}
Run load test locally using the base JavaScript compatibility mode (significantly faster):
k6 run --compatibility-mode=base {{script.js}}
Log in to cloud service using secret token:
k6 login cloud --token {{secret}}
Run load test on cloud infrastructure:
k6 cloud {{script.js}}
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
