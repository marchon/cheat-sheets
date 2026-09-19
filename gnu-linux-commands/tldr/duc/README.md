# duc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/duc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sv
,
git clean
,
miniserve
,
orca c
.
duc
Duc is a collection of tools for indexing, inspecting and visualizing disk usage. Duc maintains a database of accumulated sizes of directories of the file system, allowing queries this database, or create fancy graphs to show where data is.
More information:
https://duc.zevv.nl/
.
Index the /usr directory, writing to the default database location ~/.duc.db:
duc index {{/usr}}
List all files and directories under /usr/local, showing relative file sizes in a [g]raph:
duc ls -Fg {{/usr/local}}
List all files and directories under /usr/local using treeview recursively:
duc ls -Fg -R {{/usr/local}}
Start the graphical interface to explore the file system using sunburst graphs:
duc gui {{/usr}}
Run the ncurses console interface to explore the file system:
duc ui {{/usr}}
Dump database info:
duc info
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
