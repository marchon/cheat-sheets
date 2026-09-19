# for

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/for/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hsw cli
,
git annex
,
masscan
,
gh reference
.
for
Perform a command several times.
More information:
https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs
.
Execute the given commands for each of the specified items:
for {{variable}} in {{item1 item2 ...}}; do {{echo "Loop is executed"}}; done
Iterate over a given range of numbers:
for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "Loop is executed"}}; done
Iterate over a given list of files:
for {{variable}} in {{path/to/file1 path/to/file2 ...}}; do {{echo "Loop is executed"}}; done
Iterate over a given list of directories:
for {{variable}} in {{path/to/directory1/ path/to/directory2/ ...}}; do {{echo "Loop is executed"}}; done
Perform a given command in every directory:
for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "Loop is executed"}}) done
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
