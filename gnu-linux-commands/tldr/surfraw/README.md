# surfraw

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/surfraw/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
adb shell
,
ss local
,
openscad
.
surfraw
CLI to query a variety of web search engines.
Consists of a collection of elvi, each of which knows how to search a specific website.
More information:
http://surfraw.org
.
Display the list of supported website search scripts (elvi):
surfraw -elvi
Open the elvi's results page for a specific search in the browser:
surfraw {{elvi}} "{{search_terms}}"
Display an elvi description and its specific options:
surfraw {{elvi}} -local-help
Search using an elvi with specific options and open the results page in the browser:
surfraw {{elvi}} {{elvi_options}} "{{search_terms}}"
Display the URL to the elvi's results page for a specific search:
surfraw -print {{elvi}} "{{search_terms}}"
Search using the alias:
sr {{elvi}} "{{search_terms}}"
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
