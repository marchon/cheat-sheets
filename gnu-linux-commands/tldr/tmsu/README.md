# tmsu

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tmsu/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az term
,
encfs
,
git show ref
.
tmsu
Simple command-line tool for tagging files.
More information:
https://tmsu.org
.
Tag a specific file with multiple tags:
tmsu tag {{path/to/file.mp3}} {{music}} {{big-jazz}} {{mp3}}
Tag multiple files:
tmsu tag --tags "{{music mp3}}" {{*.mp3}}
List tags of specified file(s):
tmsu tags {{*.mp3}}
List files with specified tag(s):
tmsu files {{big-jazz}} {{music}}
List files with tags matching boolean expression:
tmsu files "{{(year >= 1990 and year <= 2000)}} and {{grunge}}"
Mount tmsu virtual filesystem to an existing directory:
tmsu mount {{path/to/directory}}
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
