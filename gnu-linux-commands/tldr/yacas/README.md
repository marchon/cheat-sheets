# yacas

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/yacas/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
timeout
,
asciidoctor
,
mat2
,
enscript
.
yacas
Yet Another Computer Algebra System.
More information:
http://www.yacas.org
.
Start an interactive
yacas
session:
yacas
While in a
yacas
session, execute a statement:
{{Integrate(x)Cos(x)}};
While in a
yacas
session, display an example:
{{Example()}};
Quit from a
yacas
session:
{{quit}}
Execute one or more
yacas
scripts (without terminal or prompts), then exit:
yacas -p -c {{path/to/script1}} {{path/to/script2}}
Execute and print the result of one statement, then exit:
echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -p -c /dev/stdin
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
