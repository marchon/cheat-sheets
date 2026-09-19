# odps

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/odps/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zmore
,
git diff
,
jpegoptim
,
git checkout index
.
odps
Aliyun ODPS (Open Data Processing Service) command-line tool.
Some subcommands such as
odps inst
have their own usage documentation.
More information:
https://www.alibabacloud.com/help/doc-detail/27971.htm
.
Start the command-line with a custom configuration file:
odpscmd --config={{odps_config.ini}}
Switch current project:
use {{project_name}};
Show tables in the current project:
show tables;
Describe a table:
desc {{table_name}};
Show table partitions:
show partitions {{table_name}};
Describe a partition:
desc {{table_name}} partition ({{partition_spec}});
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
