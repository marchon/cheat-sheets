# rtl_sdr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rtl_sdr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws cur
,
inkview
,
streamlink
.
rtl_sdr
Raw data recorder for RTL-SDR receivers.
Data is encoded using I/Q sampling (aka quadrature sampling).
More information:
https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr
.
Save RAW data from a frequency (specified in Hz) to a file:
rtl_sdr -f {{100000000}} {{path/to/file}}
Pipe data to another program:
rtl_sdr -f {{100000000}} - | {{aplay}}
Read a specified number of samples:
rtl_sdr -f {{100000000}} -n {{20}} -
Specify the sample rate in Hz (ranges 225001-300000 and 900001-3200000):
rtl_sdr -f {{100000000}} -s {{2400000}} -
Specify the device by its index:
rtl_sdr -f {{100000000}} -d {{0}} -
Specify the gain:
rtl_sdr -f {{100000000}} -g {{20}} -
Specify the output block size:
rtl_sdr -f {{100000000}} -b {{9999999}} -
Use synchronous output:
rtl_sdr -f {{100000000}} -S -
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
