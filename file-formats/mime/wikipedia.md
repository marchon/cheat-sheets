# MIME

Cloned from https://en.wikipedia.org/wiki/MIME.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 19045.

Multipurpose Internet Mail Extensions (MIME) is a standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, images, and application programs. Message bodies may consist of multiple parts, and header information may be specified in non-ASCII character sets. Email messages with MIME formatting are typically transmitted with standard protocols, such as the Simple Mail Transfer Protocol (SMTP), the Post Office Protocol (POP), and the Internet Message Access Protocol (IMAP).
MIME is an Internet standard – specified in the following request for comments (RFC) publications: RFC 2045,
RFC 2046,
RFC 2047,
RFC 4288,
RFC 4289 and 
RFC 2049. The integration with SMTP email is specified in 
RFC 1521 and 
RFC 1522.
Although the MIME formalism was designed mainly for SMTP, its content types are also important in other communication protocols. In the Hypertext Transfer Protocol (HTTP) for the World Wide Web, servers insert a MIME header field at the beginning of any Web transmission. Clients use the content type header to select an appropriate viewer application for the type of data indicated.


== History ==
MIME originated from the Andrew Messaging System, which was part of Andrew Project developed at Carnegie Mellon University (CMU), as a cross-platform alternative to the Andrew-specific data format.


== MIME header fields ==


=== MIME-Version ===
The presence of this header field indicates the message is MIME-formatted. The value is typically "1.0". The field appears as follows:

MIME-Version: 1.0

According to MIME co-creator Nathaniel Borenstein, the version number was introduced to permit changes to the MIME protocol in subsequent versions. However, Borenstein admitted short-comings in the specification that hindered the implementation of this feature:

We did not adequately specify how to handle a future MIME version. ... So if you write something that knows 1.0, what should you do if you encounter 2.0 or 1.1? I sort of thought it was obvious but it turned out everyone implemented that in different ways. And the result is that it would be just about impossible for the Internet to ever define a 2.0 or a 1.1.


=== Content-Disposition ===
The original MIME specifications only described the structure of mail messages. They did not address the issue of presentation styles. The content-disposition header field was added in RFC 2183 to specify the presentation style. A MIME part can have:

an inline content disposition, which means that it should be automatically displayed when the message is displayed, or
an attachment content disposition, in which case it is not displayed automatically and requires some form of action from the user to open it.
In addition to the presentation style, the field Content-Disposition also provides parameters for specifying the name of the file, the creation date and modification date, which can be used by the reader's mail user agent to store the attachment.
The following example is taken from RFC 2183, where the header field is defined:

Content-Disposition: attachment; filename=genome.jpeg;
  modification-date="Wed, 12 Feb 1997 16:29:51 -0500";

The filename may be encoded as defined in RFC 2231.
As of 2010, a majority of mail user agents did not follow this prescription fully. The widely used Mozilla Thunderbird mail client ignores the content-disposition fields in the messages and uses independent algorithms for selecting the MIME parts to display automatically. Thunderbird prior to version 3 also sends out newly composed messages with inline content disposition for all MIME parts. Most users are unaware of how to set the content disposition to attachment. Many mail user agents also send messages with the file name in the name parameter of the content-type header instead of the filename parameter of the header field Content-Disposition. This practice is discouraged, as the file name should be specified either with the parameter filename, or with both the parameters filename and name.
In HTTP, the response header field Content-Disposition: attachment is usually used as a hint to the client to present the response body as a downloadable file. Typically, when receiving such a response, a Web browser prompts the user to save its content as a file, instead of displaying it as a page in a browser window, with filename suggesting the default file name.


=== Content-Transfer-Encoding ===
In June 1992, MIME (RFC 1341, since made obsolete by RFC 2045) defined a set of methods for representing binary data in formats other than ASCII text format. The content-transfer-encoding: MIME header field has 2-sided significance:

