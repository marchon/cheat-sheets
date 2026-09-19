# jhsdb

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jhsdb/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xkcdpass
,
nm classic
,
git reset file
.
jhsdb
Attach to a Java process or launch a postmortem debugger to analyze the core dump from a crashed Java Virtual Machine.
More information:
https://manned.org/jhsdb
.
Print stack and locks information of a Java process:
jhsdb jstack --pid {{pid}}
Open a core dump in interactive debug mode:
jhsdb clhsdb --core {{path/to/core_dump}} --exe {{path/to/jdk/bin/java}}
Start a remote debug server:
jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}
Connect to a process in interactive debug mode:
jhsdb clhsdb --pid {{pid}}
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
