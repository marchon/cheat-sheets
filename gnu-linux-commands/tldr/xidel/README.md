# xidel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xidel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fold
,
sha256sum
,
git delta
,
blender
.
xidel
Download and extract data from HTML/XML pages as well as JSON APIs.
More information:
https://www.videlibri.de/xidel.html
.
Print all URLs found by a Google search:
xidel {{https://www.google.com/search?q=test}} --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"
Print the title of all pages found by a Google search and download them:
xidel {{https://www.google.com/search?q=test}} --follow "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" --extract {{//title}} --download {{'{$host}/'}}
Follow all links on a page and print the titles, with XPath:
xidel {{https://example.org}} --follow {{//a}} --extract {{//title}}
Follow all links on a page and print the titles, with CSS selectors:
xidel {{https://example.org}} --follow "{{css('a')}}" --css {{title}}
Follow all links on a page and print the titles, with pattern matching:
xidel {{https://example.org}} --follow "{{
{.}
*}}" --extract "{{
{.}
}}"
Read the pattern from example.xml (which will also check if the element containing "ood" is there, and fail otherwise):
xidel {{path/to/example.xml}} --extract "{{
ood
{.}
}}"
Print all newest Stack Overflow questions with title and URL using pattern matching on their RSS feed:
xidel {{http://stackoverflow.com/feeds}} --extract "{{
{title:=.}
{uri:=@href}
+}}"
Check for unread Reddit mail, Webscraping, combining CSS, XPath, JSONiq, and automatically form evaluation:
xidel {{https://reddit.com}} --follow "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" --extract "{{css('#mail')/@title}}"
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
