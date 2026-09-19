# amass-enum

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/amass-enum/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
runsv
,
lex
,
m4
,
git apply
,
ipsumdump
.
amass enum
Find subdomains of a domain.
More information:
https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand
.
Passively find subdomains of a domain:
amass enum -passive -d {{domain_name}}
Find subdomains of a domain and actively verify them attempting to resolve the found subdomains:
amass enum -active -d {{domain_name}} -p {{80,443,8080}}
Do a brute force search for subdomains:
amass enum -brute -d {{domain_name}}
Save the results to a text file:
amass enum -o {{output_file}} -d {{domain_name}}
Save the results to a database:
amass enum -o {{output_file}} -dir {{path/to/database_directory}}
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
