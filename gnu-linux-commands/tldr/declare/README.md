# declare

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/declare/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
warp cli
,
dwebp
,
tlmgr remove
.
declare
Declare variables and give them attributes.
More information:
https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins
.
Declare a string variable with the specified value:
declare {{variable}}="{{value}}"
Declare an integer variable with the specified value:
declare -i {{variable}}="{{value}}"
Declare an array variable with the specified value:
declare -a {{variable}}=({{item_a item_b item_c}})
Declare an associative array variable with the specified value:
declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})
Declare a readonly string variable with the specified value:
declare -r {{variable}}="{{value}}"
Declare a global variable within a function with the specified value:
declare -g {{variable}}="{{value}}"
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
