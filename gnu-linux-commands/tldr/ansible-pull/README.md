# ansible-pull

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ansible-pull/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tig
,
doxygen
,
axel
,
adb
,
runit
,
streamlink
.
ansible-pull
Pull ansible playbooks from a VCS repo and executes them for the local host.
More information:
https://docs.ansible.com/ansible/latest/cli/ansible-pull.html
.
Pull a playbook from a VCS and execute a default local.yml playbook:
ansible-pull -U {{repository_url}}
Pull a playbook from a VCS and execute a specific playbook:
ansible-pull -U {{repository_url}} {{playbook}}
Pull a playbook from a VCS at a specific branch and execute a specific playbook:
ansible-pull -U {{repository_url}} -C {{branch}} {{playbook}}
Pull a playbook from a VCS, specify hosts file and execute a specific playbook:
ansible-pull -U {{repository_url}} -i {{hosts_file}} {{playbook}}
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
