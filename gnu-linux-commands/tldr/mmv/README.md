# mmv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mmv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hunspell
,
lighthouse
,
latex
,
scp
.
mmv
Move and rename files in bulk.
More information:
https://manned.org/mmv.1
.
Rename all files with a certain extension to a different extension:
mmv "*{{.old_extension}}" "#1{{.new_extension}}"
Copy
report6part4.txt
to
./french/rapport6partie4.txt
along with all similarly named files:
mmv -c "{{report*part*.txt}}" "{{./french/rapport#1partie#2.txt}}"
Append all
.txt
files into one file:
mmv -a "{{*.txt}}" "{{all.txt}}"
Convert dates in filenames from "M-D-Y" format to "D-M-Y" format:
mmv "{{[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt}}" "{{#3#4-#1#2-#5#6#7#8.txt}}"
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
