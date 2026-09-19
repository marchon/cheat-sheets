# odps-auth

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/odps-auth/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sdkmanager
,
git check ref format
.
odps auth
User authorities in ODPS (Open Data Processing Service).
See also
odps
.
More information:
https://www.alibabacloud.com/help/doc-detail/27971.htm
.
Add a user to the current project:
add user {{username}};
Grant a set of authorities to a user:
grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};
Show authorities of a user:
show grants for {{username}};
Create a user role:
create role {{role_name}};
Grant a set of authorities to a role:
grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};
Describe authorities of a role:
desc role {{role_name}};
Grant a role to a user:
grant {{role_name}} to {{username}};
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
