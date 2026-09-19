# erl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/erl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
erl
,
tput
,
dvc freeze
,
flake8
,
gh secret set
.
erl
Run and manage programs in the Erlang programming language.
More information:
https://www.erlang.org
.
Compile and run sequential Erlang program as a common script and then exit:
erlc {{files}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'
Connect to a running Erlang node:
erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}
Tell the Erlang shell to load modules from a directory:
erl -pa {{directory_with_beam_files}}
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
