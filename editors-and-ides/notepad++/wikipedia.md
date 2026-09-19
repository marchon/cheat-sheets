# Notepad++

Cloned from https://en.wikipedia.org/wiki/Notepad%2B%2B.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1329953.

Notepad++ (sometimes npp or NPP) is a text and source-code editor for use with Microsoft Windows. It supports tabbed editing, which allows working with multiple open files in one window. The program's name comes from the C postfix increment operator.
Notepad++ is released as free and open-source software under a GNU General Public License (GPL) 3.0 or later. The project was originally hosted on the SourceForge software repository (2003–2010), from where it was downloaded over 28 million times, and twice won the SourceForge Community Choice Award for Best Developer Tool. The project moved to TuxFamily (2010–2015), and then to GitHub (2015–present). Notepad++ uses the Scintilla editor component. It supports Windows DirectWrite and all major Windows color font formats (COLRv0, COLRv1, and OpenType SVG).


== History ==
Notepad++ development began in September 2003 by Don Ho, a former computer science student of Paris Diderot University. Ho first used JEXT (a Java-based text editor) at his company but, dissatisfied with its poor performance, he began to develop a text editor written in C++ with Scintilla. He developed it in his spare time since the idea was rejected by his company. Notepad++ was built as a Microsoft Windows application; the developer considered, but rejected, the idea of using wxWidgets to port it to the Mac OS X and Unix platforms.
Notepad++ was first released on SourceForge on 25 November 2003, as a Windows-only application. It is based on the Scintilla editor component, and is written in C++ with only Windows API (Win32) application programming interface (API) calls using only the Standard Template Library (STL) to increase performance and reduce program size.
In January 2010 the US government obliged US-based open source project hosts to deny access from Cuba, Iran, North Korea, Sudan, and Syria to comply with U.S. law. As a response to what the developer felt was a violation of the free and open-source software (FOSS) philosophy, in June 2010 Notepad++ moved out of US territorial jurisdiction by releasing a version on TuxFamily, in France. Some community services of Notepad++ (such as the forums and bug tracker) remained on SourceForge until 2015 when Notepad++ left SourceForge completely.
In 2011 Lifehacker described Notepad++ as "The Best Programming Text Editor for Windows", stating that "if you prefer a simple, lightweight, and extensible programming plain-text editor, our first choice is the free, open-source Notepad++". Lifehacker criticized its user interface, stating that "It is, in fact, fairly ugly. Luckily you can do a lot to customize its looks, and what it lacks in polish, it makes up for in functionality".
In 2014 Lifehacker readers voted Notepad++ as the "Most Popular Text Editor", with 40% of the 16,294 respondents specifying it as their most-loved editor. The Lifehacker team summarized the program as being "fast, flexible, feature-packed, and completely free".
In 2015 Stack Overflow conducted a worldwide Developer Survey, and Notepad++ was voted as the most used text editor worldwide with 34.7% of the 26,086 respondents claiming to use it daily. Stack Overflow noted that "The more things change, the more likely it is those things are written in JavaScript with NotePad++ on a Windows machine". The 2016 survey had Notepad++ at 35.6%.
In 2015, in response to the staff hijacking of projects hosted on SourceForge, Notepad++ left SourceForge completely with the forums being moved to NodeBB and the bug tracker to GitHub. In 2019, the website, notepad-plus-plus.org, moved to Hostinger.
In March 2017 it was revealed through WikiLeaks that CIA hacking tools used Notepad++, because of its popularity, to hide malware in a modified library named scilexer.dll. Notepad++ was subsequently hardened against modified DLLs.


=== Update chain hijacking ===
In 2025, state-sponsored hackers (suspected to be Chinese APT31) hijacked the update functionality for Notepad++ by compromising its hosting provider. Organizations in East Asia were targeted, redirecting their updates to malicious servers for several months to deliver malware. The issue was resolved by migrating to a more secure host and enforcing stronger update verification. The mechanism of the attack involved a modification to the Notepad++ updater, gup.exe, with the modification introduced in Notepad++ version 8.8.8, where the executable obtains the latest application version from https://notepad-plus-plus.org/update/getDownloadUrl.php and retrieves the update URL from a file named gup.xml, with the retrieved file then saved to a temporary directory and executed; this connection could be TLS intercepted at the ISP level, allowing the download to be redirected to any URL, and although legitimate update files use a self-signed root certificate, the updater does not perform thorough checks for tampering. As a result, gup.exe executes a malicious payload named update.exe obtained from a malicious server, containing a NSIS installer which creates the %AppData%\Bluetooth\ directory, extracts four files, sets the directory to hidden, and executes BluetoothService.exe within the resulting payload. This then sideloads a malicious DLL which loads the shellcode file into memory, and then decrypts and executes it, allowing command and control over the computer by an attacker using a web interface.


== Features ==
Notepad++ is a source code editor. It features syntax highlighting, code folding, and limited autocompletion for programming, scripting, and markup languages, but not intelligent code completion or syntax checking. As such, it may properly highlight code written in a supported scheme, but it cannot verify whether the syntax is internally sound or compilable. As of version 7.6.3, Notepad++ can highlight the elements of 78 syntaxes:

