# reflac

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/reflac/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hostid
,
tlmgr paper
,
lp
,
mongoimport
.
reflac
Recompress FLAC files in-place while preserving metadata.
More information:
https://github.com/chungy/reflac
.
Recompress a directory of FLAC files:
reflac {{path/to/directory}}
Enable maximum compression (very slow):
reflac --best {{path/to/directory}}
Display filenames as they are processed:
reflac --verbose {{path/to/directory}}
Recurse into subdirectories:
reflac --recursive {{path/to/directory}}
Preserve file modification times:
reflac --preserve {{path/to/directory}}
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
