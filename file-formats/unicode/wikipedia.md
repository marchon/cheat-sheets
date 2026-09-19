# Unicode

Cloned from https://en.wikipedia.org/wiki/Unicode.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 31742.

Unicode (also known as The Unicode Standard and TUS) is a character encoding standard maintained by the Unicode Consortium designed to support the use of text in all of the world's writing systems that can be digitized. Version 18.0 defines 172,808 characters and 175 scripts used in various ordinary, literary, academic and technical contexts.
Unicode has largely supplanted the previous environment of myriad incompatible character sets used within different locales and on different computer architectures. The entire repertoire of these sets, plus many additional characters, were merged into the single Unicode set. Unicode is used to encode the vast majority of text on the Internet, including most web pages, and relevant Unicode support has become a common consideration in contemporary software development. Unicode is ultimately capable of encoding more than 1.1 million characters.
The Unicode character repertoire is synchronized with ISO/IEC 10646, each being code-for-code identical with one another. However, The Unicode Standard is more than just a repertoire within which characters are assigned. To aid developers and designers, the standard also provides charts and reference data, as well as annexes explaining concepts germane to various scripts, providing guidance for their implementation. Topics covered by these annexes include character normalization, character composition and decomposition, collation, and directionality.
Unicode encodes 3,972 emoji, with the continued development thereof conducted by the Consortium as a part of the standard. The standardization of Unicode was a major factor in enabling their widespread adoption outside of Japan.
Unicode text is processed and stored as binary data using one of several encodings, which define how to translate the standard's abstracted codes for characters into sequences of bytes. The Unicode Standard itself defines three encodings: UTF-8, UTF-16, and UTF-32, though several others exist. UTF-8 is the most widely used by a large margin, in part due to its backwards-compatibility with ASCII.


== Origin and development ==
Unicode was originally designed with the intent of transcending limitations present in all text encodings designed up to that point: each encoding was relied upon for use in its own context, but with no particular expectation of compatibility with any other. Indeed, any two encodings chosen were often totally unworkable when used together, with text encoded in one interpreted as garbage characters by the other. Most encodings had only been designed to facilitate interoperation between a handful of scripts—often primarily between a given script and Latin characters—not between a large number of scripts, and not with all of the scripts supported being treated in a consistent manner.
The philosophy that underpins Unicode seeks to encode the underlying characters—graphemes and grapheme-like units—rather than graphical distinctions considered mere variant glyphs thereof, that are instead best handled by the typeface, through the use of markup, or by some other means. In particularly complex cases, such as the treatment of orthographical variants in Han characters, there is considerable disagreement regarding which differences justify their own encodings, and which are only graphical variants of other characters.
At the most abstract level, Unicode assigns a unique number called a code point to each character. Many issues of visual representation—including size, shape, and style—are intended to be up to the discretion of the software actually rendering the text, such as a web browser or word processor. However, partially with the intent of encouraging rapid adoption, the simplicity of this original model has become somewhat more elaborate over time, and various pragmatic concessions have been made over the course of the standard's development.
The first 256 code points mirror the ISO/IEC 8859-1 standard, with the intent of trivializing the conversion of text already written in Western European scripts. To preserve the distinctions made by different legacy encodings, therefore allowing for conversion between them and Unicode without any loss of information, many characters nearly identical to others, in both appearance and intended function, were given distinct code points. For example, the Halfwidth and Fullwidth Forms block encompasses a full semantic duplicate of the Latin alphabet, because legacy CJK encodings contained both "fullwidth" (matching the width of CJK characters) and "halfwidth" (matching ordinary Latin script) characters.


=== History ===
The origins of Unicode can be traced back to the 1980s, to a group of individuals with connections to Xerox's Character Code Standard (XCCS). In 1987, Xerox employee Joe Becker, along with Apple employees Lee Collins and Mark Davis, started investigating the practicalities of creating a universal character set. With additional input from Peter Fenwick and Dave Opstad, Becker published a draft proposal for an "international/multilingual text character encoding system in August 1988, tentatively called Unicode". He explained that "the name 'Unicode' is intended to suggest a unique, unified, universal encoding".
In this document, entitled Unicode 88, Becker outlined a scheme using 16-bit characters:

Unicode is intended to address the need for a workable, reliable world text encoding. Unicode could be roughly described as "wide-body ASCII" that has been stretched to 16 bits to encompass the characters of all the world's living languages. In a properly engineered design, 16 bits per character are more than sufficient for this purpose.

This design decision was made based on the assumption that only scripts and characters in "modern" use would require encoding:

Unicode gives higher priority to ensuring utility for the future than to preserving past antiquities. Unicode aims in the first instance at the characters published in the modern text (e.g. in the union of all newspapers and magazines printed in the world in 1988), whose number is undoubtedly far below 214 = 16,384. Beyond those modern-use characters, all others may be defined to be obsolete or rare; these are better candidates for private use registration than for congesting the public list of generally useful Unicode.

