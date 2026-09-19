# gh-secret-set

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-secret-set/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
column
,
llvm g++
,
stdbuf
,
jmtpfs
.
gh secret set
Create or update GitHub secrets from the command line.
More information:
https://cli.github.com/manual/gh_secret_set
.
Set a secret for the current repository (user will be prompted for the value):
gh secret set {{name}}
Set a secret from a file for the current repository:
gh secret set {{name}} < {{path/to/file}}
Set a secret for a specific repository:
gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}
Set an organization secret for specific repositories:
gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"
Set an organization secret with a specific visibility:
gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}
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
