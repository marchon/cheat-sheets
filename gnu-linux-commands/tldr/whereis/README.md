# whereis

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/whereis/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wrangler
,
fakedata
,
grumphp
,
gixy
.
whereis
Locate the binary, source, and manual page files for a command.
More information:
https://manned.org/whereis
.
Locate binary, source and man pages for ssh:
whereis {{ssh}}
Locate binary and man pages for ls:
whereis -bm {{ls}}
Locate source of gcc and man pages for Git:
whereis -s {{gcc}} -m {{git}}
Locate binaries for gcc in
/usr/bin/
only:
whereis -b -B {{/usr/bin/}} -f {{gcc}}
Locate unusual binaries (those that have more or less than one binary on the system):
whereis -u *
Locate binaries that have unusual manual entries (binaries that have more or less than one manual installed):
whereis -u -m *
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
