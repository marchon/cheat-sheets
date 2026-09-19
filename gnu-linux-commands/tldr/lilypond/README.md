# lilypond

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lilypond/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh pool start
,
pdfgrep
,
mutt
.
lilypond
Typeset music and/or produce MIDI from file.
More information:
https://lilypond.org
.
Compile a lilypond file into a PDF:
lilypond {{path/to/file}}
Compile into the specified format:
lilypond --formats={{format_dump}} {{path/to/file}}
Compile the specified file, suppressing progress updates:
lilypond -s {{path/to/file}}
Compile the specified file, and also specify the output filename:
lilypond --output={{path/to/output_file}} {{path/to/input_file}}
Show the current version of lilypond:
lilypond --version
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
