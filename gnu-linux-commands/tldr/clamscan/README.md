# clamscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/clamscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clamscan
,
inkmake
,
openssl genrsa
.
clamscan
A command-line virus scanner.
More information:
https://www.clamav.net
.
Scan a file for vulnerabilities:
clamscan {{path/to/file}}
Scan all files recursively in a specific directory:
clamscan -r {{path/to/directory}}
Scan data from stdin:
{{command}} | clamscan -
Specify a virus database file or directory of files:
clamscan --database {{path/to/database_file_or_directory}}
Scan the current directory and output only infected files:
clamscan --infected
Output the scan report to a log file:
clamscan --log {{path/to/log_file}}
Move infected files to a specific directory:
clamscan --move {{path/to/quarantine_directory}}
Remove infected files:
clamscan --remove yes
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
