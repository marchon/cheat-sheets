# pactl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pactl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
watchexec
,
keepass2
,
objdump
.
pactl
Control a running PulseAudio sound server.
More information:
https://manned.org/pactl
.
List all sinks (or other types - sinks are outputs and sink-inputs are active audio streams):
pactl list {{sinks}} short
Change the default sink (output) to 1 (the number can be retrieved via the
list
subcommand):
pactl set-default-sink {{1}}
Move sink-input 627 to sink 1:
pactl move-sink-input {{627}} {{1}}
Set the volume of sink 1 to 75%:
pactl set-sink-volume {{1}} {{0.75}}
Toggle mute on the default sink (using the special name
@DEFAULT_SINK@
):
pactl set-sink-mute {{@DEFAULT_SINK@}} toggle
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
