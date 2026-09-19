# cut

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cut/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git describe
,
hangups
,
kubectl describe
.
cut
Cut out fields from stdin or files.
More information:
https://www.gnu.org/software/coreutils/cut
.
Print a specific character/field range of each line:
{{command}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}
Print a range of each line with a specific delimiter:
{{command}} | cut --delimiter="{{,}}" --{{characters}}={{1}}
Print a range of each line of the specific file:
cut --{{characters}}={{1}} {{path/to/file}}
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
