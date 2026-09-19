# parallel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/parallel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
scalafmt
,
git submodule
,
pio lib
.
parallel
Run commands on multiple CPU cores.
More information:
https://www.gnu.org/software/parallel
.
Gzip several files at once, using all cores:
parallel gzip ::: {{file1}} {{file2}} {{file3}}
Read arguments from stdin, run 4 jobs at once:
ls *.txt | parallel -j4 gzip
Convert JPG images to PNG using replacement strings:
parallel convert {} {.}.png ::: *.jpg
Parallel xargs, cram as many args as possible onto one command:
{{args}} | parallel -X {{command}}
Break stdin into ~1M blocks, feed each block to stdin of new command:
cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}
Run on multiple machines via SSH:
parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}
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
