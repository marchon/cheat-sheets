# cpdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cpdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
todoman
,
dolt blame
,
md5sum
,
sl
.
cpdf
CLI to manipulate existing PDF files in a variety of ways.
More information:
https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html
.
Select pages 1, 2, 3 and 6 from a source document and write those to a destination document:
cpdf {{path/to/source_document.pdf}} {{1-3,6}} -o {{path/to/destination_document.pdf}}
Merge two documents into a new one:
cpdf -merge {{path/to/source_document_one.pdf}} {{path/to/source_document_two.pdf}} -o {{path/to/destination_document.pdf}}
Show the bookmarks of a document:
cpdf -list-bookmarks {{path/to/document.pdf}}
Split a document into ten-page chunks, writing them to
chunk001.pdf
,
chunk002.pdf
, etc:
cpdf -split {{path/to/document.pdf}} -o {{path/to/chunk%%%.pdf}} -chunk {{10}}
Encrypt a document using 128bit encryption, providing
fred
as owner password and
joe
as user password:
cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{path/to/source_document.pdf}} -o {{path/to/encrypted_document.pdf}}
Decrypt a document using the owner password
fred
:
cpdf -decrypt {{path/to/encrypted_document.pdf}} owner={{fred}} -o {{path/to/decrypted_document.pdf}}
Show the annotations of a document:
cpdf -list-annotations {{path/to/document.pdf}}
Create a new document from an existing one with additional metadata:
cpdf -set-metadata {{path/to/metadata.xml}} {{path/to/source_document.pdf}} -o {{path/to/destination_document.pdf}}
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
