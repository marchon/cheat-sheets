# http-server-upload

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/http-server-upload/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh reference
,
darkhttpd
,
sha224sum
.
http-server-upload
Zero-configuration command-line HTTP server which provides a lightweight interface to upload files.
More information:
https://github.com/crycode-de/http-server-upload
.
Start an HTTP server on the default port to upload files to the current directory:
http-server-upload
Start an HTTP server with the specified maximum allowed file size for uploads in MiB (defaults to 200 MiB):
MAX_FILE_SIZE={{size_in_megabytes}} http-server-upload
Start an HTTP server on a specific port to upload files to the current directory:
PORT={{port}} http-server-upload
Start an HTTP server, storing the uploaded files in a specific directory:
UPLOAD_DIR={{path/to/directory}} http-server-upload
Start an HTTP server using a specific directory to temporarily store files during the upload process:
UPLOAD_TMP_DIR={{path/to/directory}} http-server-upload
Start an HTTP server accepting uploads with a specific token field in the HTTP post:
TOKEN={{secret}} http-server-upload
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
