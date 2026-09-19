# lsd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lsd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gitlab runner
,
brotli
,
mongod
.
lsd
List directory contents.
The next generation
ls
command, written in Rust.
More information:
https://github.com/Peltoche/lsd
.
List files and directories, one per line:
lsd -1
List all files and directories, including hidden ones, in the current directory:
lsd -a
List all files and directories with trailing
/
added to directory names:
lsd -F
List all files and directories in long format (permissions, ownership, size, and modification date):
lsd -la
List all files and directories in long format with size displayed using human-readable units (KiB, MiB, GiB):
lsd -lh
List all files and directories in long format, sorted by size (descending):
lsd -lS
List all files and directories in long format, sorted by modification date (oldest first):
lsd -ltr
Only list directories:
lsd -d {{*/}}
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
