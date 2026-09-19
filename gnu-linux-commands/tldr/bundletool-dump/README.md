# bundletool-dump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bundletool-dump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
quilt
,
calibredb
,
tye
,
git apply
.
bundletool dump
Command-line tool to manipulate Android Application Bundles.
More information:
https://developer.android.com/studio/command-line/bundletool
.
Display the
AndroidManifest.xml
of the base module:
bundletool dump manifest --bundle={{path/to/bundle.aab}}
Display a specific value from the
AndroidManifest.xml
using XPath:
bundletool dump manifest --bundle={{path/to/bundle.aab}} --xpath={{/manifest/@android:versionCode}}
Display the
AndroidManifest.xml
of a specific module:
bundletool dump manifest --bundle={{path/to/bundle.aab}} --module={{name}}
Display all the resources in the application bundle:
bundletool dump resources --bundle={{path/to/bundle.aab}}
Display the configuration for a specific resource:
bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{type/name}}
Display the configuration and values for a specific resource using the ID:
bundletool dump resources --bundle={{path/to/bundle.aab}} --resource={{0x7f0e013a}} --values
Display the contents of the bundle configuration file:
bundletool dump config --bundle={{path/to/bundle.aab}}
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