Notepad++ recognizes three newline representations (CR, CR+LF, and LF) and can convert between them on the fly. In addition, it supports reinterpreting plain text files in various character encodings and can convert them to ASCII, UTF-8, or UCS-2. As such, it can fix plain text that seems gibberish only because their character encoding is not properly detected.
Notepad++ also has features that improve plain text editing experience in general, such as:

Autosave
Finding and replacing strings of text with regular expressions
Searching text strings within opened tabs
Searching text strings in a directory
Guided indentation
Line bookmarking
Macros
Simultaneous editing
Split screen editing and synchronized scrolling
Line operations, including sorting, case conversion (uppercase, lowercase, camel case, sentence case), and removal of redundant whitespace
Tabbed document interface


=== Plugins ===
Notepad++ has support for macros and plugins, and has been remarked for its robust plugin architecture which enabled various new features to be integrated into the program. Currently, over 140 compatible plugins are developed for Notepad++, 10 of which are included by default in the program. The first plugin to be included in the program was "TextFX", which includes W3C validation for HTML and CSS, text sorting, character case alteration and quote handling.


=== Internationalization ===
Notepad++ supports internationalization through XML files in an application-specific format containing all internationalized strings (dialog captions, menu titles and items, etc.) in a certain language; this file can be reloaded from the application settings. Translations to new languages can thus be written by simply editing an existing file.


== Political messaging ==
Notepad++ is notable for being vocal in politics, particularly in human rights and support of Ukraine in the Russo-Ukrainian war.
In March 2008, the "Boycott Beijing 2008" banner was placed on Notepad++'s SourceForge.net homepage. A few months later most users in China were unable to reach the SourceForge.net website from 26 June to 24 July 2008. This led to the widespread belief that China had banned SourceForge.net in retaliation for the Boycott banner.
On June 4, 2014, Notepad++ released version 6.4.4, codenamed "Tiananmen June Fourth Incident Edition". In the release notes, the developer paid tribute to the pro-democracy protesters who were massacred in the aforementioned incident.
In January 2015, the Notepad++ website was hacked by activists from the Fallaga Team who objected to an Easter egg endorsing Je suis Charlie. The Fallaga Team has been linked to ISIL and is also believed to be responsible for the 2017 hacking of websites of the British National Health Service.
On October 29, 2019, Notepad++ released version 7.8.1, codenamed "Free Uyghur", a codename shared with two sequential versions, 7.9 (December 5, 2019) and 7.9.2 (January 16, 2020). In the release notes for 7.8.1, the developer expressed concern that hundreds of thousands of Uyghurs have been "subjected to political indoctrination, and sometimes even torture" in the Xinjiang re-education camps. He called for "additional pressure on the Chinese government to stop their oppressive actions and crimes concerning the Uyghur people". The software's dedicated site came under a distributed-denial-of-service attack and its GitHub issues page was bombarded with vitriolic nationalist comments, though it was later recovered after being moved behind Cloudflare's anti-DDoS service.
On July 16, 2020, Notepad++ released version 7.8.9, codenamed "Stand with Hong Kong", a codename shared with two sequential versions, 7.9 (September 28, 2020) and 7.9.2 (January 1, 2021). In the release notes for 7.8.9, the developer expressed his concern about the Chinese government implementation of the National Security Law in Hong Kong. In retaliation, mainland Chinese browsers developed by Tencent (QQ Browser and WeChat's built-in browser), Alibaba (UC Browser), 360 and Sogou started blocking the official site's Download page, but not other pages.
On February 3 and 15, 2022, Notepad++ released versions 8.3 and 8.3.1, both codenamed "Boycott Beijing 2022". In the release notes, the developer expressed his concern about human rights in China, especially for Uyghurs and Hongkongers. He suggested his customers to "not watch or pay attention to the games".
On February 27, 2022, Notepad++ released version 8.3.2, codenamed "Declare variables, not war". In the release notes, the developer condemned the Russian invasion of Ukraine and called for support for Ukraine. On March 15, Notepad++ released version 8.3.3, codenamed "Make Apps, not war". The developer likewise continued to express his views on the invasion, along with the next update, version 8.4, codenamed "Stand up for Ukraine", released on April 26.
From June 4 through September 17, 2024, Notepad++ released 3 consecutive updates, all of which bore political slogans calling for the support of Taiwan, including "Support Taiwan's Sovereignty" (8.6.8), "Support Taiwan's Independence" (8.6.9), and "Support Taiwan's return to the UN" (8.7).
On November 27 and 31, 2024, Notepad++ showed support for Ukraine again, with a release, version 8.7.2, codenamed "in a world of Elon, be a Zelensky", and another criticizing Elon Musk, version 8.7.3, bearing the codename "leaving X for Bluesky".
From March 8 through May 5, 2025, Notepad++ continued to express support for Ukraine once again with versions 8.7.8 through 8.8.1 released during this time; all are aptly codenamed "We Are With Ukraine".
On June 4, 2026, Notepad++ released version 8.9.6.4, which is codenamed "Tiananmen Massacre Commemoration". Within the release notes, the developer criticizes the continued political suppression and lack of government transparency regarding the Tiananmen Square protests and massacre in 1989.


== See also ==

Comparison of text editors
List of text editors


== Notes ==


== References ==


== External links ==

Official website
