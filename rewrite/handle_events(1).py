from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


@bot.event
async def on_connect():
    """
    This event is called when the bot is connected to discord, this doesn't necessary means that
    the bot is ready. Use ``on_ready`` for indication that the bot is fully prepared.

    """
    print("Bot is connected to discord")


@bot.event
async def on_resumed():
    """
    This event is called when the bot resumes a session.
    """
    print("Bot had resumed the session")


@bot.event
async def on_ready():
    """
    This event is called the bot is ready to accept payloads.
    This is called after login is successful.

    """
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))


@bot.event
async def on_error(event, *args, **kwargs):
    """
    Catches any exception that occurs during the bot's loop.
    If any exception is raised in ``on_error``, it will `not` be handled.

    The exception itself can be accessed from :class:`sys.exc_info`.

    Args:
        event:
            The name of the event that raised the exception.

        *args:
            The positional arguments for the event that raised the exception

        **kwargs:
             The keyword arguments for the event that raised the exception.

    """
    print("OH NO!, AN ERROR ;(")
    print("Error from:", event)
    print("Error context:", args, kwargs)

    from sys import exc_info

    exc_type, value, traceback = exc_info()
    print("Exception type:", exc_type)
    print("Exception value:", value)
    print("Exception traceback object:", traceback)


@bot.event
async def on_typing(channel, user, when):
    """
    This event is called when someone in an accessible channel begins
    typing.

    Args:
        channel:
            The Channel object of where the typing originated from.

        user:
            The User object that started typing.

        when:
            A :class:`datetime.datetime` object of when the user started typing.

    """
    print(user, "started to type in", channel, "on", when)


@bot.event
async def on_message(message):
    """
    When someone sends an message in somewhere accessible to the bot.

    This is the first thing called when a message is received.

    You need to add ``bot.process_commands(message)`` if you want
    the bot to process the message as a command.

    Args:
        message:
            A Message object of the message.

    """
    print("Received a message:", message)
    bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    """
    This is called when a message is deleted.

    For older messages, it's possible that this event
    might not get triggered.

    Args:
        message:
             A Message object of the deleted message.

    """
    print("This message been deleted:", message)


@bot.event
async def on_message_edit(before, after):
    """
    This is called when a message is edited. An edit could be:

     * A message has been pinned or unpinned.
     * The message content has been changed.
     * The message has received an embed (by chance [not reliable]).
     * A call message has received an update to its participants or ending time.

    For older messages, it's possible that this event
    might not get triggered.

    Args:
        before:
             A Message object of the original message.

        after:
             A Message object of the edited message.

    """
    print(before, "had been changed to", after)


@bot.event
async def on_reaction_add(reaction, user):
    """
    This is called when a message has a reaction added to it.

    The message is stored in ``reaction.message``.

    For older messages, it's possible that this event
    might not get triggered.

    Args:
        reaction:
            A Reaction object of the current state of the reaction.

        user:
            An User or Member object of the user who added the reaction.

    """
    print(user, "added", reaction, "to", reaction.message)


@bot.event
async def on_reaction_remove(reaction, user):
    """
    This is called when a message has a reaction removed from it.

    The message is stored in ``reaction.message``.

    For older messages, it's possible that this event
    might not get triggered.

    Args:
        reaction:
            A Reaction object of the current state of the reaction.

        user:
            An User or Member object of the user who removed the reaction.

    """
    print(user, "removed", reaction, "from", reaction.message)


@bot.event
async def on_reaction_clear(message, reactions):
    """
    This is called when a message has all its reactions removed from it.

    For older messages, it's possible that this event
    might not get triggered.

    Args:
        message:
            A Message object that had its reactions cleared.

        reactions:
            A list of Reaction objects that were removed.

    """
    print(reactions, "been removed from", message)


bot.run(TOKEN)
