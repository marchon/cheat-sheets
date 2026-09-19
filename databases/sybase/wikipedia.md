# Adaptive Server Enterprise

Cloned from https://en.wikipedia.org/wiki/Adaptive_Server_Enterprise.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 295744.

SAP ASE (Adaptive Server Enterprise), originally known as Sybase SQL Server, and also commonly known as Sybase DB or Sybase ASE, is a relational model database server developed by Sybase Corporation, which later became part of SAP SE. ASE was developed for the Unix operating system, and is also available for Microsoft Windows.
In 1988, Sybase, Microsoft and Ashton-Tate began development of a version of SQL Server for OS/2, but Ashton-Tate later left the group and Microsoft went on to port the system to Windows NT. When the agreement expired in 1993, Microsoft purchased a license for the source code and began to sell this product as Microsoft SQL Server. MS SQL Server and Sybase SQL Server share many features and syntax peculiarities.


== History ==
Bob Epstein left Britton Lee, Inc. to help found Sybase and carried a lot of the ideas from the hardware database with him, reasoning that standard hardware such as Intel, Motorola and Sun 32 and 64 bit processors running database software could advance much more rapidly than specialist hardware. 
Originally developed for Unix operating system platforms in 1987, Sybase Corporation's primary relational database management system product was initially marketed under the name Sybase SQL Server. Microsoft's Bill Gates praised it as the world's best SQL database engine; in 1988, SQL Server for OS/2 was co-developed for the PC by Sybase, Microsoft, and Ashton-Tate.  Ashton-Tate divested its interest and Microsoft became the lead partner after porting SQL Server to Windows NT.  Microsoft and Sybase sold and supported the product through version 4.2.1.
The key feature that made SQL Server attractive from the start was its high performance due to shared log writes, clustered indexes and a small memory footprint per user. As a result of these and other design features it performed well "out of the box".
Sybase released SQL Server 4.2 in 1992.  This release included internationalization and localization and support for symmetric multiprocessing systems.
In 1993, the co-development licensing agreement between Microsoft and Sybase ended, and the companies parted ways after an amicable solution was reached. Sybase wanted to develop on the Intel Unix platform and Microsoft wanted Windows specific solutions. As part of the agreement Sybase released the System 10 codeline to Microsoft and Microsoft gave up exclusive rights to Intel platforms. Both continuing to independently develop their respective versions of SQL Server. Sybase released Sybase SQL Server 10.0, which was part of the System 10 product family, which also included Back-up Server ( a very high performance parallel backup process), Replication Server ( to provide replicate sites), Navigation Server ( a shared nothing parallel server), Open Client/Server APIs, SQL Monitor, SA Companion and OmniSQL Gateway. Microsoft continued on with Microsoft SQL Server.
Sybase provides native low-level programming interfaces to its database server which uses a protocol called Tabular Data Stream. Prior to version 10, DBLIB (DataBase LIBrary) was used. Version 10 and onwards uses CTLIB (ClienT LIBrary).
In 1995, Sybase released SQL Server 11.0.
Starting with version 11.5 released in 1996, Sybase moved to differentiate its product from Microsoft SQL Server by renaming it to Adaptive Server Enterprise.
Sybase 11.5 added Asynchronous prefetch, case expression in sql, the optimizer can use a descending index to avoid the need for a worktable and a sort.
The Logical Process Manager was added to allow prioritization by assigning execution attributes and engine affinity.
In 1998, ASE 11.9.2 was rolled out with support for data pages locking, data rows (row-level locking), distributed joins and improved SMP performance. Indexes could now be 
created in descending order on a column, readpast concurrency option and repeatable read transaction isolation were added. A lock timeout option and task-to-engine affinity were added, 
query optimization is now delayed until a cursor is opened and the values of the variables are known.
In 1999, ASE 12.0 was released, providing support for Java, high availability and distributed transaction management. Merge joins were added, previous all joins were nested loop joins. In addition, cache partitions were added to improve performance.
In 2001, ASE 12.5 was released, providing features such as dynamic memory allocation, an EJB container, support for XML, Secure Sockets Layer (SSL) and LDAP. Also added was compressed backups, unichar UTF-16 support and multiple logical page sizes 2K, 4K, 8K, or 16K.
In 2005, Sybase released ASE 15.0. It included support for partitioning table rows in a database across individual disk devices, and "virtual columns" which are computed only when required. In ASE 15.0, many parameters that had been static (which required server reboot for the changes to take place) were made dynamic (changes take effect immediately). This improved performance and reduced downtime. For example, one parameter that was made dynamic was the "tape retention in days" (the number of days that the backup is kept on the tape media without overwriting the existing contents in the production environment).
On January 27, 2010, Sybase released ASE 15.5. It included support for in-memory and relaxed-durability databases, distributed transaction management in the shared-disk cluster, faster compression for backups as well as Backup Server Support for the IBM Tivoli Storage Manager. Deferred name resolution for user-defined stored procedures, FIPS 140-2 login password encryption, incremental data transfer, bigdatetime and bigtime datatypes and tempdb groups were also added.
In July 2010, Sybase became a wholly owned subsidiary of SAP America. On September 13, 2011, Sybase released ASE 15.7 at Techwave. It included support for: New Security features - Application Functionality Configuration Groups, a new threaded kernel, compression for large object (LOB) and regular data, End-to-End CIS Kerberos Authentication, Dual Control of Encryption Keys and Unattended Startup and extension for securing logins, roles, and password management, Login Profiles, ALTER... modify owner, External Passwords and Hidden Text, Abstract Plans in Cached Statements, Shrink Log Space, In-Row Off-Row LOB, using Large Object text, unitext, and image Datatypes in Stored Procedures, Using LOB Locators in Transact-SQL Statements, select for update to exclusively lock rows for subsequent updates within the same transaction, and for update-able cursors, Non-materialized, Non-null Columns with a default value, Fully Recoverable DDL (select into, alter table commands that require data movement, reorg rebuild), merge command, Expanded Variable-Length Rows, Allowing Unicode Noncharacters.
In April 2014, SAP released ASE 16. It included support for partition locking, CIS Support for HANA, Relaxed Query Limits, Query Plan Optimization with Star Joins, Dynamic Thread Assignment, Sort and Hash Join Operator improvements, Full-Text Auditing, Auditing for Authorization Checks Inside Stored Procedures, create or replace functionality, Query Plan and Execution Statistics in HTML, Index Compression, Full Database Encryption, Locking, Run-time locking, Metadata and Latch enhancements, Multiple Trigger support, Residual Data Removal, Configuration History Tracking, CRC checks for dump database and the ability to calculate the transaction log growth rate for a specified time period.


