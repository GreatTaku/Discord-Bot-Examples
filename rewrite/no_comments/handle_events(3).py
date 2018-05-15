from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"


@bot.event
async def on_guild_join(guild):
    print(guild, "was created/joined by the client")


@bot.event
async def on_guild_remove(guild):
    print("The bot left", guild)


@bot.event
async def on_guild_update(before, after):
    print(before, "got changed into", after)


@bot.event
async def on_guild_role_create(role):
    print(role, "was created")


@bot.event
async def on_guild_role_delete(role):
    print(role, "was deleted")


@bot.event
async def on_guild_role_update(before, after):
    print(before, "was changed to", after)


@bot.event
async def on_guild_emojis_update(guild, before, after):
    print(before, "was changed into", after, "in", guild)


@bot.event
async def on_voice_state_update(member, before, after):
    print(member, "changed their voice state from", before, "to", after)


@bot.event
async def on_member_ban(guild, user):
    print(user, "was banned from", guild)


@bot.event
async def on_member_unban(guild, user):
    print(user, "was unbanned from", guild)


@bot.event
async def on_group_join(channel, user):
    print(user, "joined", channel)


@bot.event
async def on_group_remove(channel, user):
    print(user, "left", channel)


@bot.event
async def on_relationship_add(relationship):
    print(relationship, "was initiated")


@bot.event
async def on_relationship_remove(relationship):
    print(relationship, "was terminated")


@bot.event
async def on_relationship_update(before, after):
    print(before, "was changed into", after)

bot.run(TOKEN)
