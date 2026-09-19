# numfmt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/numfmt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gpg2
,
fast
,
git changelog
,
az
,
repren
.
numfmt
Convert numbers to and from human-readable strings.
More information:
https://www.gnu.org/software/coreutils/numfmt
.
Convert 1.5K (SI Units) to 1500:
numfmt --from={{si}} {{1.5K}}
Convert 5th field (1-indexed) to IEC Units without converting header:
ls -l | numfmt --header={{1}} --field={{5}} --to={{iec}}
Convert to IEC units, pad with 5 characters, left aligned:
du -s * | numfmt --to={{iec}} --format="{{%-5f}}"
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
