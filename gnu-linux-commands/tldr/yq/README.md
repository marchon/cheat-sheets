# yq

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/yq/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
traceroute
,
hg init
,
az tag
,
pio
.
yq
A lightweight and portable command-line YAML processor.
More information:
https://mikefarah.gitbook.io/yq/
.
Output a YAML file, in pretty-print format (v4+):
yq eval {{path/to/file.yaml}}
Output a YAML file, in pretty-print format (v3):
yq read {{path/to/file.yaml}} --colors
Output the first element in a YAML file that contains only an array (v4+):
yq eval '.[0]' {{path/to/file.yaml}}
Output the first element in a YAML file that contains only an array (v3):
yq read {{path/to/file.yaml}} '[0]'
Set (or overwrite) a key to a value in a file (v4+):
yq eval '.{{key}} = "{{value}}"' --inplace {{path/to/file.yaml}}
Set (or overwrite) a key to a value in a file (v3):
yq write --inplace {{path/to/file.yaml}} '{{key}}' '{{value}}'
Merge two files and print to stdout (v4+):
yq eval-all 'select(filename == "{{path/to/file1.yaml}}") * select(filename == "{{path/to/file2.yaml}}")' {{path/to/file1.yaml}} {{path/to/file2.yaml}}
Merge two files and print to stdout (v3):
yq merge {{path/to/file1.yaml}} {{path/to/file2.yaml}} --colors
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
