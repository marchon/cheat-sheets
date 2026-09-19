# FitNesse

Cloned from https://en.wikipedia.org/wiki/FitNesse.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 2305988.

FitNesse is a web server, a wiki and an automated testing tool for software. It is based on Ward Cunningham's Framework for Integrated Test and is designed to support acceptance testing rather than unit testing in that it facilitates detailed readable description of system function.
FitNesse allows users of a developed system to enter specially formatted input (its format is accessible to non-programmers). This input is interpreted, and tests are created automatically. These tests are then executed by the system and output is returned to the user. 
The advantage of this approach is very fast feedback from users. The developer of the system to be tested needs to provide some support (classes named "fixtures", conforming to certain conventions).
FitNesse is written in Java (by Micah Martin with help from Robert C. Martin and others). The program first supported only Java, but versions for several other languages have been added over time (C++, Python, Ruby, Delphi, C#, etc.).


== Principles of FitNesse ==


=== FitNesse as a testing method ===
FitNesse was originally designed as a highly usable interface around the Fit framework. As such its intention is to support an agile style of black-box testing acceptance and regression testing. In this style of testing the functional testers in a software development project collaborate with the software developers to develop a testing suite.
FitNesse testing is based around the notion of black-box testing, in which a system under test is considered to be a black box and is tested in terms of the outputs generated in response to predetermined inputs. A functional tester is responsible for designing the tests in a functional sense and expressing them within the FitNesse tool, whereas the software developer is responsible for connecting the FitNesse tool to the system under test so that FitNesse can execute the test and compare the actual output to the expected output.
The idea behind this testing method, as described in Fit for Developing Software, is that the forced collaboration of testers and developers will improve mutual understanding of the system and requirements by forcing the two groups to develop a common language as they learn to communicate together.


=== FitNesse as a testing tool ===
Tests are described in Fitnesse as couplings of inputs and expected outputs. These couplings are expressed variations of a decision table. The FitNesse tool supports several of these variations, ranging from literal decision tables to tables that execute queries to tables that express testing scripts (i.e. a literal ordering of steps that must be followed to reach a result). The most generic form is a fully free-form table that can be interpreted in any way the test designers like. All tests are expressed in the shape of some sort of table, however.
FitNesse is focused entirely on easily creating tests, allowing testers and developers to focus on creating high-quality tests rather than getting lost in the mechanics of executing a test. Given the way FitNesse works, creating tests easily involves three factors:

Creating tables easily.
Easily translating tables into calls to the system under test.
Allowing ease and flexibility in documenting tests.
In order to meet these requirements, FitNesse leverages the wiki mechanism. Wikis classically allow for the easy and rapid creation of HTML pages and particularly simplify the expression of tables. These qualities make the basic WikiWiki language an ideal choice for a "user interface" for FitNesse: on the one hand it allows for the simple expression of very free-form tables, on the other hand it limits the contents of those tables to rather simple text. 
This means that the WikiWiki language can handle whatever shape of table is required for a particular test and at the same time limits the contents of those tables to alphanumeric text that can easily be mapped into a call to a piece of software. Finally, since each test in FitNesse is a wiki page it is possible to embed each testing table within wiki text; this allows a functional tester to include descriptive text with a reasonable layout quickly.


=== FitNesse as a software tool ===
FitNesse is a tool developed in Java and shipped as a single, executable jar file. The executable includes a wiki engine, an embedded web server, a testing engine and all the resources (images, stylesheets and so on) required to create a web site in FitNesse's own style.
FitNesse is focused very much on ease of use as a testing tool. As such it ships with all required components on board: upon execution the tool launches an embedded web server which allows test pages to be exposed locally or across the Internet with equal ease. The embedded server is quite lightweight and can be run from a laptop as well as full server machine.
Upon launch the tool deploys its own Wiki engine into its embedded server. This Wiki engine is similarly focused on simplicity, meaning that it does not require a backing database to run — it simply creates a file-based collection of wiki pages which are interpreted by the Wiki engine and served by the embedded web server. 
The default wiki created by the tool includes the FitNesse user guide and some examples. The default document repository is created complete with everything needed to publish a default wiki in the FitNesse style (that is, all the images, stylesheets, JavaScript files and so on are created together with the basic wiki page repository).
The wiki engine is quite basic but offers all the basic facilities common among wiki engines: a search engine, revision history per page and a file overview. It also offers some refactoring operations that allow for deleting, moving and renaming files. In addition, the wiki engine offers some test-specific facilities, such as standard buttons to run tests, ways of defining individual test pages and suites of tests and a historic overview of test results for trend analysis. Finally, the engine offers some minor security facilities for locking pages and securing access to the wiki.


== Test execution ==
Testing within the FitNesse system involves four components per test:

The wiki page which expresses the test as a decision table.
A testing engine, which interprets the wiki page.
A test fixture, which is invoked by the testing engine and in turn invokes the system under test.
The system under test, which is being tested.
Of these components the software development team produces two: the wiki page and the fixture (of course it also produces the system under test, but from the point of view of the black-box test only two). The wiki page includes some form of decision table which expresses a test. For example, it might express tests for a component that performs division (the example is based on the one given in the FitNesse Two Minute Example):

The link between the generic testing engine and the system under test is made by a piece of Java code called a fixture. In the case of the table above this code might look like this:

The mapping between the wiki page and the fixture is a straightforward convert-to-camel case mapping. This mapping applies to all table headings and is used to identify the name of the fixture class as well as the methods of the fixture. A heading ending in a question mark is interpreted as a value to be read from the fixture, other headers are considered inputs to the fixture. Methods of the fixture are called in column order of the decision table, from left to right.


=== Testing engines ===
The actual mapping as described above (as well as the invocation of fixture methods) is done by a testing engine. FitNesse supports two of these engines: the Fit engine and the SLIM engine.


==== Fit ====
More than an engine, Fit is a testing framework unto itself. It combines functionality to invoke tests, interpret wiki pages and generate output pages. FitNesse was originally built around Fit as a user interface, which inspired the name of the tool.
Fit is a framework that combines many responsibilities in testing rather than separating responsibilities neatly. The software developer pays a price for this fact in that fixtures for the Fit engine must inherit from Fit framework base classes. This can be inconvenient in Java, as it means that the framework claims a developer's one chance at class inheritance. It also means that a fixture, by its nature, is a heavyweight construct. These considerations have prompted the FitNesse team in recent years to move to the SLIM testing engine.


==== SLIM ====
SLIM (Simple List Invocation Method) is an alternative to Fit.
The SLIM engine is an implementation of the Slim Protocol Archived 2014-12-06 at the Wayback Machine. Rather than combining all the elements of wiki-based testing, the SLIM engine concentrates only on invoking the fixture; it runs as a separate server which is invoked remotely by the FitNesse wiki engine. The interpretation of the wiki page and the generation of the result page is now part of the wiki engine.
The SLIM engine allows for far more light-weight fixtures which are simple POJOs. These fixtures are not required to extend or use any framework classes, which simplifies their design and allows the fixture designer to concentrate on calling the system under test properly and in the simplest way possible. It also keeps the inheritance route open, allowing fixture developers to create fixture hierarchies if necessary.


== See also ==
Acceptance test-driven development
Specification by example
Acceptance testing (also referred to as functional testing)
Software performance testing
Regression testing
Watir
StoryTestIQ (STIQ) a mash-up of Selenium and the Fitness wiki (Please note: Wiki does not exist anymore (deleted in 2009), left here for reference only)


== Bibliography ==
Fit for Developing Software: Framework for Integrated Tests by Rick Mugridge; Ward Cunningham (ISBN 978-0-321-26934-8) published by Prentice Hall in June 2005
Test Driven .NET Development with FitNesse by Gojko Adzic (ISBN 978-0-9556836-0-2) published by Neuri Limited (February 28, 2008)
Phillip A. Laplante: Requirements Engineering for Software and Systems, Auerbach Publications, Boca Raton, FL, 2009, pp. 166–167, ISBN 978-1420064674


== References ==


== External links ==
Tool website
Source Repository
Languages supported by FitNesse
Discussion group dedicated to FitNesse[link removed]
FitNesse presentation
