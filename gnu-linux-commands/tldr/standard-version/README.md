# standard-version

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/standard-version/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gopass
,
light arionum cli
,
jq
.
standard-version
Automate versioning and changelog generation, with SemVer and Conventional Commits.
More information:
https://github.com/conventional-changelog/standard-version
.
Update the changelog file and tag a release:
standard-version
Tag a release without bumping the version:
standard-version --first-release
Update the changelog and tag an alpha release:
standard-version --prerelease alpha
Update the changelog and tag a specific release type:
standard-version --release-as {{major|minor|patch}}
Tag a release, preventing hooks from being verified during the commit step:
standard-version --no-verify
Tag a release committing all staged changes, not just files affected by
standard-version
:
standard-version --commit-all
Update a specific changelog file and tag a release:
standard-version --infile {{path/to/file.md}}
Display the release that would be performed without performing them:
standard-version --dry-run
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
