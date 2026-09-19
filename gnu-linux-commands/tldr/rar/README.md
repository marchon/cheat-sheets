# rar

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rar/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
openssl req
,
youtube viewer
.
rar
The RAR archiver. Supports multi-volume archives that can be optionally self-extracting.
More information:
https://manned.org/rar
.
Archive 1 or more files:
rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}
Archive a directory:
rar a {{path/to/archive_name.rar}} {{path/to/directory}}
Split the archive into parts of equal size (50M):
rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}
Password protect the resulting archive:
rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}
Encrypt file data and headers with password:
rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}
Use a specific compression level (0-5):
rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}
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
