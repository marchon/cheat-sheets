# Java Database Connectivity

Cloned from https://en.wikipedia.org/wiki/Java_Database_Connectivity.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 26257672.

Java Database Connectivity (JDBC) is an application programming interface (API) for the Java programming language which defines how a client may access a database. It is a Java-based data access technology used for Java database connectivity. It is part of the Java Standard Edition platform, from Oracle Corporation. It provides methods to query and update data in a database, and is oriented toward relational databases. A JDBC-to-ODBC bridge enables connections to any ODBC-accessible data source in the Java virtual machine (JVM) host environment.


== History and implementation ==
Sun Microsystems released JDBC as part of Java Development Kit (JDK) 1.1 on February 19, 1997.
Since then it has been part of the Java Platform, Standard Edition (Java SE).
The JDBC classes are contained in the Java package java.sql and javax.sql, as well as a few other classes elsewhere. Everything involved in JDBC is exported through module java.sql.
Starting with version 3.1, JDBC has been developed under the Java Community Process. JSR 54 specifies JDBC 3.0 (included in J2SE 1.4), JSR 114 specifies the JDBC Rowset additions (for javax.sql.RowSet), and JSR 221 is the specification of JDBC 4.0 (included in Java SE 6).
JDBC 4.1, is specified by a maintenance release 1 of JSR 221 and is included in Java SE 7.
JDBC 4.2, is specified by a maintenance release 2 of JSR 221 and is included in Java SE 8.
The latest version, JDBC 4.3, is specified by a maintenance release 3 of JSR 221 and is included in Java SE 9.


== Functionality ==

Since JDBC is mostly a collection of interface definitions and specifications, it allows multiple implementations of these interfaces to exist and be used by the same application at runtime. The API provides a mechanism for dynamically loading the correct Java packages and registering them with the JDBC Driver Manager (java.sql.DriverManager). java.sql.DriverManager is used as a java.sql.Connection factory for creating JDBC connections.
JDBC connections support creating and executing statements. JDBC connections support update statements such as SQL's CREATE, INSERT, UPDATE and DELETE, or query statements such as SELECT. Additionally, stored procedures may be invoked through a JDBC connection. JDBC represents statements using one of the following classes:

Statement – the java.sql.Statement is sent to the database server each and every time. In other words, the java.sql.Statement methods are executed using SQL statements to obtain a java.sql.ResultSet object containing the data.
PreparedStatement – java.sql.PreparedStatement is a subinterface of the java.sql.Statement interface. The statement is cached and then the execution path is pre-determined on the database server, allowing it to be executed multiple times in an efficient manner. java.sql.PreparedStatement is used to execute pre-compiled SQL statements. Running pre-compiled statements increases statement execution efficiency and performance. The java.sql.PreparedStatement is often used for dynamic statement where some input parameters must be passed into the target database. The java.sql.PreparedStatement allows the dynamic query to vary depending on the query parameter.
CallableStatement – java.sql.CallableStatement is a subinterface of the java.sql.Statement interface. It is used for executing stored procedures on the database. Both input and output parameters must be passed into the database for stored procedures.
Update statements such as INSERT, UPDATE and DELETE return an update count indicating the number of rows affected in the database as an integer. These statements do not return any other information.
Query statements return a JDBC row result set. The row result set is used to walk over the result set. Individual columns in a row are retrieved either by name or by column number. There may be any number of rows in the result set. The row result set has metadata that describes the names of the columns and their types.
There is an extension to the basic JDBC API in the javax.sql.
JDBC connections are often managed via a connection pool rather than obtained directly from the driver, like javax.sql.DataSource.


== Examples ==
When a Java application needs a database connection, one of the DriverManager.getConnection() methods is used to create a JDBC java.sql.Connection. The URL used is dependent upon the particular database and JDBC driver. It will always begin with the jdbc: protocol, but the rest is up to the particular vendor.

Starting from Java SE 7, one can use Java's try-with-resources statement to simplify the above code:

Once a connection is established, a java.sql.Statement can be created.

