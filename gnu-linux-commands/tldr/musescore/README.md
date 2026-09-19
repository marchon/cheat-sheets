# musescore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/musescore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
moro
,
lt
,
gh screensaver
,
docker compose
.
musescore
MuseScore 3 sheet music editor.
More information:
https://musescore.org/en/handbook/3/command-line-options
.
Use a specific audio driver:
musescore --audio-driver {{jack|alsa|portaudio|pulse}}
Set the MP3 output bitrate in kbit/s:
musescore --bitrate {{bitrate}}
Start MuseScore in debug mode:
musescore --debug
Enable experimental features, such as layers:
musescore --experimental
Export the given file to the specified output file. The file type depends on the given extension:
musescore --export-to {{output_file}} {{input_file}}
Print a diff between the given scores:
musescore --diff {{path/to/file1}} {{path/to/file2}}
Specify a MIDI import operations file:
musescore --midi-operations {{path/to/file}}
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
