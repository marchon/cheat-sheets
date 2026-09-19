# mysqld

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mysqld/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aapt
,
stack
,
isisdl
,
vifm
,
grunt
.
mysqld
Start the MySQL database server.
More information:
https://dev.mysql.com/doc/refman/en/mysqld.html
.
Start the MySQL database server:
mysqld
Start the server, printing error messages to the console:
mysqld --console
Start the server, saving logging output to a custom log file:
mysqld --log={{path/to/file.log}}
Print the default arguments and their values and exit:
mysqld --print-defaults
Start the server, reading arguments and values from a file:
mysqld --defaults-file={{path/to/file}}
Start the server and listen on a custom port:
mysqld --port={{port}}
Show all help options and exit:
mysqld --verbose --help
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
