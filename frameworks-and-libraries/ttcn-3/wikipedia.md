# TTCN-3

Cloned from https://en.wikipedia.org/wiki/TTCN-3.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 16604682.

TTCN-3 (Testing and Test Control Notation version 3) is a strongly typed testing language used in conformance testing of communicating systems. TTCN-3 is written by ETSI in the ES 201 873 series, and standardized by ITU-T in the Z.160 Series.
TTCN-3 has its own data types and can be combined with ASN.1, IDL and XML type definitions.


== Standard organization ==
ITU-T TTCN-3 standard is part of the Z Series and is organized in several parts:

Z.161 - Core Language defining the core textual notation
Z.162 - Tabular presentation format (TFT) - a way to present the tests in a tabular presentation
Z.163 - Graphical presentation format (GFT) - a way to present the tests graphically with a representation that is similar to the MSC
Z.164 - Operational Semantics - Defines how TTCN-3 is executed
Z.165 - TRI - Defines the API provided and required with a tester
Z.166 - TCI - Defines the API provided and required with a test controller
Z.167 - ASN.1 - Defines how to use ASN.1 data types in a TTCN-3 test suite
Z.168 - IDL to TTCN-3 mapping
Z.169 - Using XML schema with TTCN-3


== Language organization ==
. Module: The top level container in a test suite is a module. It is usually a file.

Component
component is an execution entity. A test case or a function is executed on a component.
Port
Components communicate with each other or with the SUT through ports that are mapped to each other.
Test case
A test case is a sequence of sends and receives. When a message is sent to the SUT (System Under Test) several possibles replies can be received.
Alternative
Since a test case is a sequence of stimuli followed by a set of possible responses, the notation includes alternatives. It is a compact way to list all the possible alternatives in a scenario.
Template
When sending or receiving information the value of the parameters are of paramount importance. They must be defined when sent and they must be verified when received. The template construct aims at defining the parameters values when sent or verifying the parameter values when received. Since parameters can be quite complex, defining and verifying the values is not a matter of a single line. The template allow complex verification in a single statement so that the test case stays legible.
Verdict
The verdict is the result of a test case execution. It has 5 possible values: none, pass, inconc, fail, error.


== Applications ==
TTCN-3 has been used to define conformance test suites to SIP, WiMAX, and DSRC standard protocols.
The Open Mobile Alliance adopted in 2008 a strategy of using TTCN-3 for translating some of the test cases in an enabler test specification into an executable representation.
The AUTOSAR project promoted (2008) the use of TTCN-3 within the automotive industry.
The 3GPP project promoted the use of TTCN-3 within the mobile industry.


== Architecture ==
When executing the architecture is organized as follows:

TE: TTCN-3 Executable is the executable form of the test suite.
TRI: TTCN-3 Runtime Interface is the interface between the TE and the SUT. It is divided in 2 parts:
SA: System Adaptor
PA: Platform Adaptor
TCI: TTCN-3 Control Interfaces is the interface to control the test execution. It is divided in:
TM: Test Management
TL: Test Logging
CD: Coding and Decoding
CH: Component Handling


== Example code ==
This is a TTCN-3 example with its graphical equivalent in MSC (Message Sequence Chart).


== See also ==
TTCN
ETSI


== References ==


== External links ==
ETSI TTCN-3 web site
ETSI TTCN-3 User Conference
A video introduction to TTCN-3
TTCN-3 Quick Reference Card
List of TTCN-3 tools
Exporting of Use Case Map models (ITU-T Z.151) to TTCN-3 (ITU-T Z.161)
A history of TTCN
