# satis

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/satis/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phan
,
git coauthor
,
box
,
updog
.
satis
The command-line utility for the Satis static Composer repository.
More information:
https://github.com/composer/satis
.
Initialize a Satis configuration:
satis init {{satis.json}}
Add a VCS repository to the Satis configuration:
satis add {{repository_url}}
Build the static output from the configuration:
satis build {{satis.json}} {{path/to/output_directory}}
Build the static output by updating only the specified repository:
satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}
Remove useless archive files:
satis purge {{satis.json}} {{path/to/output_directory}}
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
