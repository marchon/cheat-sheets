# ldapsearch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ldapsearch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nvm
,
pdftotext
,
tlmgr
,
llvm dis
.
ldapsearch
CLI utility for querying an LDAP directory.
More information:
https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html
.
Query an LDAP server for all items that are a member of the given group and return the object's displayName value:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName
Query an LDAP server with a no-newline password file for all items that are a member of the given group and return the object's displayName value:
ldapsearch -D '{{admin_DN}}' -y '{{password_file}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName
Return 5 items that match the given filter:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -z 5 displayName
Wait up to 7 seconds for a response:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -l 7 displayName
Invert the filter:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '(!(memberOf={{group1}}))' displayName
Return all items that are part of multiple groups, returning the display name for each item:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"
Return all items that are members of at least 1 of the specified groups:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName
Combine multiple boolean logic filters:
ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName
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
