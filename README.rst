===================================
Discord Bot Examples [DBE] (Python)
===================================

|status|

|rtd_badge| |build| |license| |language| |release| 

|important|

Discord Bot Examples (DBE) is a repository containing well-documented and easy-to-learn 
examples involving the use of `discord.py`_ library.

A more organized version of the doc-strings can be found on the 
DBE documentation: https://dbe.readthedocs.io/en/latest/

Introduction
============

Welcome to DBE! Have you ever wondered how to create your **own** discord bot? 
Here you can learn to create a personalized discord bot from scratch. 
DBE utilzes the programming language Python and the `discord.py`_ library

Purposes
--------

 * Help new discord developers start using the `discord.py`_ API
 * Step by step guide programmers through developing a working discord bot
 * Give examples of various functionalities that `discord.py`_ is capable of
 * Address the common FAQ regarding `discord.py`_
 
 Continue to Fist Step when you're ready to begin.
 
Creating a bot account
======================
 
 1.  Go to `Discord Developer Page <https://discordapp.com/developers/>`_ and 
     login or register an Discord User Account (you can loging with your personal discord account)
 2.  Go to `My Apps <https://discordapp.com/developers/applications/me>`_
 3.  Click on `New App <https://discordapp.com/developers/applications/me/create>`_
 4.  Fill in "App Name" with your bot's name (this will be your bot name, it cannot be changed)
 5.  Fill in the optional "App Description" with the description and upload a bot avatar for "App Icon"
 6.  Click on "Create App" (note: All previously added details are changable)
 7.  Go to `My Apps <https://discordapp.com/developers/applications/me>`_ and select the bot you just created
 8.  Scroll down to the "Bot" section, click "Create a Bot User", and conform your choice ("click Yes, do it!")
 9.  Click on the check mark for "Public Bot"
 10. Click on "Token: *click to reveal*", keep note of the generated token (**DO NOT SHARE THE TOKEN WITH ANYONE**)
 11. You're done at creating the bot!
 
Installing Python and dependencies
==================================

Installing Python
-----------------

 1. Go to the `Python Download Page <https://www.python.org/downloads/>`_ and download a version of Python 3
 2. Follow the installation setup (if you're on Windows, check "add python to PATH" in the setup script)
 3. Python is now installed on your system
 
Installing dependencies
-----------------------

Choose a version of discord.py, there are currently 2 major versions, rewrite (v1.0) and async (v0.16.x).

 * Rewrite is a newly developed version of discord.py, it's fully usable but it's still in active development
 * Async is the stable version of discord.py
 * If you are uncertain about which version to choose, rewrite has more functionalities than async
 
Rewrite and async is **not** compatible. 

After you chose the version you want to use, go to the directory in this GitHub repo with the version name. 
The rest of the dependencies installation tutorial will be in the README.rtf of that directory.

Continuation
============

The rest of the introduction will continue in the README.rst of the rewrite or async directories.


 
:sub:`Discord Bot Examples (DBE) is not affliated in any way with the discord.py library or the development of discord.py.`
:sub:`DBE is an example/turtorial repository developed by Taku. Read the LICENSE file for more information.`



.. 
    links:
    
.. _discord.py: https://discordpy.readthedocs.io/en/

..
    badges links:

.. |important| image:: https://img.shields.io/badge/WARNING-THIS_REPO_IS_STILL_UNDER_DEVELOPMENT--MOST_FEATURES_HAVE_NOT_BEEN_IMPLIMENTED_YET-red.svg?longCache=true&style=flat-square
               :alt: WARNING: THIS REPO IS STILL UNDER DEVELOPMENT
.. |status|    image:: https://img.shields.io/badge/status-underdevelopment-7bccc2.svg?longCache=true&style=for-the-badge
               :alt: Status: Underdevelopment
.. |rtd_badge| image:: https://readthedocs.org/projects/dbe/badge/?version=latest
               :alt: Doc: Unknown
.. |build|     image:: https://img.shields.io/badge/build-success-blue.svg
               :alt: Build: Success
.. |language|  image:: https://img.shields.io/badge/language-Python-red.svg
               :alt: Language: Python
.. |release|   image:: https://img.shields.io/github/release/GreatTaku/DiscordBotExamples/all.svg
               :alt: Release: Unknown
.. |license|   image:: https://img.shields.io/github/license/GreatTaku/DiscordBotExamples.svg
               :alt: License: MIT License
