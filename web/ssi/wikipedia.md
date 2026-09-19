# Server Side Includes

Cloned from https://en.wikipedia.org/wiki/Server_Side_Includes.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 424381.

Server Side Includes (SSI) is a simple interpreted server-side scripting language used almost exclusively for the World Wide Web. It is most useful for including the contents of one or more files into a web page on a web server (see below), using its #include directive. This could commonly be a common piece of code throughout a site, such as a page header, a page footer and a navigation menu. SSI also contains control directives for conditional features and directives for calling external programs. It is supported by Apache, LiteSpeed, nginx, IIS as well as W3C's Jigsaw. It has its roots in NCSA HTTPd.
In order for a web server to recognize an SSI-enabled HTML file and therefore carry out these instructions, either the filename should end with a special extension, by default .shtml, .stm, .shtm, or, if the server is configured to allow this, set the execution bit of the file.


== Design ==
As a simple programming language, SSI supports only one type: text. Its control flow is rather simple, choice is supported, but loops are not natively supported and can only be done by recursion using include or using HTTP redirect. The simple design of the language makes it easier to learn and use than most server-side scripting languages, while complicated server-side processing is often done with one of the more feature-rich programming languages. SSI is Turing complete.
SSI has a simple syntax: <!--#directive parameter=value parameter=value-->. Directives are placed in HTML comments so that if SSI is not enabled, users will not see the SSI directives on the page, unless they look at its source. Note that the syntax does not allow spaces between the leading <!-- and the directive. Apache tutorial on SSI stipulates the format requires a space character before the --> that closes the element.


== Examples ==
A web page containing a daily quotation could include the quotation by placing the following code into the file of the web page:
<!--#include virtual="../quote.txt"-->
With one change of the quote.txt file, all pages that include the file will display the latest daily quotation. The inclusion is not limited to files, and may also be the text output from a program, or the value of a system variable such as the current time.


== Directives ==


=== Common ===
The following are SSI directives from the times of NCSA HTTPd (the 1990s). Some implementations do not support all of them.


=== Control directives ===
Control directives are later added to SSI. They include the ubiquitous if-elif-else-endif flow control and variable writing as well as more exotic features like loops only found in some implementations.


== See also ==
ESI (Edge Side Includes)


== Notes ==


== References ==


== External links ==
Language reference from implementations:
Apache: Apache mod_include Reference. Calls directives "elements".
Nginx: Module ngx_http_ssi_module. Calls directives "commands".
NCSA HTTPd: Original NCSA HTTPd SSI Reference. Calls directives "commands".
W3C Jigsaw: Server Side Include commands. Calls directives "elements". Highly expanded with servlets, JDBC, HTTP cookie, and loops.
Tutorials:
Apache SSI Tutorial
Plain-English Guide to SSI
SSI-Developer, Apache Server Side Includes
