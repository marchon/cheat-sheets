# expr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/expr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mh_lint
,
link
,
nohup
,
gvcolor
,
ngrep
.
expr
Evaluate expressions and manipulate strings.
More information:
https://www.gnu.org/software/coreutils/expr
.
Get string length:
expr length {{string}}
Evaluate logical or math expression with an operator ('+', '-', '*', '&', '|', etc.). Special symbols should be escaped:
expr {{first_argument}} {{operator}} {{second_argument}}
Get position of the first character in 'string' that matches 'substring':
echo $(expr index {{string}} {{substring}})
Extract part of the string:
echo $(expr substr {{string}} {{position_to_start}} {{number_of_characters}}
Extract part of the string which matches a regular expression:
echo $(expr {{string}} : '\({{regular_expression}}\)')
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
