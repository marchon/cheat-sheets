# pup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ifconfig
,
streamlink
,
wuzz
,
act
.
pup
Command-line HTML parsing tool.
More information:
https://github.com/ericchiang/pup
.
Transform a raw HTML file into a cleaned, indented, and colored format:
cat {{index.html}} | pup --color
Filter HTML by element tag name:
cat {{index.html}} | pup '{{tag}}'
Filter HTML by id:
cat {{index.html}} | pup '{{div#id}}'
Filter HTML by attribute value:
cat {{index.html}} | pup '{{input[type="text"]}}'
Print all text from the filtered HTML elements and their children:
cat {{index.html}} | pup '{{div}} text{}'
Print HTML as JSON:
cat {{index.html}} | pup '{{div}} json{}'
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
