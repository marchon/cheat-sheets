# Griffon (framework)

Cloned from https://en.wikipedia.org/wiki/Griffon_(framework).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 19285693.

Griffon is an open source rich client platform framework which uses the Java, Apache Groovy, and/or Kotlin programming languages. Griffon is intended to be a high-productivity framework by rewarding use of the Model-View-Controller paradigm, providing a stand-alone development environment and hiding much of the configuration detail from the developer.
The first release is the fruit of the effort by the Groovy Swing team and an attempt to take the best of rapid application development, as indicated by its Grails-like structure, the agility of Groovy, and the availability of components for Swing. The framework was redesign from scratch for version 2, allowing different JVM programming languages to be used either in isolation or in conjunction. Supported UI toolkits are

Java Swing
JavaFX
Apache Pivot
Lanterna


== Overview ==

Griffon aims to reduce the typical confusion that occurs with traditional Java UI development. Due to the MVC structure of Griffon, developers never have to go searching for files or be confused on how to start a new project. Everything begins with:

lazybones create <template_name> <APP_NAME>

The generated project follows this structure:

%PROJECT_HOME%
    + griffon-app
       + conf                 ---> location of configuration artifacts like builder configuration
       + controllers          ---> location of controller classes
       + i18n                 ---> location of message bundles for i18n
       + lifecycle            ---> location of lifecycle scripts
       + models               ---> location of model classes
       + resources            ---> location of non code resources (images, etc)
       + views                ---> location of view classes
   + src
       + main                 ---> optional; location for Groovy and Java source files
                                   (of types other than those in griffon-app/*)

The builder infrastructure enables seamless integration of different widget libraries such as Swing, JIDE, and SwingX.
In the first release, three sample applications are included :

Greet, a Groovy Twitter client featured in the JavaOne 2009 Script Bowl,
FontPicker, an application to view the available fonts on one's machine,
SwingPad, a lightweight designer application for Griffon user interfaces.


== Plugins ==
Griffon can be extended with the use of plugins. Plugins provide run-time access to testing libraries such as Easyb and FEST, and all widget libraries besides core Swing are provided as plugins. The plugin system allows for a wide range of additions, for example

Polyglot Programming with Java, Apache Groovy, Kotlin.
SQL and NoSQL datastores like Berkleydb, CouchDB, Db4O, Neo4j, NeoDatis, Memcached and Riak.


== Publications ==


=== Books ===
Features that would eventually become integral parts of Griffon (UI builders) were featured in these books:

Groovy In Action (published by Manning)
Beginning Groovy and Grails
Books that cover Griffon:

Griffon In Action (published by Manning)
Beginning Groovy, Grails and Griffon


=== Magazine ===
GroovyMag for Groovy and Grails developers


== See also ==

Agile software development


== References ==


== External links ==
Griffon Home Page
