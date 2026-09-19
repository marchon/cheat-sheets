# newsboat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/newsboat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sd
,
pio settings
,
uudecode
,
groups
.
newsboat
An RSS/Atom feed reader for text terminals.
More information:
https://newsboat.org/
.
First import feed URLs from an OPML file:
newsboat -i {{my-feeds.xml}}
Alternatively, add feeds manually:
echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"
Start newsboat and refresh all feeds on startup:
newsboat -r
Execute a space-separated list of commands in non-interactive mode:
newsboat -x {{reload print-unread ...}}
See keyboard shortcuts (the most relevant are visible in the status line):
?
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
