# ts

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ts/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
youtube viewer
,
packtpub
,
gh config
.
ts
Add timestamps to every line from standard input.
More information:
https://joeyh.name/code/moreutils/
.
Add a timestamp to the beginning of each line:
{{some_command}} | ts
Add timestamps with microsecond precision:
{{some_command}} | ts "{{%b %d %H:%M:%.S}}"
Add [i]ncremental timestamps with microsecond precision, starting from zero:
{{some_command}} | ts -i "{{%H:%M:%.S}}"
Convert existing timestamps in a text file (eg. a log file) into [r]elative format:
cat {{path/to/file}} | ts -r
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
