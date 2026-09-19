# truncate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/truncate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bastet
,
pdfjoin
,
vue
,
b2sum
,
git revert
.
truncate
Shrink or extend the size of a file to the specified size.
More information:
https://www.gnu.org/software/coreutils/truncate
.
Set a size of 10 GB to an existing file, or create a new file with the specified size:
truncate --size {{10G}} {{filename}}
Extend the file size by 50 MiB, fill with holes (which reads as zero bytes):
truncate --size +{{50M}} {{filename}}
Shrink the file by 2 GiB, by removing data from the end of file:
truncate --size -{{2G}} {{filename}}
Empty the file's content:
truncate --size 0 {{filename}}
Empty the file's content, but do not create the file if it does not exist:
truncate --no-create --size 0 {{filename}}
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
