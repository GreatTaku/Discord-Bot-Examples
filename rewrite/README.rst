======================================
Welcome to Discord.py Rewrite Examples
======================================

Installing
==========

Console Prefixes
----------------

 * OsX, Linux, Unix distributions: 
     * ``python3``
 * Windows:
     * ``python3`` in ``PATH``: ``python3``   
     * ``python3`` not in ``PATH``: ``py -3``
     
Installing discord.py
---------------------

(Replace ``<prefix>`` with the aforementioned prefix)

First uninstall any previously installed version of `discord.py`_.
In Terminal, CMD, or any command-line console, type in the following:

``<prefix> -m pip uninstall discord.py``

And install the rewrite version of `discord.py`_:

``<prefix> -m pip install -U yarl==0.1.4 aiohttp==2.2.5 git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]``

or (if you don't have ``git``):

``<prefix> -m pip install -U yarl==0.1.4 aiohttp==2.2.5 https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]``

The ``yarl==0.1.4 aiohttp==2.2.5`` is necessary because `discord.py`_ rewrite's requirements.txt is broken.

If you're using a venv, don't forget to activate it!

You're now ready to run some examples! To run any example in this repository, 
see the README.rst in the top-level directory for directions.

Run DBE examples
================

 1. Download https://github.com/GreatTaku/DiscordBotExamples/archive/master.zip and unzip
 2. Go to the ``DiscordBotExamples/rewrite`` and find the example file you want to run
 3. Open the file, replace "TOKEN" with your bot's token
 4. In the console, type in: ``<prefix> DiscordBotExamples/rewrite/<filename>.py``
 5. And... voila! Go to discord and see your bot in action
 6. To terminate your bot, press `ctrl-c` on your keyboard

Exploring examples
==================

The recommended order to learn examples are numbered below under *Examples Index*, starting with ``introduction.py``.
If something hadn't be documented, it's probably documented in an example previous to it,
I try not to be annoying so I only document the same thing **once**.

If you only want to read the code and nothing else, there is a copy of every file without
comments in the ``no_comments`` directory.

==============
Examples Index
==============

 1. ``introduction.py``
    * exploration on basic bot structure of discord.py
    * preview on commands
    * preview on the ``on_ready`` event

2. ``handle_events(1-3).py``
    * overview on most common discord.py events
    * documentation on the events
    * runnable example for experiencing the events
    * (because there's so many events, I split them into three separate files)
    * a few events will be explained again in future examples

 ..
    links:

.. _discord.py: https://discordpy.readthedocs.io/en/rewrite

