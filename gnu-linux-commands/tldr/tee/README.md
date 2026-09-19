# tee

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tee/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gvpack
,
qmv
,
id3tag
,
glab repo
.
tee
Read from standard input and write to standard output and files (or commands).
More information:
https://www.gnu.org/software/coreutils/tee
.
Copy standard input to each file, and also to standard output:
echo "example" | tee {{path/to/file}}
Append to the given files, do not overwrite:
echo "example" | tee -a {{path/to/file}}
Print standard input to the terminal, and also pipe it into another program for further processing:
echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}
Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:
echo "example" | tee >(xargs mkdir) >(wc -c)
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
