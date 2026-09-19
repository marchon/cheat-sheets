# amass-db

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/amass-db/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
terminalizer
,
while
,
virsh help
.
amass db
Interact with an Amass database.
More information:
https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand
.
List all performed enumerations in the database:
amass db -dir {{path/to/database_directory}} -list
Show results for a specified enumeration index and domain name:
amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -show
List all found subdomains of a domain within an enumeration:
amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -names
Show a summary of the found subdomains within an enumeration:
amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -summary
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
