# VBScript

Cloned from https://en.wikipedia.org/wiki/VBScript.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 32716.

VBScript (Microsoft Visual Basic Scripting Edition) is a deprecated programming language for scripting on Microsoft Windows using Component Object Model (COM), based on classic Visual Basic and Active Scripting. It was popular with system administrators for managing computers and automating many aspects of computing environments, and has been installed by default in every desktop release of Microsoft Windows since Windows 98; in Windows Server since Windows NT 4.0 Option Pack; and optionally with Windows CE (depending on the device it is installed on).
VBScript running environments include Windows Script Host (WSH), Internet Explorer (IE), and Internet Information Services (IIS). The running environment is embeddable in other programs via the Microsoft Script Control (msscript.ocx).
In October 2023, Microsoft announced that VBScript was deprecated. In May 2024, a multi-phase deprecation schedule was announced with disabling it by default "around 2027" and removing it sometime later.


== History ==
VBScript began as part of the Microsoft Windows Script Technologies, launched in 1996. This technology (which also included JScript) was initially targeted at web developers. During a period of just over two years, VBScript advanced from version 1.0 to 2.0, and over that time it gained support from Windows system administrators seeking an automation tool more powerful than the batch language first developed in the early 1980s. On August 1, 1996, Internet Explorer was released with features that included VBScript.
In version 5.0, the functionality of VBScript was increased with new features including regular expressions; classes; the With statement; the Eval, Execute, and ExecuteGlobal functions to evaluate and execute script commands built during the execution of another script; a function-pointer system via GetRef, and Distributed COM (DCOM) support.
In version 5.5, SubMatches were added to the regular expression class in VBScript, to finally allow script authors to capture the text within the expression's groups. That capability had already been available in JScript.
With the advent of the .NET Framework, the scripting team decided to implement future support for VBScript within ASP.NET for web development, and therefore no new versions of the VBScript engine would be developed. It would henceforth be supported by Microsoft's Sustaining Engineering Team, who are responsible for bug fixes and security enhancements. After announcing plans to remove support for VBScript, Microsoft suggested migrating to Windows PowerShell or JavaScript.


== Environments ==


=== Client-side web ===
In a web page loaded by Internet Explorer, VBScript is similar in function to JavaScript. The VBScript code in the HTML is logic that interacts with the Document Object Model (DOM) of the page – allowing for functionality not possible in HTML alone. However, other web browsers such as Chrome, Firefox and Opera do not support VBScript. Therefore, when client-side scripting and cross-browser compatibility are required, developers usually choose JavaScript due to its wide cross-browser compatibility.


=== Active server page ===
VBScript is used for server-side web page functionality via Active Server Pages (ASP). The ASP engine, asp.dll, invokes vbscript.dll to run VBScript scripts. VBScript that is embedded in an ASP page is contained within <% and %> context switches. The following example displays the current time in 24-hour format.


=== Windows script host ===
VBScript can run directly in the operating system via the Windows Script Host (WSH). A script file, usually with extension .vbs can be run either via Wscript.exe for graphical user interface (GUI) or Cscript.exe for command line interface (CLI).


=== Windows script file ===
A Windows Script File (WSF), styled after XML, can include multiple VBS files and is therefore a library of VBScript code that can be reused in a modular way. The files have extension .wsf and can be executed using wscript.exe or cscript.exe, as with a .vbs file.


=== HTML Application ===
An HTML Application (HTA) is styled after HTML. The HTML in the file is used to generate the user interface, and a scripting language such as VBScript is used for the program logic. The files have extension .hta and can be executed using mshta.exe.


=== Windows Script Component ===
VBScript can also be used in a Windows Script Component, an ActiveX-enabled script class that can be invoked by other COM-enabled applications. These files have extension .wsc.


== Functionality ==


=== Language features ===
The VBScript language is modeled on classic Visual Basic. Notable features include:
A "procedure" is the main construct in VBScript for separating code into smaller modules. VBScript distinguishes between a function, which can return a result in an assignment statement, and a subroutine, which cannot. Parameters are positional, and can be passed by value or by reference.
Control structures include the usual iterative and conditional Do Loops, If-Then-Else statements, and Case statements, with some more complex variants, such as ElseIf and nested control structures.
As a memory aid in coding, and certainly for readability, there are a large number of constants, such as True and False for logical values, vbOKCancel and vbYesNo for MsgBox codes, vbBlack and vbYellow for color values, vbCR for the carriage return character, and many others.
Variables have "Variant" type by default, but it is possible (and sometimes necessary) to force a particular type (integer, date, etc.) using conversion functions (CInt, CDate, etc.)
User interaction is provided through the functions MsgBox and  InputBox which provide a simple dialogue box format for messages and input. Both functions display prompting messages, with the former returning a standard response, and the latter returning one user-supplied text or numeric value. For more elaborate GUI interaction with controls, VBScript can be used in combination with HTML, for example, in an HTML Application. Event-driven forms are not supported as in Visual Basic or Visual Basic for Applications.
Names are not case-sensitive. However, it is considered a best practice of VBScript style to be consistent and to capitalize judiciously.


