# Apache HTTP Server

Cloned from https://en.wikipedia.org/wiki/Apache_HTTP_Server.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 2581.

The Apache HTTP Server is a free and open-source cross-platform web server, released under the terms of Apache License 2.0. It is developed and maintained by a community of developers under the auspices of the Apache Software Foundation.
The vast majority of Apache HTTP Server instances run on a Linux distribution, but current versions also run on Microsoft Windows, OpenVMS, and a wide variety of Unix-like systems. Past versions also ran on NetWare, OS/2 and other operating systems, including ports to mainframes.
Originally based on the NCSA HTTPd server, development of Apache began in early 1995 after work on the NCSA code stalled. Apache played a key role in the initial growth of the World Wide Web, It quickly overtook NCSA HTTPd as the dominant web server software for HTTP. In 2009, it became the first web server software to serve more than 100 million websites.
As of March 2025, Netcraft estimated that Apache served 17.83% of the million busiest websites, with the other top four being Cloudflare at 22.99%, nginx at 20.11%, and Microsoft Internet Information Services at 4.16%. According to W3Techs' review of all web sites, in April 2026 Apache was ranked third at 23.7% and nginx first at 32.7%, with Cloudflare Server second at 27.7%.


== Name ==
According to The Apache Software Foundation, its name was chosen "from respect for the various Native American nations collectively referred to as Apache, well-known for their superior skills in warfare strategy and their inexhaustible endurance". This was in a context in which it seemed that the open internet—based on free exchange of open source code—appeared to be soon subjected to a kind of conquer by proprietary software vendor Microsoft; Apache co-creator Brian Behlendorf—originator of the name—saw his effort somewhat parallel that of Geronimo, Chief of the last of the free Apache peoples. But it conceded that the name "also makes a cute pun on 'a patchy web server'—a server made from a series of patches".
Despite the Foundation's current claim that the name was chosen out of respect for Native Americans, previous statements, such as the project's official documentation in 1995, say that the name was instead based on a pun. This documentation did not mention Native American tribes in the context of the name:

Apache is a cute name which stuck. It was based on some existing code and a series of software patches, a pun on 'A PAtCHy' server.
In addition, Behlendorf made no reference to Native American tribes when he talked about the origins of the name in a 2000 interview, where he stated that it was not a pun, but was instead chosen to be aggressive-sounding:

The name literally came out of the blue. I wish I could say that it was something fantastic, but it was out of the blue. I put it on a page and then a few months later when this project started, I pointed people to this page and said: "Hey, what do you think of that idea?" ... Someone said they liked the name and that it was a really good pun. And I was like, "A pun? What do you mean?" He said, "Well, we're building a server out of a bunch of software patches, right? So it's a patchy Web server." I went, "Oh, all right." ... When I thought of the name, no. It just sort of connoted: "Take no prisoners. Be kind of aggressive and kick some ass."

In January 2023, the US-based non-profit Natives in Tech accused the Apache Software Foundation of cultural appropriation and urged them to change the foundation's name, and consequently also the names of the software projects it hosts. The Foundation did not change the name.
When Apache is running under Unix, its process name is httpd, which is short for "HTTP daemon".


== Feature overview ==
Apache supports a variety of features, many implemented as compiled modules which extend the core functions. These include authentication features, support for server-side programming languages such as Perl, Python, Tcl and PHP, support for Secure Sockets Layer and Transport Layer Security, proxying features, URL rewriting features, logging features, and filtering support.
Apache supports data compression to reduce the size of web pages served over HTTP. ModSecurity is an open source intrusion detecting and preventing engine for web applications. Apache logs can be analyzed through a Web browser using free scripts, such as AWStats/W3Perl or Visitors.
Virtual hosting allows one Apache installation to serve many different websites. For example, one computer with one Apache installation could simultaneously serve example.com, example.org, test47.test-server.example.edu, etc.
Apache features configurable error messages, database management system (DBMS) based authentication databases, content negotiation and supports several graphical user interfaces (GUIs).
It supports password authentication and digital certificate authentication. Because the source code is freely available, anyone can adapt the server for specific needs, and there is a large public library of Apache add-ons.
A more detailed list of features is provided below:

