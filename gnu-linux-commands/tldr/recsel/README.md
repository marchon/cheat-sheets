# recsel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/recsel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kill
,
julia
,
phpenv
,
aws help
,
go fmt
.
recsel
Print records from a recfile: a human-editable, plain text database.
More information:
https://www.gnu.org/software/recutils/manual/recutils.html
.
Extract name and version field:
recsel -p name,version {{data.rec}}
Use "~" to match a string with a given regular expression:
recsel -e "{{field_name}} ~ '{{regular_expression}}' {{data.rec}}"
Use a predicate to match a name and a version:
recsel -e "name ~ '{{regular_expression}}' && version ~ '{{regular_expression}}'" {{data.rec}}
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
