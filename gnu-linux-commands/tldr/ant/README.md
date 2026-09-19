# ant

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ant/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go generate
,
dvc destroy
,
kdeconnect cli
.
ant
Apache Ant.
Tool for building and managing Java-based projects.
More information:
https://ant.apache.org
.
Build a project with default build file
build.xml
:
ant
Build a project using build file other than
build.xml
:
ant -f {{buildfile.xml}}
Print information on possible targets for this project:
ant -p
Print debugging information:
ant -d
Execute all targets that do not depend on fail target(s):
ant -k
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