Loadable Dynamic Modules
Multiple Request Processing modes (MPMs) including Event-based/Async, Threaded and Prefork.
Highly scalable (easily handles more than 10,000 simultaneous connections)
Handling of static files, index files, auto-indexing and content negotiation
.htaccess per-directory configuration support
Reverse proxy with caching (module mod_proxy)
Load balancing with in-band health checks
Multiple load balancing mechanisms
Fault tolerance and Failover with automatic recovery
WebSocket, FastCGI, Simple Common Gateway Interface (SCGI), Apache JServ Protocol (AJP) and uWSGI support with caching
Dynamic configuration
Transport Layer Security (TLS/SSL) with Server Name Indication (SNI) and OCSP stapling support, via OpenSSL or wolfSSL (module mod_ssl)
Name- and IP address-based virtual servers
IPv6-compatible
HTTP/2 support
Fine-grained authentication and authorization access control (modules mod_access, mod_auth, mod_digest, mod_auth_digest) 
gzip data compression and decompression (module mod_gzip)
URL rewriting (module mod_rewrite)
Filtering (modules mod_include, mod_ext_filter)
Headers and content rewriting
Custom logging with rotation (module mod_log_config)
Concurrent connection limiting
Request processing rate limiting
Bandwidth throttling
Server Side Includes
IP address-based geolocation
User and Session tracking
WebDAV
Embedded scripting in Perl, PHP, Lua
Common Gateway Interface (CGI) support
public_html per-user web-pages
Generic expression parser
Real-time status views
FTP support (by a separate module)


== Performance ==
Instead of implementing a single architecture, Apache provides a variety of MultiProcessing Modules (MPMs) which determine how the server handles multiple connections and requests. These modules allow Apache to run in either a process-based mode, a hybrid (process and thread) mode, or an event-driven mode, in order to better match the demands of different environments. Choice of MPM and configuration is therefore important. 
For delivering static pages, Apache 2.2 series was considered significantly slower than nginx and varnish. To address this issue, the Apache developers created the Event MPM, which mixes the use of several processes and several threads per process in an asynchronous event-based loop. This architecture as implemented in the Apache 2.4 series performs at least as well as event-based web servers, according to Jim Jagielski and other independent sources. However, some independent but significantly outdated benchmarks show that it is still half as fast as nginx, e.g.


== Licensing ==
The Apache HTTP Server codebase was relicensed to the Apache 2.0 License (from the previous 1.1 license) in January 2004, and Apache HTTP Server 1.3.31 and 2.0.49 were the first releases using the new license.
The OpenBSD project did not like the change and continued the use of pre-2.0 Apache versions, effectively forking Apache 1.3.x for its purposes. They initially replaced it with nginx, and soon after made their own replacement, OpenBSD Httpd, based on the Relayd project.


=== Versions ===
Version 1.1:
The Apache License 1.1 was approved by the ASF in 2000: The primary change from the 1.0 license is in the 'advertising clause' (section 3 of the 1.0 license); derived products are no longer required to include attribution in their advertising materials, only in their documentation.
Version 2.0:
The ASF adopted the Apache License 2.0 in January 2004. The stated goals of the license included making the license easier for non-ASF projects to use, improving compatibility with GPL-based software, allowing the license to be included by reference instead of listed in every file, clarifying the license on contributions, and requiring a patent license on contributions that necessarily infringe a contributor's own patents.


== Development ==

The Apache HTTP Server Project is a collaborative software development effort aimed at creating a robust, commercial-grade, feature-rich and freely available source code implementation of an HTTP (Web) server. The project is jointly managed by a group of volunteers located around the world, using the Internet and the Web to communicate, plan, and develop the server and its related documentation. This project is part of the Apache Software Foundation. In addition, hundreds of users have contributed ideas, code, and documentation to the project.
Apache 2.4 dropped support for BeOS, TPF, A/UX, NeXT, and Tandem platforms.


== Security ==
Older versions of Apache were vulnerable to a denial-of-service attack called Slowloris, which creates many simultaneous partially completed requests, exhausting the server's pool of available connections. Since Apache 2.2.15, Apache ships the module mod_reqtimeout as the official solution supported by the developers.


== See also ==

.htaccess
.htpasswd
ApacheBench
Comparison of web server software
IBM HTTP Server
LAMP (software bundle)
XAMPP
List of Apache modules
List of free and open-source software packages
POSSE project
suEXEC
Apache Tomcat - another web server developed by the Apache Software Foundation


== References ==


== External links ==

Official website
