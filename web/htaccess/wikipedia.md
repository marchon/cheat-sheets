# .htaccess

Cloned from https://en.wikipedia.org/wiki/.htaccess.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 554518.

A .htaccess (hypertext access) file is a directory-level configuration file supported by several web servers, used for configuration of website-access settings such as URL redirection, access control, and MIME type handling. The leading dot makes it a hidden file in Unix-like environments.
A site may contain more than one .htaccess file. The files are placed inside the web tree—inside directories and their subdirectories—which is why they are also called distributed configuration files.
Each .htaccess file acts as a local override of the server's main configuration file (such as httpd.conf) for the directory it occupies and all subdirectories beneath it.
The original purpose—reflected in the name—was per-directory access control, for example requiring a password to reach web content. In practice .htaccess files are now used to configure many other settings: content types, character encoding, CGI handlers, and URL rewriting rules.


== History ==
The .htaccess file format originated with the NCSA HTTPd server, where it was introduced to let shared-hosting users control access to their own directories without modifying the server-wide configuration. When the Apache HTTP Server project was founded in 1995 as a continuation of NCSA HTTPd, it retained the format and filename for compatibility. Other web servers, including Oracle iPlanet Web Server and the Zeus Web Server, later added .htaccess support even though their native configuration formats differ substantially.


== Format and language ==
.htaccess files use a subset of the Apache HTTP Server directive syntax, which is the same format as the server's main httpd.conf configuration file. Directives are plain-text instructions, one per line, that Apache interprets on each request.
Some directives—particularly those provided by mod_rewrite—accept regular expressions using PCRE syntax. PCRE is used only within those specific directives (such as RewriteRule and RewriteCond); it is not a property of the .htaccess format itself.
For historical reasons the format is recognized by servers such as Oracle iPlanet Web Server and Zeus Web Server, even though those servers use different native configuration formats.


== Common usage ==
Authorization and authentication
A .htaccess file commonly restricts access to a directory. It is often paired with a .htpasswd file that stores usernames and password hashes.
URL rewriting
Servers use .htaccess with mod_rewrite to rewrite long or complex URLs to shorter, more readable forms.
Access control
The Allow and Deny directives (or Require in Apache 2.4) restrict access by IP address, domain, or other criteria, and can block unwanted bots or referrers.
Server-side includes
The Options +Includes directive enables server-side include processing for a directory.
Directory listing
The Options directive controls whether the server generates an automatic index when no default document is present.
Custom error responses
The ErrorDocument directive maps HTTP error codes—such as 404 Not Found or 301 Moved Permanently—to custom pages.
MIME types
The AddType directive instructs Apache how to serve files with non-standard or missing extensions.
Cache control
.htaccess files can set Cache-Control and Expires headers via mod_headers or mod_expires, reducing bandwidth use and server load.
HTTPS and HSTS
Enforcing HTTPS on Apache typically requires RewriteRule directives and Header directives in .htaccess. Syntax errors in these rules can cause failed redirects or broken HSTS deployment.


== Advantages ==
Immediate effect
Because .htaccess files are read on every request, changes take effect immediately—unlike the main server configuration, which requires a server restart.
Non-privileged users
On shared web hosting servers, .htaccess allows individual users to adjust their own directory configuration without access to the server's main configuration files.


== Disadvantages ==
Using the main server configuration file httpd.conf is generally preferred for performance and security reasons:

Performance
Each HTTP request causes Apache to check for .htaccess files in the requested directory and every parent directory where overrides are permitted. On high-traffic servers this adds measurable filesystem overhead. Directives can be migrated from .htaccess to httpd.conf to eliminate this cost.
Security
Allowing users to modify server configuration can introduce security issues if the permitted directives are not carefully restricted.
Syntax sensitivity
Apache will return a server error (typically 500) for the entire directory if the .htaccess file contains a syntax error, making all resources in that directory inaccessible.


== See also ==
Semantic URL
Rewrite engine
httpd.conf


== References ==


== External links ==
Apache HTTP Server Tutorial: .htaccess files — official Apache documentation
