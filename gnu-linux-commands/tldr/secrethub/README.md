# secrethub

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/secrethub/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ocamlc
,
git root
,
semver
,
quilt
.
secrethub
A tool to keep secrets out of config files.
More information:
https://secrethub.io
.
Print a secret to stdout:
secrethub read {{path/to/secret}}
Generate a random value and store it as a new or updated secret:
secrethub generate {{path/to/secret}}
Store a value from the clipboard as a new or updated secret:
secrethub write --clip {{path/to/secret}}
Store a value supplied on stdin as a new or updated secret:
echo "{{secret_value}}" | secrethub write {{path/to/secret}}
Audit a repository or secret:
secrethub audit {{path/to/repo_or_secret}}
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
