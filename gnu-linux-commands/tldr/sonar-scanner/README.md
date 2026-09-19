# sonar-scanner

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sonar-scanner/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
scan build
,
terminalizer
,
protoc
.
sonar-scanner
SonarScanner is a generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant.
More information:
https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
.
Scan a project with configuration file in your project's root directory named
sonar-project.properties
:
sonar-scanner
Scan a project using configuration file other than
sonar-project.properties
:
sonar-scanner -D{{project.settings=myproject.properties}}
Print help information:
sonar-scanner -h
Print debugging information:
sonar-scanner -X
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
