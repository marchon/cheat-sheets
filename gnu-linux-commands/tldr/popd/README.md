# popd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/popd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
testssl
,
symfony
,
xephyr
,
git maintenance
.
popd
Remove a directory placed on the directory stack via the pushd shell built-in.
See also
pushd
to place a directory on the stack and
dirs
to display directory stack contents.
More information:
https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html
.
Remove the top directory from the stack and cd to it:
popd
Remove the Nth directory (starting from zero to the left from the list printed with
dirs
):
popd +N
Remove the Nth directory (starting from zero to the right from the list printed with
dirs
):
popd -N
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
