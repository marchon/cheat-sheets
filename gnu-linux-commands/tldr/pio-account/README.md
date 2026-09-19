# pio-account

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-account/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dart
,
kill
,
crictl
,
lldb
,
mutt
,
exit
.
pio account
Manage your PlatformIO account in the command-line.
More information:
https://docs.platformio.org/en/latest/core/userguide/account/
.
Register a new PlatformIO account:
pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}
Permanently delete your PlatformIO account and related data:
pio account destroy
Log in to your PlatformIO account:
pio account login --username {{username}} --password {{password}}
Log out of your PlatformIO account:
pio account logout
Update your PlatformIO profile:
pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}
Show detailed information about your PlatformIO account:
pio account show
Reset your password using your username or email:
pio account forgot --username {{username_or_email}}
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
