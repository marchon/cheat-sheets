# prettier

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/prettier/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
calc
,
vlc
,
dotnet restore
,
multitail
.
prettier
An opinionated code formatter for JavaScript, JSON, CSS, YAML, and more.
More information:
https://prettier.io/
.
Format a file and print the result to stdout:
prettier {{path/to/file}}
Check if a specific file has been formatted:
prettier --check {{path/to/file}}
Run with a specific configuration file:
prettier --config {{path/to/config_file}} {{path/to/file}}
Format a file or directory, replacing the original:
prettier --write {{path/to/file_or_directory}}
Format files or directories recursively using single quotes and no trailing commas:
prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}
Format JavaScript and TypeScript files recursively, replacing the original:
prettier --write "**/*.{js,jsx,ts,tsx}"
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
