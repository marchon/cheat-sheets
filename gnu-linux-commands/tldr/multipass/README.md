# multipass

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/multipass/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ocrmypdf
,
sh
,
umask
,
svn changelist
.
multipass
CLI to manage Ubuntu virtual machines using native hypervisors.
More information:
https://multipass.run/
.
List the aliases that can be used to launch an instance:
multipass find
Launch a new instance, set its name and use a cloud-init configuration file:
multipass launch -n {{instance_name}} --cloud-init {{configuration_file}}
List all the created instances and some of their properties:
multipass list
Start a specific instance by name:
multipass start {{instance_name}}
Show the properties of an instance:
multipass info {{instance_name}}
Open a shell prompt on a specific instance by name:
multipass shell {{instance_name}}
Delete an instance by name:
multipass delete {{instance_name}}
Mount a directory into a specific instance:
multipass mount {{path/to/local/directory}} {{instance_name}}:{{path/to/target/directory}}
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