=== VBScript functionalities ===
When hosted by the Windows Script Host, VBScript provides numerous features which are common to scripting languages, but not available from Visual Basic 6.0. These features include:

Named and unnamed command line arguments
Stdin and stdout, which could be redirected
WSH.Echo which writes to the console and cannot be redirected
WSH.ExitCode which can be tested from DOS batch files, or by the process which invoked the script file
Network printers
Network shares
Special folders, e.g. Desktop, Favorites, MyDocuments and so on
Network user information, such as group membership
Methods for runtime execution of text defined at runtime: Eval and Execute
Methods for executing scripts on remote machines
Windows Management Instrumentation (WMI)
Functionality for embedding a VBScript engine in other applications, using a widely known language
CScript, the command line runner, provides options for:

Interactive or batch mode
Invoking debug mode from the command line
Error reporting including the line number


=== Additional functionality ===
File system management, file modification, and streaming text operations are implemented with the Scripting Runtime Library scrrun.dll. This provides objects such as FileSystemObject, File, and TextStream, which expose the Windows file system to the programmer.
Binary file and memory I/O are provided by the "ADODB.Stream" class, which can also be used for string builders (to avoid excessive string concatenation, which can be costly), and to interconvert byte arrays and strings. Database access is made possible through ActiveX Data Objects (ADO), and the IIS Metabase can be manipulated using the GetObject() function with sufficient permissions (useful for creating and destroying sites and virtual directories). XML files and schemas can be manipulated with the Microsoft XML Library Application Programming Interfaces (msxml6.dll, msxml3.dll), which also can be used to retrieve content from the World Wide Web via the XMLHTTP and ServerXMLHTTP objects (class strings "MSXML2.XMLHTTP.6.0" and "MSXML2.ServerXMLHTTP.6.0", respectively).
Functionality can also be added through ActiveX technologies. Security concerns have led to many ActiveX controls being blacklisted in the Internet Explorer process by Microsoft, which deploys the killbit via monthly Windows security updates to disable vulnerable Microsoft and third party code.
Programmers can utilize the extensibility via COM (ActiveX) modules to specifically equip the Script Host and VBScript with required or desired functions. The "VTool" component, for instance, adds a number of dialog windows, binary file access, and other functionality.


== Development tools ==
Microsoft does not routinely make available an IDE (Integrated Development Environment) for VBScript,  although the Microsoft Script Editor has been bundled with certain versions of Microsoft Office.
For debugging purposes the Microsoft Script Debugger can still be used in current Windows versions, even though the tool has not been updated in years. It allows the user to set break points in the VBScript code but the user interface is more than clumsy.
There are VBScript debuggers available from third-party sources, and many text editors offer syntax highlighting for the language.
During execution, when an error occurs, the script host issues a message stating the type of error and the number of the offending line.


== Uses ==
Although VBScript is a general-purpose scripting language, several particular areas of use are noteworthy. First, it used to be widely used among system administrators in the Microsoft environment, but it has since been vastly surpassed by PowerShell. Second, VBScript is the scripting language for OpenText UFT One, a test automation tool. A third area to note is the adoption of VBScript as the internal scripting language for some embedded applications, such as industrial operator interfaces and human machine interfaces. The hierarchical DBMS InterSystems Caché (which has its roots in the language MUMPS) also supports an implementation of VBScript, Cache BASIC, for programming stored code.
VBScript omits several useful features of the full Visual Basic, such as strong typing, extended error trapping and the ability to pass a variable number of parameters to a subroutine. However, its use is relatively widespread because it is easy to learn and because those who implement code in the language need not pay royalties to Microsoft as long as the VBScript trade mark is acknowledged. When an organization licenses Visual Basic for Applications (VBA) from Microsoft, as companies such as Autodesk, StatSoft, Great Plains Accounting and Visio (subsequently acquired by Microsoft) have done, it is allowed to redistribute the full VBA code-writing and debugging environment with its product.
VBScript is used in place of VBA as the macro language of Outlook 97.
VBScript can be effectively used for automating day to day office tasks as well as monitoring in the Windows-based environment. It can also be used in collaboration with ADODB ActiveX Data Objects (ADODB) for effective database connectivity.
VBScript can also be used to create malware and viruses, such as the ILOVEYOU worm that spread through email attachment in Outlook 97 that cost billions of dollars.


== See also ==
AppleScript
FastTrack Scripting Host
HTML Components
JavaScript
JScript .NET
JScript
PerlScript
Windows PowerShell
Windows Script File


== References ==


== External links ==

VBScript Language Reference, Microsoft Docs
Is VBScript Dead?, isvbscriptdead.com
VBScript Commands, ss64.com
VBScript How-to guides and examples, ss64.com
WMI Overview, Microsoft TechNet
