# tox

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tox/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cradle deploy
,
sendmail
,
gh formatting
.
tox
Automate Python testing across multiple Python versions.
Use tox.ini to configure environments and test command.
More information:
https://github.com/tox-dev/tox
.
Run tests on all test environments:
tox
Create a
tox.ini
configuration:
tox-quickstart
List the available environments:
tox --listenvs-all
Run tests on a specific environment (e.g. python 3.6):
tox -e {{py36}}
Force the virtual environment to be recreated:
tox --recreate -e {{py27}}
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
