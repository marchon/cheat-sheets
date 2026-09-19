# chroma

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/chroma/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git blame someone else
,
handbrakecli
.
chroma
Chroma is a general-purpose syntax highlighting library and corresponding command, for Go.
More information:
https://github.com/alecthomas/chroma
.
Highlight a source file with python lexer and output to terminal:
chroma --lexer="{{python}}" {{source_file}}
Highlight a source file with the Go lexer and output to an HTML file:
chroma --lexer="{{go}}" --formatter="{{html}}" {{source_file}} > {{html_file}}
Highlight a source file with the C++ lexer and output to an SVG, using the Monokai style:
chroma --lexer="{{c++}}" --formatter="{{svg}}" --syle="{{monokai}}" {{source_file}} > {{svg_file}}
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
