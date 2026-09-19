# promtool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/promtool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ocamlc
,
electrum
,
watson
,
mpv
,
tcpdump
.
promtool
Tooling for the Prometheus monitoring system.
More information:
https://prometheus.io/docs/prometheus/latest/getting_started/
.
Check if the config files are valid or not (if present report errors):
promtool check config {{config_file.yml}}
Check if the rule files are valid or not (if present report errors):
promtool check rules {{rules_file.yml}}
Pass Prometheus metrics over stdin to check them for consistency and correctness:
curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics
Unit tests for rules config:
promtool test rules {{test_file.yml}}
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
