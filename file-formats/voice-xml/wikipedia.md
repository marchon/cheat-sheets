# VoiceXML

Cloned from https://en.wikipedia.org/wiki/VoiceXML.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 177206.

VoiceXML (VXML) is a digital document standard for specifying interactive media and voice dialogs between humans and computers. It is used for developing audio and voice response applications, such as banking systems and automated customer service portals. VoiceXML applications are developed and deployed in a manner analogous to how a web browser interprets and visually renders the Hypertext Markup Language (HTML) it receives from a web server. VoiceXML documents are interpreted by a voice browser and in common deployment architectures, users interact with voice browsers via the public switched telephone network (PSTN).
The VoiceXML document format is based on Extensible Markup Language (XML). It is a standard developed by the World Wide Web Consortium (W3C).


== Usage ==
VoiceXML applications are commonly used in many industries and segments of commerce. These applications include order inquiry, package tracking, driving directions, emergency notification, wake-up, flight tracking, voice access to email, customer relationship management, prescription refilling, audio news magazines, voice dialing, real-estate information and national directory assistance applications. 
VoiceXML has tags that instruct the voice browser to provide speech synthesis, automatic speech recognition, dialog management, and audio playback.  The following is an example of a VoiceXML document:

When interpreted by a VoiceXML interpreter this will output "Hello world" with synthesized speech.
Typically, HTTP is used as the transport protocol for fetching VoiceXML pages.  Some applications may use static VoiceXML pages, while others rely on dynamic VoiceXML page generation using an application server like Tomcat, Weblogic, IIS, or WebSphere.
Historically, VoiceXML platform vendors have implemented the standard in different ways, and added proprietary features.  But the VoiceXML 2.0 standard, adopted as a W3C Recommendation on 16 March 2004, clarified most areas of difference. The VoiceXML Forum, an industry group promoting the use of the standard, provides a conformance testing process that certifies vendors' implementations as conformant.


== History ==
AT&T Corporation, IBM, Lucent, and Motorola formed the VoiceXML Forum in March 1999, in order to develop a standard markup language for specifying voice dialogs.  By September 1999 the Forum released VoiceXML 0.9 for member comment, and in March 2000 they published VoiceXML 1.0. Soon afterwards, the Forum turned over the control of the standard to the W3C. The W3C produced several intermediate versions of VoiceXML 2.0, which reached the final "Recommendation" stage in March 2004.
VoiceXML 2.1 added a relatively small set of additional features to VoiceXML 2.0, based on feedback from implementations of the 2.0 standard. It is backward compatible with VoiceXML 2.0 and reached W3C Recommendation status in June 2007.


== Future versions of the standard ==
VoiceXML 3.0 was slated to be the next major release of VoiceXML, with new major features. However, with the disbanding of the VoiceXML Forum in May 2022, the development of the new standard was scrapped.


== Implementations ==
As of December 2022, there are few VoiceXML 2.0/2.1 platform implementations being offered.

Hewlett-Packard (OCMP)
OnMobile (Ozone Speech Platform)
Alvaria
Avaya (Avaya Experience Portal)
OpenVXI
Cisco
Genesys (company)
Nuance Communications
Phonologies
Plum Voice
Telesoft Technologies


== Related standards ==
The W3C's Speech Interface Framework also defines these other standards closely associated with VoiceXML.


=== SRGS and SISR ===
The Speech Recognition Grammar Specification (SRGS) is used to tell the speech recognizer what sentence patterns it should expect to hear: these patterns are called grammars. Once the speech recognizer determines the most likely sentence it heard, it needs to extract the semantic meaning from that sentence and return it to the VoiceXML interpreter.  This semantic interpretation is specified via the Semantic Interpretation for Speech Recognition (SISR) standard. SISR is used inside SRGS to specify the semantic results associated with the grammars, i.e., the set of ECMAScript assignments that create the semantic structure returned by the speech recognizer.


=== SSML ===
The Speech Synthesis Markup Language (SSML) is used to decorate textual prompts with information on how best to render them in synthetic speech, for example which speech synthesizer voice to use or when to speak louder or softer.


=== PLS ===
The Pronunciation Lexicon Specification (PLS) is used to define how words are pronounced. The generated pronunciation information is meant to be used by both speech recognizers and speech synthesizers in voice browsing applications.


=== CCXML ===
The Call Control eXtensible Markup Language (CCXML) is a complementary W3C standard.  A CCXML interpreter is used on some VoiceXML platforms to handle the initial call setup between the caller and the voice browser, and to provide telephony services like call transfer and disconnect to the voice browser.  CCXML can also be used in non-VoiceXML contexts.


=== MSML, MSCML, MediaCTRL ===
In media server applications, it is often necessary for several call legs to interact with each other, for example in a multi-party conference.  Some deficiencies were identified in VoiceXML for this application and so companies designed specific scripting languages to deal with this environment.  The Media Server Markup Language (MSML) was Convedia's solution, and Media Server Control Markup Language (MSCML) was Snowshore's solution. Snowshore is now owned by Dialogic and Convedia is now owned by Radisys.  These languages also contain 'hooks' so that external scripts (like VoiceXML) can run on call legs where IVR functionality is required.
There was an IETF working group called mediactrl ("media control") that was working on a successor for these scripting systems, which it is hoped will progress to an open and widely adopted standard. The mediactrl working group concluded in 2013.


== See also ==
ECMAScript – the scripting language used in VoiceXML
OpenVXI – an open source VoiceXML interpreter library 
SCXML – State Chart XML


== References ==


== External links ==

W3C's Voice Browser Working Group, Official VoiceXML Standards
VoiceXML Forum Archived 2021-05-05 at the Wayback Machine, VoiceXML Trademark Holder
VoiceXML tutorials
