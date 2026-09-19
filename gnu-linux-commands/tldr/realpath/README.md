# realpath

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/realpath/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
badblocks
,
nop
,
sccmap
,
lp
,
josm
.
realpath
Display the resolved absolute path for a file or directory.
More information:
https://www.gnu.org/software/coreutils/realpath
.
Display the absolute path for a file or directory:
realpath {{path/to/file_or_directory}}
Require all path components to exist:
realpath --canonicalize-existing {{path/to/file_or_directory}}
Resolve ".." components before symlinks:
realpath --logical {{path/to/file_or_directory}}
Disable symlink expansion:
realpath --no-symlinks {{path/to/file_or_directory}}
Suppress error messages:
realpath --quiet {{path/to/file_or_directory}}
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
