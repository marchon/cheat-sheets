# smalltalkci

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/smalltalkci/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ia
,
git archive
,
cppclean
,
pio lib
.
smalltalkci
Framework for testing Smalltalk projects with GitHub Actions, Travis CI, AppVeyor, GitLab CI, and others.
More information:
https://github.com/hpi-swa/smalltalkCI
.
Run tests for a configuration file:
smalltalkci {{path/to/.smalltalk.ston}}
Run tests for the
.smalltalk.ston
configuration in the current directory:
smalltalkci
Debug tests in headful mode (show VM window):
smalltalkci --headful
Download and prepare a well-known smalltalk image for the tests:
smalltalkci --smalltalk {{Squeak64-Trunk}}
Specify a custom Smalltalk image and VM:
smalltalkci --image {{path/to/Smalltalk.image}} -- vm {{path/to/vm}}
Clean up caches and delete builds:
smalltalkci --clean
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
