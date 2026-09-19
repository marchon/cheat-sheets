# aws-ecr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-ecr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git format patch
,
pueue group
.
aws ecr
Push, pull, and manage container images.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html
.
Authenticate Docker with the default registry (username is AWS):
aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com
Create a repository:
aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}
Tag a local image for ECR:
docker tag {{container_name}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}
Push an image to a repository:
docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}
Pull an image from a repository:
docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}
Delete an image from a repository:
aws ecr batch-delete-image  --repository-name {{repository}} --image-ids imageTag={{latest}}
Delete a repository:
aws ecr delete-repository --repository-name {{repository}} --force
List images within a repository:
aws ecr list-images --repository-name {{repository}}
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
