# mk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
troff
,
pdflatex
,
mysqld
,
go tool
.
mk
Task runner for targets described in Mkfile.
Mostly used to control the compilation of an executable from source code.
More information:
http://doc.cat-v.org/plan_9/4th_edition/papers/mk
.
Call the first target specified in the Mkfile (usually named "all"):
mk
Call a specific target:
mk {{target}}
Call a specific target, executing 4 jobs at a time in parallel:
NPROC=4 mk {{target}}
Force mking of a target, even if source files are unchanged:
mk -w{{target}} {{target}}
Assume all targets to be out of date. Thus, update
target
and all of its dependencies:
mk -a {{target}}
Keep going as far as possible on error:
mk -k
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
