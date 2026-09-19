# pathchk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pathchk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg pull
,
patch
,
psysh
,
borg
,
git rev parse
.
pathchk
Check the validity and portability of one or more pathnames.
More information:
https://www.gnu.org/software/coreutils/pathchk
.
Check pathnames for validity in the current system:
pathchk {{path1 path2 …}}
Check pathnames for validity on a wider range of POSIX compliant systems:
pathchk -p {{path1 path2 …}}
Check pathnames for validity on all POSIX compliant systems:
pathchk --portability {{path1 path2 …}}
Only check for empty pathnames or leading dashes (-):
pathchk -P {{path1 path2 …}}
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
