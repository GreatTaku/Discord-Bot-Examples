# import necessary modules
from discord.ext import commands

# creates a bot instance with "$" as the command prefix
bot = commands.Bot("$")


TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


# a command in discord.py is <command-prefix><command-name>
# this creates a command that can be triggered by `$hello`, ie. "hello" is the command name
@bot.command(pass_context=True)
async def hello(ctx):  # note: discord commands must be coroutines, so define the function with `async def`
    # the ctx argument is passed as the first positional argument when pass_context=True
    # this is required if you need to access the "context" of this command's origin

    # you can access the author (type discord.Member) and channel (type discord.Channel) of the command as followed:
    message_author = ctx.message.author  # both .author and .channel can only be accessed from the message instance
    message_channel = ctx.message.channel

    # prints "<username> said hello" to the console
    print("{} said hello".format(message_author))

    # bot.send_message(...) is a coroutine, so it must be awaited
    # this sends a message "Hello, <username>!" to the message channel
    await bot.send_message(message_channel, "Hello, {}!".format(message_author.name))
    # bot.send_message takes the destination and content as the first and second positional arguments
    # more info on string formatting: https://pyformat.info


# This is how you define a discord.py event
@bot.event
async def on_ready():  # the event `on_ready` is triggered when the bot is ready to function
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))

# starts the bot with the corresponding token
bot.run(TOKEN)
