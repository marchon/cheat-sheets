# kotlinc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kotlinc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh help
,
openssl
,
molecule
,
apktool
.
kotlinc
Kotlin compiler.
More information:
https://kotlinlang.org/docs/command-line.html
.
Start a REPL (interactive shell):
kotlinc
Compile a Kotlin file:
kotlinc {{path/to/file.kt}}
Compile several Kotlin files:
kotlinc {{path/to/file1.kt path/to/file2.kt ...}}
Execute a specific Kotlin Script file:
kotlinc -script {{path/to/file.kts}}
Compile a Kotlin file into a self contained jar file with the Kotlin runtime library included:
kotlinc {{path/to/file.kt}} -include-runtime -d {{path/to/file.jar}}
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
