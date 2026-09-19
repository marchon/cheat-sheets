# nohup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nohup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
x11docker
,
peco
,
img2pdf
,
ng
,
chroma
.
nohup
Allows for a process to live when the terminal gets killed.
More information:
https://www.gnu.org/software/coreutils/nohup
.
Run a process that can live beyond the terminal:
nohup {{command}} {{command_arguments}}
Launch nohup in background mode:
nohup {{command}} {{command_arguments}} &
Run a shell script that can live beyond the terminal:
nohup {{path/to/script.sh}} &
Run a process and write the output to a specific file:
nohup {{command}} {{command_arguments}} > {{path/to/output_file}} &
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
