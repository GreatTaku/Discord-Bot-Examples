from discord.ext import commands

bot = commands.Bot("$")
TOKEN = "TOKEN"


@bot.command(pass_context=True)
async def hello(ctx):  # registered command: `$hello`

    message_author = ctx.message.author
    message_channel = ctx.message.channel

    print("{} said hello".format(message_author))
    await bot.send_message(message_channel, "Hello, {}!".format(message_author.name))


@bot.event
async def on_ready():
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))

bot.run(TOKEN)
