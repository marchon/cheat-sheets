# Db4o

Cloned from https://en.wikipedia.org/wiki/Db4o.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 21116821.

db4o (database for objects) was an embeddable open-source object database for Java and .NET developers. It was developed, commercially licensed and supported by Actian. In October 2014, Actian declined to continue to actively pursue and promote the commercial db4o product offering for new customers.


== History ==
The term object-oriented database system dates back to around 1985, though the first research developments in this area started during the mid-1970s. The first commercial object database management systems were created in the early 1990s; these added the concept of native database driven persistence into the field of object-oriented development.
The second wave of growth was observed in the first decade of the 21st century, when object-oriented databases written completely in an object-oriented language appeared on the market. db4o is one of the examples of such systems written completely in Java and C#.
The db4o project was started in 2000 by chief architect Carl Rosenberger, shipping in 2001. It was used in enterprise and academic applications prior to its commercial announcement in 2004 by newly created private company Db4objects Inc.
In 2008 db4o was purchased by Versant corporation, which marketed it as open-source bi-licensed software: commercial and the GNU General Public License (GPL).


== Overview ==
db4o represents an object-oriented database model. One of its main goals is to provide an easy and native interface to persistence for object oriented programming languages. Development with db4o database does not require a separate data model creation, the application's class model defines the structure of the data. db4o attempts to avoid the object/relational impedance mismatch by eliminating the relational layer from a software project. db4o is written in Java and .NET and provides the respective APIs. It can run on any operating system that supports Java or .NET. It is offered under licenses including GPL, the db4o Opensource Compatibility License (dOCL), and a commercial license for use in proprietary software.
Developers using relational databases can view db4o as a complementary tool. The db4o-RDBMS data exchange can be implemented using db4o Replication System (dRS). dRS can also be used for migration between object (db4o) and relational (RDBMS) technologies.
As an embedded database db4o can be run in application process. It is distributed as a library (jar/dll).


== Features ==


=== One-line-of-code database ===
db4o contains a function to store any object:

SomeClass here does not require any interface implementations, annotations or attributes added. It can be any application class including third-party classes contained in referenced libraries.
All field objects (including collections) are saved automatically. Special cases can be handled through writing custom type handlers.


=== Embeddable ===
db4o is designed to be embedded in clients or other software components invisible to the end user. Thus, db4o needs no separate installation mechanism, but comes as a single library file with a footprint of around 670kB in the .NET version and around 1MB in the Java version.


=== Client-server mode ===
Client/server version allows db4o to communicate between client and server-side applications. It uses TCP/IP for client-server communication and allows to configure port number. Communication is implemented through messaging.
Due to a feature referred to as "Generic Reflection", db4o can work without implementing persistent classes on the server. However, this mode has limitations.


=== Dynamic schema evolution ===
db4o supports automatic object schema evolution for the basic class model changes (field name deletion/addition). More complex class model modifications, like field name change, field type change, hierarchy move are not automated out-of-the box, but can be automated by writing small utility update program (see documentation).
This feature can be viewed as an advantage over relational model, where any change in the schema results in mostly manual code review and upgrade to match the schema changes.


