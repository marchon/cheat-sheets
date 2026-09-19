# strip-nondeterminism

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/strip-nondeterminism/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jmap
,
picard
,
ghc
,
php
,
git abort
.
strip-nondeterminism
A tool to remove non-deterministic information (e.g. timestamps) from files.
More information:
https://salsa.debian.org/reproducible-builds/strip-nondeterminism
.
Strip nondeterministic information from a file:
strip-nondeterminism {{path/to/file}}
Strip nondeterministic information from a file manually specifying the filetype:
strip-nondeterminism --type {{filetype}} {{path/to/file}}
Strip nondeterministic information from a file; instead of removing timestamps set them to the specified UNIX timestamp:
strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}
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
