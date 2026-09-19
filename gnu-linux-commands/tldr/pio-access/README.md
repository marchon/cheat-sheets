# pio-access

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-access/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ufraw batch
,
mount
,
pactl
,
du
,
fping
.
pio access
Set the access level on published resources (packages) in the registry.
More information:
https://docs.platformio.org/en/latest/core/userguide/access/
.
Grant a user access to a resource:
pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}
Remove a user's access to a resource:
pio access revoke {{username}} {{resource_urn}}
Show all resources that a user or team has access to and the access level:
pio access list {{username}}
Restrict access to a resource to specific users or team members:
pio access private {{resource_urn}}
Allow all users access to a resource:
pio access public {{resource_urn}}
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
