from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


@bot.event
async def on_private_channel_create(channel):
    """
    This event is called when a direct message (DM) channel is created.

    This can be called for both group private channel or direct private channel.

    Args:
        channel:
            The DMChannel or GroupChannel object of the created channel.

    """
    print(channel, "had just been created")


@bot.event
async def on_private_channel_delete(channel):
    """
    This event is called when a direct message (DM) channel is deleted.

    This can be called for both group private channel or direct private channel.

    Args:
        channel:
            The DMChannel or GroupChannel object of the deleted channel.

    """
    print(channel, "had just been deleted")


@bot.event
async def on_private_channel_update(before, after):
    """
    This event is called when a group direct message (DM) channel is updated.

    Such as name change, topic change, etc.

    Group DM cannot be accessed by bot accounts.

    Args:
        before:
            The GroupChannel object of the original channel.
        after:
            The GroupChannel object of the updated channel.

    """
    print(before, "had been updated into", after)


@bot.event
async def on_private_channel_pins_update(channel, last_pin):
    """
    This event is called whenever a message is pinned or unpinned from a private channel.

    This can be called for both group private channel or direct private channel.

    Args:
        channel:
            The DMChannel or GroupChannel object of the deleted channel.

        last_pin:
            A :class:`datetime.datetime` object for when the latest message was pinned or None if there are no pins.

    """
    print(channel, "received a message pin on", last_pin)


@bot.event
async def on_guild_channel_create(channel):
    """
    This event is called whenever a guild (server) channel is created.

    This can be a voice channel, a text channel, or a category channel.

    The guild can be accessed by ``channel.guild``

    Args:
        channel:
            A TextChannel or VoiceChannel or CategoryChannel object that is created.

    """
    print(channel, "is created in", channel.guild)


@bot.event
async def on_guild_channel_delete(channel):
    """
    This event is called whenever a guild (server) channel is deleted.

    This can be a voice channel, a text channel, or a category channel.

    The guild can be accessed by ``channel.guild``

    Args:
        channel:
            A TextChannel or VoiceChannel or CategoryChannel object that is deleted.

    """
    print(channel, "is deleted from", channel.guild)


@bot.event
async def on_guild_channel_update(before, after):
    """
    This event is called whenever a guild (server) channel is updated.

    Such as name, topic, permission, etc. changes.

    This can be a voice channel, a text channel, or a category channel.

    The guild can be accessed by ``before.guild`` or ``after.guild``

    Args:
        before:
            The original TextChannel or VoiceChannel or CategoryChannel object before being updated.

        after:
            The new TextChannel or VoiceChannel or CategoryChannel object that got updated.

    """
    print(before, "was changed to", after)


@bot.event
async def on_guild_channel_pins_update(channel, last_pin):
    """
    This event is called whenever a message is pinned or unpinned from a guild (server) channel.

    This can be a voice channel, a text channel, or a category channel.

    Args:
        channel:
            A TextChannel or VoiceChannel or CategoryChannel object that had it pins updated.

        last_pin:
            A :class:`datetime.datetime` object of when the latest message
            was pinned, :const:`None` if there are no pins.

    """
    print(channel, "had its pins updated on", last_pin)


@bot.event
async def on_member_join(member):
    """
    This event is called when a member joins a guild (server).

    The Guild object can be access by ``member.guild``.

    Args:
        member:
            The Member object of the member that joined the guild.

    """
    print(member, "joined", member.guild)


@bot.event
async def on_member_remove(member):
    """
    This event is called when a member leaves a guild (server).

    The Guild object can be access by ``member.guild``.

    Args:
        member:
            The Member object of the member that left the guild.

    """
    print(member, "left", member.guild)


@bot.event
async def on_member_update(before, after):
    """
    This event is called when a member updates its profile.

    Such as when the status, game playing, avatar, nickname, roles, etc. is changed.

    The Guild object can be access by ``before.guild`` or ``after.guild``.

    Args:
        before:
            The original Member object of the member that got updated.

        after:
            The new Member object of the member that got updated.

    """
    print(before, "got changed into", after, "in", before.guild)


bot.run(TOKEN)
