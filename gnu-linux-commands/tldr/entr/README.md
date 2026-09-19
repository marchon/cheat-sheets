# entr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/entr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh config
,
csvstat
,
dcfldd
,
hg status
.
entr
Run arbitrary commands when files change.
More information:
https://manned.org/entr
.
Rebuild with
make
if any file in any subdirectory changes:
{{ag -l}} | entr {{make}}
Rebuild and test with
make
if any
.c
source files in the current directory change:
{{ls *.c}} | entr {{'make && make test'}}
Send a
SIGTERM
to any previously spawned ruby subprocesses before executing
ruby main.rb
:
{{ls *.rb}} | entr -r {{ruby main.rb}}
Run a command with the changed file (
/_
) as an argument:
{{ls *.sql}} | entr {{psql -f}} /_
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
