# py-spy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/py-spy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cordova
,
gixy
,
pio boards
,
netlify
.
py-spy
A sampling profiler for Python programs.
More information:
https://github.com/benfred/py-spy
.
Show a live view of the functions that take the most execution time of a running process:
py-spy top --pid {{pid}}
Start a program and show a live view of the functions that take the most execution time:
py-spy top -- python {{path/to/file.py}}
Produce an SVG flame graph of the function call execution time:
py-spy record -o {{path/to/profile.svg}} --pid {{pid}}
Dump the call stack of a running process:
py-spy dump --pid {{pid}}
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
