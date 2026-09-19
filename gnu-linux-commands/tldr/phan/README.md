# phan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
magick
,
tcpdump
,
cupsd
,
hello
,
pathchk
.
phan
A static analysis tool for PHP.
More information:
https://github.com/phan/phan
.
Generate a
.phan/config.php
in the current directory:
phan --init
Generate a Phan configuration file using a specific level (1 being strictest to 5 being the least strict):
phan --init --init-level {{level}}
Analyze the current directory:
phan
Analyze one or more directories:
phan --directory {{path/to/directory}} --directory {{path/to/another_directory}}
Specify a config file (defaults to
.phan/config.php
):
phan --config-file {{path/to/config.php}}
Specify the output mode:
phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}
Specify the number of parallel processes:
phan --processes {{number_of_processes}}
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
