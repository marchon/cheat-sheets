# lp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clear
,
transcode
,
paste
,
vim
,
meson
.
lp
Print files.
More information:
https://manned.org/lp
.
Print the output of a command to the default printer (see
lpstat
command):
echo "test" | lp
Print a file to the default printer:
lp {{path/to/filename}}
Print a file to a named printer (see
lpstat
command):
lp -d {{printer_name}} {{path/to/filename}}
Print N copies of file to default printer (replace N with desired number of copies):
lp -n {{N}} {{path/to/filename}}
Print only certain pages to the default printer (print pages 1, 3-5, and 16):
lp -P 1,3-5,16 {{path/to/filename}}
Resume printing a job:
lp -i {{job_id}} -H resume
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
