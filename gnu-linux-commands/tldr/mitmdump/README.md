# mitmdump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mitmdump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ptargrep
,
git archive
,
rev
,
jupytext
.
mitmdump
View, record, and programmatically transform HTTP traffic.
The command-line counterpart to mitmproxy.
More information:
https://docs.mitmproxy.org/stable/overview-tools/#mitmdump
.
Start a proxy and save all output to a file:
mitmdump -w {{filename}}
Filter a saved traffic file to just POST requests:
mitmdump -nr {{input_filename}} -w {{output_filename}} "{{~m post}}"
Replay a saved traffic file:
mitmdump -nc {{filename}}
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
