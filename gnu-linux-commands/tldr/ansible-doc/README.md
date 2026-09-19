# ansible-doc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ansible-doc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pyenv
,
infection
,
go fix
,
sc im
.
ansible-doc
Display information on modules installed in Ansible libraries.
Display a terse listing of plugins and their short descriptions.
More information:
https://docs.ansible.com/ansible/latest/cli/ansible-doc.html
.
List available action plugins (modules):
ansible-doc --list
List available plugins of a specific type:
ansible-doc --type {{plugin_type}} --list
Show information about a specific action plugin (module):
ansible-doc {{plugin_name}}
Show information about a plugin with a specific type:
ansible-doc --type {{plugin_type}} {{plugin_name}}
Show the playbook snippet for action plugin (modules):
ansible-doc --snippet {{plugin_name}}
Show information about an action plugin (module) as JSON:
ansible-doc --json {{plugin_name}}
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
