# git-send-email

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-send-email/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
maza
,
rcat
,
odps func
,
jcal
,
redis cli
.
git send-email
Send a collection of patches as emails.
Patches can be specified as files, directions, or a revision list.
More information:
https://git-scm.com/docs/git-send-email
.
Send the last commit in the current branch:
git send-email -1
Send a given commit:
git send-email -1 {{commit}}
Send multiple (e.g. 10) commits in the current branch:
git send-email {{-10}}
Send an introductory email message for the patch series:
git send-email -{{number_of_commits}} --compose
Review and edit the email message for each patch you're about to send:
git send-email -{{number_of_commits}} --annotate
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
