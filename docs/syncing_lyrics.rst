Syncing/Graphics: Background
============================

Before we get into the specifics of what karaoke software is available, here's some background to better contextualize the options.

Karaoke Styles
--------------

There are a few different ways to release karaoke and the intended style may have some impact on the available options to create it as well, so here's a little background that may help the rest of this section make more sense.

While there is a lot of variation, there are basically two main styles of karaoke. For lack of a better term, let's call them Eastern and Western (if anyone knows of proper, accepted terms for these, please share). Eastern-style karaoke has a large focus on video, and usually has one or two lines of lyrics at the top or bottom of the screen (like a subtitle on TV). In Western-style karaoke, the lyrics are the main focus. While there can in some cases be background video or effects, the text is generally larger, there's usually more lines, and it is often centered on the screen.

diveBar creators have thus far mostly created Western-style karaoke. If you prefer to create Eastern-style, you are definitely still welcome in the community, but you may also consider joining the `Karaoke Mugen community <https://mugen.karaokes.moe/en/contact.html>`_ as they are going to be better equipped to help you with that style of karaoke's best practices.


Karaoke File Formats
--------------------

There are three basic format types used to distribute karaoke nowadays:

Video
^^^^^

These are just regular video files that can play in any video player. Any modern karaoke software will also support it, but there are still some KJs using old software that doesn't. Typically karaoke creators distribute in the .mp4 format, with H.264 video and AAC audio, because it has great player compatibility, including hardware acceleration, and quality. When uploading to YouTube, just about any video format can be used. If you have a fast Internet connection, your best bet is usually to upload whatever video format your karaoke software generates instead of transcoding it first, to minimize quality degradation as YouTube will transcode it again anyway.

CD+G Graphics plus audio
^^^^^^^^^^^^^^^^^^^^^^^^

This is an old standard from the 1980s. It's technically a way to add graphics onto a CD alongside the audio, but now it is almost always distributed as .cdg files with corresponding audio files with the same filename (typically .mp3 files). Most karaoke software also supports playing files where the .cdg and .mp3 file have been combined into a .zip archive.

Despite the age and limitations of the format, a lot of karaoke creators still use it due to its wide compatibility with karaoke software, either as a primary or fallback option. But beware it does have a lot of technical limitations - maximum of 16 colors on screen at a time, 288x192 resolution (excluding the border which can only be a solid color), limited bandwidth to make changes on screen, etc. Since it's so limited in animation/motion capability, it can really only be used for Western-style karaoke. It also can't be directly uploaded to YouTube, so while it can be distributed for offline use as CDG, it will need to be converted to video for YouTube.

Video + Subtitle
^^^^^^^^^^^^^^^^

These are video files with the music and background video and a subtitle file packaged along with it that contains the lyric scroll (in most cases using the .ass format since it has good karaoke wipe support). This works very well for Eastern-style karaoke, and is the standard for Karaoke Mugen's library.

At diveBar, while many of us use subtitles in our process, we typically hard sub them into the video to ensure compatibility with software designed for Western-style karaoke and for consistency in text layout and fonts. Hard subbing is also recommended for YouTube upload, as YouTube only has minimal subtitle support, and people's local settings could cause the CC option to be off by default.
