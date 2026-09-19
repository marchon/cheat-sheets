# shuf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/shuf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
flutter
,
terraform plan
,
git whatchanged
.
shuf
Generate random permutations.
More information:
https://www.gnu.org/software/coreutils/shuf
.
Randomize the order of lines in a file and output the result:
shuf {{filename}}
Only output the first 5 entries of the result:
shuf --head-count={{5}} {{filename}}
Write the output to another file:
shuf {{filename}} --output={{output_filename}}
Generate 3 random numbers in the range 1-10 (inclusive):
shuf --head-count={{3}} --input-range={{1-10}} --repeat
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
