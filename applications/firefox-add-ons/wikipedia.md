# Add-on (Mozilla)

Cloned from https://en.wikipedia.org/wiki/Add-on_(Mozilla).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1907070.

For Mozilla software, an add-on is a software component that extends the functionality of the Firefox web browser and related applications – although most are browser extensions. Mozilla provides add-ons to users via its official add-on website.
In 2017, Mozilla enacted major changes to the application programming interface (API) for extensions in Firefox, replacing the long-standing XPCOM-based add-on APIs with the WebExtensions API that is modeled after Google Chrome's API. Thus add-ons that remain compatible with Firefox are now largely compatible with Chrome as well. As of January 2026, there are more than 74,000 add-ons and over 511,000 themes available for Firefox.


== Add-ons categories ==


=== Themes ===
Early versions of Firefox supported themes that could greatly change the appearance of the browser, but this was scaled back over time. Current themes are limited to changing the background and text color of toolbars, formerly called personas, now called Firefox Themes.


=== WebExtensions ===
Starting with Firefox 57, only the new WebExtensions API is supported for extensions, relegating the older extension technology as legacy.


=== Legacy extensions ===
Prior to 2017, Firefox supported extensions developed via various APIs: XUL, XPCOM, and Jetpack. Mozilla now refers to these as legacy extensions.


=== Plug-ins ===
Plug-ins are no longer supported in Firefox. In the past, they were used to handle media types for which the application did not have built-in capability. They were deprecated due to security concerns and improvements in Web APIs. The last one that was officially supported was Adobe Flash Player, which Adobe discontinued in 2020.


== Security ==
Mozilla had no mechanism to restrict the privileges of legacy Firefox extensions. This meant that a legacy extension could read or modify the data used by another extension or any file accessible to the user running Mozilla applications. The current implementation WebExtensions API imposes security restrictions.
Starting with Firefox 40, Mozilla began to roll out a requirement for extension signing. It is now required in all official Firefox releases.


== Website ==

The Mozilla add-ons website is the official repository for Firefox add-ons. In contrast to mozdev.org which provides free hosting for Mozilla-related projects, the add-ons site is tailored for users. By default, Firefox automatically checks the site for updates to installed add-ons.
In January 2008, Mozilla announced that the site had accumulated a total of 600 million add-on downloads and that over 100 million installed add-ons automatically check the site for updates every day. In July 2012, the total had increased to 3 billion downloads from the site.


== References ==


== External links ==
Official add-on website
WebExtensions API reference documentation
Extension Workshop, Mozilla's site for Firefox extension developer documentation
