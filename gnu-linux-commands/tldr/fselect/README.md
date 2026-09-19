# fselect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fselect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rector
,
vdir
,
wrk
,
fc
,
elixir
,
webstorm
.
fselect
Find files with SQL-like queries.
More information:
https://github.com/jhspetersson/fselect
.
Select full path and size from temporary or config files in a given directory:
fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}
Find square images:
fselect path from {{path/to/directory}} where width = height
Find old-school rap 320kbps MP3 files:
fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}
Select only the first 5 results and output as JSON:
fselect size, path from {{path/to/directory}} limit {{5}} into json
Use SQL aggregate functions to calculate minimum, maximum and average size of files in a directory:
fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"
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
