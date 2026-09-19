# opusenc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/opusenc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue edit
,
openssl dgst
,
go
.
opusenc
Convert WAV or FLAC audio to Opus.
More information:
https://opus-codec.org/docs/opus-tools/opusenc.html
.
Convert WAV to Opus using default options:
opusenc {{path/to/input.wav}} {{path/to/output}}.opus
Convert stereo audio at the highest quality level:
opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output}}.opus
Convert 5.1 surround sound audio at the highest quality level:
opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output}}.opus
Convert speech audio at the lowest quality level:
opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out}}.opus
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
