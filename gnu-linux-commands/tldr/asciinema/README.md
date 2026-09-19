# asciinema

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/asciinema/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dotnet build
,
ruby
,
kafkacat
.
asciinema
Record and replay terminal sessions, and optionally share them on asciinema.org.
More information:
https://asciinema.org/
.
Associate the local install of
asciinema
with an asciinema.org account:
asciinema auth
Make a new recording (once finished, user will be prompted to upload it or save it locally):
asciinema rec
Make a new recording and save it to a local file:
asciinema rec {{path/to/file}}.cast
Replay a terminal recording from a local file:
asciinema play {{path/to/file}}.cast
Replay a terminal recording hosted on asciinema.org:
asciinema play https://asciinema.org/a/{{cast_id}}
Make a new recording, limiting any idle time to at most 2.5 seconds:
asciinema rec -i {{2.5}}
Print the full output of a locally saved recording:
asciinema cat {{path/to/file}}.cast
Upload a locally saved terminal session to asciinema.org:
asciinema upload {{path/to/file}}.cast
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