It indicates whether or not a binary-to-text encoding scheme has been used on top of the original encoding as specified within the Content-Type header:
If such a binary-to-text encoding method has been used, it states which one.
If not, it provides a descriptive label for the format of content, with respect to the presence of 8-bit or binary content.
The RFC and the IANA's list of transfer encodings define the values shown below, which are not case sensitive. '7bit', '8bit', and 'binary' mean that no binary-to-text encoding on top of the original encoding was used. In these cases, the header field is actually redundant for the email client to decode the message body, but it may still be useful as an indicator of what type of object is being sent. Values 'quoted-printable' and 'base64' tell the email client that a binary-to-text encoding scheme was used and that appropriate initial decoding is necessary before the message can be read with its original encoding (e.g. UTF-8).

Suitable for use with normal SMTP:
7bit – up to 998 octets per line of the code range 1..127 with CR and LF (codes 13 and 10 respectively) only allowed to appear as part of a CRLF line ending. This is the default value.
quoted-printable – used to encode arbitrary octet sequences into a form that satisfies the rules of 7bit. Designed to be efficient and mostly human-readable when used for text data consisting primarily of US-ASCII characters but also containing a small proportion of bytes with values outside that range.
base64 – used to encode arbitrary octet sequences into a form that satisfies the rules of 7bit. Designed to be efficient for non-text 8 bit and binary data. Sometimes used for text data that frequently uses non-US-ASCII characters.
Suitable for use with SMTP servers that support the 8BITMIME SMTP extension (RFC 6152):
8bit – up to 998 octets per line with CR and LF (codes 13 and 10 respectively) only allowed to appear as part of a CRLF line ending.
Suitable for use with SMTP servers that support the BINARYMIME SMTP extension (RFC 3030):
binary – any sequence of octets.
There is no encoding defined which is explicitly designed for sending arbitrary binary data through SMTP transports with the 8BITMIME extension. Thus, if BINARYMIME isn't supported, base64 or quoted-printable (with their associated inefficiency) are sometimes still useful. This restriction does not apply to other uses of MIME such as Web Services with MIME attachments or MTOM.


== Encoded-Word ==
Since RFC 2822, conforming message header field names and values use ASCII characters; values that contain non-ASCII data should use the MIME encoded-word syntax (RFC 2047) instead of a literal string. This syntax uses a string of ASCII characters indicating both the original character encoding (the "charset") and the content-transfer-encoding used to map the bytes of the charset into ASCII characters.
The form is: "=?charset?encoding?encoded text?=".

charset may be any character set registered with IANA. Typically it would be the same charset as the message body.
encoding can be either "Q" denoting Q-encoding that is similar to the quoted-printable encoding, or "B" denoting base64 encoding.
encoded text is the Q-encoded or base64-encoded text.
An encoded-word may not be more than 75 characters long, including charset, encoding, encoded text, and delimiters. If it is desirable to encode more text than will fit in an encoded-word of 75 characters, multiple encoded-words (separated by CRLF SPACE) may be used.


=== Difference between Q-encoding and quoted-printable ===
The ASCII codes for the question mark ("?") and equals sign ("=") may not be represented directly as they are used to delimit the encoded word. The ASCII code for space may not be represented directly because it could cause older parsers to split up the encoded word undesirably. To make the encoding smaller and easier to read the underscore is used to represent the ASCII code for space creating the side effect that underscore cannot be represented directly. The use of encoded words in certain parts of header fields imposes further restrictions on which characters may be represented directly.
For example,
Subject: =?iso-8859-1?Q?=A1Hola,_se=F1or!?=
is interpreted as "Subject: ¡Hola, señor!".
The encoded-word format is not used for the names of the headers fields (for example Subject). These names are usually English terms and always in ASCII in the raw message. When viewing a message with a non-English email client, the header field names might be translated by the client.


== Multipart messages ==
The MIME multipart message contains a boundary in the header field Content-Type:; this boundary, which must not occur in any of the parts, is placed between the parts, and at the beginning and end of the body of the message, as follows:

Each part consists of its own content header (zero or more Content- header fields) and a body. Multipart content can be nested. The Content-Transfer-Encoding of a multipart type must always be "7bit", "8bit" or "binary" to avoid the complications that would be posed by multiple levels of decoding. The multipart block as a whole does not have a charset; non-ASCII characters in the part headers are handled by the Encoded-Word system, and the part bodies can have charsets specified if appropriate for their content-type.
Notes:

