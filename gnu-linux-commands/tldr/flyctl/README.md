# flyctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/flyctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ptpython3
,
pueue completions
.
flyctl
Command-line tool for flyctl.io.
More information:
https://github.com/superfly/flyctl
.
Sign into a Fly account:
flyctl auth login
Launch an application from a specific Dockerfile (the default path is the current working directory):
flyctl launch --dockerfile {{path/to/dockerfile}}
Open the current deployed application in the default web browser:
flyctl open
Deploy the Fly applications from a specific Dockerfile:
flyctl deploy --dockerfile {{path/to/dockerfile}}
Open the Fly Web UI for the current application in a web browser:
flyctl dashboard
List all applications in the logged-in Fly account:
flyctl apps list
View the status of a specific running application:
flyctl status --app {{app_name}}
Show version information:
flyctl version
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