In early 1989, the Unicode working group expanded to include Ken Whistler and Mike Kernaghan of Metaphor, Karen Smith-Yoshimura and Joan Aliprand of Research Libraries Group, and Glenn Wright of Sun Microsystems. The Research Libraries Group had an existing solution for East Asian character sets, which became one of the inputs to the Unicode character set. In 1990, Michel Suignard and Asmus Freytag of Microsoft and NeXT's Rick McGowan had also joined the group. By the end of 1990, most of the work of remapping existing standards had been completed, and a final review draft of Unicode was ready.
The Unicode Consortium was incorporated in California on 3 January 1991, and the first volume of The Unicode Standard was published that October. The second volume, now adding Han ideographs, was published in June 1992.
In 1996, a surrogate character mechanism was implemented in Unicode 2.0, so that Unicode was no longer restricted to 16 bits. This increased the Unicode codespace to over a million code points, which allowed for the encoding of many historic scripts, such as Egyptian hieroglyphs, and thousands of rarely used or obsolete characters that had not been anticipated for inclusion in the standard. Among these characters are various rarely used CJK characters—many mainly being used in proper names, making them far more necessary for a universal encoding than the original Unicode architecture envisioned.


=== Unicode Consortium ===

The Unicode Consortium is a non-profit organization that coordinates Unicode's development. Full members include most of the main computer software and hardware companies (and few others) with any interest in text-processing standards, including Adobe, Apple, Google, IBM, Meta (previously as Facebook), Microsoft, Netflix, and SAP.
Over the years several countries or government agencies have been members of the Unicode Consortium.
The Consortium has the ambitious goal of eventually replacing existing character encoding schemes with Unicode and its standard Unicode Transformation Format (UTF) schemes, as many of the existing schemes are limited in size and scope and are incompatible with multilingual environments.
The Unicode Bulldog Award is given to people deemed to be influential in Unicode's development, with recipients including Tatsuo Kobayashi, Thomas Milo, Roozbeh Pournader, Ken Lunde, and Michael Everson.


=== Scripts covered ===

As of September 2025, a total of 172 scripts (alphabets, abugidas and syllabaries) are included in Unicode, covering most major writing systems in use today. There are still scripts that are not yet encoded, particularly those mainly used in historical, liturgical, and academic contexts. Further additions of characters to the already encoded scripts, as well as symbols, in particular for mathematics and music also occur.


=== Proposals for adding scripts ===
The Unicode Roadmap Committee (Michael Everson, Rick McGowan, Ken Whistler, V.S. Umamaheswaran) maintain the list of scripts that are candidates or potential candidates for encoding and their tentative code block assignments on the Unicode Roadmap page of the Unicode Consortium website. For some scripts on the Roadmap, such as Jurchen and Khitan large script, encoding proposals have been made and they are working their way through the approval process. For other scripts, such as Numidian and Rongorongo, no proposal has yet been made, and they await agreement on character repertoire and other details from the user communities involved.
Some modern invented scripts which have not yet been included in Unicode (e.g., Tengwar) or which do not qualify for inclusion in Unicode due to lack of real-world use (e.g., Klingon) are listed in the ConScript Unicode Registry, along with unofficial but widely used private use area code assignments.
There is also a Medieval Unicode Font Initiative focused on special Latin medieval characters. Part of these proposals has been already included in Unicode.

The Script Encoding Initiative (SEI), a project created by Deborah Anderson at the University of California, Berkeley, was founded in 2002 with the goal of funding proposals for scripts not yet encoded in the standard. Now run by Anushah Hossain, SEI has become a major source of proposed additions to the standard in recent years. Although SEI collaborates with the Unicode Consortium and the ISO/IEC 10646 standards process, it operates independently, supporting the technical, linguistic, and historical research needed to prepare formal proposals. SEI maintains a database of scripts that have yet to be encoded in the Unicode Standard on the project's website.


=== Versions ===
The Unicode Consortium together with the ISO have developed a shared repertoire following the initial publication of The Unicode Standard: Unicode and the ISO's Universal Coded Character Set (UCS) use identical character names and code points. However, the Unicode versions do differ from their ISO equivalents in two significant ways.
While the UCS is a simple character map, Unicode specifies the rules, algorithms, and properties necessary to achieve interoperability between different platforms and languages. Thus, The Unicode Standard includes more information, covering in-depth topics such as bitwise encoding, collation, and rendering. It also provides a comprehensive catalog of character properties, including those needed for supporting bidirectional text, as well as visual charts and reference data sets to aid implementers. Previously, The Unicode Standard was sold as a print volume containing the complete core specification, standard annexes, and code charts. However, version 5.0, published in 2006, was the last version printed this way. Starting with version 5.2, only the core specification, published as a print-on-demand paperback, may be purchased. The full text, on the other hand, is published as a free PDF on the Unicode website.
A practical reason for this publication method highlights the second significant difference between the UCS and Unicode—the frequency with which updated versions are released and new characters added. The Unicode Standard has regularly released annual expanded versions, occasionally with more than one version released in a calendar year and with rare cases where the scheduled release had to be postponed. For instance, in April 2020, a month after version 13.0 was published, the Unicode Consortium announced they had changed the intended release date for version 14.0, pushing it back six months to September 2021 due to the COVID-19 pandemic.
Thus far, the following versions of The Unicode Standard have been published. Update versions, which do not include any changes to character repertoire, are signified by the third number (e.g., "version 4.0.1") and are omitted in the table below.


== Architecture and terminology ==


=== Codespace and code points ===
The Unicode Standard defines a codespace: a sequence of integers called code points in the range from 0 to 1114111, notated according to the standard as U+0000–U+10FFFF. The codespace is a systematic, architecture-independent representation of The Unicode Standard; actual text is processed as binary data via one of several Unicode encodings, such as UTF-8.
In this normative notation, the two-character prefix U+ always precedes a written code point, and the code points themselves are written as hexadecimal numbers. At least four hexadecimal digits are always written, with leading zeros prepended as needed. For example, the code point U+00F7 ÷ DIVISION SIGN is padded with two leading zeros, but U+13254 𓉔 EGYPTIAN HIEROGLYPH O004 () is not padded.
There are a total of 1112064 valid code points within the codespace. This number arises from the limitations of the UTF-16 character encoding, which can encode the 216 code points in the range U+0000 through U+FFFF except for the 211 code points in the range U+D800 through U+DFFF, which are used as surrogate pairs to encode the 220 code points in the range U+10000 through U+10FFFF.


