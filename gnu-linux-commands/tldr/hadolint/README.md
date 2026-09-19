# hadolint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hadolint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ed
,
lpass
,
multipass
,
pass
,
deno
.
hadolint
Dockerfile linter.
More information:
https://github.com/hadolint/hadolint
.
Lint a Dockerfile:
hadolint {{path/to/Dockerfile}}
Lint a Dockerfile, displaying the output in JSON format:
hadolint --format {{json}} {{path/to/Dockerfile}}
Lint a Dockerfile, displaying the output in a specific format:
hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}
Lint a Dockerfile ignoring specific rules:
hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}
Lint multiple Dockerfiles using specific trusted registries:
hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile}} {{path/to/another/Dockerfile}}
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
