# logstash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/logstash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tput
,
pdfseparate
,
nix
,
git repack
.
logstash
An Elasticsearch ETL (extract, transform and load) tool.
Commonly used to load data from various sources (such as databases and log files) into Elasticsearch.
More information:
https://www.elastic.co/products/logstash
.
Check validity of a Logstash configuration:
logstash --configtest --config {{logstash_config.conf}}
Run Logstash using configuration:
sudo logstash --config {{logstash_config.conf}}
Run Logstash with the most basic inline configuration string:
sudo logstash -e 'input {} filter {} output {}'
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
