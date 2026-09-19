# gnomon

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gnomon/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh pr merge
,
git ignore
,
rtv
.
gnomon
Utility to annotate console logging statements with timestamps and find slow processes.
More information:
https://github.com/paypal/gnomon
.
Use UNIX (or DOS) pipes to pipe the stdout of any command through gnomon:
{{npm test}} | gnomon
Show number of seconds since the start of the process:
{{npm test}} | gnomon --type=elapsed-total
Show an absolute timestamp in UTC:
{{npm test}} | gnomon --type=absolute
Set a high threshold of 0.5 seconds for the elapsed time; exceeding which the timestamp will be colored bright red:
{{npm test}} | gnomon --high {{0.5}}
Set a medium threshold of 0.2 seconds (Timestamp will be colored bright yellow):
{{npm test}} | gnomon --medium {{0.2}}
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
