# puppet-apply

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/puppet-apply/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio settings
,
rclone
,
units
,
xml unescape
.
puppet apply
Apply Puppet manifests locally.
More information:
https://puppet.com/docs/puppet/7/man/apply.html
.
Apply a manifest:
puppet apply {{path/to/manifest}}
Execute puppet code:
puppet apply --execute {{code}}
Use a specific module and hiera config file:
puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}
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
