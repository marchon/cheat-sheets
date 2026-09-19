# swagger-codegen

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/swagger-codegen/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ssh keyscan
,
qmv
,
supervisord
.
swagger-codegen
Generate code and documentation for your REST api from a OpenAPI/swagger definition.
More information:
https://github.com/swagger-api/swagger-codegen
.
Generate documentation and code from an OpenAPI/swagger file:
swagger-codegen generate -i {{swagger_file}} -l {{language}}
Generate Java code using the library retrofit2 and the option useRxJava2:
swagger-codegen generate -i {{http://petstore.swagger.io/v2/swagger.json}} -l {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}
List available languages:
swagger-codegen langs
Display help options for the generate command:
swagger-codegen help {{generate}}
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
