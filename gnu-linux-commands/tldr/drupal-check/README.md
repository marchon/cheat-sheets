# drupal-check

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/drupal-check/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git clean
,
curl
,
particle
,
csvsql
.
drupal-check
Check Drupal PHP code for deprecations.
More information:
https://github.com/mglaman/drupal-check
.
Check the code in a specific directory for deprecations:
drupal-check {{path/to/directory}}
Check the code excluding a comma-separated list of directories:
drupal-check --exclude-dir {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}
Don't show a progress bar:
drupal-check --no-progress {{path/to/directory}}
Perform static analysis to detect bad coding practices:
drupal-check --analysis {{path/to/directory}}
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
