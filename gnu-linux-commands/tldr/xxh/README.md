# xxh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xxh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cloc
,
ps
,
php artisan
,
expose
,
glab release
.
xxh
Bring your shell with all of your customizations through SSH sessions.
Note: xxh does not install anything into system directories on the target machine; removing
~/.xxh
will clear all traces of xxh on the target machine.
More information:
https://github.com/xxh/xxh
.
Connect to a host and run the current shell:
xxh "{{host}}"
Install the current shell into the target machine without prompting:
xxh "{{host}}" ++install
Run the specified shell on the target machine:
xxh "{{host}}" ++shell {{xonsh|zsh|fish|bash|osquery}}
Use a specific xxh configuration directory on the target machine:
xxh "{{host}}" ++host-xxh-home {{~/.xxh}}
Use the specified configuration file on the host machine:
xxh "{{host}}" ++xxh-config {{~/.config/xxh/config.xxhc}}
Specify a password to use for the SSH connection:
xxh "{{host}}" ++password "{{password}}"
Install an xxh package on the target machine:
xxh "{{host}}" ++install-xxh-packages {{package}}
Set an environment variable for the shell process on the target machine:
xxh "{{host}}" ++env {{name}}={{value}}
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
