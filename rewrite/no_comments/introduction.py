from discord.ext import commands

bot = commands.Bot("$")
TOKEN = "TOKEN"


@bot.command()
async def hello(ctx):  # registered command: `$hello`

    message_author = ctx.author
    message_channel = ctx.channel

    print("{} said hello".format(message_author))
    await message_channel.send("Hello, {}!".format(message_author.name))


@bot.event
async def on_ready():
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))

bot.run(TOKEN)
