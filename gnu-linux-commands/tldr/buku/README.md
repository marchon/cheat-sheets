# buku

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/buku/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gox
,
nix env
,
ssh keygen
,
notmuch
.
buku
Command-line browser-independent bookmark manager.
More information:
https://github.com/jarun/Buku
.
Display all bookmarks matching "keyword" and with "privacy" tag:
buku {{keyword}} --stag {{privacy}}
Add bookmark with tags "search engine" and "privacy":
buku --add {{https://example.com}} {{search engine}}, {{privacy}}
Delete a bookmark:
buku --delete {{bookmark_id}}
Open editor to edit a bookmark:
buku --write {{bookmark_id}}
Remove "search engine" tag from a bookmark:
buku --update {{bookmark_id}} --tag {{-}} {{search engine}}
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
