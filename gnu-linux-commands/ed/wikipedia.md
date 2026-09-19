# Ed (text editor)

Cloned from https://en.wikipedia.org/wiki/Ed_(text_editor).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 9771.

ed (pronounced as distinct letters, ) is a line editor. It was one of the first features of the Unix operating system. Although not commonly used today, it remains part of the POSIX and Open Group standards, alongside the full-screen editor vi.


== History ==
The ed text editor was one of the first three key elements of the Unix operating system—assembler, editor, and shell—developed by Ken Thompson in August 1969 on a PDP-7 at AT&T Bell Labs. Many of its features came from the qed text editor developed at Thompson's alma mater University of California, Berkeley.Thompson was very familiar with qed, and had reimplemented it on the CTSS and Multics systems. Thompson's versions of qed were notable as the first to implement regular expressions. Regular expressions are also implemented in ed, though their implementation is considerably less general than that in qed.
Dennis M. Ritchie produced what Doug McIlroy later described as the "definitive" ed, and aspects of ed went on to influence ex, and later vi.  The non-interactive Unix command grep was inspired by a common special use of qed and later ed, where the command g/re/p performs a global regular expression search and prints the lines containing matches.  The Unix stream editor, sed, implemented many of the scripting features of qed that were not supported by ed on Unix.
The ed commands are often imitated in other line-based editors. For example, CP/M's ED, EDLIN in early MS-DOS versions and 32-bit versions of Windows NT has a somewhat similar syntax, and text editors in many MUDs (LPMud and descendants, for example) use ed-like syntax. These editors, however, are typically more limited in function.
In current practice, ed is rarely used interactively, yet is sometimes used in shell scripts. For interactive use, ed was subsumed by the sam, vi and Emacs editors in the 1980s. ed can be found on virtually every version of Unix and Linux available, and as such is useful for people who have to work with multiple versions of Unix. On Unix-based operating systems, some utilities like SQL*Plus run ed as the editor if the EDITOR and VISUAL environment variables are not defined. If something goes wrong, ed is sometimes the only editor available. This is often the only time when it is used interactively.


== Features ==

Features of ed include:

available on essentially all Unix systems (and mandatory on systems conforming to the Single Unix Specification)
support for regular expressions
powerful automation can be achieved by feeding commands from standard input
The GNU version includes options intended to enhance feedback. Using ed -v -p: provides a simple prompt and enables more useful feedback messages. The -p switch is defined in POSIX since XPG2 (1987).


== User experience ==
Known for its terseness, ed gives almost no feedback, and has been called (by Peter H. Salus) "the most user-hostile editor ever created", even when compared to the contemporary (and notoriously complex) TECO. For example, the message that ed produces in case of error and when it wants to confirm exit without saving, is merely "?". It does not report the current filename or line number, or even display the results of a change to the text, unless requested. Older versions (c. 1981) did not even ask for confirmation when a quit command was issued when there were unsaved changes. This terseness was appropriate in early versions of Unix, when a console was a teletype, modems were slow, and memory was limited. As computer technology improved and these constraints loosened, editors with more feedback became the norm.
The glibc documentation notes an error code called ED with its description (errorstr) merely a single question mark, noting "the experienced user will know what is wrong."


== Example ==
Here is an example transcript of an ed session. For clarity, commands and text typed by the user are in normal color, and output from ed is gray color.

a
ed is the standard Unix text editor.
This is line number two.
.
2i
.
,l
ed is the standard Unix text editor.$
$
This is line number two.$
w text.txt
63
3s/two/three/
,l
ed is the standard Unix text editor.$
$
This is line number three.$
w text.txt
65
q

The end result is a simple text file text.txt containing the following text:

ed is the standard Unix text editor.
This is line number three.

Started with an empty file, the a command appends text (all ed commands are single letters). The command puts ed in insert mode, inserting the characters that follow and is terminated by a single dot on a line. The two lines that are entered before the dot end up in the file buffer. The 2i command also goes into insert mode, and will insert the entered text (a single empty line in our case) before line two. All commands may be prefixed by a line number to operate on that line.
In the line ,l, the lowercase L stands for the list command. The command is prefixed by a range, in this case , which is a shortcut for 1,$. A range is two line numbers separated by a comma ($ means the last line). In return, ed lists all lines, from first to last. These lines are ended with dollar signs, so that white space at the end of lines is clearly visible.
Once the empty line is inserted in line 2, the line which reads "This is line number two." is now actually the third line. This error is corrected with 3s/two/three/, a substitution command. The 3 will apply it to the correct line; following the command is the text to be replaced, and then the replacement. Listing all lines with ,l the line is shown now to be correct.
w text.txt writes the buffer to the file text.txt making ed respond with 65, the number of characters written to the file. q will end an ed session.


== See also ==
Editor war
Edlin, the standard MS-DOS line editor which was inspired by ed
List of POSIX commands
Sam (text editor)
Grep


== Notes ==


== References ==


== External links ==

ed: edit text – Shell and Utilities Reference, The Single UNIX Specification, Version 5 from The Open Group
Manual page from Unix First Edition describing ed.
ed(1): text editor – Version 7 Unix Programmer's Manual
ed(1): text editor – Plan 9 Programmer's Manual, Volume 1, a direct descendant of the original ed.
GNU ed homepage
A History of UNIX before Berkeley section 3.1 describes the history of ed.
