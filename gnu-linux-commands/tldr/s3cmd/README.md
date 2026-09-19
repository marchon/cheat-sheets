# s3cmd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/s3cmd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zfs
,
bower
,
glances
,
comby
,
astyle
.
s3cmd
Command line tool and client for uploading, retrieveing and managing data in S3 compatible object storage.
More information:
https://s3tools.org/s3cmd
.
Invoke configuration/reconfiguration tool:
s3cmd --configure
List Buckets/Folders/Objects:
s3cmd ls s3://{{bucket|path/to/file}}
Create Bucket/Folder:
s3cmd mb s3://{{bucket}}
Download a specific file from a bucket:
s3cmd get s3://{{bucket_name}}/{{path/to/file}} {{path/to/local_file}}
Upload a file to a bucket:
s3cmd put {{local_file}} s3://{{bucket}}/{{file}}
Move an object to a specific bucket location:
s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}
Delete a specific object:
s3cmd rm s3://{{bucket}}/{{object}}
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
