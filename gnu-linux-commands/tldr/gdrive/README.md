# gdrive

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gdrive/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gtop
,
gops
,
git send email
,
cake
.
gdrive
Command-line tool to interact with Google Drive.
Folder/file ID can be obtained from the Google Drive folder or ID URL.
More information:
https://github.com/gdrive-org/gdrive
.
Upload a local path to the parent folder with the specified ID:
gdrive upload -p {{id}} {{path/to/file_or_folder}}
Download file or directory by ID to current directory:
gdrive download {{id}}
Download to a given local path by its ID:
gdrive download --path {{path/to/folder}} {{id}}
Create a new revision of an ID using a given file or folder:
gdrive update {{id}} {{path/to/file_or_folder}}
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
