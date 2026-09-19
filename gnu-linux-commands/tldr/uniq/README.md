# uniq

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/uniq/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pygmentize
,
tlmgr update
,
behat
.
uniq
Output the unique lines from the given input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
More information:
https://www.gnu.org/software/coreutils/uniq
.
Display each line once:
sort {{file}} | uniq
Display only unique lines:
sort {{file}} | uniq -u
Display only duplicate lines:
sort {{file}} | uniq -d
Display number of occurrences of each line along with that line:
sort {{file}} | uniq -c
Display number of occurrences of each line, sorted by the most frequent:
sort {{file}} | uniq -c | sort -nr
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
