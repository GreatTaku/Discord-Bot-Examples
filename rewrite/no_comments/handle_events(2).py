from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"


@bot.event
async def on_private_channel_create(channel):
    print(channel, "had just been created")


@bot.event
async def on_private_channel_delete(channel):
    print(channel, "had just been deleted")


@bot.event
async def on_private_channel_update(before, after):
    print(before, "had been updated into", after)


@bot.event
async def on_private_channel_pins_update(channel, last_pin):
    print(channel, "received a message pin on", last_pin)


@bot.event
async def on_guild_channel_create(channel):
    print(channel, "is created in", channel.guild)


@bot.event
async def on_guild_channel_delete(channel):
    print(channel, "is deleted from", channel.guild)


@bot.event
async def on_guild_channel_update(before, after):
    print(before, "was changed to", after)


@bot.event
async def on_guild_channel_pins_update(channel, last_pin):
    print(channel, "had its pins updated on", last_pin)


@bot.event
async def on_member_join(member):
    print(member, "joined", member.guild)


@bot.event
async def on_member_remove(member):
    print(member, "left", member.guild)


@bot.event
async def on_member_update(before, after):
    print(before, "got changed into", after, "in", before.guild)


bot.run(TOKEN)
