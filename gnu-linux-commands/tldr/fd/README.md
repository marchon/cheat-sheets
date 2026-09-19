# fd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git missing
,
git push
,
tldrl
.
fd
An alternative to
find
.
Aims to be faster and easier to use than
find
.
More information:
https://github.com/sharkdp/fd
.
Recursively find files matching the given pattern in the current directory:
fd {{pattern}}
Find files that begin with "foo":
fd {{'^foo'}}
Find files with a specific extension:
fd --extension {{txt}}
Find files in a specific directory:
fd {{pattern}} {{path/to/directory}}
Include ignored and hidden files in the search:
fd --hidden --no-ignore {{pattern}}
Execute a command on each search result returned:
fd {{pattern}} --exec {{command}}
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
