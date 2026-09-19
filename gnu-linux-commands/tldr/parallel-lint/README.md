# parallel-lint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/parallel-lint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cargo rustc
,
elm
,
sn
,
xetex
,
texliveonfly
.
parallel-lint
A tool to check the syntax of PHP files in parallel.
More information:
https://github.com/JakubOnderka/PHP-Parallel-Lint
.
Lint a specific directory:
parallel-lint {{path/to/directory}}
Lint a directory using the specified number of parallel processes:
parallel-lint -j {{processes}} {{path/to/directory}}
Lint a directory, excluding the specified directory:
parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}
Lint a directory of files using a comma-separated list of extension(s):
parallel-lint -e {{php,html,phpt}} {{path/to/directory}}
Lint a directory and output the results as JSON:
parallel-lint --json {{path/to/directory}}
Lint a directory and show Git Blame results for rows containing errors:
parallel-lint --blame {{path/to/directory}}
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
