# read

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/read/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
umount
,
last
,
github label sync
.
read
BASH builtin for retrieving data from standard input.
More information:
https://manned.org/read.1p
.
Store data that you type from the keyboard:
read {{variable}}
Store each of the next lines you enter as values of an array:
read -a {{array}}
Specify the number of maximum characters to be read:
read -n {{character_count}} {{variable}}
Use a specific character as a delimiter instead of a new line:
read -d {{new_delimiter}} {{variable}}
Do not let backslash (\) act as an escape character:
read -r {{variable}}
Display a prompt before the input:
read -p "{{Enter your input here: }}" {{variable}}
Do not echo typed characters (silent mode):
read -s {{variable}}
Read stdin and perform an action on every line:
while read line; do echo "$line"; done
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
