# Shell script

Cloned from https://en.wikipedia.org/wiki/Shell_script.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 28938.

A shell script is a computer program designed to be run by a Unix shell, a command-line interpreter.
The various dialects of shell scripts are considered to be command languages. Typical operations performed by shell scripts include file manipulation, program execution, and printing text. A script which sets up the environment, runs the program, and does any necessary cleanup or logging, is called a wrapper.
The term is also used more generally to mean the automated mode of running an operating system shell. Different operating systems each use a particular name for these functions.  All Unix-like systems include at least one POSIX shell, typically either bash or the zsh compatibility mode.


== Capabilities ==


=== Comments ===
Comments are ignored by the shell. They typically begin with the hash symbol (#), and continue until the end of the line.


=== Configurable choice of scripting language ===
The shebang, or hash-bang, is a special kind of comment which the system uses to determine what interpreter to use to execute the file. The shebang must be the first line of the file, and start with "#!". In Unix-like operating systems, the characters following the "#!" prefix are interpreted as a path to an executable program that will interpret the script.


=== Shortcuts ===
A shell script can provide a convenient variation of a system command where special environment settings, command options, or post-processing apply automatically, but in a way that allows the new script to still act as a fully normal Unix command.
One example would be to create a version of ls, the command to list files, giving it a shorter command name of l, which would be normally saved in a user's bin directory as /home/username/bin/l, and a default set of command options pre-supplied.

Here, the first line uses a shebang to indicate which interpreter should execute the rest of the script, and the second line makes a listing with options for file format indicators, columns, all files (none omitted), and a size in blocks. The LC_COLLATE=C sets the default collation order to not fold upper and lower case together, not intermix dotfiles with normal filenames as a side effect of ignoring punctuation in the names (dotfiles are usually only shown if an option like -a is used), and the "$@" causes any parameters given to l to pass through as parameters to ls, so that all of the normal options and other syntax known to ls can still be used.
The user could then simply use l for the most commonly used short listing.
Beyond simply providing a set of default for a command, scripts provide for running multiple commands automatically upon script invocation. This one, ll, merely clears the terminal of all other text before running a listing command.

As in the prior example, this ls -al invocation lists the files and directories that are in the directory from which the script is being run, or any directories given after ll on the command line, which are automatically substituted in for the "$@". The -la command options here cause "all" directory contents to be shown in "long" format.


=== Batch jobs ===
Shell scripts allow several commands that would be entered manually at a command-line interface to be executed automatically, and without having to wait for a user to trigger each stage of the sequence. For example, in a directory with three C source code files, rather than manually running the four commands required to build the final program from them, one could instead create a script for POSIX-compliant shells, here named build and kept in the directory with them, which would compile them automatically:

The script would allow a user to save the file being edited, pause the editor, and then just run ./build to create the updated program, test it, and then return to the editor. Since the 1980s or so, however, scripts of this type have been replaced with utilities like make which are specialized for building programs.


=== Generalization ===
Simple batch jobs are not unusual for isolated tasks, but using shell loops, tests, and variables provides much more flexibility to users. A POSIX sh script to convert JPEG images to PNG images, where the image names are provided on the command-line—possibly via wildcards—instead of each being listed within the script, can be created with this file, typically saved in a file like /home/username/bin/jpg2png

The jpg2png command can then be run on an entire directory full of JPEG images with just /home/username/bin/jpg2png *.jpg


=== Programming ===
Many modern shells also supply various features usually found only in more sophisticated general-purpose programming languages, such as control-flow constructs, variables, comments, arrays, subroutines and so on. With these sorts of features available, it is possible to write reasonably sophisticated applications as shell scripts. However, they are still limited by the fact that most shell languages have little or no support for data typing systems, classes, threading, complex math, and other common full language features, and are also generally much slower than compiled code or interpreted languages written with speed as a performance goal.
The standard Unix tools sed and awk provide extra capabilities for shell programming; Perl can also be embedded in shell scripts as can other scripting languages like Tcl. Perl and Tcl come with graphics toolkits as well.


== Typical shell languages ==


=== Bourne family ===
The POSIX standard shell language "sh" is based on the original Bourne shell (sh). It is no longer in common use, but the following programs implement a language of this family and remain common:

Almquist shell (ash), Kenneth Almquist's re-implementation of Bourne.
BusyBox, a collection of small programs commonly found on embedded systems, includes a version of ash, which tends to serve as the only sh on such systems.
Debian Almquist shell (dash), Debian's fork of NetBSD ash, intended as a (much) faster replacement of bash in package-installation scripts. Includes some convenience features such as local.
GNU Bash (bash), the POSIX-compatible shell of the GNU project. Includes numerous feature additions, including many from ksh. The default shell on most Linux distributions.
Z shell (zsh), a liberally-licensed shell with many additions. Is not very Bourne-compatible in the default configuration, but includes an emulate command for compatibility with many other shells.
Formerly-popular shells include:

The original Bourne shell (sh), which had many variants under many different licenses and featuring differing additions.
Old shell (osh), a "port of the standard command interpreter from Sixth Edition UNIX"
KornShell (ksh), David Korn's Bourne-derived shell, a major influence on later shells.
pdksh, a Public Domain clone of ksh.
Bourne shell features some influence from ALGOL, specifically in the choice of flow control: if ~ then ~ elif ~ then ~ else ~ fi, case ~ in ~ esac. 


=== Other Unix shells ===
No longer popular but historically noteworthy:

Tenex C Shell (tcsh) and its predecessor the C shell (csh)
Tcl shell (tclsh)
The C and Tcl shells have flow-control syntax quite similar to that of similarly-named programming languages.
(The latter is actually based on the Tcl interpreter and provides the full Tcl language.)
Newer non-Bourne-like shells in common use on Unix-like and UNIX systems include:

Nushell (nu)
xonsh shell (xonsh), pronounced "conch", a Python-based shell. The language is a superset of Python 3.
Fish shell (fish). Although not POSIX-compatible or Bash-compatible, it draws inspirations from bashisms.
PowerShell (pwsh)
(Nushell, xonch, and PowerShell are cross-platform beyond Unix-likes and UNIX: they also work natively on Windows.)


=== Other command-line shells ===
Many programming languages feature REPLs that may be used as shells. Examples include those for Python, Ruby, C, Java, Perl, Pascal, Rexx etc. The various shells plus tools like awk, sed, grep, and BASIC, Lisp, C and so forth contributed to the Perl programming language.
The standard shell of Microsoft Windows is cmd.exe, which has rudimentary scripting capabilities. It is partly compatible with its even simpler predecessor COMMAND.COM.
So called remote shells such as 

a Remote Shell (rsh)
a Secure Shell (ssh)
are really just tools to run a more complex shell on a remote system and have no 'shell' like characteristics themselves.


== Other scripting languages ==

Many powerful scripting languages, such as Rexx, Python, Perl, and Tcl, have been introduced to address tasks that are too large, complex, or repetitive to be comfortably handled by traditional shell scripts, while avoiding the overhead associated with compiled languages like C or Java.
Although the distinction between scripting languages and general-purpose high-level programming languages is often debated, scripting languages are typically characterized by their interpreted nature, simplified syntax, and primary use in automating tasks, coordinating system operations, and writing "glue code" between components. Even when scripting languages such as Python, Rexx, or JavaScript support compilation to bytecode or use JIT to improve performance, they are still commonly referred to as "scripting languages" due to their historical association with automation, lightweight tooling, and scripting environments rather than standalone application development.
Scripting is a form of programming. While "scripting" may emphasize lightweight, task-oriented automation, the broader term "programming" encompasses both scripting and software development in compiled or structured languages. As such, scripting involves writing code to instruct a computer to perform specific tasks—meeting the fundamental definition of programming.


== Life cycle ==
Shell scripts often serve as an initial stage in software development, and are often subject to conversion later to a different underlying implementation, most commonly being converted to Perl, Python, or C. The interpreter directive allows the implementation detail to be fully hidden inside the script, rather than being exposed as a filename extension, and provides for seamless reimplementation in different languages with no impact on end users.
While files with the ".sh" file extension are usually a shell script of some kind, most shell scripts do not have any filename extension.


== Advantages and disadvantages ==
One of the biggest advantages of writing a shell script is that the commands and syntax are exactly the same as those directly entered at the command-line. The programmer does not have to switch to a totally different syntax, as they would if the script were written in a different language, or if a compiled language were used.
Often, writing a shell script is much quicker than writing the equivalent code in other programming languages. The many advantages include easy program or file selection, quick start, and interactive debugging. A shell script can be used to provide a sequencing and decision-making linkage around existing programs, and for moderately sized scripts the absence of a compilation step is an advantage. Interpretive running makes it easy to write debugging code into a script and re-run it to detect and fix bugs. Non-expert users can use scripting to tailor the behavior of programs, and shell scripting provides some limited scope for multiprocessing.
On the other hand, shell scripting is prone to costly errors. Inadvertent typing errors such as rm -rf * / (instead of the intended rm -rf */) are folklore in the Unix community; a single extra space converts the command from one that deletes all subdirectories contained in the current directory, to one which deletes everything from the file system's root directory. Similar problems can transform cp and mv into dangerous weapons, and misuse of the > redirect can delete the contents of a file.
Another significant disadvantage is the slow execution speed and the need to launch a new process for almost every shell command executed. When a script's job can be accomplished by setting up a pipeline in which efficient filter commands perform most of the work, the slowdown is mitigated, but a complex script is typically several orders of magnitude slower than a conventional compiled program that performs an equivalent task.
There are also compatibility problems between different platforms. Larry Wall, creator of Perl, famously wrote that "It's easier to port a shell than a shell script", referring to the inconsistent behavior of command-line programs across systems. (His specific example would have been fixed by POSIX standardization of grep.)
Similarly, more complex scripts can run into the limitations of the shell scripting language itself; the limits make it difficult to write quality code, and extensions by various shells to ameliorate problems with the original shell language can make problems worse.
Many disadvantages of using some script languages are caused by design flaws within the language syntax or implementation, and are not necessarily imposed by the use of a text-based command-line; there are a number of shells which use other shell programming languages or even full-fledged languages like Scsh (which uses Scheme).


== Interoperability among scripting languages ==
Many scripting languages share similar syntax and features due to their adherence to the POSIX standard, and several shells provide modes to emulate or maintain compatibility with others. This allows scripts written for one shell to often run in another with minimal changes.
For example, Bash supports much of the original Bourne shell syntax and offers a POSIX-compliant mode to improve portability. However, Bash also includes a number of extensions not found in POSIX, commonly referred to as bashisms. While these features enhance scripting capabilities, they may reduce compatibility with other shells like Dash or ksh.
A script that uses features specific to a certain shell may use a matching shebang (#!) as the first line, so that the operating system will use the specified interpreter (e.g. /bin/bash) to run the script, though this will not be sufficient when a feature is added to a shell without changing its name, or when one manually runs the script (e.g. sh foo.sh).
A script can also check which shell it is being ran on and exit before the missing features are used, for example:

In the example above, the opening lines of the script is written in pure POSIX shell. When a non-bash shell run the script, $BASH_VERSINFO will not be set; this triggers the test and causes the script to exit before the incompatible line is reached. When a bash version prior to 4.x runs the script, the same test is triggered by numeric comparison (-lt). (declare -A declares an associative array, a feature new to bash 4.0 and not found on previous versions.)


== Shell scripting on other operating systems ==
Interoperability software such as Cygwin, the MKS Toolkit, Interix (formerly part of Microsoft Windows Services for UNIX), Hamilton C shell, and UWIN (AT&T Unix for Windows) enables Unix shell programs to run on Windows NT-based systems, though some features may not be fully supported on the older MS-DOS/Windows 95 platforms. Earlier versions of the MKS Toolkit also provided support for OS/2. 
Scripting languages are, by definition, able to be extended. On Unix and other POSIX-compliant systems, awk and sed are used to extend the string and numeric processing ability of shell scripts. Tcl, Perl, Rexx, and Python have graphics toolkits and can be used to code functions and procedures for shell scripts which pose a speed bottleneck (C, Fortran, assembly language &c are much faster still) and to add functionality not available in the shell language such as sockets and other connectivity functions, heavy-duty text processing, working with numbers if the calling script does not have those abilities, self-writing and self-modifying code, techniques like recursion, direct memory access, various types of sorting and more, which are difficult or impossible in the main script, and so on. Visual Basic for Applications and VBScript can be used to control and communicate with such things as spreadsheets, databases, scriptable programs of all types, telecommunications software, development tools, graphics tools and other software which can be accessed through the Component Object Model.


== See also ==
Glue code
Interpreter directive
Shebang symbol (#!)
Unix shells
PowerShell
Windows Script Host


== References ==


== External links ==

An Introduction To Shell Programming by Greg Goebel
UNIX / Linux shell scripting tutorial by Steve Parker
Shell Scripting Primer (Apple)
What to watch out for when writing portable shell scripts by Peter Seebach
Free Unix Shell scripting books
Beginners/BashScripting, Ubuntu Linux
