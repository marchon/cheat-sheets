# az-pipelines

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-pipelines/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
screen
,
gh pr create
,
fnm
,
gdrive
.
az pipelines
Manage Azure Pipelines resources.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/pipelines
.
Create a new Azure Pipeline (YAML based):
az pipelines create --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}
Delete a specific pipeline:
az pipelines delete --org {{organization_url}} --project {{project_name}} --id {{pipeline_id}}
List pipelines:
az pipelines list --org {{organization_url}} --project {{project_name}}
Enqueue a specific pipeline to run:
az pipelines run --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}
Get the details of a specific pipeline:
az pipelines show --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}
Update a specific pipeline:
az pipelines update --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}
Get a list of agents in a pool:
az pipelines agent list --org {{organization_url}} --pool-id {{agent_pool}}
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
