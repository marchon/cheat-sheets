# fish

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fish/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arduino
,
numfmt
,
sqsc
,
printf
,
ssh agent
.
fish
The Friendly Interactive SHell, a command-line interpreter designed to be user friendly.
More information:
https://fishshell.com
.
Start an interactive shell session:
fish
Start an interactive shell session without loading startup configs:
fish --no-config
Execute specific commands:
fish --command "{{echo 'fish is executed'}}"
Execute a specific script:
fish {{path/to/script.fish}}
Check a specific script for syntax errors:
fish --no-execute {{path/to/script.fish}}
Execute specific commands from stdin:
{{echo "echo 'fish is executed'"}} | fish
Start an interactive shell session in private mode, where the shell does not access old history or save new history:
fish --private
Define and export an environmental variable that persists across shell restarts (builtin):
set --universal --export {{variable_name}} {{variable_value}}
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
