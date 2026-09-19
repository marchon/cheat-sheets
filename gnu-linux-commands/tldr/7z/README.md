# 7z

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/7z/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lua
,
openssl req
,
ipcs
,
cbonsai
.
7z
File archiver with a high compression ratio.
More information:
https://www.7-zip.org
.
[a]rchive a file or directory:
7z a {{path/to/archive.7z}} {{path/to/file_or_directory}}
Encrypt an existing archive (including filenames):
7z a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}
E[x]tract an archive preserving the original directory structure:
7z x {{path/to/archive.7z}}
E[x]tract an archive to a specific directory:
7z x {{path/to/archive.7z}} -o{{path/to/output}}
E[x]tract an archive to stdout:
7z x {{path/to/archive.7z}} -so
[a]rchive using a specific archive type:
7z a -t{{7z|bzip2|gzip|lzip|tar|zip}} {{path/to/archive.7z}} {{path/to/file_or_directory}}
[l]ist the contents of an archive:
7z l {{path/to/archive.7z}}
List available archive types:
7z i
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
