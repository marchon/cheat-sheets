# printf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/printf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xetex
,
license
,
twm
,
bvnc
,
tlmgr shell
.
printf
Format and print text.
More information:
https://www.gnu.org/software/coreutils/printf
.
Print a text message:
printf "{{%s\n}}" "{{Hello world}}"
Print an integer in bold blue:
printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}
Print a float number with the Unicode Euro sign:
printf "{{\u20AC %.2f\n}}" {{123.4}}
Print a text message composed with environment variables:
printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"
Store a formatted message in a variable (does not work on zsh):
printf -v {{myvar}} {{"This is %s = %d\n" "a year" 2016}}
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