=== Code planes and blocks ===

The Unicode codespace is divided into 17 planes, numbered 0 to 16. Plane 0 is the Basic Multilingual Plane (BMP), and contains the most commonly used characters. All code points in the BMP are accessed as a single code unit in UTF-16 encoding and can be encoded in one, two or three bytes in UTF-8. Code points in planes 1 through 16 (the supplementary planes) are accessed as surrogate pairs in UTF-16 and encoded in four bytes in UTF-8.
Within each plane, characters are allocated within named blocks of related characters. The size of a block is always a multiple of 16, and is often a multiple of 128, but is otherwise arbitrary. Characters required for a given script may be spread out over several different, potentially disjunct blocks within the codespace.


=== General Category property ===
Each code point is assigned a classification, listed as the code point's General Category property. Here, at the uppermost level code points are categorized as one of Letter, Mark, Number, Punctuation, Symbol, Separator, or Other. Under each category, each code point is then further subcategorized. In most cases, other properties must be used to adequately describe all the characteristics of any given code point.

The 1024 points in the range U+D800–U+DBFF are known as high-surrogate code points, and code points in the range U+DC00–U+DFFF (1024 code points) are known as low-surrogate code points. A high-surrogate code point followed by a low-surrogate code point forms a surrogate pair in UTF-16 in order to represent code points greater than U+FFFF. In principle, these code points cannot otherwise be used, though in practice this rule is often ignored, especially when not using UTF-16.
A small set of code points are guaranteed never to be assigned to characters, although third-parties may make independent use of them at their discretion. There are 66 of these noncharacters: U+FDD0–U+FDEF and the last two code points in each of the 17 planes (e.g. U+FFFE, U+FFFF, U+1FFFE, U+1FFFF, ..., U+10FFFE, U+10FFFF). The set of noncharacters is stable, and no new noncharacters will ever be defined. Like surrogates, the rule that these cannot be used is often ignored, although the operation of the byte order mark assumes that U+FFFE will never be the first code point in a text. The exclusion of surrogates and noncharacters leaves 1111998 code points available for use.
Private use code points are considered to be assigned, but they intentionally have no interpretation specified by The Unicode Standard such that any interchange of such code points requires an independent agreement between the sender and receiver as to their interpretation. There are three private use areas in the Unicode codespace:

Private Use Area: U+E000–U+F8FF (6400 characters),
Supplementary Private Use Area-A: U+F0000–U+FFFFD (65534 characters),
Supplementary Private Use Area-B: U+100000–U+10FFFD (65534 characters).
Graphic characters are those defined by The Unicode Standard to have particular semantics, either having a visible glyph shape or representing a visible space. As of Unicode 17.0, there are 159629 graphic characters.
Format characters are characters that do not have a visible appearance but may have an effect on the appearance or behavior of neighboring characters. For example, U+200C  ZERO WIDTH NON-JOINER and U+200D  ZERO WIDTH JOINER may be used to change the default shaping behavior of adjacent characters (e.g. to inhibit ligatures or request ligature formation). There are 172 format characters in Unicode 17.0.
65 code points, the ranges U+0000–U+001F and U+007F–U+009F, are reserved as control codes, corresponding to the C0 and C1 control codes as defined in ISO/IEC 6429. U+0009 TAB, U+000A LINE FEED, and U+000D CARRIAGE RETURN are widely used in texts using Unicode. In a phenomenon known as mojibake, the C1 code points are improperly decoded according to the Windows-1252 codepage, previously widely used in Western European contexts.
Together, graphic, format, control code, and private use characters are collectively referred to as assigned characters. Reserved code points are those code points that are valid and available for use, but have not yet been assigned. As of Unicode 17.0, there are 814664 reserved code points.


=== Abstract characters ===

The set of graphic and format characters defined by Unicode does not correspond directly to the repertoire of abstract characters representable under Unicode. Unicode encodes characters by associating an abstract character with a particular code point. However, not all abstract characters are encoded as a single Unicode character, and some abstract characters may be represented in Unicode by a sequence of two or more characters. For example, a Latin small letter "i" with an ogonek, a dot above, and an acute accent, which is required in Lithuanian, is represented by the character sequence U+012F; U+0307; U+0301. Unicode maintains a list of uniquely named character sequences for abstract characters that are not directly encoded in Unicode.
All assigned characters have a unique and immutable name by which they are identified. This immutability has been guaranteed since version 2.0 of The Unicode Standard by its Name Stability policy. In cases where a name is seriously defective and misleading, or has a serious typographical error, a formal alias may be defined that applications are encouraged to use in place of the official character name. For example, U+A015 ꀕ YI SYLLABLE WU has the formal alias YI SYLLABLE ITERATION MARK, and U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET (sic) has the formal alias PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRACKET.


