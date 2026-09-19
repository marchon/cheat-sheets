# phpcpd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phpcpd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
newsboat
,
more
,
nano
,
whereis
,
route
.
phpcpd
A copy and paste detector for PHP code.
More information:
https://github.com/sebastianbergmann/phpcpd
.
Analyze duplicated code for a specific file or directory:
phpcpd {{path/to/file_or_directory}}
Analyze using fuzzy matching for variable names:
phpcpd --fuzzy {{path/to/file_or_directory}}
Specify a minimum number of identical lines (defaults to 5):
phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}
Specify a minimum number of identical tokens (defaults to 70):
phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}
Exclude a directory from analysis (must be relative to the source):
phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}
Output the results to a PHP-CPD XML file:
phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}
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
