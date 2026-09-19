# optipng

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/optipng/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh browse
,
composer require checker
.
optipng
PNG file optimization utility.
More information:
http://optipng.sourceforge.net
.
Compress a PNG with default settings:
optipng {{path/to/file.png}}
Compress a PNG with the best compression:
optipng -o{{7}} {{path/to/file.png}}
Compress a PNG with the fastest compression:
optipng -o{{0}} {{path/to/file.png}}
Compress a PNG and add interlacing:
optipng -i {{1}} {{path/to/file.png}}
Compress a PNG and preserve all metadata (including file timestamps):
optipng -preserve {{path/to/file.png}}
Compress a PNG and remove all metadata:
optipng -strip all {{path/to/file.png}}
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