Before the first boundary is an area that is ignored by MIME-compliant clients. This area is generally used to put a message to users of old non-MIME clients.
It is up to the sending mail client to choose a boundary string that doesn't clash with the body text. Typically this is done by inserting a long random string.
The last boundary must have two hyphens at the end.


=== Multipart subtypes ===
The MIME standard defines various multipart-message subtypes, which specify the nature of the message parts and their relationship to one another. The subtype is specified in the Content-Type header field of the overall message. For example, a multipart MIME message using the digest subtype would have its Content-Type set as "multipart/digest".
The RFC initially defined four subtypes: mixed, digest, alternative and parallel. A minimally compliant application must support mixed and digest; other subtypes are optional. Applications must treat unrecognized subtypes as "multipart/mixed". Additional subtypes, such as signed and form-data, have since been separately defined in other RFCs.


==== mixed ====
multipart/mixed is used for sending files with different Content-Type header fields inline (or as attachments). If sending pictures or other easily readable files, most mail clients will display them inline (unless explicitly specified with Content-Disposition: attachment in which case offered as attachments). The default content-type for each part is "text/plain".
The type is defined in RFC 2046.


==== digest ====
multipart/digest is a simple way to send multiple text messages. The default content-type for each part is "message/rfc822".
The MIME type is defined in RFC 2046.


==== alternative ====
The multipart/alternative subtype indicates that each part is an "alternative" version of the same (or similar) content, each in a different format denoted by its "Content-Type" header. The order of the parts is significant.  RFC1341 states: In general, user agents that compose multipart/alternative entities should place the body parts in increasing order of preference, that is, with the preferred format last.
Systems can then choose the "best" representation they are capable of processing; in general, this will be the last part that the system can understand, although other factors may affect this.
Since a client is unlikely to want to send a version that is less faithful than the plain text version, this structure places the plain text version (if present) first. This makes life easier for users of clients that do not understand multipart messages.
Most commonly, multipart/alternative is used for email with two parts, one plain text (text/plain) and one HTML (text/html). The plain text part provides backwards compatibility while the HTML part allows use of formatting and hyperlinks. Most email clients offer a user option to prefer plain text over HTML; this is an example of how local factors may affect how an application chooses which "best" part of the message to display.
While it is intended that each part of the message represent the same content, the standard does not require this to be enforced in any way. At one time, anti-spam filters would only examine the text/plain part of a message, because it is easier to parse than the text/html part. But spammers eventually took advantage of this, creating messages with an innocuous-looking text/plain part and advertising in the text/html part. Anti-spam software eventually caught up on this trick, penalizing messages with very different text in a multipart/alternative message.
The type is defined in RFC 2046.


==== related ====
A multipart/related is used to indicate that each message part is a component of an aggregate whole. It is for compound objects consisting of several inter-related components –  proper display cannot be achieved by individually displaying the constituent parts. The message consists of a root part (by default, the first) which reference other parts inline, which may in turn reference other parts. Message parts are commonly referenced by Content-ID. The syntax of a reference is unspecified and is instead dictated by the encoding or protocol used in the part.
One common usage of this subtype is to send a web page complete with images in a single message. The root part would contain the HTML document, and use image tags to reference images stored in the latter parts.
The type is defined in RFC 2387.


==== report ====
multipart/report is a message type that contains data formatted for a mail server to read. It is split between a text/plain (or some other content/type easily readable) and a message/delivery-status, which contains the data formatted for the mail server to read.
The type is defined in RFC 6522.


==== signed ====
A multipart/signed message is used to attach a digital signature to a message. It has exactly two body parts, a body part and a signature part. The whole of the body part, including mime fields, is used to create the signature part. Many signature types are possible, like "application/pgp-signature" (RFC 3156) and "application/pkcs7-signature" (S/MIME).
The type is defined in RFC 1847.


==== encrypted ====
A multipart/encrypted message has two parts. The first part has control information that is needed to decrypt the application/octet-stream second part. Similar to signed messages, there are different implementations which are identified by their separate content types for the control part. The most common types are "application/pgp-encrypted" (RFC 3156) and "application/pkcs7-mime" (S/MIME).
The MIME type defined in RFC 1847.


