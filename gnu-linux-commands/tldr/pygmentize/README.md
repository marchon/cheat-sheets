# pygmentize

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pygmentize/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phpbu
,
docker exec
,
az feedback
.
pygmentize
Python-based syntax highlighter.
More information:
https://pygments.org/docs/cmdline/
.
Highlight file syntax and print to standard output (language is inferred from the file extension):
pygmentize {{file.py}}
Explicitly set the language for syntax highlighting:
pygmentize -l {{javascript}} {{input_file}}
List available lexers (processors for input languages):
pygmentize -L lexers
Save output to a file in HTML format:
pygmentize -f html -o {{output_file.html}} {{input_file.py}}
List available output formats:
pygmentize -L formatters
Output an HTML file, with additional formatter options (full page, with line numbers):
pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}
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
