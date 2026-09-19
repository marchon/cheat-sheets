# glib-compile-resources

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glib-compile-resources/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kahlan
,
deluge
,
noti
,
strip nondeterminism
.
glib-compile-resources
Compiles resource files (e.g. images) into a binary resource bundle.
These may be linked into GTK applications using the GResource API.
More information:
https://manned.org/glib-compile-resources
.
Compile resources referenced in
file.gresource.xml
to a .gresource binary:
glib-compile-resources {{file.gresource.xml}}
Compile resources referenced in
file.gresource.xml
to a C source file:
glib-compile-resources --generate-source {{file.gresource.xml}}
Compile resources in
file.gresource.xml
to a chosen target file, with
.c
,
.h
or
.gresource
extension:
glib-compile-resources --generate --target={{file.ext}} {{file.gresource.xml}}
Print a list of resource files referenced in
file.gresource.xml
:
glib-compile-resources --generate-dependencies {{file.gresource.xml}}
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
