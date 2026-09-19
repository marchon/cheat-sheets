# pdfjoin

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdfjoin/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tac
,
cksum
,
sonar scanner
,
fgrep
.
pdfjoin
PDF merging utility based on pdfjam.
More information:
https://github.com/rrthomas/pdfjam-extras
.
Merge two PDFs into one with the default suffix "joined":
pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}
Merge the first page of each given file together:
pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}
Save pages 3 to 5 followed by page 1 to a new PDF with custom suffix:
pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}
Merge page subranges from two PDFs:
pdfjoin {/path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}
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
