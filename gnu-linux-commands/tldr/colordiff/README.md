# colordiff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/colordiff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio update
,
takeout
,
fls
,
supervisorctl
.
colordiff
A tool to colorize diff output.
The Perl script colordiff is a wrapper for
diff
and produces the same output but with pretty syntax highlighting. Color schemes can be customized.
More information:
https://github.com/kimmel/colordiff
.
Compare files:
colordiff {{file1}} {{file2}}
Output in two columns:
colordiff -y {{file1}} {{file2}}
Ignore case differences in file contents:
colordiff -i {{file1}} {{file2}}
Report when two files are the same:
colordiff -s {{file1}} {{file2}}
Ignore white spaces:
colordiff -w {{file1}} {{file2}}
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
