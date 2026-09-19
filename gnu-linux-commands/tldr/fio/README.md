# fio

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fio/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xdelta
,
llc
,
mktemp
,
gibo
,
pdfseparate
.
fio
Flexible I/O tester.
Tool that will spawn a number of threads or processes doing a particular type of I/O action.
More information:
https://fio.readthedocs.io/en/latest/fio_doc.html
.
Test random reads:
sudo fio --filename={{path/to/file}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly
Test sequential reads:
sudo fio --filename={{path/to/file}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly
Test random read/write:
sudo fio --filename={{path/to/file}} --size=500GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1
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
