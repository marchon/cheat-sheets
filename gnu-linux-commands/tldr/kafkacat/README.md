# kafkacat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kafkacat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
loadtest
,
drush
,
bzip2
,
aws
,
git delete tag
.
kafkacat
Apache Kafka producer and consumer tool.
More information:
https://github.com/edenhill/kafkacat
.
Consume messages starting with the newest offset:
kafkacat -C -t {{topic}} -b {{brokers}}
Consume messages starting with the oldest offset and exit after the last message is received:
kafkacat -C -t {{topic}} -b {{brokers}} -o beginning -e
Consume messages as a Kafka consumer group:
kafkacat -G {{group_id}} {{topic}} -b {{brokers}}
Publish message by reading from stdin:
echo {{message}} | kafkacat -P -t {{topic}} -b {{brokers}}
Publish messages by reading from a file:
kafkacat -P -t {{topic}} -b {{brokers}} {{path/to/file}}
List metadata for all topics and brokers:
kafkacat -L -b {{brokers}}
List metadata for a specific topic:
kafkacat -L -t {{topic}} -b {{brokers}}
Get offset for a topic/partition for a specific point in time:
kafkacat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}
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
