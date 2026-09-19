# java

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/java/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
badblocks
,
hardhat
,
csvstat
,
bat
.
java
Java Application Launcher.
More information:
https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html
.
Execute a java
.class
file that contains a main method by using just the class name:
java {{classname}}
Execute a java program and use additional third-party or user-defined classes:
java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{classname}}
Execute a
.jar
program:
java -jar {{filename.jar}}
Execute a
.jar
program with debug waiting to connect on port 5005:
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}
Display JDK, JRE and HotSpot versions:
java -version
Display usage information for the java command:
java -help
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
