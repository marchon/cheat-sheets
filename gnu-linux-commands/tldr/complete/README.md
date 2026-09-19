# complete

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/complete/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fselect
,
ps
,
rector
,
composer require checker
.
complete
Provides argument autocompletion to shell commands.
More information:
https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html
.
Apply a function that performs autocompletion to a command:
complete -F {{function}} {{command}}
Apply a command that performs autocompletion to another command:
complete -C {{autocomplete_command}} {{command}}
Apply autocompletion without appending a space to the completed word:
complete -o nospace -F {{function}} {{command}}
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
