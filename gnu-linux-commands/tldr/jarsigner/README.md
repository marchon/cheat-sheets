# jarsigner

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jarsigner/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nm classic
,
dog
,
sequelize
,
jetifier
.
jarsigner
Sign and verify Java Archive (JAR) files.
More information:
https://docs.oracle.com/javase/9/tools/jarsigner.htm
.
Sign a JAR file:
jarsigner {{path/to/file.jar}} {{keystore_alias}}
Sign a JAR file with a specific algorithm:
jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}
Verify the signature of a JAR file:
jarsigner -verify {{path/to/file.jar}}
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
