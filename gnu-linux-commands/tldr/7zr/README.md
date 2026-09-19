# 7zr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/7zr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sops
,
file
,
phpbu
,
watch
,
virsh pool destroy
.
7zr
File archiver with a high compression ratio.
Similar to
7z
except that it only supports
.7z
files.
More information:
https://www.7-zip.org
.
[a]rchive a file or directory:
7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}
Encrypt an existing archive (including file names):
7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}
E[x]tract an archive preserving the original directory structure:
7zr x {{path/to/archive.7z}}
E[x]tract an archive to a specific directory:
7zr x {{path/to/archive.7z}} -o{{path/to/output}}
E[x]tract an archive to stdout:
7zr x {{path/to/archive.7z}} -so
[l]ist the contents of an archive:
7zr l {{path/to/archive.7z}}
List available archive types:
7zr i
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
