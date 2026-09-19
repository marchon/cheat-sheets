# tesseract

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tesseract/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
surge
,
fish
,
gh pr
,
consul kv
,
neofetch
.
tesseract
OCR (Optical Character Recognition) engine.
More information:
https://github.com/tesseract-ocr/tesseract
.
Recognize text in an image and save it to
output.txt
(the
.txt
extension is added automatically):
tesseract {{image.png}} {{output}}
Specify a custom language (default is English) with an ISO 639-2 code (e.g. deu = Deutsch = German):
tesseract -l deu {{image.png}} {{output}}
List the ISO 639-2 codes of available languages:
tesseract --list-langs
Specify a custom page segmentation mode (default is 3):
tesseract -psm {{0_to_10}} {{image.png}} {{output}}
List page segmentation modes and their descriptions:
tesseract --help-psm
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
