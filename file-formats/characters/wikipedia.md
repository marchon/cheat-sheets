# Character (computing)

Cloned from https://en.wikipedia.org/wiki/Character_(computing).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 73443.

In computing and telecommunications, a character is the encoded representation of a natural language character (including letter, numeral and punctuation), whitespace (space or tab), or a control character (controls computer hardware that consumes character-based data). A sequence of characters is called a string.
Some character encoding systems represent each character using a fixed number of bits whereas other systems use varying sizes. Various fixed-length sizes were used for now obsolete systems such as the six-bit character code, the five-bit Baudot code and even 4-bit systems (with only 16 possible values). The more modern ASCII system uses the 8-bit byte for each character. Today, the Unicode-based UTF-8 encoding uses a varying number of byte-sized code units to define a code point which combine to encode a character.


== Terminology ==


=== Character ===
In general, a character is a symbol (such as a letter or number) that represents information, and in the context of computing is a representation of such a symbol that may be accepted by a computer. A character implies an encoding of information, often as defined by a standard such as ANSI or Unicode.


=== Character set ===
A character set identifies a repertoire of characters that are each mapped to a unique numeric value.


=== Glyph ===
Glyph describes a particular visual appearance of a character. Many computer fonts consist of glyphs that are indexed by the numerical code of the corresponding character.
With the advent and widespread acceptance of Unicode and bit-agnostic coded character sets, a character is increasingly being seen as a unit of information, independent of any particular visual manifestation. The ISO/IEC 10646 (Unicode) International Standard defines character, or abstract character as "a member of a set of elements used for the organization, control, or representation of data". Unicode's definition supplements this with explanatory notes that encourage the reader to differentiate between characters, graphemes, and glyphs, among other things. Such differentiation is an instance of the wider theme of the separation of presentation and content.
For example, the Hebrew letter aleph ("א") is often used by mathematicians to denote certain kinds of infinity (ℵ), but it is also used in ordinary Hebrew text. In Unicode, these two uses are considered different characters, and have two different Unicode numerical identifiers ("code points"), though they may be rendered identically. Conversely, the Chinese logogram for water ("水") may have a slightly different appearance in Japanese texts than it does in Chinese texts, and local typefaces may reflect this. But nonetheless in Unicode they are considered the same character, and share the same code point.
The Unicode standard differentiates between these abstract characters and coded characters or encoded characters that have been paired with numeric codes that facilitate their representation in computers.


=== Combining character ===
The combining character is addressed by Unicode which allocates a code point to each of:

'i ' (U+0069),
the combining diaeresis (U+0308), and
'ï' (U+00EF).
This makes it possible to code the middle character of the word 'naïve' either as a single character 'ï' or as a combination of the character 'i ' with the combining diaeresis: (U+0069 LATIN SMALL LETTER I + U+0308 COMBINING DIAERESIS); this is also rendered as 'ï '.


== char ==

In C, char (short for character) is a data type with size one byte, but unlike the de facto size of byte as 8 bits, this use of byte is less specific. Byte is defined to be large enough to contain any member of the "basic execution character set". The number of bits used by a compiler is accessible via the CHAR_BIT macro. By far the most common size is 8 bits, and POSIX requires it to be 8 bits. In modern C standards, char is required to hold UTF-8 code units which requires a minimum size of 8 bits.
Since a Unicode code point may require as many as 21 bits. the char type is generally not large enough for every character. Nonetheless, the char type is well-suited for the UTF-8 encoding where each code point requires 1 to 4 bytes.
The fact that a character was historically stored in a single byte has led to the terms "char" and "character" being used interchangeably and this leads to confusion today when multibyte encodings such as UTF-8 are used. Modern POSIX documentation attempts to fix this by defining "character" as a sequence of one or more bytes representing a single graphic symbol or control code, and uses "byte" when referring to char data. However it still contains errors such as defining an array of char as a character array (rather than a byte array).
Unicode can be stored in strings of code units that are larger than char called wide characters. The original C type was called wchar_t. Due to some platforms defining wchar_t as 16 bits and others defining it as 32 bits, current versions provide unambiguous char16_t and char32_t. Even then the objects being stored might not be characters, for instance the variable-length UTF-16 is often stored in arrays of char16_t.
Other languages also have a char type. Many, including C++, use 8-bit bytes like C. Others, such as Java, use 2-byte, wide storage to more directly accommodate UTF-16.


== See also ==
Character (symbol) – Character as a semiotic sign or symbol
Character literal – Type of literal in programming
Combining character – Non-spacing character that modifies another character
Fill character
Homoglyph – Different glyphs which are visually similar
Universal Character Set characters – Complete list of the characters available on most computers


== References ==


== External links ==
Characters: A Brief Introduction by The Linux Information Project (LINFO)
ISO/IEC TR 15285:1998 summarizes the ISO/IEC's character model, focusing on terminology definitions and differentiating between characters and glyphs
