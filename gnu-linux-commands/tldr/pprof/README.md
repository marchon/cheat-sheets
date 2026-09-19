# pprof

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pprof/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue shutdown
,
sort
,
espeak
.
pprof
Command-line tool for visualization and analysis of profile data.
More information:
https://github.com/google/pprof
.
Generate a text report from a specific profiling file, on fibbo binary:
pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}
Generate a graph and open it on a web browser:
pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}
Run pprof in interactive mode to be able to manually launch
pprof
on a file:
pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}
Run a web server that serves a web interface on top of
pprof
:
pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}
Fetch a profile from an HTTP server and generate a report:
pprof {{http://localhost:8080/debug/pprof}}
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
