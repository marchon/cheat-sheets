# dotnet-ef

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dotnet-ef/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pg_ctl
,
tabula
,
unflatten
,
openssl x509
.
dotnet ef
Perform design-time development tasks for Entity Framework Core.
More information:
https://docs.microsoft.com/ef/core/cli/dotnet
.
Update the database to a specified migration:
dotnet ef database update {{migration}}
Drop the database:
dotnet ef database drop
List available
DbContext
types:
dotnet ef dbcontext list
Generate code for a
DbContext
and entity types for a database:
dotnet ef dbcontext scaffold {{connection_string}} {{provider}}
Add a new migration:
dotnet ef migrations add {{name}}
Remove the last migration, rolling back the code changes that were done for the latest migration:
dotnet ef migrations remove
List available migrations:
dotnet ef migrations list
Generate a SQL script from migrations range:
dotnet ef migrations script {{from_migration}} {{to_migration}}
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
