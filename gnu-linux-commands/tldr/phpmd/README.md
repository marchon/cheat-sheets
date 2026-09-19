# phpmd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phpmd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
delta
,
gist
,
nodemon
,
rails generate
.
phpmd
A PHP mess detector that checks for common potential problems.
More information:
https://github.com/phpmd/phpmd
.
Display a list of available rulesets and formats:
phpmd
Scan a file or directory for problems using comma-separated rulesets:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}}
Specify the minimum priority threshold for rules:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --minimumpriority {{priority}}
Include only the specified extensions in analysis:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --suffixes {{extensions}}
Exclude the specified comma-separated directories:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --exclude {{directory_patterns}}
Output the results to a file instead of stdout:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --reportfile {{path/to/report_file}}
Ignore the use of warning-suppressive PHPDoc comments:
phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --strict
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
