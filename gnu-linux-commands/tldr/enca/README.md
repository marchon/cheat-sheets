# enca

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/enca/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phing
,
uncrustify
,
amass enum
.
enca
Detect and convert the encoding of text files.
More information:
https://github.com/nijel/enca
.
Detect file(s) encoding according to the system's locale:
enca {{file1 file2 ...}}
Detect file(s) encoding specifying a language in the POSIX/C locale format (e.g. zh_CN, en_US):
enca -L {{language}} {{file1 file2 ...}}
Convert file(s) to a specific encoding:
enca -L {{language}} -x {{to_encoding}} {{file1 file2 ...}}
Create a copy of an existing file using a different encoding:
enca -L {{language}} -x {{to_encoding}} < {{original_file}} > {{new_file}}
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
