# odps-func

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/odps-func/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
magento
,
pio upgrade
,
drush
,
php coveralls
.
odps func
Manage functions in ODPS (Open Data Processing Service).
See also
odps
.
More information:
https://www.alibabacloud.com/help/doc-detail/27971.htm
.
Show functions in the current project:
list functions;
Create a Java function using a
.jar
resource:
create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';
Create a Python function using a
.py
resource:
create function {{func_name}} as {{script.Func}} using '{{script.py}}';
Delete a function:
drop function {{func_name}};
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
