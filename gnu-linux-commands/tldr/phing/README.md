# phing

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phing/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git verify tag
,
vboxmanage
.
phing
A PHP build tool based on Apache Ant.
More information:
https://www.phing.info
.
Perform the default task in the
build.xml
file:
phing
Initialize a new build file:
phing -i {{path/to/build.xml}}
Perform a specific task:
phing {{task_name}}
Specify a custom build file path:
phing -f {{path/to/build.xml}} {{task_name}}
Specify a log file to output to:
phing -b {{path/to/log_file}} {{task_name}}
Specify custom properties to use in the build:
phing -D{{property}}={{value}} {{task_name}}
Specify a custom listener class:
phing -listener {{class_name}} {{task_name}}
Build using verbose output:
phing -verbose {{task_name}}
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
