# bundletool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bundletool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
samtools
,
gh pr merge
,
vala
,
gcc
.
bundletool
Command-line tool to manipulate Android Application Bundles.
Some subcommands such as
bundletool validate
have their own usage documentation.
More information:
https://developer.android.com/studio/command-line/bundletool
.
Display help for a subcommand:
bundletool help {{subcommand}}
Generate APKs from an application bundle (prompts for keystore password):
bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}
Generate APKs from an application bundle giving the keystore password:
bundletool build-apks --bundle={{path/to/bundle.aab}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} –ks-pass={{pass:the_password}} --output={{path/to/file.apks}}
Generate APKs including only one single APK for universal usage:
bundletool build-apks --bundle={{path/to/bundle.aab}} --mode={{universal}} --ks={{path/to/key.keystore}} --ks-key-alias={{key_alias}} --output={{path/to/file.apks}}
Install the right combination of APKs to an emulator or device:
bundletool install-apks --apks={{path/to/file.apks}}
Estimate the download size of an application:
bundletool get-size total --apks={{path/to/file.apks}}
Generate a device specification JSON file for an emulator or device:
bundletool get-device-spec --output={{path/to/file.json}}
Verify a bundle and display detailed information about it:
bundletool validate --bundle={{path/to/bundle.aab}}
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
