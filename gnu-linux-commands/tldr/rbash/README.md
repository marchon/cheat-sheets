# rbash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rbash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nice
,
nu
,
lwp request
,
runsvdir
.
rbash
Restricted Bash shell, equivalent to
bash --restricted
.
Does not permit changing the working directory, redirecting command output, or modifying environment variables, among other things.
See also
histexpand
for history expansion.
More information:
https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell
.
Start an interactive shell session:
rbash
Execute a command and then exit:
rbash -c "{{command}}"
Execute a script:
rbash {{path/to/script.sh}}
Execute a script, printing each command before executing it:
rbash -x {{path/to/script.sh}}
Execute commands from a script, stopping at the first error:
rbash -e {{path/to/script.sh}}
Read and execute commands from stdin:
rbash -s
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
