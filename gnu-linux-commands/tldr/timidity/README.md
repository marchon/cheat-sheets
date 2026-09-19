# timidity

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/timidity/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
corepack
,
gnomon
,
infection
,
tye
.
timidity
TiMidity++ is a MIDI file player and converter.
More information:
http://timidity.sourceforge.net
.
Play a MIDI file:
timidity {{path/to/file.mid}}
Play a MIDI file in a loop:
timidity --loop {{path/to/file.mid}}
Play a MIDI file in a specific key (0 = C major/A minor, -1 = F major/D minor, +1 = G major/E minor, etc.):
timidity --force-keysig={{-flats|+sharps}} {{path/to/file.mid}}
Convert a MIDI file to PCM (WAV) audio:
timidity --output-mode={{w}} --output-file={{path/to/file.wav}} {{path/to/file.mid}}
Convert a MIDI file to FLAC audio:
timidity --output-mode={{F}} --output-file={{path/to/file.flac}} {{path/to/file.mid}}
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
