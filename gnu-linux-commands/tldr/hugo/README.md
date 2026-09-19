# hugo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hugo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fzf
,
git sizer
,
kompose
,
phpstorm
.
hugo
Template-based static site generator. Uses modules, components, and themes.
More information:
https://gohugo.io
.
Create a new Hugo site:
hugo new site {{path/to/site}}
Create a new Hugo theme (themes may also be downloaded from https://themes.gohugo.io/):
hugo new theme {{theme_name}}
Create a new page:
hugo new {{section_name}}/{{filename}}
Build a site to the
./public/
directory:
hugo
Build a site including pages that are marked as a "draft":
hugo --buildDrafts
Build a site to a given directory:
hugo --destination {{path/to/destination}}
Build a site, start up a webserver to serve it, and automatically reload when pages are edited:
hugo server
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
