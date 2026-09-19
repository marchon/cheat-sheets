# aws-s3api

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-s3api/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
emacs
,
svgr
,
bandwhich
,
mdp
,
doctl compute droplet
.
aws s3api
Create and delete Amazon S3 buckets and edit bucket properties.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html
.
Create a bucket:
aws s3api create-bucket --bucket {{bucket_name}}
Delete a bucket:
aws s3api delete-bucket --bucket {{bucket_name}}
List buckets:
aws s3api list-buckets
List the objects inside of a bucket and only show each object's key and size:
aws s3api list-objects --bucket {{bucket_name}} --query '{{Contents[].{Key: Key, Size: Size}}}'
Add an object to a bucket:
aws s3api put-object --bucket {{bucket_name}} --key {{object_key}} --body {{path/to/file}}
Download object from a bucket (The output file is always the last argument):
aws s3api get-object --bucket {{bucket_name}} --key {{object_key}} {{path/to/output_file}}
Apply an Amazon S3 bucket policy to a specified bucket:
aws s3api put-bucket-policy --bucket {{bucket_name}} --policy file://{{path/to/bucket_policy.json}}
Download the Amazon S3 bucket policy from a specified bucket:
aws s3api get-bucket-policy --bucket {{bucket_name}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{path/to/bucket_policy}}
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
