KBS: Additional Tutorials and Walkthroughs
==========================================

.. contents::

Video Tutorials
---------------

.. youtube:: fRD3wpP622E
   :privacy_mode:

`Add count-ins <https://youtu.be/fRD3wpP622E>`_ - From Carpy


.. youtube:: PPfBBqCOKlQ
   :privacy_mode:

`Full process - The Tüül magic slashes, UVR5, Audacity, kbp2ass, Kdenlive <https://youtu.be/PPfBBqCOKlQ>`_ - From Rose

.. youtube:: iKZOuOYnmDU
   :privacy_mode:

`Remastering a track with kbp2video <https://youtu.be/iKZOuOYnmDU>`_ - From It Might Be Karaoke

.. youtube:: JG3iokNlp28
   :privacy_mode:

`Full process - UVR5, Sneedacity, ffmpeg (old version) <https://youtu.be/JG3iokNlp28>`_ - From Karaoketuottaja

Walkthroughs / Demos
--------------------

.. youtube:: sK_rf7HcDq8
   :privacy_mode:

`Advanced - positioning background vocals in-line <https://youtu.be/sK_rf7HcDq8>`_ - From lopendash

.. youtube:: nFZWd1cNkL8
   :privacy_mode:

`Syncing with a RockBand Guitar?! <https://youtu.be/nFZWd1cNkL8>`_ - From RankAmateur Feelgood Machine

.. youtube:: ZLOS0M7o9Rc
   :privacy_mode:

`Livestream on using kbp2ass <https://youtu.be/ZLOS0M7o9Rc>`_ - From It Might Be Karaoke

.. youtube:: somDrn1UJJY
   :privacy_mode:

`Karaoke creation with kbp2ass and Shotcut <https://youtu.be/somDrn1UJJY>`_ - From Lopenash

.. youtube:: cQlVjK7tYus
   :privacy_mode:

`kbp2video updates for Feb 2024 <https://youtu.be/cQlVjK7tYus>`_ - From It Might Be Karaoke

.. youtube:: V-XxmLopywM
   :privacy_mode:

`Demo on Linux with kbp2ass <https://youtu.be/V-XxmLopywM>`_ - From It Might Be Karaoke

Text Tutorials
--------------

Background Vocal Timing
^^^^^^^^^^^^^^^^^^^^^^^

Guide by Acorlei aka Lone Wolf Karaoke

Listen, I hate it, you hate it, we all hate it, but background vocals are notoriously difficult to time in your syncing. As a result, they often go untimed, or even, (dare I say it?) FIXED. *shudder* Well, there’s a way you too can sync the background vocals with the foreground, so your friends and other patrons can sing along with the lead. But here’s the thing… you’re basically button mashing through the areas that need the sync, and then editing the rest later. Try and keep on time with the lead, so at least that much will be clean when you finish your first sync.

Remember no good track ever was born from laziness.

.. grid::
   
   .. grid-item::
      :columns: 12 12 12 4
      :child-align: center
   
      .. image:: images/kbs_overlap.png
         :width: 428px
         :alt: Screenshot of KBS edit window, showing two lines with overlapping wipe timing

   .. grid-item::
      :columns: 6 6 7 5
      :child-align: center

      As you can see from the first NIFTY little picture here, you can actually stack lyrics on top of each other. The easiest way (if you’re using Karaoke Builder Studio 5), is to Shift-Click a stack which will turn the entire stack gray (see image on the right). Then, just click and drag it to the location it’s supposed to be. If your background vocals overlap with leads… you’re going to have to fix some stuff. But thankfully, each end of a syllable can be dragged to increase or decrease its wiping speed. 

   .. grid-item::
      :columns: 6 6 5 3
      :child-align: center
   
      .. image:: images/kbs_line_selected.png
         :width: 174px
         :alt: Screenshot of KBS edit window, showing a line selected

.. grid::
   
   .. grid-item::
      :columns: 3 1 2 1
      :child-align: center
   
      .. image:: images/slow_arrows_of_doom.png
         :width: 40px
         :alt: screenshot of KBS edit window, showing arrow buttons for moving track (slowly)

   .. grid-item::
      :columns: 9 11 10 11
      :child-align: center
      
      If’n you’re on an earlier version of KBS, I’m so sorry. It’s not nearly as easy; you’ll have to use the dreaded slow-arrows of doom. (See left) 

