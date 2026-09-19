# HotSpot

Cloned from https://en.wikipedia.org/wiki/HotSpot.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1800920.

HotSpot, released as Java HotSpot Performance Engine, is a Java virtual machine for desktop and server computers, developed by Sun Microsystems which was purchased by and became a division of Oracle Corporation in 2010. Its features include improved performance via methods such as just-in-time compilation and adaptive optimization. It is the de facto reference Java Virtual Machine.


== History ==
The Java HotSpot Performance Engine was released on April 27, 1999, built on technologies from an implementation of the programming language Smalltalk named Strongtalk, originally developed by Longview Technologies, which traded as Animorphic. The Longview virtual machine was based on the Self virtual machine, with an interpreter replacing the fast-and-dumb first compiler. When Sun cancelled the Self project, two key people, Urs Hölzle and Lars Bak left Sun to start Longview. In 1997, Sun Microsystems purchased Animorphic.
Shortly after acquiring Animorphic, Sun decided to write a new stronger just-in-time (JIT) compiler for the Java virtual machine, named HotSpot server compiler (internal name C2), which was initially developed by Clifford Click and was an extension of his PhD thesis on optimizing compilers. The compiler name HotSpot is derived from the software's behavior: as it runs Java bytecode, as with the Self VM, HotSpot continually analyzes the program's performance for hot spots which are executed often or repeatedly. These are then targeted for optimizing, leading to high-performance execution with a minimum of overhead for less performance-critical code. In one report, the JVM beat some C++ or C code in some benchmarks.
Initially available as an add-on for Java 1.2, HotSpot became the default Sun JVM in Java 1.3.


== Features ==
JRE (originally from Sun, now from Oracle) features two virtual machines, one called Client and the other Server. The Client version is tuned for quick loading. It makes use of interpretation. The Server version loads more slowly, putting more effort into producing highly optimized JIT compilations to yield higher performance. Both VMs compile only often-run methods, using a configurable invocation-count threshold to decide which methods to compile.
Tiered compiling, an option introduced in Java 7, uses both the client and server compilers in tandem to provide faster startup time than the server compiler, but similar or better peak performance. Starting in Java 8, tiered compilation is the default for the server VM.
HotSpot is written in C++ and Assembly. In 2007, Sun estimated it comprised approximately 250,000 lines of source code. Hotspot provides:

A Java class loader
A templating Java bytecode interpreter
Client (C1) and Server (C2) Just-in Time Compilers, optimized for their respective uses
Several garbage collectors (including the low-latency ZGC and low-pause-time Shenandoah)
A set of supporting runtime libraries
Serviceability features


=== JVM flags ===
HotSpot supports many command-line arguments for options of the virtual machine execution. Some are standard and must be found in any conforming Java virtual machine; others are specific to HotSpot and may not be found in other JVMs (options that begin with -X or -XX are non-standard).


== License ==
On 13 November 2006, the HotSpot JVM and the Java Development Kit (JDK) were licensed under the GNU General Public License (GPL) version 2. This is the code that became part of Java 7.


== Supported platforms ==


=== Maintained by Oracle ===
As with the entire Java Development Kit (JDK), HotSpot is supported by Oracle Corporation on Windows, Linux, and macOS. Supported instruction set architectures (ISAs) are x86-64 and AArch64. Since JDK 15, Solaris and SPARC are no longer supported.


=== Ports by third parties ===
Ports are also available by third parties for various other Unix operating systems. Several different hardware architectures are supported, including x86, PowerPC, and SPARC (Solaris only).
Porting HotSpot is difficult, as much of it is almost extensively written in assembly language, though several sections of it are also written in purely standards conformant ISO C++. To remedy this, the IcedTea project has developed a generic port of the HotSpot interpreter called zero-assembler Hotspot (or zero), with almost no assembly code. This port is intended for easy adaptation of the interpreter component of HotSpot to any Linux processor architecture. The code of zero-assembler Hotspot is used for all the non-x86 architecture ports of HotSpot (PowerPC, Itanium (IA-64), S390 and ARM) since version 1.6.


== See also ==

List of Java virtual machines
Comparison of Java virtual machines
Java performance
OpenJDK
Da Vinci Machine, a project to prototype the extension of the JVM to add support for dynamic programming languages


== References ==


== External links ==
Official website
A list of HotSpot VMOptions
The Java Virtual Machine Specification
History of the original Strongtalk-HotSpot team
"Sun announces availability of the Java Hotspot Performance Engine". Archived from the original on December 18, 2006. Retrieved March 27, 2014.{{cite web}}:  CS1 maint: bot: original URL status unknown (link)
HotSpot Mercurial source code development repository (version control system) for JDK8
