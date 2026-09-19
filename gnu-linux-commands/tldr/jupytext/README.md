# jupytext

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jupytext/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hexo
,
speedtest
,
sendmail
,
wpa_supplicant
.
jupytext
Tool to convert Jupyter notebooks to plain text documents, and back again.
More information:
https://jupytext.readthedocs.io
.
Turn a notebook into a paired
.ipynb
/
.py
notebook:
jupytext --set-formats ipynb,py {{notebook.ipynb}}
Convert a notebook to a
.py
file:
jupytext --to py {{notebook.ipynb}}
Convert a
.py
file to a notebook with no outputs:
jupytext --to notebook {{notebook.py}}
Convert a
.md
file to a notebook and run it:
jupytext --to notebook --execute {{notebook.md}}
Update the input cells in a notebook and preserve outputs and metadata:
jupytext --update --to notebook {{notebook.py}}
Update all paired representations of a notebook:
jupytext --sync {{notebook.ipynb}}
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