=== Precomposed vis-à-vis composite characters ===
Unicode includes a mechanism for modifying characters that greatly extends the supported repertoire of glyphs. This covers the use of combining diacritical marks that may be added after the base character by the user. Multiple combining diacritics may be simultaneously applied to the same character. Unicode also contains precomposed versions of most letter/diacritic combinations in normal use. These make the conversion to and from legacy encodings simpler, and allow applications to use Unicode as an internal text format without having to implement combining characters. For example, é can be represented in Unicode as U+0065 e LATIN SMALL LETTER E followed by U+0301 ◌́ COMBINING ACUTE ACCENT, and equivalently as the precomposed character U+00E9 é LATIN SMALL LETTER E WITH ACUTE. Thus, users often have multiple equivalent ways of encoding the same character. The mechanism of canonical equivalence within The Unicode Standard ensures the practical interchangeability of these equivalent encodings.
An example of this arises with the Korean alphabet Hangul: Unicode provides a mechanism for composing Hangul syllables from their individual Hangul Jamo subcomponents. However, it also provides 11172 combinations of precomposed syllables made from the most common jamo.
CJK characters presently only have codes for uncomposable radicals and precomposed forms. Most Han characters have either been intentionally composed from, or reconstructed as compositions of, simpler orthographic elements called radicals, so in principle Unicode could have enabled their composition as it did with Hangul. While this could have greatly reduced the number of required code points, as well as allowing the algorithmic synthesis of many arbitrary new characters, the complexities of character etymologies and the post-hoc nature of radical systems add immense complexity to the proposal. Indeed, attempts to design CJK encodings on the basis of composing radicals have been met with difficulties resulting from the reality that Chinese characters do not decompose as simply or as regularly as Hangul does.
The CJK Radicals Supplement block is assigned to the range U+2E80–U+2EFF, and the Kangxi radicals are assigned to U+2F00–U+2FDF. The Ideographic Description Sequences block covers the range U+2FF0–U+2FFB, but The Unicode Standard warns against using its characters as an alternate representation for characters encoded elsewhere:

This process is different from a formal encoding of an ideograph. There is no canonical description of unencoded ideographs; there is no semantic assigned to described ideographs; there is no equivalence defined for described ideographs. Conceptually, ideographic descriptions are more akin to the English phrase "an 'e' with an acute accent on it" than to the character sequence <U+0065, U+0301>.


=== Ligatures ===

Many scripts, including Arabic and Devanāgarī, have special orthographic rules that require certain combinations of letterforms to be combined into special ligature forms. The rules governing ligature formation can be quite complex, requiring special script-shaping technologies such as ACE (Arabic Calligraphic Engine by DecoType in the 1980s and used to generate all the Arabic examples in the printed editions of The Unicode Standard), which became the proof of concept for OpenType (by Adobe and Microsoft), Graphite (by SIL International), or AAT (by Apple).
Instructions are also embedded in fonts to tell the operating system how to properly output different character sequences. A simple solution to the placement of combining marks or diacritics is assigning the marks a width of zero and placing the glyph itself to the left or right of the left sidebearing (depending on the direction of the script they are intended to be used with). A mark handled this way will appear over whatever character precedes it, but will not adjust its position relative to the width or height of the base glyph; it may be visually awkward and it may overlap some glyphs. Real stacking is impossible but can be approximated in limited cases (for example, Thai top-combining vowels and tone marks can just be at different heights to start with). Generally, this approach is only effective in monospaced fonts but may be used as a fallback rendering method when more complex methods fail.


=== Standardized subsets ===
Several subsets of Unicode are standardized: Microsoft Windows since Windows NT 4.0 supports WGL-4 with 657 characters, which is considered to support all contemporary European languages using the Latin, Greek, or Cyrillic script. Other standardized subsets of Unicode include the Multilingual European Subsets: MES-1 (Latin scripts only; 335 characters), MES-2 (Latin, Greek, and Cyrillic; 1062 characters) and MES-3A & MES-3B (two larger subsets, not shown here). MES-2 includes every character in MES-1 and WGL-4.
The standard DIN 91379 specifies a subset of Unicode letters, special characters, and sequences of letters and diacritic signs to allow the correct representation of names and to simplify data exchange in Europe. This standard supports all of the official languages of all European Union countries, as well as the German minority languages and the official languages of Iceland, Liechtenstein, Norway, and Switzerland. To allow the transliteration of names in other writing systems to the Latin script according to the relevant ISO standards, all necessary combinations of base letters and diacritic signs are provided.

Rendering software that cannot process a Unicode character appropriately often displays it as an open rectangle, or as U+FFFD to indicate the position of the unrecognized character. Some systems have made attempts to provide more information about such characters. Apple's Last Resort font will display a substitute glyph indicating the Unicode range of the character, and the SIL International's fallback font will display a box showing the hexadecimal scalar value of the character.


=== Mapping and encodings ===
Several mechanisms have been specified for storing a series of code points as a series of bytes.
Unicode defines two mapping methods: the Unicode Transformation Format (UTF) encodings, and the Universal Coded Character Set (UCS) encodings. An encoding maps the range of Unicode code points to sequences of values in some fixed-size range, termed code units, each code point to a unique sequence. The numbers in the names of the encodings indicate the number of bits per code unit (for UTF encodings) or the number of bytes per code unit (for UCS encodings and UTF-1). UTF-8 and UTF-16 are the most commonly used encodings. UCS-2 is an obsolete subset of UTF-16; UCS-4 and UTF-32 are functionally equivalent.
UTF encodings include:

