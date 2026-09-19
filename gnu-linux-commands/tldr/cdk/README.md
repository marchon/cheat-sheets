# cdk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cdk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git worktree
,
llvm as
,
unalias
.
cdk
A CLI for AWS Cloud Development Kit (CDK).
More information:
https://docs.aws.amazon.com/cdk/latest/guide/cli.html
.
List the stacks in the app:
cdk ls
Synthesize and print the CloudFormation template for the specified stack(s):
cdk synth {{stack_name}}
Deploy a space-separated list of stacks:
cdk deploy {{stack_name}}
Destroy a space-separated list of stacks:
cdk destroy {{stack_name}}
Compare the specified stack with the deployed stack or a local CloudFormation template:
cdk diff {{stack_name}}
Create a new CDK project in the current directory for a specified language:
cdk init -l {{language_name}}
Open the CDK API reference in your browser:
cdk doc
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
