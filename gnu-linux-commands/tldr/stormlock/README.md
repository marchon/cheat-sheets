# stormlock

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stormlock/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio project
,
dune
,
stl2gts
,
pio test
.
Stormlock
Centralized locking system.
More information:
https://github.com/tmccombs/stormlock
.
Acquire a lease for resource:
stormlock aquire {{resource}}
Release the given lease for the given resource:
stormlock release {{resource}} {{lease_id}}
Show information on the current lease for a resource, if any:
stormlock current {{resource}}
Test if a lease for given resource is currently active:
stormlock is-held {{resource}} {{lease_id}}
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