UTF-8, which uses one to four 8-bit units per code point, and has maximal compatibility with ASCII
UTF-16, which uses one 16-bit unit per code point below U+010000, and a surrogate pair of two 16-bit units per code point in the range U+010000 to U+10FFFF
UTF-32, which uses one 32-bit unit per code point
UTF-EBCDIC, not specified as part of The Unicode Standard, which uses one to five 8-bit units per code point, intended to maximize compatibility with EBCDIC
UTF-8 uses one to four 8-bit units (bytes) per code point and, being compact for Latin scripts and ASCII-compatible, provides the de facto standard encoding for the interchange of Unicode text. It is used by FreeBSD and most recent Linux distributions as a direct replacement for legacy encodings in general text handling.
The UCS-2 and UTF-16 encodings specify the Unicode byte order mark (BOM) for use at the beginnings of text files, which may be used for byte-order detection (or byte endianness detection). The BOM, encoded as U+FEFF  ZERO WIDTH NO-BREAK SPACE, has the important property of unambiguity on byte reorder, regardless of the Unicode encoding used; U+FFFE (the result of byte-swapping U+FEFF) does not equate to a legal character, and U+FEFF in places other than the beginning of text conveys the zero-width non-break space.
The same character converted to UTF-8 becomes the byte sequence EF BB BF. The Unicode Standard allows the BOM "can serve as a signature for UTF-8 encoded text where the character set is unmarked". Some software developers have adopted it for other encodings, including UTF-8, in an attempt to distinguish UTF-8 from local 8-bit code pages. However RFC 3629, the UTF-8 standard, recommends that byte order marks be forbidden in protocols using UTF-8, but discusses the cases where this may not be possible. In addition, the large restriction on possible patterns in UTF-8 (for instance there cannot be any lone bytes with the high bit set) means that it should be possible to distinguish UTF-8 from other character encodings without relying on the BOM.
In UTF-32 and UCS-4, one 32-bit code unit serves as a fairly direct representation of any character's code point (although the endianness, which varies across different platforms, affects how the code unit manifests as a byte sequence). In the other encodings, each code point may be represented by a variable number of code units. UTF-32 is widely used as an internal representation of text in programs (as opposed to stored or transmitted text), since every Unix operating system that uses the GCC compilers to generate software uses it as the standard "wide character" encoding. Recent versions of the Python programming language (beginning with 2.2) may also be configured to use UTF-32 as the representation for Unicode strings, effectively disseminating such encoding in high-level coded software.
Punycode, another encoding form, enables the encoding of Unicode strings into the limited character set supported by the ASCII-based Domain Name System (DNS). The encoding is used as part of IDNA, which is a system enabling the use of Internationalized Domain Names in all scripts that are supported by Unicode. Earlier and now historical proposals include UTF-5 and UTF-6.
GB18030 is another encoding form for Unicode, from the Standardization Administration of China. It is the official character set of the People's Republic of China (PRC). BOCU-1 and SCSU are Unicode compression schemes. The April Fools' Day RFC of 2005 specified two parody UTF encodings, UTF-9 and UTF-18.


== Adoption ==

Unicode, in the form of UTF-8, has been the most common encoding for the World Wide Web since 2008. It has near-universal adoption, and much of the non-UTF-8 content is found in other Unicode encodings, e.g. UTF-16. As of 2024, UTF-8 accounts for on average 98.3% of all web pages (and 983 of the top 1,000 highest-ranked web pages). Although many pages only use ASCII characters to display content, UTF-8 was designed with 8-bit ASCII as a subset and almost no websites now declare their encoding to only be ASCII instead of UTF-8. Over a third of the languages tracked have 100% UTF-8 use.
All internet protocols maintained by Internet Engineering Task Force, e.g. File Transfer Protocol (FTP), have required support for UTF-8 since the publication of RFC 2277 in 1998, which specified that all IETF protocols "MUST be able to use the UTF-8 charset".


=== Operating systems ===
Unicode has become the dominant scheme for the internal processing and storage of text. Although a great deal of text is still stored in legacy encodings, Unicode is used almost exclusively for building new information processing systems. Early adopters tended to use UCS-2 (the fixed-length two-byte obsolete precursor to UTF-16) and later moved to UTF-16 (the variable-length current standard), as this was the least disruptive way to add support for non-BMP characters. The best known such system is Windows NT (and its descendants, 2000, XP, Vista, 7, 8, 10, and 11), which uses UTF-16 as the sole internal character encoding. The Java and .NET bytecode environments, macOS, and KDE also use it for internal representation. Partial support for Unicode can be installed on Windows 9x through the Microsoft Layer for Unicode.
UTF-8 (originally developed for Plan 9) has become the main storage encoding on most Unix-like operating systems (though others are also used by some libraries) because it is a relatively easy replacement for traditional extended ASCII character sets. UTF-8 is also the most common Unicode encoding used in HTML documents on the World Wide Web.
Multilingual text-rendering engines which use Unicode include Uniscribe and DirectWrite for Microsoft Windows, ATSUI and Core Text for macOS, and Pango for GTK+ and the GNOME desktop.


=== Input methods ===

Because keyboard layouts cannot have simple key combinations for all characters, several operating systems provide alternative input methods that allow access to the entire repertoire.
ISO/IEC 14755, which standardises methods for entering Unicode characters from their code points, specifies several methods. There is the Basic method, where a beginning sequence is followed by the hexadecimal representation of the code point and the ending sequence. There is also a screen-selection entry method specified, where the characters are listed in a table on a screen, such as with a character map program.
Online tools for finding the code point for a known character include Unicode Lookup by Jonathan Hedley and Shapecatcher by Benjamin Milde. In Unicode Lookup, one enters a search key (e.g. "fractions"), and a list of corresponding characters with their code points is returned. In Shapecatcher, based on Shape context, one draws the character in a box and a list of characters approximating the drawing, with their code points, is returned.


