# calibredb

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/calibredb/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ping6
,
tlmgr remove
,
clojure
.
calibredb
Tool to manipulate the your e-book database.
Part of the Calibre e-book library.
More information:
https://manual.calibre-ebook.com/generated/en/calibredb.html
.
List e-books in the library with additional information:
calibredb list
Search for e-books displaying additional information:
calibredb list --search {{search_term}}
Search for just ids of e-books:
calibredb search {{search_term}}
Add one or more e-books to the library:
calibredb add {{file1 file2 …}}
Recursively add all e-books under a directory to the library:
calibredb add -r {{path/to/directory}}
Remove one or more e-books from the library. You need the e-book IDs (see above):
calibredb remove {{id1 id2 …}}
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
