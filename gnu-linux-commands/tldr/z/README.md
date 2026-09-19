# z

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/z/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bcomps
,
spfquery
,
shred
,
sha224sum
.
z
Tracks the most used (by frecency) directories and enables quickly navigating to them using string patterns or regular expressions.
More information:
https://github.com/rupa/z
.
Go to a directory that contains "foo" in the name:
z {{foo}}
Go to a directory that contains "foo" and then "bar":
z {{foo}} {{bar}}
Go to the highest-ranked directory matching "foo":
z -r {{foo}}
Go to the most recently accessed directory matching "foo":
z -t {{foo}}
List all directories in
z
's database matching "foo":
z -l {{foo}}
Remove the current directory from
z
's database:
z -x .
Restrict matches to subdirectories of the current directory:
z -c {{foo}}
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
