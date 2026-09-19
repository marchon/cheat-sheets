# case

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/case/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jrnl
,
takeout
,
rbt
,
influx
,
gacutil
.
case
Branch based on the value of an expression.
More information:
https://manned.org/case
.
Match a variable against string literals to decide which command to run:
case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac
Combine patterns with |, use * as a fallback pattern:
case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac
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
