# odps-tunnel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/odps-tunnel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ldapsearch
,
git pr
,
ack
,
masscan
.
odps tunnel
Data tunnel in ODPS (Open Data Processing Service).
See also
odps
.
More information:
https://www.alibabacloud.com/help/doc-detail/27971.htm
.
Download table to local file:
tunnel download {{table_name}} {{file}};
Upload local file to a table partition:
tunnel upload {{file}} {{table_name}}/{{partition_spec}};
Upload table specifying field and record delimiters:
tunnel upload {{file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};
Upload table using multiple threads:
tunnel upload {{file}} {{table_name}} -threads {{num}};
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
