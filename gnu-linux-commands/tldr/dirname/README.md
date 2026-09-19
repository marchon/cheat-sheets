# dirname

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dirname/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
type
,
xml edit
,
virsh pool list
.
dirname
Calculates the parent directory of a given file or directory path.
More information:
https://www.gnu.org/software/coreutils/dirname
.
Calculate the parent directory of a given path:
dirname {{path/to/file_or_directory}}
Calculate the parent directory of multiple paths:
dirname {{path/to/file_a}} {{path/to/directory_b}}
Delimit output with a NUL character instead of a newline (useful when combining with
xargs
):
dirname --zero {{path/to/directory_a}} {{path/to/file_b}}
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
