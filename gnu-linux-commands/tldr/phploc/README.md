# phploc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/phploc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az pipelines
,
envoy
,
rails db
.
phploc
A tool for quickly measuring the size and analyzing the structure of a PHP project.
More information:
https://github.com/sebastianbergmann/phploc
.
Analyze a directory and print the result:
phploc {{path/to/directory}}
Include only specific files from a comma-separated list (globs are allowed):
phploc {{path/to/directory}} --names {{files}}
Exclude specific files from a comma-separated list (globs are allowed):
phploc {{path/to/directory}} --names-exclude {{files}}
Exclude a specific directory from analysis:
phploc {{path/to/directory}} --exclude {{path/to/exclude_directory}}
Log the results to a specific CSV file:
phploc {{path/to/directory}} --log-csv {{path/to/file}}
Log the results to a specific XML file:
phploc {{path/to/directory}} --log-xml {{path/to/file}}
Count PHPUnit test case classes and test methods:
phploc {{path/to/directory}} --count-tests
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
