# man

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/man/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mosquitto_sub
,
pinta
,
hg status
.
man
Format and display manual pages.
More information:
https://www.man7.org/linux/man-pages/man1/man.1.html
.
Display the man page for a command:
man {{command}}
Display the man page for a command from section 7:
man {{7}} {{command}}
List all available sections for a command:
man -f {{command}}
Display the path searched for manpages:
man --path
Display the location of a manpage rather than the manpage itself:
man -w {{command}}
Display the man page using a specific locale:
man {{command}} --locale={{locale}}
Search for manpages containing a search string:
man -k "{{search_string}}"
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
