# glab-mr-merge

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glab-mr-merge/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
diffoscope
,
wuzz
,
gh issue
,
whoami
.
glab mr merge
Merge GitLab merge requests.
More information:
https://glab.readthedocs.io/en/latest/mr/merge.html
.
Merge the merge request associated with the current branch interactively:
glab mr merge
Merge the specified merge request, interactively:
glab mr merge {{mr_number}}
Merge the merge request, removing the branch on both the local and the remote:
glab mr merge --remove-source-branch
Squash the current merge request into one commit with the message body and merge:
glab mr merge --squash --message="{{commit_message_body}}"
Display help:
glab mr merge --help
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
