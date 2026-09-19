# date

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/date/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
heroku
,
fio
,
entr
,
cp
,
gpg2
,
shred
.
date
Set or display the system date.
More information:
https://www.gnu.org/software/coreutils/date
.
Display the current date using the default locale's format:
date +"%c"
Display the current date in UTC and ISO 8601 format:
date -u +"%Y-%m-%dT%H:%M:%SZ"
Display the current date as a Unix timestamp (seconds since the Unix epoch):
date +%s
Display a specific date (represented as a Unix timestamp) using the default format:
date -d @1473305798
Convert a specific date to the Unix timestamp format:
date -d "{{2018-09-01 00:00}}" +%s --utc
Display the current date using the RFC-3339 format (
YYYY-MM-DD hh:mm:ss TZ
):
date --rfc-3339=s
Set the current date using the format
MMDDhhmmYYYY.ss
(
YYYY
and
.ss
are optional):
date {{093023592021.59}}
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
