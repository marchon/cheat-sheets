# tr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
man
,
awslogs
,
git ls remote
,
serverless
.
tr
Translate characters: run replacements based on single characters and character sets.
More information:
https://www.gnu.org/software/coreutils/tr
.
Replace all occurrences of a character in a file, and print the result:
tr {{find_character}} {{replace_character}} < {{filename}}
Replace all occurrences of a character from another command's output:
echo {{text}} | tr {{find_character}} {{replace_character}}
Map each character of the first set to the corresponding character of the second set:
tr '{{abcd}}' '{{jkmn}}' < {{filename}}
Delete all occurrences of the specified set of characters from the input:
tr -d '{{input_characters}}' < {{filename}}
Compress a series of identical characters to a single character:
tr -s '{{input_characters}}' < {{filename}}
Translate the contents of a file to upper-case:
tr "[:lower:]" "[:upper:]" < {{filename}}
Strip out non-printable characters from a file:
tr -cd "[:print:]" < {{filename}}
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
