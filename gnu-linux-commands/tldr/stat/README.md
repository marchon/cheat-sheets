# stat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansible pull
,
nc
,
atoum
,
bssh
,
truncate
.
stat
Display file and filesystem information.
More information:
https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html
.
Show file properties such as size, permissions, creation and access dates among others:
stat {{file}}
Same as above but in a more concise way:
stat -t {{file}}
Show filesystem information:
stat -f {{file}}
Show only octal file permissions:
stat -c "%a %n" {{file}}
Show owner and group of the file:
stat -c "%U %G" {{file}}
Show the size of the file in bytes:
stat -c "%s %n" {{file}}
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
