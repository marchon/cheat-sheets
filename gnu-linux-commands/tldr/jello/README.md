# jello

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jello/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
logname
,
orca c
,
git delete tag
.
jello
A command-line JSON processor using Python syntax.
More information:
https://github.com/kellyjonbrazil/jello
.
Pretty-print JSON or JSON-Lines data from stdin to stdout:
cat {{file.json}} | jello
Output a schema of JSON or JSON Lines data from stdin to stdout (useful for grep):
cat {{file.json}} | jello -s
Output all elements from arrays (or all the values from objects) in JSON or JSON-Lines data from stdin to stdout:
cat {{file.json}} | jello -l
Output the first element in JSON or JSON-Lines data from stdin to stdout:
cat {{file.json}} | jello _[0]
Output the value of a given key of each element in JSON or JSON-Lines data from stdin to stdout:
cat {{file.json}} | jello '[i.{{key_name}} for i in _]'
Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys
key_name
and
other_key_name
):
cat {{file.json}} | jello '{"{{my_new_key}}": _.{{key_name}}, "{{my_other_key}}": _.{{other_key_name}}}'
Output the value of a given key to a string (and disable JSON output):
cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'
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
