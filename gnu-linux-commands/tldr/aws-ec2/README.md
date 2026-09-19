# aws-ec2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-ec2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git flow
,
mplayer
,
standard
,
k8s unused secret detector
.
aws ec2
CLI for AWS EC2.
Provides secure and resizable computing capacity in the AWS cloud to enable faster development and deployment of applications.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html
.
Show list of all available EC2 commands:
aws ec2 help
Show help for specific EC2 subcommand:
aws ec2 {{subcommand}} help
Display information about a specific instance:
aws ec2 describe-instances --instance-ids {{instance_id}}
Display information about all instances:
aws ec2 describe-instances
Display information about all EC2 volumes:
aws ec2 describe-volumes
Delete an EC2 volume:
aws ec2 delete-volume --volume-id {{volume_id}}
Create a snapshot from an EC2 volume:
aws ec2 create-snapshot --volume-id {{volume_id}}
List available AMIs (Amazon Machine Images):
aws ec2 describe-images
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
