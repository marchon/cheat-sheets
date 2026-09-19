# gixy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gixy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
circo
,
tree
,
clamscan
,
lein
,
gcalcli
.
gixy
Analyze nginx configuration files.
More information:
https://github.com/yandex/gixy
.
Analyze nginx configuration (default path:
/etc/nginx/nginx.conf
):
gixy
Analyze nginx configuration but skip specific tests:
gixy --skips {{http_splitting}}
Analyze nginx configuration with the specific severity level:
gixy {{-l|-ll|-lll}}
Analyze nginx configuration files on the specific path:
gixy {{path/to/configuration_file_1}} {{path/to/configuration_file_2}}
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
