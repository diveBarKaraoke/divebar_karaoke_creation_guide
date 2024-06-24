Vocal Isolation
===============

The first step in creating a karaoke video is to isolate the vocals from the instruments in a song. Unless you can get official stems, the way to go is to use vocal reduction/isolation utilities, which often include multiple AI models you can try. The most effective models for isolating vocals from instruments currently include Ultimate Vocal Remover (UVR), MDX 23c 8K, Mel-RoFormer and Demucs. Each model has strengths and weaknesses. The current consensus is that Mel-RoFormer is the most versatile and effective at vocal isolation (June 18, 2024).

Sourcing the original audio
---------------------------

In order to isolate an instrumental track, you must first source the original audio if you don’t already have a digital copy of the song. For best results, use lossless audio, such as FLAC or WAV. If not available, use as high of quality as you can get.

If you need to pull the audio from YouTube, you'll get the best quality by searching for "Song Artist - Song Name (Topic)". These are the official releases from the artists, though YouTube does still reencode them to fairly low bitrate (~128 kbps). For example, see this video for a Marcy Playground release and note the channel name displays "Marcy Playground - Topic": `<https://youtu.be/ytK71-PoVG8>`_

Creating stems
--------------

In most cases, we recommend using one of the following two utilities for vocal removal:

* :doc:`uvr`: If you have a PC or laptop with a good video card or CPU, you can use this utility to run separation for free on your own system. It will take several seconds per track to run on GPU, or several minutes per track on CPU.
* :doc:`x-minus`: This is the recommended online tool, because it keeps up very well with the models available. It does have a monthly fee to use all the functionality, but it is very low.

Here's a comparison of these two and some other similar utilities. These are by no means a comprehensive set of options, but represent what we believe to be the best available in terms of convenience and quality.

.. 
    This table is a bit finicky (see e.g. the hard-coded widths), but I
    couldn't really figure out a better way to organize this data

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 9 16 15 15 15 15 15

   * - Feature
     - :ref:`audio-separator <other_separators:python-audio-separator>`
     - :ref:`other_separators:Google Colab` [#f1]_
     - :ref:`other_separators:MVSEP`
     - :ref:`other_separators:The Tüül`
     - :doc:`UVR <uvr>`
     - :doc:`x-minus <x-minus>`
   * - How to run
     - Local [#f4]_
     - Web
     - Web
     - Web
     - Local
     - Web
   * - Ease of Use Rank [#f2]_
     - 6 [#f3]_
     - 5
     - 3
     - 1
     - 4
     - 2
   * - Cost
     - Free
     - Free [#f7]_
     - $0.00 - $0.30 / track [#f8]_
     - Free
     - Free
     - $0.00 - $0.01 / minute [#f9]_
   * - Model selection
     - Med
     - Low [#f5]_
     - High
     - None
     - High
     - High
   * - Speed of model updates
     - Med
     - Fast [#f10]_
     - Med [#f11]_
     - Slow
     - Med
     - Fast
   * - Parameter customization
     - Low
     - Low [#f6]_
     - High
     - None
     - High
     - Med

.. rubric:: Notes

.. [#f1] This isn't exactly one solution, as anyone can create a Colab. But most of the ones people have created tend to work in similar ways. This also assumes you're able to find an existing one rather than creating your own.
.. [#f4] Since this is distributed as a Python library, you can also use it to create your own Google Colab or similar.
.. [#f2] This is a ranking of user experience/ease of use, 1 being the easiest. It is of course subjective, but I (Matt M) thought it would helpful to have regardless. Feel free to look into the specifics of each option to better estimate the expected ease of use for you in particular.
.. [#f3] This is assuming you aren't familiar with running Python or Docker. If you are, this may be much easier.
.. [#f7] With typical usage. You may need to buy compute units if your usage is substantial.
.. [#f8] Some functionality is available for free, but it runs at low priority so it may be slow. The fanciest ensemble option they have is premium only and costs 6 "credits" which can be anywhere from $0.017-$0.05 each depending on how many you buy at a time. A basic separation costs only one credit.
.. [#f9] Some functionality is available for free, but a subscription is recommended. Subscriptions provide weekly quotas of minutes of audio processed. The least expensive plan is currently $3.30 per month, which includes 330 minutes of processing per week. When processing an ensemble it counts as double minutes, and demucs 4-stem counts as quadruple, so that's where the max cost per minute is derived.
.. [#f5] Again, since there are multiple Colabs available, this can vary, but this is the typical case.
.. [#f10] If you can find a new Colab, which is a challenge in and of itself.
.. [#f11] They do have a lot of their own models which are obviously the latest version, but they are not always up to date on the MDX/UVR models, which do move fast.
.. [#f6] Colabs typically do not have many included options, but on the other hand, you can edit their code to change parameters if you are capable.

.. toctree::
   :hidden:

   uvr
   x-minus
   other_separators

Vocal Isolation Models
----------------------

Most of the available tools share a lot of separation models. Here's an overview of some of the best ones. This below guide to the relative strengths and weaknesses of each vocal isolation method was written by Peareoke. New models are being added constantly each with its own merits. If you’re not sure which is the most effective currently, just ask and someone will let you know.

Mel-RoFormer and BS-RoFormer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are currently the best models for making karaoke instrumentals. These models were created by cross-training with other previous AIs (including the ones listed below) using new datasets.

If you want to include background vocals from the song in your karaoke video, try using mel-roformer (kar) or uvr bve2. Roformer Kar will include the backing vocals with the instrumental track when separating. BVE2 will try to isolate just the background vocals so you will have to use an audio editor to merge the sound.

UVR
^^^

UVR was the first model to gain widespread use. The vast majority of karaoke tracks on youtube made more than a year ago were created using UVR5 or a previous iteration. It is a very good starting place for folks intimidated by the huge variety of models as it almost always produces a usable result. While it’s not currently the most effective, that may change in the future as it gets updated frequently.

MDX
^^^

MDX is another great option for vocal isolation. Like UVR it separates a track into an instrumental and vocal stem. MDX models also iterate frequently. As of June 4th, 2024, mdx 23c 8k is the most effective MDX model.

demucs
^^^^^^

`Demucs <https://github.com/facebookresearch/demucs>`_, created by Facebook parent company Meta, has the ability to separate a track into as many as six stems: bass, drums, guitar, vocals, piano, other (last two not available on x-minus). Unfortunately the component parts do not isolate as cleanly as other AI models at this time. There are instances where it can still be effective to add sound back into the mix that might be missing from an isolation using another method.

