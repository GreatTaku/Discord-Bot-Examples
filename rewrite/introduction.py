# import necessary modules
from discord.ext import commands

# creates a bot instance with "$" as the command prefix
bot = commands.Bot("$")


TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


# a command in discord.py is <command-prefix><command-name>
# this creates a command that can be triggered by `$hello`, ie. "hello" is the command name
@bot.command()
async def hello(ctx):  # note: discord commands must be coroutines, so define the function with `async def`
    # the ctx argument is automatically passed as the first positional argument

    # you can access the author (type discord.Member) and channel (type discord.TextChannel) of the command as followed:
    message_author = ctx.author
    message_channel = ctx.channel

    # prints "<username> said hello" to the console
    print("{} said hello".format(message_author))

    # Member.send(...) is a coroutine, so it must be awaited
    # this sends a message "Hello, <username>!" to the message channel
    await message_channel.send("Hello, {}!".format(message_author.name))
    # more info on string formatting: https://pyformat.info


# This is how you define a discord.py event
@bot.event
async def on_ready():  # the event `on_ready` is triggered when the bot is ready to function
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))

# starts the bot with the corresponding token
bot.run(TOKEN)
