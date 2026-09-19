# shopt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/shopt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pest
,
scp
,
sdiff
,
cf
,
tmpmail
,
dvc destroy
.
shopt
Manage Bash shell options: variables (stored in
$BASHOPTS
) that control behavior specific to the Bash shell.
Generic POSIX shell variables (stored in
$SHELLOPTS
) are managed with the
set
command instead.
More information:
https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html
.
List of all settable options and whether they are set:
shopt
Set an option:
shopt -s {{option_name}}
Unset an option:
shopt -u {{option_name}}
Print a list of all options and their status formatted as runnable
shopt
commands:
shopt -p
Show help for the command:
help shopt
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
