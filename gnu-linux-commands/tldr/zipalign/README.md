# zipalign

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zipalign/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pngcheck
,
dumpcap
,
nproc
,
lighthouse
.
zipalign
Zip archive alignment tool.
Part of the Android SDK build tools.
More information:
https://developer.android.com/studio/command-line/zipalign
.
Align the data of a ZIP file on 4-byte boundaries:
zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}
Check that a ZIP file is correctly aligned on 4-byte boundaries and display the results in a verbose manner:
zipalign -v -c {{4}} {{path/to/input.zip}}
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
