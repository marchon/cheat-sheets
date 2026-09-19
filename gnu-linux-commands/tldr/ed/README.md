# ed

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ed/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
slackcat
,
lwp request
,
ocamlopt
.
ed
The original Unix text editor.
More information:
https://www.gnu.org/software/ed/manual/ed_manual.html
.
Start ed, editing an empty document (which can be saved as a new file in the current directory):
ed
Start ed, editing an empty document, with
:
as a command prompt indicator:
ed -p :
Start ed editing an existing file (this shows the byte count of the loaded file):
ed -p : {{path/to/file}}
Toggle the printing of error explanations. (By default, explanations are not printed and only a
?
appears):
H
Add text to the current document. Mark completion by entering a period by itself in a new line:
a
{{text_to_insert}}
.
Print the entire document (
,
is a shortcut to the range
1,$
which covers the start to the end of the document):
,p
Write the current document to a new file (the filename can be omitted if
ed
was called with an existing file):
w {{filename}}
Quit ed:
q
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
