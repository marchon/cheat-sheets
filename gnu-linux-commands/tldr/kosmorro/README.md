# kosmorro

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kosmorro/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
montage
,
todo
,
feh
,
gh browse
,
vimtutor
.
kosmorro
Compute the ephemerides and the events for a given date, at a given position on Earth.
More information:
http://kosmorro.space
.
Get ephemerides for Paris, France:
kosmorro --latitude={{48.7996}} --longitude={{2.3511}}
Get ephemerides for Paris, France, in the UTC+2 timezone:
kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}
Get ephemerides for Paris, France, on June 9th, 2020:
kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}
Generate a PDF (note: TeXLive must be installed):
kosmorro --format={{pdf}} --output={{path/to/file.pdf}}
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
