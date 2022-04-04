discord.py Ark Api
##################

Using discord.py to interact with ark's web API.

Dependencies
============

- `discord.py <https://github.com/Rapptz/discord.py>`__
- `aiohttp <https://github.com/aio-libs/aiohttp>`__
- `python-dotenv <https://github.com/theskumar/python-dotenv>`__

Installing
==========

**Install Python Here:** `Python <https://www.python.org/downloads/>`_ 

**Python 3.6 or higher is required**

Downloading the files
---------------------

Click green Code button in the top right and click download ZIP

Or install using `Git <https://git-scm.com/>`_ in a terminal

.. code-block:: sh

    $ git clone https://github.com/ItsYeeBoi/discord.py-Ark-API
    $ cd discord.py-Ark-API


Example .env file
-----------------

.. code-block:: text

    # Discord Token
    TOKEN=PUT DISCORD TOKEN HERE
    # Discord Prefix
    PREFIX=!

To get your Discord token follow this guide: `Discord Token <https://www.writebots.com/discord-bot-token/>`_ 

Intalling Dependencies
----------------------

.. code-block:: sh

    pip install -r requirements.txt

Running The Bot
===============

Windows:
--------

Double click main.py file it should open command prompt then the bot is running

Or in command prompt run the command

.. code-block:: sh

    python main.py

To run the bot with PM2:

`Nodejs <https://nodejs.org/en/download/>`_ needs to be installed

.. code-block:: sh

    npm install pm2 -g
    pm2 start main.py

Linux:
------

.. code-block:: sh

    nano .env or gedit .env
    pip install -r requirements.txt
    cd Bot
    python3 main.py

If pip isn't installed use:

.. code-block:: sh

    apt install python3-pip


To Run The Bot Using PM2:

.. code-block:: sh

    apt install nodejs
    apt install npm
    npm install pm2 -g
    cd Bot
    pm2 start main.py --interpreter python3

Plans
-----
- Add PC Server List Using BattleMetrics
- More Features Like Industrial Forge Calculator
- Add More General Commands For Bot

  - Bot Stats
  - Bot Presence
  - Better Help Command

Links
-----

- `Ark Web API <https://ark.fandom.com/wiki/Web_API>`__
- `discord.py <https://github.com/Rapptz/discord.py>`__
- `aiohttp <https://github.com/aio-libs/aiohttp>`__
- `python-dotenv <https://github.com/theskumar/python-dotenv>`__