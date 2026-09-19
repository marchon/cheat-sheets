# hive

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hive/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ts
,
dict
,
darkhttpd
,
jhat
,
phpdox
.
hive
CLI tool for Apache Hive.
More information:
https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli
.
Start a Hive interactive shell:
hive
Run HiveQL:
hive -e "{{hiveql_query}}"
Run a HiveQL file with a variable substitution:
hive --define {{key}}={{value}} -f {{path/to/file.sql}}
Run a HiveQL with HiveConfig (e.g.
mapred.reduce.tasks=32
):
hive --hiveconf {{conf_name}}={{conf_value}}
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