=== Email ===

MIME defines two different mechanisms for encoding non-ASCII characters in email, depending on whether the characters are in email headers (such as the "Subject:"), or in the text body of the message; in both cases, the original character set is identified as well as a transfer encoding. For email transmission of Unicode, the UTF-8 character set and the Base64 or the Quoted-printable transfer encoding are recommended, depending on whether much of the message consists of ASCII characters. The details of the two different mechanisms are specified in the MIME standards and generally are hidden from users of email software.
The IETF has defined a framework for internationalized email using UTF-8, and has updated several protocols in accordance with that framework.
The adoption of Unicode in email has been very slow. Some East Asian text is still encoded in encodings such as ISO-2022, and some devices, such as mobile phones, still cannot correctly handle Unicode data. Support has been improving, however. Many major free mail providers such as Yahoo! Mail, Gmail, and Outlook.com support it.


=== Web ===

All W3C recommendations have used Unicode as their document character set since HTML 4.0. Web browsers have supported Unicode, especially UTF-8, for many years. There used to be display problems resulting primarily from font related issues; e.g. v6 and older of Microsoft Internet Explorer did not render many code points unless explicitly told to use a font that contains them.
Although syntax rules may affect the order in which characters are allowed to appear, XML (including XHTML) documents, by definition, comprise characters from most of the Unicode code points, with the exception of:

FFFE or FFFF.
most of the C0 control codes,
the permanently unassigned code points D800–DFFF,
HTML characters manifest either directly as bytes according to the document's encoding, if the encoding supports them, or users may write them as numeric character references based on the character's Unicode code point. For example, the references &#916;, &#1049;, &#1511;, &#1605;, &#3671;, &#12354;, &#21494;, &#33865;, and &#47568; (or the same numeric values expressed in hexadecimal, with &#x as the prefix) should display on all browsers as Δ, Й, ק ,م, ๗, あ, 叶, 葉, and 말.
When specifying URIs, for example as URLs in HTTP requests, non-ASCII characters must be percent-encoded.


=== Fonts ===

Unicode is not in principle concerned with fonts per se, seeing them as implementation choices. Any given character may have many allographs, from the more common bold, italic and base letterforms to complex decorative styles. A font is "Unicode compliant" if the glyphs in the font can be accessed using code points defined in The Unicode Standard. The standard does not specify a minimum number of characters that must be included in the font; some fonts have quite a small repertoire.
Free and retail fonts based on Unicode are widely available, since TrueType and OpenType support Unicode (and Web Open Font Format (WOFF and WOFF2) is based on those). These font formats map Unicode code points to glyphs, but OpenType and TrueType font files are restricted to 65,535 glyphs. Collection files provide a "gap mode" mechanism for overcoming this limit in a single font file. (Each font within the collection still has the 65,535 limit, however.) A TrueType Collection file would typically have a file extension of ".ttc".
Thousands of fonts exist on the market, but fewer than a dozen fonts—sometimes described as "pan-Unicode" fonts—attempt to support the majority of Unicode's character repertoire. Instead, Unicode-based fonts typically focus on supporting only basic ASCII and particular scripts or sets of characters or symbols. Several reasons justify this approach: applications and documents rarely need to render characters from more than one or two writing systems; fonts tend to demand resources in computing environments; and operating systems and applications show increasing intelligence in regard to obtaining glyph information from separate font files as needed, i.e., font substitution. Furthermore, designing a consistent set of rendering instructions for tens of thousands of glyphs constitutes a monumental task; such a venture passes the point of diminishing returns for most typefaces.


=== Newlines ===
Unicode partially addresses the newline problem that occurs when trying to read a text file on different platforms. Unicode defines a large number of characters that conforming applications should recognize as line terminators.
In terms of the newline, Unicode introduced U+2028  LINE SEPARATOR and U+2029  PARAGRAPH SEPARATOR. This was an attempt to provide a Unicode solution to encoding paragraphs and lines semantically, potentially replacing all of the various platform solutions. In doing so, Unicode does provide a way around the historical platform-dependent solutions. Nonetheless, few if any Unicode solutions have adopted these Unicode line and paragraph separators as the sole canonical line ending characters. However, a common approach to solving this issue is through newline normalization. This is achieved with the Cocoa text system in macOS and also with W3C XML and HTML recommendations. In this approach, every possible newline character is converted internally to a common newline (which one does not really matter since it is an internal operation just for rendering). In other words, the text system can correctly treat the character as a newline, regardless of the input's actual encoding.


== Issues ==


=== Character unification ===


==== Han unification ====

