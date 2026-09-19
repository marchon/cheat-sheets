# gist

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gist/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
loadtest
,
aws help
,
phpbu
,
pathchk
.
gist
Upload code to https://gist.github.com.
More information:
https://github.com/defunkt/gist
.
Log in in gist on this computer:
gist --login
Create a gist from any number of text files:
gist {{file.txt}} {{file2.txt}}
Create a private gist with a description:
gist --private --description "{{A meaningful description}}" {{file.txt}}
Read contents from stdin and create a gist from it:
{{echo "hello world"}} | gist
List your public and private gists:
gist --list
List all public gists for any user:
gist --list {{username}}
Update a gist using the ID from URL:
gist --update {{GIST_ID}} {{file.txt}}
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
