from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"


@bot.event
async def on_member_join(member):
    print(member, "joined", member.server)


@bot.event
async def on_member_remove(member):
    print(member, "left", member.server)


@bot.event
async def on_member_update(before, after):
    print(before, "got changed into", after, "in", before.server)


@bot.event
async def on_server_join(server):
    print(server, "was created/joined by the bot")


@bot.event
async def on_server_remove(server):
    print("The bot left", server)


@bot.event
async def on_server_update(before, after):
    print(before, "got changed into", after)


@bot.event
async def on_server_role_create(role):
    print(role, "was created in", role.server)


@bot.event
async def on_server_role_delete(role):
    print(role, "was deleted in", role.server)


@bot.event
async def on_server_role_update(before, after):
    print(before, "was changed to", after, "in", before.server)


@bot.event
async def on_server_emojis_update(server, before, after):
    print(before, "was changed into", after, "in", server)


@bot.event
async def on_voice_state_update(before, after):
    print(before, "changed their voice state into", after)


@bot.event
async def on_member_ban(server, user):
    print(user, "was banned from", server)


@bot.event
async def on_member_unban(server, user):
    print(user, "was unbanned from", server)


async def on_group_join(channel, user):
    print(user, "joined", channel)


@bot.event
async def on_group_remove(channel, user):
    print(user, "left", channel)


bot.run(TOKEN)