The Ideographic Research Group (IRG) is tasked with advising the Consortium and ISO regarding Han unification, or Unihan, especially the further addition of CJK unified and compatibility ideographs to the repertoire. The IRG is composed of experts from each region that has historically used Chinese characters. However, despite the deliberation within the committee, Han unification has consistently been one of the most contested aspects of The Unicode Standard since the genesis of the project.
Existing character set standards such as the Japanese JIS X 0208 (encoded by Shift JIS) defined unification criteria, meaning rules for determining when a variant Chinese character is to be considered a handwriting/font difference (and thus unified), versus a spelling difference (to be encoded separately). Unicode's character model for CJK characters was based on the unification criteria used by JIS X 0208, as well as those developed by the Association for a Common Chinese Code in China.
Due to the standard's principle of encoding semantic instead of stylistic variants, Unicode has received criticism for not assigning code points to certain rare and archaic kanji variants, possibly complicating processing of ancient and uncommon Japanese names. Since it places particular emphasis on Chinese, Japanese and Korean sharing many characters in common, Han unification is also sometimes perceived as treating the three as the same thing. Regional differences in the expected forms of characters, in terms of typographical conventions and curricula for handwriting, do not always fall along language boundaries: although Hong Kong and Taiwan both write Chinese languages using Traditional Chinese characters, the preferred forms of characters differ between Hong Kong and Taiwan in some cases.
Less-frequently-used alternative encodings exist, often predating Unicode, with character models differing from this paradigm, aimed at preserving the various stylistic differences between regional and/or nonstandard character forms. One example is the TRON Code favored by some users for handling historical Japanese text, though not widely adopted among the Japanese public. Another is the CCCII encoding adopted by library systems in Hong Kong, Taiwan and the United States. These have their own drawbacks in general use, leading to the Big5 encoding (introduced in 1984, four years after CCCII) having become more common than CCCII outside of library systems. Although work at Apple based on Research Libraries Group's CJK Thesaurus, which was used to maintain the EACC variant of CCCII, was one of the direct predecessors of Unicode's Unihan set, Unicode adopted the JIS-style unification model.
The earliest version of Unicode had a repertoire of fewer than 21,000 Han characters, largely limited to those in relatively common modern usage. As of version 17.0, the standard now encodes more than 101,000 Han characters, and work is continuing to add thousands more—largely historical and dialectal variant characters used throughout the Sinosphere.
Modern typefaces provide a means to address some of the practical issues in depicting unified Han characters with various regional graphical representations. The 'locl' OpenType table allows a renderer to select a different glyph for each code point based on the text locale. The Unicode variation sequences can also provide in-text annotations for a desired glyph selection; this requires registration of the specific variant in the Ideographic Variation Database.


==== Italic or cursive characters in Cyrillic ====

If the appropriate glyphs for characters in the same script differ only in the italic, Unicode has generally unified them, as can be seen in the comparison among a set of seven characters' italic glyphs as typically appearing in Russian, traditional Bulgarian, Macedonian, and Serbian texts at right, meaning that the differences are displayed through smart font technology or manually changing fonts. The same OpenType 'locl' technique is used.


==== Localised case pairs ====
For use in the Turkish alphabet and Azeri alphabet, Unicode includes a separate dotless lowercase I (ı) and a dotted uppercase I (İ). However, the usual ASCII letters are used for the lowercase dotted i and the uppercase dotless I, matching how they are handled in the earlier ISO 8859-9. As such, case-insensitive comparisons for those languages have to use different rules than case-insensitive comparisons for other languages using the Latin script. This can have security implications if, for example, sanitization code or access control relies on case-insensitive comparison.
By contrast, the Icelandic eth (ð), the barred D (đ) and the retroflex D (ɖ), which usually look the same in uppercase (Đ), are given the opposite treatment, and encoded separately in both letter-cases (in contrast to the earlier ISO 6937, which unifies the uppercase forms). Although it allows for case-insensitive comparison without needing to know the language of the text, this approach also has issues, requiring security measures relating to homoglyph attacks.


==== Diacritics on lowercase I ====

Whether the lowercase letter I is expected to retain its tittle when a diacritic applies also depends on local conventions.


=== Security ===
Unicode has a large number of homoglyphs, many of which look very similar or identical to ASCII letters. Substitution of these can make an identifier or URL that looks correct, but directs to a different location than expected. Additionally, homoglyphs can also be used for manipulating the output of natural language processing (NLP) systems. Mitigation requires disallowing these characters, displaying them differently, or requiring that they resolve to the same identifier; all of this is complicated due to the huge and constantly changing set of characters.
A security advisory was released in 2021 by two researchers, one from the University of Cambridge and the other from the University of Edinburgh, in which they assert that the BiDi marks can be used to make large sections of code do something different from what they appear to do. The problem was named "Trojan Source". In response, code editors started highlighting marks to indicate forced text-direction changes.
The UTF-8 and UTF-16 encodings do not accept all possible sequences of code units. Implementations vary in what they do when reading an invalid sequence, which has led to security bugs.


=== Mapping to legacy character sets ===
Unicode was designed to provide code-point-by-code-point round-trip format conversion to and from any preexisting character encodings, so that text files in older character sets can be converted to Unicode and then back and get back the same file, without employing context-dependent interpretation. That has meant that inconsistent legacy architectures, such as combining diacritics and precomposed characters, both exist in Unicode, giving more than one method of representing some text. This is most pronounced in the three different encoding forms for Korean Hangul. Since version 3.0, any precomposed characters that can be represented by a combined sequence of already existing characters can no longer be added to the standard to preserve interoperability between software using different versions of Unicode.
Injective mappings must be provided between characters in existing legacy character sets and characters in Unicode to facilitate conversion to Unicode and allow interoperability with legacy software. Lack of consistency in various mappings between earlier Japanese encodings such as Shift-JIS or EUC-JP and Unicode led to round-trip format conversion mismatches, particularly the mapping of the character JIS X 0208 '～' (1-33, WAVE DASH), heavily used in legacy database data, to either U+FF5E ～ FULLWIDTH TILDE (in Microsoft Windows) or U+301C 〜 WAVE DASH (other vendors).
Some Japanese computer programmers objected to Unicode because it requires them to separate the use of U+005C \ REVERSE SOLIDUS (backslash) and U+00A5 ¥ YEN SIGN, which was mapped to 0x5C in JIS X 0201, and a lot of legacy code exists with this usage. (This encoding also replaces tilde '~' 0x7E with macron '¯', now 0xAF.) The separation of these characters exists in ISO 8859-1, from long before Unicode.


