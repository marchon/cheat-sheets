# cloc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cloc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
diff pdf
,
serve
,
dirsearch
,
typeset
.
cloc
Count, and compute differences of, lines of source code and comments.
More information:
https://github.com/AlDanial/cloc
.
Count all the lines of code in a directory:
cloc {{path/to/directory}}
Count all the lines of code in a directory, displaying a progress bar during the counting process:
cloc --progress=1 {{path/to/directory}}
Compare 2 directory structures and count the differences between them:
cloc --diff {{path/to/directory/one}} {{path/to/directory/two}}
Ignore files that are ignored by VCS, such as files specified in
.gitignore
:
cloc --vcs git {{path/to/directory}}
Count all the lines of code in a directory, displaying the results for each file instead of each language:
cloc --by-file {{path/to/directory}}
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
