# firefox

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/firefox/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pax
,
dotnet publish
,
loadtest
.
firefox
A free and open source web browser.
More information:
https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
.
Launch Firefox and open a web page:
firefox {{https://www.duckduckgo.com}}
Open a new window:
firefox --new-window {{https://www.duckduckgo.com}}
Open a private (incognito) window:
firefox --private-window
Search for "wikipedia" using the default search engine:
firefox --search "{{wikipedia}}"
Launch Firefox in safe mode, with all extensions disabled:
firefox --safe-mode
Take a screenshot of a web page in headless mode:
firefox --headless --screenshot {{path/to/output_file.png}} {{https://example.com/}}
Use a specific profile to allow multiple separate instances of Firefox to run at once:
firefox --profile {{path/to/directory}} {{https://example.com/}}
Set Firefox as the default browser:
firefox --setDefaultBrowser
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
