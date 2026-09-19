# envsubst

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/envsubst/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git clear soft
,
pt
,
zdb
,
pactl
.
envsubst
Substitutes environment variables with their value in shell format strings.
Variables to be replaced should be in either
${var}
or
$var
format.
More information:
https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html
.
Replace environment variables in stdin and output to stdout:
echo '{{$HOME}}' | envsubst
Replace environment variables in an input file and output to stdout:
envsubst < {{path/to/input_file}}
Replace environment variables in an input file and output to a file:
envsubst < {{path/to/input_file}} > {{path/to/output_file}}
Replace environment variables in an input file from a space-separated list:
envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}
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
