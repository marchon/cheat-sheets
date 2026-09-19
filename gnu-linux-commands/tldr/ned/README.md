# ned

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ned/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
magick
,
rabin2
,
git imerge
,
gh help
.
ned
Is like
grep
but with powerful replace capabilities.
Unlike
sed
, as it isn't restricted to line oriented editing.
More information:
https://github.com/nevdelap/ned
.
Recursively search starting in the current directory, ignoring case:
ned --ignore-case --recursive '{{^[dl]og}}' {{.}}
Search always showing colored output:
ned --colors '{{^[dl]og}}' {{.}}
Search never showing colored output:
ned --colors=never '{{^[dl]og}}' {{.}}
Search ignoring certain files:
ned --recursive --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}
Simple replace:
ned '{{dog}}' --replace '{{cat}}' {{.}}
Replace using numbered group references:
ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' --replace '{{the $2 dog and the $1 dog}}' {{.}}
Replace changing case:
ned '{{([a-z]+) dog}}' --case-replacements --replace '{{\U$1\E! dog}}' --stdout {{.}}
Preview results of a find and replace without updating the target files:
ned '{{^[sb]ad}}' --replace '{{happy}}' --stdout {{.}}
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
