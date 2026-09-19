# mongoimport

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mongoimport/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arduino builder
,
lein
,
pactl
.
mongoimport
Imports content from a JSON, CSV, or TSV file into a MongoDB database.
More information:
https://docs.mongodb.com/database-tools/mongoimport/
.
Import a JSON file into a specific collection:
mongoimport --file={{path/to/file.json}} --uri={{mongodb_uri}} --collection={{collection_name}}
Import a CSV file, using the first line of the file to determine field names:
mongoimport --type={{csv}} --file={{path/to/file.csv}} --db={{database_name}} --collection={{collection_name}}
Import a JSON array, using each element as a separate document:
mongoimport --jsonArray --file={{path/to/file.json}}
Import a JSON file using a specific mode and a query to match existing documents:
mongoimport --file={{path/to/file.json}} --mode={{delete|merge|upsert}} --upsertFields="{{field1,field2,...}}"
Import a CSV file, reading field names from a separate CSV file and ignoring fields with empty values:
mongoimport --type={{csv}} --file={{path/to/file.csv}} --fieldFile={{path/to/field_file.csv}} --ignoreBlanks
Display help:
mongoimport --help
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
