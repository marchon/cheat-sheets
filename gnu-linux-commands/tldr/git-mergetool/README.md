# git-mergetool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-mergetool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
uniq
,
typeset
,
ifconfig
,
deb get
.
git mergetool
Run merge conflict resolution tools to resolve merge conflicts.
More information:
https://git-scm.com/docs/git-mergetool
.
Launch the default merge tool to resolve conflicts:
git mergetool
List valid merge tools:
git mergetool --tool-help
Launch the merge tool identified by a name:
git mergetool --tool {{tool_name}}
Don't prompt before each invocation of the merge tool:
git mergetool --no-prompt
Explicitly use the GUI merge tool (see the
merge.guitool
config variable):
git mergetool --gui
Explicitly use the regular merge tool (see the
merge.tool
config variable):
git mergetool --no-gui
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
