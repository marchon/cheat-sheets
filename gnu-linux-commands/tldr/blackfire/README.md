# blackfire

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/blackfire/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gunicorn
,
speedcrunch
,
ipaggcreate
.
blackfire
A command-line profiling tool for PHP.
More information:
https://blackfire.io
.
Initialize and configure the Blackfire client:
blackfire config
Launch the Blackfire agent:
blackfire agent
Launch the Blackfire agent on a specific socket:
blackfire agent --socket="{{tcp://127.0.0.1:8307}}"
Run the profiler on a specific program:
blackfire run {{php path/to/file.php}}
Run the profiler and collect 10 samples:
blackfire --samples={{10}} run {{php path/to/file.php}}
Run the profiler and output results as JSON:
blackfire --json run {{php path/to/file.php}}
Upload a profiler file to the Blackfire web service:
blackfire upload {{path/to/file}}
View the status of profiles on the Blackfire web service:
blackfire status
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
