# webstorm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/webstorm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
curl
,
git browse
,
lt
,
git reset file
.
webstorm
The JetBrains JavaScript IDE.
More information:
https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html
.
Open the current directory in WebStorm:
webstorm
Open a specific directory in WebStorm:
webstorm {{path/to/directory}}
Open specific files in the LightEdit mode﻿:
webstorm -e {{path/to/file1 path/to/file2 ...}}
Open and wait until done editing a specific file in the LightEdit mode:
webstorm --wait -e {{path/to/file}}
Open a file with the cursor at the specific line:
webstorm --line {{line_number}} {{path/to/file}}
Open and compare files (supports up to 3 files):
webstorm diff {{path/to/file1}} {{path/to/file2}}
Open and perform a three-way merge:
webstorm merge {{path/to/left_file}} {{path/to/right_file}} {{path/to/target_file}}
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