They’ll get your lyrics where they need to be, but you’re going to be sitting there for about an hour and a half while you wait for THIS PROGRAM THAT WAS DEVELOPED IN THE NINETIES AND NEVER OPTIMIZED FOR MODERN SYSTEMS EVEN THOUGH IT’S BEING ACTIVELY DEVELOPED THIRTY YEARS LATER THERE ARE STILL NEXT TO ZERO QUALITY OF LIFE IMPROVEMENTS AND— and I’m cool. Chill out, calm head.

See what I mean? If you’re also going to be having background vocals running while your lead is actively singing, don’t forget to give them a different style.

.. grid::
   
   .. grid-item::
      :columns: 12 12 12 6
      :padding: 2
      :child-align: center

      .. image:: images/kbs_set_style.png
         :alt: Screenshot of KBS main window, with two lines selected, indicating they have a different style set

   .. grid-item::
      :columns: 12 12 12 6
      :padding: 2
      :child-align: center
   
      .. image:: images/kbs_styles.png
         :alt: Screenshot of KBS style tab, showing a background style was created

That way, your lead doesn’t get confused while singing. CTRL-Click the background vocals and make sure their “Line Style” is set to your background. Make sure that the style is distinctive as well, to also prevent confusion. Different colors often help. 

KBS Keyboard Shortcuts
^^^^^^^^^^^^^^^^^^^^^^

Guide by Matt M (It Might Be Karaoke)

KBS has a lot of keyboard shortcuts that can be used to improve the efficiency of authoring tracks. This attempts to cover all of them. If you notice any missing or incorrect, please :doc:`report them <feedback>` so the document can be updated.

Sync Window
"""""""""""

* :kbd:`Space` -- Next word (hold down to maintain wiping on a long word/syllable at the end of a line)
* :kbd:`Control` -- Pause wiping (add gap, especially useful for mid-line pauses)
* :kbd:`P` -- Play/Pause the audio
* :kbd:`B` -- Back (delete all sync data for the current page (or previous if you have not entered anything yet on this one) and start it again)
* :kbd:`Control-Q`/:kbd:`Alt-F4` -- Exit sync window without saving (will prompt to confirm)

Main Window
"""""""""""

* :kbd:`Control-N` -- New Project
* :kbd:`Control-O` -- Open Project
* :kbd:`Control-S` -- Save Project
* :kbd:`Control-B` -- Build (dropdown)
* :kbd:`Control-R` -- Reset display/remove timings (shows prompt)
* :kbd:`Control-P`/:kbd:`Control-Space` -- Play/Pause the audio from the currently selected line/position on the Jump slider
* Mouse wheel over Play button for volume (no keyboard shortcut seems to be available)
* :kbd:`Left`/:kbd:`Right`/:kbd:`Home`/:kbd:`End`/:kbd:`Shift-Left`/etc -- Standard text editing controls work in syllable/word fields as well as the field for the audio file
* :kbd:`Control-Q`/:kbd:`Alt-F4` -- Exit KBS (will prompt to save, exit without saving, or cancel exit operation)

Tab traversal is a bit odd, but it can still be helpful. Before sync, the traversal order is the following (:kbd:`Tab`/:kbd:`Shift-Tab` to move forward/back):

[Unknown] ↔ **Page List** → [Dead End]

**Bold** signifies the initially selected item.

[Unknown] means that I can't figure out which UI element is selected, and attempting to activate it does not seem to do anything. [Dead End] means not only that it's unclear which element is selected, but tab traversal break entirely after selecting it.

There is also a second traversal available, not connected to the first (select one of the elements in it, then you can move through it):

[Dead End] ← Track/Wiping/Split tabs ↔ [Unknown] ↔ [Unknown] ↔ Audio File textbox ↔ Lyrics text area ↔ [Unknown] ↔ Help ↔ [Unknown] ↔ CDG Player ↔ Play button ↔ [Unknown] ↔ [Unknown] ↔ [Unknown]

