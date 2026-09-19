# copyq

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/copyq/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dotnet build
,
asdf
,
wapm
,
redis cli
.
copyq
Clipboard manager with advanced features.
More information:
https://hluk.github.io/CopyQ/
.
Launch CopyQ to store clipboard history:
copyq
Show current clipboard content:
copyq clipboard
Insert raw text into the clipboard history:
copyq add -- {{text1}} {{text2}} {{text3}}
Insert text containing escape sequences ('\n', '\t') into the clipboard history:
copyq add {{firstline\nsecondline}}
Print the content of the first 3 items in the clipboard history:
copyq read 0 1 2
Copy a file's contents into the clipboard:
copyq copy < {{file.txt}}
Copy a JPEG image into the clipboard:
copyq copy image/jpeg < {{image.jpg}}
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
