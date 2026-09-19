# Microsoft Foundation Class Library

Cloned from https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 291891.

Microsoft Foundation Class Library (MFC) is a C++ object-oriented library for developing desktop applications for Windows.
MFC was introduced by Microsoft in 1992 and quickly gained widespread use. While Microsoft has introduced alternative application frameworks since then, MFC remains widely used.


== History ==
MFC was introduced in 1992 with Microsoft's C/C++ 7.0 compiler for use with 16-bit versions of Windows as an extremely thin object-oriented C++ wrapper for the Windows API. C++ was just beginning to replace C for development of commercial application software at the time. Direct Windows API calls in an MFC program are rarely needed. Instead programs create objects from Microsoft Foundation Class classes and call member functions belonging to those objects. Many of those functions share their names with corresponding API functions.
One quirk of MFC is the use of "Afx" as the prefix for many functions, macros and the standard precompiled header name "stdafx.h". During early development, what became MFC was called "Application Framework Extensions" and abbreviated "Afx". The name Microsoft Foundation Classes (MFC) was adopted too late in the release cycle to change these references.
MFC 8.0 was released with Visual Studio 2005. MFC 9.0 was released with Visual Studio 2008. On April 7, 2008, Microsoft released an update to the MFC classes as an out-of-band update to Visual Studio 2008 and MFC 9. The update features new user interface constructs, including the ribbons and associated UI widgets, fully customizable toolbars, docking panes which can either be freely floated or docked to any side and document tabs.
MFC was initially a feature of the commercial versions of Visual Studio. As such, it is not included in the freeware Visual C++ Express. The Community edition of Visual Studio, introduced in 2014, however, includes MFC.
Object Windows Library (OWL), designed for use with Borland's Turbo C++ compiler, was a competing product introduced by Borland around the same time. Eventually, Borland discontinued OWL development and licensed the distribution of the MFC headers, libraries and DLLs from Microsoft for a short time, though it never offered fully integrated support for MFC. Borland later released Visual Component Library to replace the OWL framework.


== Features ==

MFC is a library that wraps portions of the Windows API in C++ classes, including functionality that enables them to use a default application framework. Classes are defined for many of the handle-managed Windows objects and also for predefined windows and common controls.
At the time of its introduction, MFC provided C++ macros for Windows message-handling (via Message Maps), exceptions, run-time type information (RTTI), serialization and dynamic class instantiation. The macros for message-handling aimed to reduce memory consumption by avoiding gratuitous virtual table use and also to provide a more concrete structure for various Visual C++-supplied tools to edit and manipulate code without parsing the full language. The message-handling macros replaced the virtual function mechanism provided by C++.
The macros for serialization, exceptions, and RTTI predated availability of these features in Microsoft C++ by a number of years. 32-bit versions of MFC, for Windows NT 3.1 and later Windows operating systems, used compilers that implemented the language features and updated the macros to simply wrap the language features instead of providing customized implementations, realizing upward compatibility.
The MFC ribbon resource editor allows the developer to design the ribbon graphically instead of having to use the XML-based declarative markup like the RibbonX API. Optionally, ribbon components may be programmed directly by calling a new set of ribbon class methods. The developer may mix graphical and programmatic ribbon development as is convenient. The MFC application wizard has also been upgraded to support the new features, including a check-box to select whether the application will use the ribbon or the docking panes. The new functionality is provided in new classes so that old applications still continue to run. This update builds on top of BCGSoft’s BCGControlBar Library Professional Edition. Microsoft has imposed additional licensing requirements on users of the ribbons. These include a requirement to adhere to Microsoft UI Design Guidelines, and an anti-competition clause prohibiting the use of the UI in applications which compete with Microsoft Office.
MFC can be used by linking a static library or by adding the MFC dynamic-link library (DLL).


== See also ==
Active Template Library (ATL)
Boost (C++ libraries)
GLib
GTK
gtkmm
JUCE
POCO C++ Libraries
Qt
Standard Template Library (STL)
Windows.h
Windows Template Library (WTL)
WxWidgets


== References ==


== Further reading ==
Jones, Richard M. (2000). Introduction to MFC programming with Visual C++. New Jersey: Prentice–Hall. ISBN 978-0-13-016629-6.
Kruglinski, David (1997). Inside Visual C++ (4 ed.). Microsoft Press. ISBN 9781572315655.
Madkour, Tarek (June 2007). "An Inside Look At The Next Generation Of Visual C++". MSDN Magazine. Vol. 22, no. 6. Microsoft. ISSN 1528-4859.
Microsoft (1995). Microsoft Visual C++: Programming with MFC (2 ed.). Microsoft Press. ISBN 9781556159213.
Murray, W. H.; Pappas, C. H. (2000). MFC Programming in C++ with the Standard Template Libraries. New Jersey: Prentice–Hall. ISBN 978-0-13-016111-6.
Prosise, Jeff (1999). Programming Windows with MFC (2 ed.). Microsoft Press. ISBN 9781572316959.
Shepherd, George (1996). MFC Internals (7 ed.). Addison–Wesley. ISBN 9780201407211.
Walnum, C.; Robichaux, P. E. (1997). Using MFC and ATL. Que. ISBN 978-0-78-970751-2.


== External links ==
The latest supported Visual C++ downloads - Microsoft
Where can I download Visual C++ Redistributables? - Microsoft
MSDN MFC Reference - Microsoft
MFC: Visual Studio 2005 and Beyond - Microsoft