== Structure ==
A single standalone installation of ASE typically comprises one "dataserver" and one corresponding "backup server". In multi server installation many dataservers can share one  backup server. A dataserver consists of system databases and user databases. Minimum system databases that are mandatory for normal working of dataserver are 'master', 'tempdb', 'model', 'sybsystemdb' and 'sybsystemprocs'. 'master' database holds critical system related information that includes, logins, passwords, and dataserver configuration parameters. 'tempdb' is used for storage of data that are required for intermediate processing of queries, and temporary data. 'model' is used as a template for creating new databases. 'sybsystemprocs' consists of system supplied stored procedures that queries system tables and manipulates data in them.
ASE is a single process multithreaded dataserver application.


== Editions ==
SAP ASE currently has two "editions", "Enterprise edition" and "Platform edition".  The "Platform edition" includes licenses enabling several unspecified features (probably the newer, in memory high performance options and the disaster recovery functionality (near synchronous replication to a hot spare)) 
The "express edition" (used to be free, but limited to four server engines and 50 GB of disk space per server) is no longer available after version 16.0 SP03.  There was no public statement about this, but it is documented in SAP note 3231519.  Instead of the express edition, a 90 day trial version of ASE is available 


== Optional Features Requiring Additional Licenses ==
As per: SAP ASE docs -> Installation and Upgrade Guide for os_type -> Licensing Your Software -> Knowing the Product License Type -> Optional Feature Licenses there are the following optional ASE features each requiring a separate type of license:

Database MemScale - The MemScale option is a licensed option introduced in SAP ASE version 16.0 SP02 as part of the SQL Server Administration group. This option includes various features, including:
Compiled queries (simplified native access plans)
Transactional memory
Latch-free indexes
In-memory row storage (IMRS) of "hot" rows.  Writes to these rows go only to memory.  I.e., it's not just a disk cache.
In Memory Database - Includes the option to flush the data to disk on polite shutdown and, if successfully flushed, restore data from disk to the memory db on startup (can be time consuming)
Always-on - A high availability (HA) disaster recovery (DR) solution using synchronous or near-synchronous replication of an ASE database server (implemented using the SAP Replication Server)
Workload Analyzer - Enables the capture, analysis, and replay of a production workload non-disruptively and enables the user to utilize the captured workload to diagnose problems and understand and manage configuration changes proactively.
Security and Directory Services - Provides lightweight directory services and network-based authentication and encryption using SSL and Kerberos.
Encrypted Columns - Increases security parameters and allows for addition of datatypes.
Partitions - Enables semantic partitioning for table row data.
Active Messaging - Send or receive messages to a queue using JMS (Java Message Service/Jakarta Messaging) and MQ (IBM messaging) technologies.
Compression
Tivoli Storage Manager (TSM) - Enables the database to back up and restore operations to IBM Tivoli Storage Manager.


== See also ==
SQL Anywhere
Sybase
List of relational database management systems
Comparison of relational database management systems


== References ==


== External links ==
SAP Sybase ASE official website
SAP Sybase ASE online documentation
SAP ASE Community
What's New from 15.7 to 16.0.3.7
