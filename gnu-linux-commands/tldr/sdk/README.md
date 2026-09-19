# sdk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sdk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
printf
,
batch
,
inkscape
,
redis server
.
sdk
Tool for managing parallel versions of multiple Software Development Kits.
Supports Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x and many others.
More information:
https://sdkman.io/usage
.
Install a specific version of Gradle:
sdk install {{gradle}} {{gradle_version}}
Switch to a specific version of Gradle:
sdk use {{gradle}} {{gradle_version}}
Check current Gradle version:
sdk current {{gradle}}
List all Software Development Kits available to install:
sdk list
List all available versions for a specific Software Development Kit:
sdk list {{sdk_name}}
List all installed Software Development Kits:
sdk current
Update Gradle to the latest version:
sdk upgrade {{gradle}}
Uninstall a particular version of Gradle:
sdk rm {{gradle}} {{gradle_version}}
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
