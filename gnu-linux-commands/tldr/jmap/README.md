# jmap

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jmap/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dd
,
git browse
,
crunch
,
mosquitto_pub
.
jmap
Java Memory Map Tool.
More information:
https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html
.
Print shared object mappings for a Java process (output like pmap):
jmap {{java_pid}}
Print heap summary information:
jmap -heap {{filename.jar}} {{java_pid}}
Print histogram of heap usage by type:
jmap -histo {{java_pid}}
Dump contents of the heap into a binary file for analysis with jhat:
jmap -dump:format=b,file={{filename}} {{java_pid}}
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
