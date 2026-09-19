# scalafmt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/scalafmt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hostname
,
pass otp
,
chgrp
,
hg commit
.
scalafmt
Code formatter for Scala.
Configurations are stored in the
.scalafmt.conf
file.
More information:
https://scalameta.org/scalafmt
.
Reformat all
.scala
files in the current directory recursively:
scalafmt
Reformat specific files or directories with a custom formatting configuration:
scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory}} {{path/to/file_or_directory}} {{...}}
Check if files are correctly formatted, returning
0
if all files respect the formatting style:
scalafmt --config {{path/to/.scalafmt.conf}} --test
Exclude files or directories:
scalafmt --exclude {{path/to/file_or_directory}} {{...}}
Format only files that were edited against the current Git branch:
scalafmt --config {{path/to/.scalafmt.conf}} --mode diff
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
