# comby

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/comby/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
awk
,
git create branch
,
lex
,
compgen
.
comby
Tool for structural code search and replace that supports many languages.
More information:
https://github.com/comby-tools/comby
.
Match and rewrite templates, and print changes:
comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b], :[a])}}' {{.rs}}
Match and rewrite with rewrite properties:
comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b].Capitalize, :[a])}}' {{.rs}}
Match and rewrite in-place:
comby -in-place '{{match_pattern}}' '{{rewrite_pattern}}'
Only perform matching and print matches:
comby -match-only '{{match_pattern}}' ""
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