==== form-data ====
The MIME type multipart/form-data is used to express values submitted through a form. Originally defined as part of HTML 4.0, it is most commonly used for submitting files with HTTP. It is specified in RFC 7578, superseding RFC 2388. example


==== x-mixed-replace ====
The content type multipart/x-mixed-replace was developed as part of a technology to emulate server push and streaming over HTTP.
All parts of a mixed-replace message have the same semantic meaning. However, each part invalidates –  "replaces" –  the previous parts as soon as it is received completely. Clients should process the individual parts as soon as they arrive and should not wait for the whole message to finish.
Originally developed by Netscape, it is still supported by Mozilla, Firefox, Safari, and Opera. It is commonly used in IP cameras as the MIME type for MJPEG streams. It was supported by Chrome for main resources until 2013 (images can still be displayed using this content type).


==== byterange ====
The multipart/byterange is used to represent noncontiguous byte ranges of a single message, it is used by HTTP when a server returns multiple byte ranges and is defined in RFC 2616.


=== RFC documentation ===
RFC 1426, SMTP Service Extension for 8bit-MIMEtransport. J. Klensin, N. Freed, M. Rose, E. Stefferud, D. Crocker. February 1993.
RFC 1847, Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted
RFC 3156, MIME Security with OpenPGP
RFC 2045, MIME Part One: Format of Internet Message Bodies
RFC 2046, MIME Part Two: Media Types. N. Freed, Nathaniel Borenstein. November 1996.
RFC 2047, MIME Part Three: Message Header Extensions for Non-ASCII Text. Keith Moore. November 1996.
(RFC 4288, MIME Part Four: Media Type Specifications and Registration Procedures. Obsoleted by RFC 6838.)
RFC 6838, Media Type Specifications and Registration Procedures. J. Klensin, N. Freed, T. Hansen. January 2013. (Obsoletes RFC 4288.)
RFC 4289, MIME Part Four: Registration Procedures. J. Klensin, N. Freed. December 2005.
RFC 2049, MIME Part Five: Conformance Criteria and Examples. N. Freed, N. Borenstein. November 1996.
RFC 2183, Communicating Presentation Information in Internet Messages: The Content-Disposition Header Field. Troost, R., Dorner, S. and K. Moore. August 1997.
RFC 2231, MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations. N. Freed, K. Moore. November 1997.
RFC 2387, The MIME Multipart/Related Content-type
RFC 1521, Mechanisms for Specifying and Describing the Format of Internet Message Bodies
RFC 7578, Returning Values from Forms: multipart/form-data


== See also ==
Direct Internet Message Encapsulation –  a now-superseded, Microsoft-proposed protocol intended as a streamlined MIME, primarily for use in web services
Object Linking and Embedding – Technology developed by Microsoft
SOAP with Attachments
Unicode and email – Relationship between Unicode and email
Uuencoding – Form of binary-to-text encoding
VPIM


== References ==


== Further reading ==
Hughes, L (1998). Internet Email Protocols, Standards and Implementation. Artech House Publishers. ISBN 978-0-89006-939-4.
Johnson, K (2000). Internet Email Protocols: A Developer's Guide. Addison-Wesley Professional. ISBN 978-0-201-43288-6.
Loshin, P (1999). Essential Email Standards: RFCs and Protocols Made Practical. John Wiley & Sons. ISBN 978-0-471-34597-8.
Rhoton, J (1999). Programmer's Guide to Internet Mail: SMTP, POP, IMAP, and LDAP. Elsevier. ISBN 978-1-55558-212-8.
Wood, D (1999). Programming Internet Mail. O'Reilly. ISBN 978-1-56592-479-6.


== External links ==
MIME Media Types –  comprising a list of directories of content types and subtypes, maintained by Internet Assigned Numbers Authority.
List of Character Sets
Properly Configuring Server MIME Types
An easy to follow description of multipart messages from MH & nmh
"The MIME guys: How two Internet gurus changed e-mail forever". February 1, 2011.
Free Online PHP MIME checker
Free Online MIME Email Validator
