# mosquitto_passwd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mosquitto_passwd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
host
,
sha384sum
,
mixxx
,
git sizer
.
mosquitto_passwd
Manage password files for mosquitto.
See also
mosquitto
, the MQTT server that this manages.
More information:
https://mosquitto.org/man/mosquitto_passwd-1.html
.
Add a new user to a password file (will prompt to enter the password):
mosquitto_passwd {{path/to/password_file}} {{username}}
Create the password file if it doesn't already exist:
mosquitto_passwd -c {{path/to/password_file}} {{username}}
Delete the specified username instead:
mosquitto_passwd -D {{path/to/password_file}} {{username}}
Upgrade an old plain-text password file to a hashed password file:
mosquitto_passwd -U {{path/to/password_file}}
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
