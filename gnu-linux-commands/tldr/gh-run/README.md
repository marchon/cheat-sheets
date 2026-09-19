# gh-run

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-run/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gitlab runner
,
dog
,
godot
,
expand
.
gh run
View, run and watch recent GitHub Actions workflow runs.
More information:
https://cli.github.com/manual/gh_run
.
Interactively select a run to see information about the jobs:
gh run view
Display information about a specific run:
gh run view {{workflow_run_number}}
Display information about the steps of a job:
gh run view --job={{job_number}}
Display the log of a job:
gh run view --job={{job_number}} --log
Check a specific workflow and exit with a non-zero status if the run failed:
gh run view {{workflow_run_number}} --exit-status && {{echo "run pending or passed"}}
Interactively select an active run and wait until it's done:
gh run watch
Display the jobs for a run and wait until it's done:
gh run watch {{workflow_run_number}}
Re-run a specific workflow:
gh run rerun {{workflow_run_number}}
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
