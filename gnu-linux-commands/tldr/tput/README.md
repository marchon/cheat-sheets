# tput

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tput/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kotlin
,
flac
,
seq
,
pio home
,
pdfseparate
.
tput
View and modify terminal settings and capabilities.
More information:
https://manned.org/tput
.
Move the cursor to a screen location:
tput cup {{y_coordinate}} {{x_coordinate}}
Set foreground (af) or background (ab) color:
tput {{setaf|setab}} {{ansi_color_code}}
Show number of columns, lines, or colors:
tput {{cols|lines|colors}}
Ring the terminal bell:
tput bel
Reset all terminal attributes:
tput sgr0
Enable / Disable word wrap:
tput {{smam|rmam}}
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