When buttons are selected, they can be activated with :kbd:`Space` or :kbd:`Enter`. Pages can be navigated with :kbd:`Up`/:kbd:`Down`, and you can jump to the first/last with :kbd:`PageUp`/:kbd:`PageDown`. Tabs can be switched with :kbd:`Left`/:kbd:`Right` (or :kbd:`Up`/:kbd:`Down`).

After sync, the traversal is as follows:

[Dead End] ← [Unknown] ↔ Track/Wiping/Split tabs ↔ [Unknown] ↔ Across ↔ Down ↔ Rotation ↔ [Unknown] ↔ Audio File textbox ↔ [Unknown] ↔ Help ↔ Reset ↔ CDG Player ↔ Play button ↔ [Unknown] ↔ [Unknown] ↔ Each syllable on the line ↔ **Page List** → [Before Page List*]

“Before Page List” is a strange place where :kbd:`Shift-Tab` goes back to the syllables but :kbd:`Tab` goes nowhere.

Edit Window
"""""""""""

* :kbd:`Control-S` -- Save Project
* :kbd:`Control-A` -- Select All (helpful for bulk movement of timings)
* :kbd:`Control-B` -- Build (dropdown)
* :kbd:`Control-R` -- Reset display/remove timings (shows prompt)
* :kbd:`Space`/:kbd:`P` -- Play/Pause audio from current position
* :kbd:`L` -- Play current line (closest to cursor if nothing is selected, otherwise *first* selected line)
* :kbd:`PageUp`/:kbd:`PageDown` -- Move back/forward 10 seconds
* :kbd:`Home`/:kbd:`End` -- Move to start/end of audio
* Mouse wheel advances 50 frames (.5 seconds) in wiping tab, 100 in display/remove (no keyboard shortcut). Adding :kbd:`Control` changes it to 1 (both tabs)
* :kbd:`Control-Q`/:kbd:`Alt-F4` -- Quit editing **without saving** (does **NOT** prompt)

With one or more syllables/words selected in the **Lyrics Wiping** tab:

* :kbd:`Up`/:kbd:`Down` -- Move wiping times (start and end). With all tracks selected, this is like the adjust whole track button, but only adjusting the wipe instead of the wipe and display/remove like that does.
* :kbd:`Shift-Up`/:kbd:`Shift-Down` -- Adjust wipe start time
* :kbd:`Control-Up`/:kbd:`Control-Down` -- Adjust wipe end time

With the above, add :kbd:`Alt` to toggle sticky borders (which you'll almost always want turned off with :kbd:`Up`/:kbd:`Down` and on with :kbd:`Shift-Up`/:kbd:`Shift-Down`)

Note that some functionality in the arrow buttons in the wiping UI can changed by keyboard modifiers:

* :kbd:`Control` -- Adjust by 5 frames instead of 1
* :kbd:`Alt` -- Toggle sticky borders

Additionally, click selection behavior can be changed with the following keyboard modifiers:

* :kbd:`Control` -- Select syllable/word without deselecting the current selection
* :kbd:`Shift` -- Select all syllables/words on a line

With one or more lines selected in the **Display/Remove** tab:

* :kbd:`Left`/:kbd:`Right` -- Move line timing (display and remove). With all tracks selected, this is like the adjust whole track button, but only adjusting the display/remove instead of both the wipe and display/remove like that does.
* :kbd:`Control-Left`/:kbd:`Control-Right` -- Adjust display time
* :kbd:`Alt-Left`/:kbd:`Alt-Right` -- Adjust remove time

Note that some functionality in the arrow buttons in the display/remove UI can changed by keyboard modifiers:

* :kbd:`Control` -- Adjust by 10 frames instead of 2
* :kbd:`Alt` -- Snap to timer (cursor) - note this is the only way to adjust by 1 frame, by using :kbd:`Control` with mouse wheel to move the cursor, then snapping to it

Additionally, click selection behavior can be changed with the following keyboard modifiers:

* :kbd:`Control` -- Select line without deselecting the current selection
* :kbd:`Shift` -- Select all lines in a page