Note that java.sql.Connections, java.sql.Statements, and java.sql.ResultSets often tie up operating system resources such as sockets or file descriptors. In the case of java.sql.Connections to remote database servers, further resources are tied up on the server, e.g. cursors for currently open java.sql.ResultSets.
It is vital to close() any JDBC object as soon as it has played its part;
garbage collection should not be relied upon.
The above try-with-resources construct is a code pattern that obviates this.
Data is retrieved from the database using a database query mechanism. The example below shows creating a statement and executing a query.

The following code is an example of a java.sql.PreparedStatement query which uses conn and class from the first example:

If a database operation fails, JDBC raises an SQLException. There is typically very little one can do to recover from such an error, apart from logging it with as much detail as possible. It is recommended that the java.sql.SQLException be translated into an application domain exception (an unchecked one) that eventually results in a transaction rollback and a notification to the user.
The following code is an example of a database transaction:

For an example of a java.sql.CallableStatement (to call stored procedures in the database), see the JDBC API Guide documentation.


== JDBC drivers ==

JDBC drivers are client-side adapters (installed on the client machine, not on the server) that convert requests from Java programs to a protocol that the DBMS can understand.


=== Types ===
Commercial and free drivers provide connectivity to most relational-database servers. These drivers fall into one of the following types:

Type 1 that calls native code of the locally available ODBC driver. (Note: In JDBC 4.2, JDBC-ODBC bridge has been removed)
Type 2 that calls database vendor native library on a client side. This code then talks to database over the network.
Type 3, the pure-java driver that talks with the server-side middleware that then talks to the database.
Type 4, the pure-java driver that uses database native protocol.
Note also a type called an internal JDBC driver - a driver embedded with JRE in Java-enabled SQL databases. It is used for Java stored procedures. This does not fit into the classification scheme above, although it would likely resemble either a type 2 or type 4 driver (depending on whether the database itself is implemented in Java or not). An example of this is the KPRB (Kernel Program Bundled) driver
supplied with Oracle RDBMS. "jdbc:default:connection" offers a relatively standard way of making such a connection (at least the Oracle database and Apache Derby support it). However, in the case of an internal JDBC driver, the JDBC client actually runs as part of the database being accessed, and so can access data directly rather than through network protocols.


=== Sources ===
Oracle provides a list of some JDBC drivers and vendors
Simba Technologies ships an SDK for building custom JDBC Drivers for any custom/proprietary relational data source
CData Software ships type 4 JDBC Drivers for various applications, databases, and Web APIs.
DataDirect Technologies provides a comprehensive suite of fast Type 4 JDBC drivers for all major database they advertise as Type 5
IDS Software provides a Type 3 JDBC driver for concurrent access to all major databases. Supported features include resultset caching, SSL encryption, custom data source, dbShield
JDBaccess is a Java persistence library for MySQL and Oracle which defines major database access operations in an easy usable API above JDBC
JNetDirect provides a suite of fully Sun J2EE certified high-performance JDBC drivers.
JDBCR4 is a service program written by Scott Klement to allow access to JDBC from RPG on the IBM i.
HSQLDB is a RDBMS with a JDBC driver and is available under a BSD license.
SchemaCrawler is an open source API that leverages JDBC, and makes database metadata available as plain old Java objects (POJOs)


== See also ==
GNU Data Access (GDA)
JDBCFacade
Open Database Connectivity (ODBC)
Object–relational mapping (ORM)


== Citations ==


== References ==
Bai, Ying (2022). SQL Server Database Programming with Java. Cham: Springer International Publishing. doi:10.1007/978-3-031-06553-8. ISBN 978-3-030-92686-1.
Horstmann, Cay (April 15, 2022). Core Java. Oracle Press Java. ISBN 978-0-13-787107-0.


== External links ==

JDBC API Guide
java.sql API Javadoc documentation
javax.sql API Javadoc documentation
O/R Broker Scala JDBC framework
SqlTool Open source, command-line, generic JDBC client utility. Works with any JDBC-supporting database.
JDBC URL Strings and related information of All Databases.
