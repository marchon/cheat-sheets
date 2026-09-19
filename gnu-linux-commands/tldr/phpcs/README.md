# phpcs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phpcs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arch
,
mogrify
,
git grep
,
7z
,
traefik
.
phpcs
Tokenize PHP, JavaScript and CSS files to detect violations of a defined set of coding standards.
More information:
https://github.com/squizlabs/PHP_CodeSniffer
.
Sniff the specified directory for issues (defaults to the PEAR standard):
phpcs {{path/to/directory}}
Display a list of installed coding standards:
phpcs -i
Specify a coding standard to validate against:
phpcs {{path/to/directory}} --standard {{standard}}
Specify comma-separated file extensions to include when sniffing:
phpcs {{path/to/directory}} --extensions {{file_extension(s)}}
Specify the format of the output report (e.g.
full
,
xml
,
json
,
summary
):
phpcs {{path/to/directory}} --report {{format}}
Set config variables to be used during the process:
phpcs {{path/to/directory}} --config-set {{key}} {{value}}
A comma-separated list of files to load before processing:
phpcs {{path/to/directory}} --bootstrap {{file(s)}}
Don't recurse into subdirectories:
phpcs {{path/to/directory}} -l
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
