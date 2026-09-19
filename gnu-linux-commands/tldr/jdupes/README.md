# jdupes

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jdupes/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cloc
,
sops
,
inkview
,
wordgrinder
.
jdupes
A powerful duplicate file finder and an enhanced fork of fdupes.
More information:
https://github.com/jbruchon/jdupes
.
Search a single directory:
jdupes {{directory}}
Search multiple directories:
jdupes {{directory1}} {{directory2}}
Search all directories recursively:
jdupes --recurse {{directory}}
Search directory recursively and let user choose files to preserve:
jdupes --delete --recurse {{directory}}
Search multiple directories and follow subdirectores under directory2, not directory1:
jdupes {{directory1}} --recurse: {{directory2}}
Search multiple directories and keep the directory order in result:
jdupes -O {{directory1}} {{directory2}} {{directory3}}
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
