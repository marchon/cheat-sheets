# install

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/install/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
shred
,
llc
,
xxd
,
mupdf
,
gixy
,
cmatrix
.
install
Copy files and set attributes.
Copy files (often executable) to a system location like
/usr/local/bin
, give them the appropriate permissions/ownership.
More information:
https://www.gnu.org/software/coreutils/install
.
Copy files to the destination:
install {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
Copy files to the destination, setting their ownership:
install --owner {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
Copy files to the destination, setting their group ownership:
install --group {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
Copy files to the destination, setting their
mode
:
install --mode {{+x}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
Copy files and apply access/modification times of source to the destination:
install --preserve-timestamps {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
Copy files and create the directories at the destination if they don't exist:
install -D {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}
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
