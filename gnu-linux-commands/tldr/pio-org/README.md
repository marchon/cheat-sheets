# pio-org

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-org/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git archive
,
vimdiff
,
qemu img
.
pio org
Manage PlatformIO organizations and their owners.
More information:
https://docs.platformio.org/en/latest/core/userguide/org/
.
Create a new organization:
pio org create {{organization_name}}
Delete an organization:
pio org destroy {{organization_name}}
Add a user to an organization:
pio org add {{organization_name}} {{username}}
Remove a user from an organization:
pio org remove {{organization_name}} {{username}}
List all organizations the current user is a member of and their owners:
pio org list
Update the name, email or display name of an organization:
pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}
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
