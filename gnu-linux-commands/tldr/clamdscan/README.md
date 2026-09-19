# clamdscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/clamdscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdftk
,
az account
,
fastmod
,
patchwork
.
clamdscan
A command-line virus scanner using the ClamAV Daemon.
More information:
https://www.clamav.net
.
Scan a file or directory for vulnerabilities:
clamdscan {{path/to/file_or_directory}}
Scan data from stdin:
{{command}} | clamdscan -
Scan the current directory and output only infected files:
clamdscan --infected
Output the scan report to a log file:
clamdscan --log {{path/to/log_file}}
Move infected files to a specific directory:
clamdscan --move {{path/to/quarantine_directory}}
Remove infected files:
clamdscan --remove
Use multiple threads to scan a directory:
clamdscan --multiscan
Pass the file descriptor instead of streaming the file to the daemon:
clamdscan --fdpass
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
