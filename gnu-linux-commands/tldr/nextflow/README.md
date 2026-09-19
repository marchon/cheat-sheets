# nextflow

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nextflow/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
youtube dl
,
mutagen
,
gcc
,
tcpdump
.
nextflow
Tool for running computational pipelines. Mostly used for bioinformatics workflows.
More information:
https://www.nextflow.io
.
Run a pipeline, use cached results from previous runs:
nextflow run {{main.nf}} -resume
Run a specific release of a remote workflow from GitHub:
nextflow run {{user/repo}} -revision {{release_tag}}
Run with a given work directory for intermediate files, save execution report:
nextflow run {{workflow}} -work-dir {{path/to/directory}} -with-report {{report.html}}
Show details of previous runs in current directory:
nextflow log
Remove cache and intermediate files for a specific run:
nextflow clean -force {{run_name}}
List all downloaded projects:
nextflow list
Pull the latest version of a remote workflow from Bitbucket:
nextflow pull {{user/repo}} -hub bitbucket
Update Nextflow:
nextflow self-update
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
