# fdroid

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fdroid/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git mergetool
,
http
,
ned
,
sha224sum
.
fdroid
F-Droid build tool.
F-Droid is an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform.
More information:
https://f-droid.org/
.
Build a specific app:
fdroid build {{app_id}}
Build a specific app in a build server VM:
fdroid build {{app_id}} --server
Publish the app to the local repository:
fdroid publish {{app_id}}
Install the app on every connected device:
fdroid install {{app_id}}
Check if the metadata is formatted correctly:
fdroid lint --format {{app_id}}
Fix the formatting automatically (if possible):
fdroid rewritemeta {{app_id}}
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
