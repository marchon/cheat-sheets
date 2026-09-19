# hyperfine

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hyperfine/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clojure
,
luac
,
nix
,
basename
,
exrex
.
hyperfine
A command-line benchmarking tool.
More information:
https://github.com/sharkdp/hyperfine/
.
Run a basic benchmark, performing at least 10 runs:
hyperfine '{{make}}'
Run a comparative benchmark:
hyperfine '{{make target1}}' '{{make target2}}'
Change minimum number of benchmarking runs:
hyperfine --min-runs {{7}} '{{make}}'
Perform benchmark with warmup:
hyperfine --warmup {{5}} '{{make}}'
Run a command before each benchmark run (to clear caches, etc.):
hyperfine --prepare '{{make clean}}' '{{make}}'
Run a benchmark where a single parameter changes for each run:
hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'
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
