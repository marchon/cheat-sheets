# git-effort

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-effort/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kompose
,
airpaste
,
git pull
,
lebab
.
git effort
Display how much activity a file has had, showing commits per file and "active days" i.e. total number of days that contributed to the file.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-effort
.
Display each file in the repository, showing commits and active days:
git effort
Display files modified by a specific number of commits or more, showing commits and active days:
git effort --above {{5}}
Display files modified by a specific author, showing commits and active days:
git effort -- --author="{{username}}"
Display files modified since a specific time/date, showing commits and active days:
git effort -- --since="{{last month}}"
Display only the specified files or directories, showing commits and active days:
git effort {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}
Display all files in a specific directory, showing commits and active days:
git effort {{path/to/directory/*}}
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
