# dirs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dirs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fd
,
pass otp
,
mutagen
,
symfony
.
dirs
Displays or manipulates the directory stack.
The directory stack is a list of recently visited directories that can be manipulated with the
pushd
and
popd
commands.
More information:
https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins
.
Display the directory stack with a space between each entry:
dirs
Display the directory stack with one entry per line:
dirs -p
Display only the nth entry in the directory stack, starting at 0:
dirs +{{N}}
Clear the directory stack:
dirs -c
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
