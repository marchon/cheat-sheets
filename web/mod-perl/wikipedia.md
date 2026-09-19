# Mod perl

Cloned from https://en.wikipedia.org/wiki/Mod_perl.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 224619.

mod_perl is an optional module for the Apache HTTP server. It embeds a Perl interpreter into the Apache server. In addition to allowing Apache modules to be written in the Perl programming language, it allows the Apache web server to be dynamically configured by Perl programs. However, its most common use is so that dynamic content produced by Perl scripts can be served in response to incoming requests, without the significant overhead of re-launching the Perl interpreter for each request.
Slash, which runs the web site Slashdot, is written using mod_perl.
mod_perl can emulate a Common Gateway Interface (CGI) environment, so that existing Perl CGI scripts can benefit from the performance boost without having to be re-written.
Unlike CGI (and most other web application environments), mod_perl provides complete access to the Apache API, allowing programmers to write handlers for all phases in the Apache request cycle, manipulate Apache's internal tables and state mechanisms, share data between Apache processes or threads, alter or extend the Apache configuration file parser, and add Perl code to the configuration file itself, among other things.


== See also ==

CGI.pm
FastCGI


== References ==


== External links ==
Official website
Why mod_perl?
The magic of mod_perl
Writing Apache Modules with Perl and C
The mod_perl Developer's Cookbook
mod_perl2 User's Guide 
An easy step-by-step installation guide for mod_perl2 on Unix/Linux and Windows/ReactOS
