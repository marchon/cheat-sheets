# lerna

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lerna/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
where
,
iperf3
,
duplicacy
,
ykinfo
.
lerna
A tool for managing JavaScript projects with multiple packages.
More information:
https://lerna.js.org
.
Initialize project files (
lerna.json
,
package.json
,
.git
, etc.):
lerna init
Install all external dependencies of each package and symlink together local dependencies:
lerna bootstrap
Run a specific script for every package that contains it in its
package.json
:
lerna run {{script}}
Execute an arbitrary shell command in every package:
lerna exec -- {{ls}}
Publish all packages that have changed since the last release:
lerna publish
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
