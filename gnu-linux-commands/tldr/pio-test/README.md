# pio-test

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-test/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mkfifo
,
pdftotext
,
false
,
csvcut
.
pio test
Run local tests on a PlatformIO project.
More information:
https://docs.platformio.org/en/latest/core/userguide/cmd_test.html
.
Run all tests in all environments of the current PlatformIO project:
pio test
Test only specific environments:
pio test --environment {{environment1}} --environment {{environment2}}
Run only tests whose name matches a specific glob pattern:
pio test --filter "{{pattern}}"
Ignore tests whose name matches a specific glob pattern:
pio test --ignore "{{pattern}}"
Specify a port for firmware uploading:
pio test --upload-port {{upload_port}}
Specify a custom configuration file for running the tests:
pio test --project-conf {{path/to/platformio.ini}}
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
