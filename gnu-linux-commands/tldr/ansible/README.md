# ansible

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ansible/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab mr create
,
dotnet build
.
ansible
Manage groups of computers remotely over SSH. (use the
/etc/ansible/hosts
file to add new groups/hosts).
Some subcommands such as
ansible galaxy
have their own usage documentation.
More information:
https://www.ansible.com/
.
List hosts belonging to a group:
ansible {{group}} --list-hosts
Ping a group of hosts by invoking the ping module:
ansible {{group}} -m ping
Display facts about a group of hosts by invoking the setup module:
ansible {{group}} -m setup
Execute a command on a group of hosts by invoking command module with arguments:
ansible {{group}} -m command -a '{{my_command}}'
Execute a command with administrative privileges:
ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'
Execute a command using a custom inventory file:
ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'
List the groups in an inventory:
ansible localhost -m debug -a '{{var=groups.keys()}}'
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
