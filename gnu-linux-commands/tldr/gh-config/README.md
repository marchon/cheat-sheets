# gh-config

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-config/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh domblklist
,
nvm
,
pretty bytes
.
gh config
Change configuration for GitHub cli.
More information:
https://cli.github.com/manual/gh_config
.
Display what Git protocol is being used:
gh config get git_protocol
Set protocol to SSH:
gh config set git_protocol {{ssh}}
Use
delta
in side-by-side mode as the default pager for all
gh
commands:
gh config set pager '{{delta --side-by-side}}'
Set text editor to Vim:
gh config set editor {{vim}}
Reset to default text editor:
gh config set editor {{""}}
Disable interactive prompts:
gh config set prompt {{disabled}}
Set a specific configuration value:
gh config set {{key}} {{value}}
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
