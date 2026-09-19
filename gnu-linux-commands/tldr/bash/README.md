# bash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
odps func
,
scp
,
fish
,
more
,
aws help
.
bash
Bourne-Again SHell, an
sh
-compatible command-line interpreter.
See also
histexpand
for history expansion.
More information:
https://gnu.org/software/bash/
.
Start an interactive shell session:
bash
Execute a command and then exit:
bash -c "{{command}}"
Execute a script:
bash {{path/to/script.sh}}
Execute a script, printing each command before executing it:
bash -x {{path/to/script.sh}}
Execute commands from a script, stopping at the first error:
bash -e {{path/to/script.sh}}
Read and execute commands from stdin:
bash -s
Print the Bash version (
$BASH_VERSION
contains the version without license information):
bash --version
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
