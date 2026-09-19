# mpg321

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mpg321/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ogrmerge.py
,
loc
,
valgrind
,
ledger
.
mpg321
High Performance MPEG 1.0/2.0/2.5 Audio Player for Layer 1, 2, and 3.
Mpg321 was written (sometime in 1999) to be a drop-in replacement for the (previously) non-free mpg123 player.
More information:
http://mpg321.sourceforge.net/
.
Play an audio source exactly N times (N=0 means forever):
mpg321 -l {{N}} {{path/to/file_a|URL}} {{path/to/file_b|URL}} {{...}}
Play a directory recursively:
mpg321 -B {{path/to/directory}}
Enable Basic Keys (
*
or
/
- Increase or decrease volume,
n
- Skip song,
m
- Mute/unmute.) while playing:
mpg321 -K {{path/to/file_a|URL}} {{path/to/file_b|URL}} {{...}}
Play files randomly until interrupted:
mpg321 -Z {{path/to/file_a|URL}} {{path/to/file_b|URL}} {{...}}
Shuffle the files before playing them once:
mpg321 -z {{path/to/file_a|URL}} {{path/to/file_b|URL}} {{...}}
Play all files in the current directory and subdirectories, randomly (until interrupted), with Basic Keys enabled:
mpg321 -B -Z -K .
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
