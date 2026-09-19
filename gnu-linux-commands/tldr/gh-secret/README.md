# gh-secret

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-secret/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bashmarks
,
gunzip
,
aria2c
,
wipeclean
.
gh secret
Manage GitHub secrets from the command-line.
More information:
https://cli.github.com/manual/gh_secret
.
List secret keys for the current repository:
gh secret list
List secret keys for a specific organization:
gh secret list --org {{organization}}
List secret keys for a specific repository:
gh secret list --repo {{owner}}/{{repository}}
Set a secret for the current repository (user will be prompted for the value):
gh secret set {{name}}
Set a secret from a file for the current repository:
gh secret set {{name}} < {{path/to/file}}
Set an organization secret for specific repositories:
gh secret set {{name}} --org {{organization}} --repos {{repository1,repository2}}
Remove a secret for the current repository:
gh secret remove {{name}}
Remove a secret for a specific organization:
gh secret remove {{name}} --org {{organization}}
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
