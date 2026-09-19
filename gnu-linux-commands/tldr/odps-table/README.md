# odps-table

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/odps-table/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tlmgr gui
,
tred
,
gpg tui
,
webtorrent
.
odps table
Create and modify tables in ODPS (Open Data Processing Service).
See also
odps
.
More information:
https://www.alibabacloud.com/help/doc-detail/27971.htm
.
Create a table with partition and lifecycle:
create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};
Create a table based on the definition of another table:
create table {{table_name}} like {{another_table}};
Add partition to a table:
alter table {{table_name}} add partition ({{partition_spec}});
Delete partition from a table:
alter table {{table_name}} drop partition ({{partition_spec}});
Delete table:
drop table {{table_name}};
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
