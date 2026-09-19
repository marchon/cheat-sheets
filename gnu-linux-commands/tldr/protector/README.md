# protector

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/protector/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
duplicacy
,
go clean
,
cowsay
,
popd
.
protector
Protect or unprotect branches on GitHub repositories.
More information:
https://github.com/jcgay/protector
.
Protect branches of a GitHub repository (create branch protection rules):
protector {{branches_regex}} -repos {{organization/repository}}
Use the dry run to see what would be protected (can also be used for freeing):
protector -dry-run {{branches_regex}} -repos {{organization/repository}}
Free branches of a GitHub repository (delete branch protection rules):
protector -free {{branches_regex}} -repos {{organization/repository}}
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
