# reflex

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/reflex/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
texdoc
,
in toto sign
,
pylint
.
reflex
Tool to watch a directory and rerun a command when certain files change.
More information:
https://github.com/cespare/reflex
.
Rebuild with
make
if any file changes:
reflex make
Compile and run Go application if any
.go
file changes:
reflex --regex='{{\.go$}}' {{go run .}}
Ignore a directory when watching for changes:
reflex --inverse-regex='{{^dir/}}' {{command}}
Run command when reflex starts and restarts on file changes:
reflex --start-service=true {{command}}
Substitute the filename that changed in:
reflex -- echo {}
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
