# black

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/black/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
trans
,
gdb
,
brew bundle
,
dircolors
.
black
A Python auto code formatter.
More information:
https://github.com/psf/black
.
Auto-format a file or entire directory:
black {{path/to/file_or_directory}}
Format the code passed in as a string:
black -c "{{code}}"
Output the changes that would be applied for each file:
black --diff {{path/to/file_or_directory}}
Perform a dry run (print what would be done without actually doing it):
black --check {{path/to/file_or_directory}}
Auto-format a file or directory emitting exclusively error messages to stderr:
black --quiet {{path/to/file_or_directory}}
Auto-format a file or directory without replacing single quotes with double quotes (adoption helper, avoid using this for new projects):
black --skip-string-normalization {{path/to/file_or_directory}}
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
