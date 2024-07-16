Helper Software
===============

This is a catch-all page for any kind of alternate syncing tools, converters, and automation tools. These are a lot of these available, and it's unlikely this can ever cover all of them, but if you have info on a tool you think should be here, please :doc:`let us know <feedback>`.

Alternate Syncing
-----------------

Kadda OK Tools
^^^^^^^^^^^^^^

`Kadda OK Tools <https://github.com/KaddaOK/KaddaOKTools>`_ is an application to create a karaoke project from lyric timing that provides several options:

- Manual - It has its own syncer built in that can be used to tap out the timing like many karaoke graphics programs
- Imported - It can import a project file from :doc:`kbs` or :doc:`ytmm`, or a timing file from `NeMo Forced Aligner <https://github.com/KaddaOK/Forced-Aligner-for-Karaoke>`_
- Automated - It can create the timing with Azure Speech Services

It can export to YouTube Movie Maker formats (.rzlrc + .rzmmpj) as well as Karaoke Builder Studio projects (.kbp)

Converters
----------

kbp2video
^^^^^^^^^

`kbp2video <https://github.com/itmightbekaraoke/kbp2video>`_ is a tool to convert .kbp files from Karaoke Builder Studio into videos.  It works differently from most other converters supporting the .kbp format in that it tries to faithfully reproduce not only the lyric timings, but the formatting and layout as much as possible. It is also able to hard sub any .ass subtitle into a video, not just ones it generated from .kbp files. In addition, it's starting to add some support for importing lyrics files (currently Enhanced LRC and Doblon Lyrics Export).

kbputils
^^^^^^^^

`kbputils <https://github.com/ItMightBeKaraoke/kbputils>`_ is used internally by kbp2video, but it provides a non-GUI way to convert from .kbp to .ass, programmatically modify parts of a .kbp file, or recently create a .kbp out of an Enhanced LRC or Doblon Lyrics Export.

kbp2ass
^^^^^^^

`kbp2ass <https://github.com/Aeden-B/kbp2ass>`_ is a nodejs-based .kbp to .ass converter that predates kbputils. It's currently used in Karaoke Mugen to allow importing .kbp files to their library. See `this overview <https://itmightbekaraoke.com/kbp2ass/>`_ to better understand the current state of kbp2ass and the options for using it.

Kadda OK Tools (again)
^^^^^^^^^^^^^^^^^^^^^^

See :ref:`above <helper_software:Kadda OK Tools>`, but worth listing here too as it can convert to/from .kbp and .rzlrc, and from .ctm (NeMo Forced Align).

Ultimate CD+G to Video Karaoke Converter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Ultimate CD+G to Video Karaoke Converter <https://www.powerkaraoke.com/src/prod-ultimate-cdg-karaoke-video-converter.php>`_ is a tool from Doblon to upscale CDG into videos. It can be helpful to improve the appearance of CDGs, especially if you have a lot of them. The upscaling is noticeable so it's often better to use a converter that renders text from the project file, like the above options. Note that this is the successor to "Power CDG+G to Video" and "Power CD+G to MP4", so if you have heard of either of those, it's the same concept.


Automation
----------

Karaoke Prep
^^^^^^^^^^^^

`Karaoke Prep <https://github.com/karaokenerds/karaoke-prep>`_ is a tool that automates the work before and after syncing a track. Specifically, it will

1. Download a track or playlist from YouTube
2. Pull lyrics from Genius
3. Separate audio into stems
4. Replace audio track in your karaoke video with the instrumental stem
5. Upload to YouTube

Lyrics Transcriber
^^^^^^^^^^^^^^^^^^

`Lyrics Transcriber <https://github.com/karaokenerds/python-lyrics-transcriber>`_ is a tool to automate syncing of lyrics. It uses lyrics from Genius or Spotify, GPT to correct lyrics, and OpenAI Whisper to sync them. It outputs MidiCo .lrc and .ass formats, and can render the .ass to video. It does not create a result that is as good as manual syncing.

Helpers
-------

The Tüül
^^^^^^^^

:doc:`the_tuul` is already listed in Karaoke Graphics Software, but listing here as a reminder that its Lyrics tool can be used to help syllabify lyrics prior to use in any karaoke software.
