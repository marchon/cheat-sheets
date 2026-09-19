# hg-pull

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hg-pull/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
openscad
,
inkview
,
nth
,
pdfseparate
.
hg pull
Pull changes from a specified repository to the local repository.
More information:
https://www.mercurial-scm.org/doc/hg.1.html#pull
.
Pull from the "default" source path:
hg pull
Pull from a specified source repository:
hg pull {{path/to/source_repository}}
Update the local repository to the head of the remote:
hg pull --update
Pull changes even when the remote repository is unrelated:
hg pull --force
Specify a specific revision changeset to pull up to:
hg pull --rev {{revision}}
Specify a specific branch to pull:
hg pull --branch {{branch}}
Specify a specific bookmark to pull:
hg pull --bookmark {{bookmark}}
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
