# git-instaweb

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-instaweb/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git reauthor
,
identify
,
gtop
.
git instaweb
Helper to launch a GitWeb server.
More information:
https://git-scm.com/docs/git-instaweb
.
Launch a GitWeb server for the current Git repository:
git instaweb --start
Listen only on localhost:
git instaweb --start --local
Listen on a specific port:
git instaweb --start --port {{1234}}
Use a specified HTTP daemon:
git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}
Also auto-launch a web browser:
git instaweb --start --browser
Stop the currently running GitWeb server:
git instaweb --stop
Restart the currently running GitWeb server:
git instaweb --restart
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