=== Native queries ===
Rather than using string-based APIs (such as SQL, OQL, JDOQL, EJB QL, and SODA), Native Queries (NQ) allow developers to simply use the programming language itself (e.g., Java, C#, or VB.NET) to access the database and thus avoid a constant, productivity-reducing context switch between programming language and data access API. Native Queries also provide type safety, as well as remove the need to sanitize against code injection (see SQL Injection).


=== LINQ ===
LINQ support is fully integrated in db4o for .NET version 3.5. LINQ allows the creation of object-oriented queries of any complexity with the benefit of compile-time checking, IDE Intellisense integration and automated refactoring.
Due to integration with some open-source libraries db4o also allows optimized LINQ queries on Compact Framework.
LINQ can be used both against relational and object data storage, thus providing a bridge between them. It can also be used as an abstraction layer, allowing to easily switch the underlying database technology.


== Disadvantages ==
The drawbacks and difficulties faced by other Object Databases also apply to Db4o:

Other things that work against ODBMS seem to be the lack of interoperability  with a great number of tools/features that are taken for granted concerning SQL, including but not limited to industry standard connectivity, reporting tools, OLAP tools, and backup and recovery standards. Object databases also lack a formal mathematical foundation, unlike the relational model, and this in turn leads to weaknesses in their query support. However, some ODBMSs fully support SQL in addition to navigational access, e.g. Objectivity/SQL++, Matisse, and InterSystems CACHÉ. Effective use may require compromises to keep both paradigms in sync.
Disadvantages specific to Db4o may include:

Lack of full-text indexing, poor performance on full-text search
Lack of Indexing for string types, meaning text based searches can potentially be very slow
"There is no general query language like SQL which can be used for data analyzing or by other applications. This does not allow db4o to be very flexible in a heterogeneous environment"
Replication cannot be done administratively—i.e. one needs to program an application to achieve replication.  "This is contrary to most RDBMS, where administrators manage servers and replication between them."
Deleted fields are not immediately removed, just hidden until the next Defrag
No built-in support to import/export data to/from text, XML or JSON files


== Portability and cross-platform deployment ==
db4o supported Java's JDK 1.1.x through 6.0 and runs on Java EE and Java SE. db4o also runs with Java ME dialects that support reflection, such as CDC, Personal Profile, Symbian OS, SavaJe and Zaurus. Depending on customer demand, db4o will also run on dialects without reflection, such as CLDC, MIDP, BlackBerry and Palm OS.
db4o was successfully tested on JavaFX and Silverlight.
db4o ran on Android.
db4o uses a custom feature called "generic reflector" to represent class information, when class definitions are not available, which allows to use it in a mixed Java-.NET environment, for example Java client - .NET server and vice versa. Generic reflector also aids the conversion of the project between environments, as the database does not have to be converted.


== Documentation and support ==
db4o provides sources of documentation: tutorial, reference documentation, API documentation, online paircasts  and blogs. Information can also be retrieved from forums  and community additions (articles, translated documentation sources, sample projects etc.).
For commercial users db4o suggests dDN (db4o developer network) subscription with guaranteed 24-hour support and live pairing sessions with the client – Xtreme Connect.


== Object Manager ==
Object Management Enterprise (OME) is a db4o database browsing tool, which is available as a plugin to Eclipse and MS Visual Studio 2005/2008. OME allows the browsing of classes and objects in the database, connection to a database server, building queries using drag&drop and using database statistics.
OME provide some administrative functions as indexing, de-fragmentation and backup.
OME was initially suggested to customers as a commercial product only available to dDN subscribers. From the db4o version 7.8 OME was included into standard db4o distribution and the source was made available to the public in db4o svn repository.


== Versions ==
db4o releases development, production and stable builds. Development version provides the newest features and is released for testing, community feedback and evaluation. Production version is meant to be used in production environment and includes features that have been already evaluated and proven by time. Stable version is meant to be used in final product shipment.
db4o also runs a continuous build, which is triggered by any new change committed to the SVN code repository. This build is open to community and can be used to evaluate the latest changes and acquire the newest features.
db4o build name format is meant to provide all the necessary information about the version, time of build and supported platform:
For example: db4o-7.2.30.9165-java.zip
db4o – name of the product, i.e. db4o database engine
7.2 – the release number
30 – iteration number, i.e. a sequential number identifying a development week
9165 – SVN revision number, corresponding to the last commit that triggered the build
java – Java version of db4o. .NET version is identified by “net” for .NET 2.0 releases or “net35” for .NET 3.5 version. .NET version includes the corresponding Compact Framework release.
db4o public SVN repository is also available for the developers to get the source code and build versions locally with or without custom modifications.
Below is a short summary of the main features of the stable, production and development builds:


== References ==


== Further reading ==
Stefan Edlich, Jim Paterson, Henrik Hörning, Reidar Hörning, The definitive guide to db4o, Apress, 2006, ISBN 1-59059-656-0
Ted Neward, The busy Java developer's guide to db4o, (7-article series), IBM DeveloperWorks


== External links ==

Article about RETSCAN, a retina scanning system using db4o. Drdobbs.com.
