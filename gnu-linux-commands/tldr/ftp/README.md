# ftp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ftp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
transmission create
,
neomutt
.
ftp
Tools to interact with a server via File Transfer Protocol.
More information:
https://manned.org/ftp
.
Connect to an FTP server:
ftp {{ftp.example.com}}
Connect to an FTP server specifying its IP address and port:
ftp {{ip_address}} {{port}}
Switch to binary transfer mode (graphics, compressed files, etc):
binary
Transfer multiple files without prompting for confirmation on every file:
prompt off
Download multiple files (glob expression):
mget {{*.png}}
Upload multiple files (glob expression):
mput {{*.zip}}
Delete multiple files on the remote server:
mdelete {{*.txt}}
Rename a file on the remote server:
rename {{original_filename}} {{new_filename}}
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
