from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"


@bot.event
async def on_resumed():
    print("Bot had resumed the session")


@bot.event
async def on_ready():
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))


@bot.event
async def on_error(event, *args, **kwargs):
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
    print(user, "started to type in", channel, "on", when)


@bot.event
async def on_message(message):
    print("Received a message:", message)
    bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    print("This message been deleted:", message)


@bot.event
async def on_message_edit(before, after):
    print(before, "had been changed to", after)


@bot.event
async def on_reaction_add(reaction, user):
    print(user, "added", reaction, "to", reaction.message)


@bot.event
async def on_reaction_remove(reaction, user):
    print(user, "removed", reaction, "from", reaction.message)


@bot.event
async def on_reaction_clear(message, reactions):
    print(reactions, "been removed from", message)


@bot.event
async def on_channel_create(channel):
    print(channel, "had just been created")


@bot.event
async def on_channel_delete(channel):
    print(channel, "had just been deleted")


@bot.event
async def on_channel_update(before, after):
    print(before, "had been updated into", after)


bot.run(TOKEN)
