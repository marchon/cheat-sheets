# gh-workflow

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-workflow/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bash
,
git sizer
,
scc
,
kubeadm
,
ansible vault
.
gh workflow
List, view, and run GitHub Actions workflows.
More information:
https://cli.github.com/manual/gh_workflow
.
Interactively select a workflow to view the latest jobs for:
gh workflow view
View a specific workflow in the default browser:
gh workflow view {{id|workflow_name|filename.yml}} --web
Display the YAML definition of a specific workflow:
gh workflow view {{id|workflow_name|filename.yml}} --yaml
Display the YAML definition for a specific Git branch or tag:
gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}} --yaml
List workflow files (use
--all
to include disabled workflows):
gh workflow list
Run a manual workflow with parameters:
gh workflow run {{id|workflow_name|filename.yml}} --raw-field {{param1}}={{value1}} --raw-field {{param2}}={{value2}}
Run a manual workflow using a specific branch or tag with JSON parameters from stdin:
echo '{{{"param1":"value1", "param2":"value2"}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch_or_tag_name}}
Enable or disable a specific workflow:
gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}
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
