# mmdc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mmdc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue shutdown
,
gops
,
qdbus
,
redis cli
.
mmdc
CLI for mermaid, a diagram generation tool with a domain-specific language.
A mermaid definition file is taken as input and a SVG, PNG, or PDF file is generated as output.
More information:
https://mermaid-js.github.io/mermaid/
.
Convert a file to the specified format (automatically determined from the file extension):
mmdc --input {{input.mmd}} --output {{output.svg}}
Specify the theme of the chart:
mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}
Specify the background color of the chart (e.g.
lime
,
"#D8064F"
, or
transparent
):
mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}
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
