# sbt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sbt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws s3
,
git locked
,
rga
,
convmv
.
sbt
Build tool for Scala and Java projects.
More information:
https://www.scala-sbt.org/1.x/docs/
.
Start a REPL (interactive shell):
sbt
Create a new Scala project from an existing Giter8 template hosted on GitHub:
sbt new {{scala/hello-world.g8}}
Compile and run all tests:
sbt test
Delete all generated files in the
target
directory:
sbt clean
Compile the main sources in
src/main/scala
and
src/main/java
directories:
sbt compile
Use the specified version of sbt:
sbt -sbt-version {{version}}
Use a specific jar file as the sbt launcher:
sbt -sbt-jar {{path}}
List all sbt options:
sbt -h
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
