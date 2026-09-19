# pgbench

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pgbench/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
printf
,
lein
,
doctl account
,
nix env
.
pgbench
Run a benchmark test on PostgreSQL.
More information:
https://www.postgresql.org/docs/10/pgbench.html
.
Initialize a database with a scale factor of 50 times the default size:
pgbench --initialize --scale={{50}} {{database_name}}
Benchmark a database with 10 clients, 2 worker threads, and 10,000 transactions per client:
pgbench --client={{10}} --jobs={{2}} --transactions={{10000}} {{database_name}}
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
