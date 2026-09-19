# typeset

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/typeset/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
uptime
,
patchwork
,
nasm
,
docker commit
.
typeset
Declare variables and give them attributes.
More information:
https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins
.
Declare a string variable with the specified value:
typeset {{variable}}="{{value}}"
Declare an integer variable with the specified value:
typeset -i {{variable}}="{{value}}"
Declare an array variable with the specified value:
typeset {{variable}}=({{item_a item_b item_c}})
Declare an associative array variable with the specified value:
typeset -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})
Declare a readonly variable with the specified value:
typeset -r {{variable}}="{{value}}"
Declare a global variable within a function with the specified value:
typeset -g {{variable}}="{{value}}"
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
