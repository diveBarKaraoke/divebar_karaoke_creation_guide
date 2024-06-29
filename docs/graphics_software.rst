Karaoke Graphics Software
=========================

There are a lot of different pieces of karaoke software available. Here's a comparison of many of the options.

Software Options
----------------

.. toctree::
   :hidden:

   kbs
   midico
   doblon
   the_tuul
   ytmm
   other_graphics_software


.. list-table::
   :header-rows: 1

   * - Software
     - Platform
     - Cost
   * - :doc:`kbs`
     - Windows [#f22]_
     - $99
   * - :doc:`midico`
     - Mac
     - €88.90 [#f16]_
   * - :doc:`doblon`
     - Windows
     - $308 [#f17]_
   * - :doc:`the_tuul`
     - Browser
     - Free
   * - :doc:`ytmm`
     - Windows
     - $29.99 [#f18]_
   * - :ref:`other_graphics_software:Karaoke Animator`
     - Android
     - Free [#f19]_
   * - :ref:`other_graphics_software:Karaoke Lyric Editor`
     - Windows, Mac, Linux
     - Free [#f20]_
   * - :ref:`other_graphics_software:Aegisub`
     - Windows, Mac, Linux
     - Free
   * - :ref:`other_graphics_software:Video Editors` [#f2]_
     - Varying
     - Varying
   * - :ref:`other_graphics_software:MyKaraoke Video` [#f3]_
     - Browser
     - Unknown [#f21]_

Syncing Features
----------------

.. list-table::
   :header-rows: 1

   * - Software                                                                                                                         
     - Ease of sync
     - Syllable support
     - Redo parts of sync
     - Edit after sync
   * - Karaoke Builder Studio
     - Easy
     - Yes
     - By page
     - Yes
   * - MidiCo
     - Easy
     - Yes
     - Any point
     - Yes
   * - Doblon [#f1]_
     - Easy
     - Yes
     - By word or 10 second increment
     - Yes
   * - The Tüül
     - Easy
     - Yes
     - By page
     - No [#f6]_
   * - YouTube Movie Maker
     - Medium
     - Yes [#f4]_
     - Any point
     - Yes
   * - Karaoke Animator
     - Medium
     - No
     - None
     - Yes
   * - Karaoke Lyric Editor
     - Medium
     - Yes [#f5]_
     - Any point
     - Yes
   * - Aegisub
     - Hard
     - Yes [#f5]_
     - n/a [#f15]_
     - Yes [#f15]_
   * - Video Editors [#f2]_
     - Very Hard
     - n/a
     - n/a [#f15]_
     - Yes [#f15]_
   * - MyKaraoke Video [#f3]_
     - Easy
     - No
     - By line
     - Yes [#f23]_

Output Features
---------------

.. list-table::
   :header-rows: 1

   * - Software                                                                                                                         
     - CDG Support
     - Good video export [#f8]_
     - Background media [#f12]_
     - Style support
     - Custom Positioning
   * - Karaoke Builder Studio
     - Yes
     - No [#f11]_
     - No [#f11]_
     - Yes, per line
     - Yes, per line
   * - MidiCo
     - Yes
     - Yes
     - Yes
     - Yes, per part
     - Page layout only
   * - Doblon [#f1]_
     - Yes
     - Yes
     - Yes
     - Yes, per part
     - Page layout only
   * - The Tüül
     - No
     - Yes [#f10]_
     - No [#f13]_
     - One text style only
     - No [#f14]_
   * - YouTube Movie Maker
     - No
     - Yes [#f9]_
     - Yes
     - Yes, per line
     - Yes, by layer
   * - Karaoke Animator
     - No
     - Yes
     - No
     - One text style only
     - None
   * - Karaoke Lyric Editor
     - Yes [#f7]_
     - Yes
     - No
     - One text style only
     - Vertical alignment on page only
   * - Aegisub
     - No
     - Yes
     - Yes
     - Yes, per syllable
     - Yes, per line
   * - Video Editors [#f2]_
     - No
     - Yes
     - Yes
     - Yes
     - Yes, arbitrary
   * - MyKaraoke Video [#f3]_
     - No
     - Yes
     - Yes
     - One style, set colors only
     - No

.. rubric:: Notes

.. [#f22] Also verified to mostly work in Linux with Wine.
.. [#f16] Base software plus Advanced Karaoke Maker plugin, which is necessary to create decent karaoke.
.. [#f17] CD+G and video combo bundle (CD+G Createor Pro and Karaoke Video Creator) - minimum viable purchase is just the regular Karaoke CD+G Creator for $119, but that gives you only CD+G support, and none of the advanced features like duets or overwrite mode to allow wipe to keep up with faster songs.
.. [#f18] There is a free version, but it is a bit limited, so at least the Gold version is recommended. The only potentially problematic limitations on the Gold version are that videos are limited to 10 minutes, and free updates are limited to 2 years. The Platinum edition removes both of those and is currently $49.99.
.. [#f19] Some functionality is ad-supported.
.. [#f20] Registration is encouraged but not required (starting at $12.99/year)
.. [#f21] Currently free, but there is expected to be some pricing model eventually.
.. [#f1] This assumes you have both their CDG and video software, sync timings in one, and use both to export.
.. [#f6] Not in the software itself, but you can export a .ass file that could be edited in a subtitle or text editor.
.. [#f4] Karaoke wipes use keyframe-based animation keyframes being able to occur sub-word or even sub-letter.
.. [#f5] These don't have a syllable separator character, but sync start/stop points can be manually inserted between letters.
.. [#f15] These don't really have a sync process at all, so they are entirely based on editing.
.. [#f23] In current beta version
.. [#f2] There are certainly many video editors available with varying features. This assumes you have one that does not have a specific karaoke feature, but does support layers and keyframe-based animation.
.. [#f3] This is still new to the game, so features may soon increase.
.. [#f8] This means if you export at a resolution, it renders the text at that resolution rather than scaling.
.. [#f12] Apply an image or video behind the lyrics.
.. [#f11] KBS itself doesn't support this, but there are tools that can work with the .kbp format or the .lrc format it can export and get this.
.. [#f10] 720p export only, though you can export .ass and render a higer resolution video yourself.
.. [#f13] Not by itself, but you can add the .ass subtitle it provides to a video to achieve this.
.. [#f9] Free version has limited resolution.
.. [#f7] It's hard to get a good result due to the way it sizes the font.
.. [#f14] Not built in, but you can export to .ass and position there.
