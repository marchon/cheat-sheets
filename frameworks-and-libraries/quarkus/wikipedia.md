# Quarkus

Cloned from https://en.wikipedia.org/wiki/Quarkus.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 64767574.

Quarkus is a Java framework optimised for resource efficiency and developer experience. Key technology components surrounding it are OpenJDK HotSpot and GraalVM. Quarkus provides developers with a unified reactive and imperative programming model to address a wider range of distributed application architectures.


== Version history ==


== Distributions ==


=== GraalVM Community Edition (CE) and GraalVM Enterprise Edition (EE) ===
GraalVM is a Java Virtual Machine for compiling and running applications written in different languages to a native machine binary. GraalVM Community Edition has varying support and licensing requirements.


=== Mandrel ===
Mandrel is a downstream distribution of GraalVM CE, supporting the same capabilities to build native executables but based on the open source OpenJDK. Mandrel aims to make GraalVM easy to consume by Quarkus applications by only including GraalVM CE components that Quarkus needs. Red Hat began commercial support for using Mandrel to build native Quarkus applications since the Quarkus 1.7 release in October 2020.


== Design pillars ==


=== Container first ===
Quarkus was designed around the container-first and Kubernetes-native philosophy, optimizing for low memory usage and fast startup times. 
As much processing as possible is done at build time, including taking a closed-world assumption approach to building and running applications. This optimization means that, in most cases, all code that does not have an execution path at runtime isn't loaded into the JVM.
In Quarkus, classes used only at application startup are invoked at build time and not loaded into the runtime JVM. Quarkus also avoids reflection as much as possible, instead favoring static class binding. These design principles aim to reduce the size, and ultimately the memory footprint, of the application running on the JVM while also enabling Quarkus to be natively-native.
Quarkus' uses the native image capability of GraalVM to compile JVM bytecode to a native machine binary. GraalVM aggressively removes any unreachable code found within the application's source code as well as any of its dependencies. Combined with Linux containers and Kubernetes, a Quarkus application runs as a native Linux executable, eliminating the JVM. 


=== Dependencies on existing libraries ===
Quarkus depends on various technologies, standards, libraries, and APIs, including contexts & dependency injection (CDI), Jax-rs, Java persistence api (JPA), Java Transaction API (JTA), Apache Camel, and Hibernate.
Quarkus is amenable to ahead-of-time compilation, as are the libraries it depends on. It also supports conventional deployment using a JVM.


== References ==


== Bibliography ==
Marc Nuri San Felix (Nov 2022). Full Stack Quarkus and React. Packt. ISBN 9781800562738
Eric Deandrea, Daniel Oh, Charles Moulliard (August 2021). Quarkus for Spring Developers 1st Edition. Red Hat Developer
John Clingan, Ken Finnigan (December 2021). Kubernetes Native Microservices With Quarkus and MicroProfile 1st Edition. Manning. ISBN 9781617298653.
Tayo Koleoso (August 26, 2020). Beginning Quarkus Framework: Build Cloud-Native Enterprise Java Applications and Microservices 1st Edition. Apress ISBN  1484260317.
Alex Soto Bueno, Jason Porter (July 14, 2020). Quarkus Cookbook: Kubernetes-Optimized Java Solutions 1st Edition. OReilly. ISBN 1492062650.
Francesco Marchioni (December 13, 2019),  Hands-On Cloud-Native Applications with Java and Quarkus: Build high performance, Kubernetes-native Java serverless applications 1st Edition. Packt. ISBN  1838821473
