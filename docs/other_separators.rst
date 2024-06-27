Other Separation Utilities
==========================

python-audio-separator
----------------------

`python-audio-sparator <https://github.com/karaokenerds/python-audio-separator>`_ is a newer option for creating stems. It uses code from UVR5, but instead of providing a GUI, it provides a module that can be used in Python code, and a CLI. It is a great option to include in automation or run from a cloud server, including potentially creating your own Google Colab. The learning curve is high compared to the other options unless you're familiar with running Python or Docker. It also may lag a bit behind UVR in supporting new models.

Google Colab
------------

This is a catch-all referring to all the Colabs that have been floating around. `Google Colab <https://colab.google/>`_ is a tool to run code on Google's servers. With typical usage levels, this will probably be free for you. Most vocal isolation Colabs support a particular model with not a lot of settings to adjust unless you delve into the code a bit. If you want to know the current Colabs people are using, ask in `#vocal-isolation <https://discord.com/channels/918644502128885760/918681357562036246>`_. It would be nearly impossible to keep this document up to date with them.

To get an idea of the kind of process involved to run a separation model with Colab, see `this old tutorial <https://youtu.be/w6eIf8y6SY4>`_.

MVSEP
-----

`MVSEP <https://mvsep.com/>`_ is a web-based separation utility, similar to x-minus. It offers more models than x-minus, but can sometimes lag behind on the getting the latest updates to models. It does have a lot available for free, but lossless output as well as some of the models require purchase of "credits" to run. Free conversions are also deprioritized so they often run very slowly.

The Tüül
--------

`The Tüül <https://the-tuul.com/>`_ has the capability to split audio, currently only available when you use it to create a full karaoke video (see :doc:`our page on it <the_tuul>`). It uses a single model with default settings, though it often does a good enough job.
