# security-checker

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/security-checker/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az appconfig
,
mocha
,
jello
,
deno
.
security-checker
Check if a PHP application uses dependencies with known security vulnerabilities.
More information:
https://github.com/sensiolabs/security-checker
.
Look for security issues in the project dependencies (based on the
composer.lock
file in the current directory):
security-checker security:check
Use a specific
composer.lock
file:
security-checker security:check {{path/to/composer.lock}}
Return results as a JSON object:
security-checker security:check --format=json
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
