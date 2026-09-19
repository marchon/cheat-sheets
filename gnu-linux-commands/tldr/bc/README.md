# bc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc list
,
phpstorm
,
unison
,
tailscale up
.
bc
An arbitrary precision calculator language.
See also:
dc
.
More information:
https://manned.org/man/bc.1
.
Start an interactive session:
bc
Start an interactive session with the standard math library enabled:
bc --mathlib
Calculate an expression:
echo '{{5 / 3}}' | bc
Execute a script:
bc {{path/to/script.bc}}
Calculate an expression with the specified scale:
echo 'scale = {{10}}; {{5 / 3}}' | bc
Calculate a sine/cosine/arctangent/natural logarithm/exponential function using
mathlib
:
echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib
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
