# rich

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rich/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
direnv
,
zmv
,
phpdox
,
git mr
,
browser sync
.
rich
Rich CLI is a toolbox for fancy output in the terminal.
More information:
https://github.com/Textualize/rich-cli
.
Display a file with syntax highlighting:
rich {{path/to/file.py}}
Add line numbers, and indentation guides:
rich {{path/to/file.py}} --line-number --guides
Apply a theme:
rich {{path/to/file.py}} --theme {{monokai}}
Display a file in an interactive pager:
rich {{path/to/file.py}} --pager
Display contents from a URL:
rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager
Export a file as HTML:
rich {{path/to/file.md}} --export-html {{path/to/file.html}}
Display text with formatting tags, custom alignment, and line width:
rich --print {{"Hello [green on black]Stylized[/green on black] [bold]World[/bold]"}} --{{left|center|right}} --width {{10}}
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
