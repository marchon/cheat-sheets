# protoc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/protoc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
yarn
,
hsd cli
,
kitex
,
progress
.
protoc
Parse Google Protobuf
.proto
files and generate output in the specified language.
More information:
https://developers.google.com/protocol-buffers
.
Generate Python code from a
.proto
file:
protoc --python_out={{path/to/output_directory}} {{input_file.proto}}
Generate Java code from a
.proto
file that imports other
.proto
files:
protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}
Generate code for multiple languages:
protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}
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
