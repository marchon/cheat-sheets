# ansible-inventory

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ansible-inventory/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pssh
,
gatsby
,
llvm config
,
terragrunt
.
ansible-inventory
Display or dump an Ansible inventory.
See also:
ansible
.
More information:
https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html
.
Display the default inventory:
ansible-inventory --list
Display a custom inventory:
ansbile-inventory --list --inventory {{path/to/file_or_script_or_directory}}
Display the default inventory in YAML:
ansible-inventory --list --yaml
Dump the default inventory to a file:
ansible-inventory --list --output {{path/to/file}}
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