=== Indic scripts ===

Indic scripts such as Tamil and Devanagari are each allocated only 128 code points, matching the ISCII standard. The correct rendering of Unicode Indic text requires transforming the stored logical order characters into visual order and the forming of ligatures (also known as conjuncts) out of components. Some local scholars argued in favor of assignments of Unicode code points to these ligatures, going against the practice for other writing systems, though Unicode contains some Arabic and other ligatures for backward compatibility purposes only. Encoding of any new ligatures in Unicode will not happen, in part, because the set of ligatures is font-dependent, and Unicode is an encoding independent of font variations. The same kind of issue arose for the Tibetan script in 2003 when the Standardization Administration of China proposed encoding 956 precomposed Tibetan syllables, but these were rejected for encoding by the relevant ISO committee (ISO/IEC JTC 1/SC 2).
Thai alphabet support has been criticized for its ordering of Thai characters. The vowels เ, แ, โ, ใ, ไ that are written to the left of the preceding consonant are in visual order instead of phonetic order, unlike the Unicode representations of other Indic scripts. This complication is due to Unicode inheriting the Thai Industrial Standard 620, which worked in the same way, and was the way in which Thai had always been written on keyboards. This ordering problem complicates the Unicode collation process slightly, requiring table lookups to reorder Thai characters for collation. Even if Unicode had adopted encoding according to spoken order, it would still be problematic to collate words in dictionary order. E.g., the word แสดง [sa dɛːŋ] "perform" starts with a consonant cluster "สด" (with an inherent vowel for the consonant "ส"), the vowel แ-, in spoken order would come after the ด, but in a dictionary, the word is collated as it is written, with the vowel following the ส.


=== Combining characters ===

Characters with diacritical marks can generally be represented either as a single precomposed character or as a decomposed sequence of a base letter plus one or more non-spacing marks. For example, ḗ (precomposed e with macron and acute above) and ḗ (e followed by the combining macron above and combining acute above) should be rendered identically, both appearing as an e with a macron (◌̄) and acute accent (◌́), but in practice, their appearance may vary depending upon what rendering engine and fonts are being used to display the characters. Similarly, underdots, as needed in the romanization of Indic languages, will often be placed incorrectly. Unicode characters that map to precomposed glyphs can be used in many cases, thus avoiding the problem, but where no precomposed character has been encoded, the problem can often be solved by using a specialist Unicode font such as Charis SIL that uses Graphite, OpenType ('gsub'), or AAT technologies for advanced rendering features.


=== Anomalies ===

The Unicode Standard has imposed rules intended to guarantee stability. Depending on the strictness of a rule, a change can be prohibited or allowed. For example, a "name" given to a code point cannot and will not change. But a "script" property is more flexible, by Unicode's own rules. In version 2.0, Unicode changed many code point "names" from version 1. At the same moment, Unicode stated that, thenceforth, an assigned name to a code point would never change. This implies that when mistakes are published, these mistakes cannot be corrected, even if they are trivial (as happened in one instance with the spelling BRAKCET for BRACKET in a character name). In 2006 a list of anomalies in character names was first published, and, as of June 2021, there were 104 characters with identified issues, for example:

U+034F ͏ COMBINING GRAPHEME JOINER: Does not join graphemes.
U+2118 ℘ SCRIPT CAPITAL P: This is a small letter. The capital is U+1D4AB 𝒫 MATHEMATICAL SCRIPT CAPITAL P.
U+A015 ꀕ YI SYLLABLE WU: This is not a Yi syllable, but a Yi iteration mark.
U+FE18 ︘ PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET: bracket is spelled incorrectly. (Spelling errors are resolved by using Unicode alias names.)
While Unicode defines the script designator (name) to be "Phags_Pa", in that script's character names, a hyphen is added: U+A840 ꡀ PHAGS-PA LETTER KA. This, however, is not an anomaly, but the rule: hyphens are replaced by underscores in script designators.


== See also ==
Comparison of Unicode encodings
International Components for Unicode (ICU), now as ICU-TC a part of Unicode
List of binary codes
List of Unicode characters
List of XML and HTML character entity references
Lotus Multi-Byte Character Set (LMBCS), a parallel development with similar intentions
Open-source Unicode typefaces
Religious and political symbols in Unicode
Standards related to Unicode
Unicode symbol
Universal Coded Character Set


== Notes ==


== References ==


== Further reading ==

Haralambous, Yannis; Martin Dürst (2019). "Unicode from a Linguistic Point of View". In Haralambous, Yannis (ed.). Proceedings of Graphemics in the 21st Century, Brest 2018. Brest: Fluxus Editions. pp. 167–183. doi:10.36824/2018-graf-hara1. ISBN 978-2-9570549-1-6.


== External links ==

Unicode, Inc.
Unicode Technical Site
The Unicode Standard
Unicode Character Code Charts
Unicode Character Name Index
Alan Wood's Unicode Resources –  contains lists of word processors with Unicode capability; fonts and characters are grouped by type; characters are presented in lists, not grids.
Unicode BMP Fallback Font – displays the Unicode 6.1 value of any character in a document, including in the Private Use Area, rather than the glyph itself.
The World's Writing Systems, all 293 known writing systems with their Unicode status (128 not yet encoded as of June 2024)
