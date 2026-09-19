# xdelta

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xdelta/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
conda create
,
pio remote
,
pnpm
.
xdelta
Delta encoding utility.
Often used for applying patches to binary files.
More information:
http://xdelta.org
.
Apply a patch:
xdelta -d -s {{path/to/input_file}} {{path/to/delta_file.xdelta}} {{path/to/output_file}}
Create a patch:
xdelta -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/output_file.xdelta}}
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
