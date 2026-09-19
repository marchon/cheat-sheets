# pageres

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pageres/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
spark
,
git show unmerged branches
.
pageres
Capture screenshots of websites in various resolutions.
More information:
https://github.com/sindresorhus/pageres-cli
.
Take multiple screenshots of multiple URLs at different resolutions:
pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}
Provide specific options for a URL, overriding global options:
pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop
Provide a custom filename template:
pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}
Capture a specific element on a page:
pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'
Hide a specific element:
pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'
Capture a screenshot of a local file:
pageres {{local_file_path.html}} {{1366x768}}
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
