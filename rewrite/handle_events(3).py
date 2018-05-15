from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


@bot.event
async def on_guild_join(guild):
    """
    This event is called when a guild (server) is either created by the bot
     or when the bot joins a guild.

    Args:
        guild:
            The Guild object of the joined guild.

    """
    print(guild, "was created/joined by the client")


@bot.event
async def on_guild_remove(guild):
    """
    This event is called when the bot is no longer in a guild (server).

    This can be either be:

     * The bot got kicked.
     * The bot got banned.
     * The bot left the guild.
     * The guild get deleted.

    Args:
        guild:
            The Guild object that's left by the bot.

    """
    print("The bot left", guild)


@bot.event
async def on_guild_update(before, after):
    """
    This event is called the guild (server) got updated.

    This can be either be:

     * Name changes.
     * AFK channel changes.
     * AFK timeout.
     * etc.

    Args:
        before:
            The Guild object prior to the update.

        after:
            The Guild object after the update.

    """
    print(before, "got changed into", after)


@bot.event
async def on_guild_role_create(role):
    """
    This event is called when a new role is created in a guild (server).

    Args:
        role:
            The Role object of the created role.

    """
    print(role, "was created")


@bot.event
async def on_guild_role_delete(role):
    """
    This event is called when a new role is deleted in a guild (server).

    Args:
        role:
            The Role object of the deleted role.

    """
    print(role, "was deleted")


@bot.event
async def on_guild_role_update(before, after):
    """
    This event is called when a role is updated in a guild (server).

    Args:
        before:
            The Role object of the original role.

        after:
            The Role object of the updated role.

    """
    print(before, "was changed to", after)


@bot.event
async def on_guild_emojis_update(guild, before, after):
    """
    This event is called when the guild (server) adds or removes emojis.

    Args:
        guild:
            The Guild object that hosts the updated emojis.

        before:
            A list of Emoji objects before being updated.

        after:
            A list of Emoji objects after being updated.

    """
    print(before, "was changed into", after, "in", guild)


@bot.event
async def on_voice_state_update(member, before, after):
    """
    This event is called when a member changed their voice state.

    This can be:

     * A member joins a voice channel.
     * A member leaves a voice channel.
     * A member becomes muted or deafened a voice channel.

    Args:
        member:
            A Member object whose voice states changed.

        before:
            The original VoiceState object before getting changed.

        after:
            The new VoiceState object after getting changed.

    """
    print(member, "changed their voice state from", before, "to", after)


@bot.event
async def on_member_ban(guild, user):
    """
    This event is called when a member is banned from a guild (server).

    Args:
        guild:
            The Guild object of where the user got banned from.

        user:
            The User object of the one who got banned.

    """
    print(user, "was banned from", guild)


@bot.event
async def on_member_unban(guild, user):
    """
    This event is called when a member is unbanned from a guild (server).

    Args:
        guild:
            The Guild object of where the user got unbanned from.

        user:
            The User object of the one who got unbanned.

    """
    print(user, "was unbanned from", guild)


@bot.event
async def on_group_join(channel, user):
    """
    This event is called when someone joins a group direct channel (DM).

    Group DM cannot be accessed by bot accounts.

    Args:
        channel:
            The PrivateChannel object with PrivateChannel.type is ChannelType.group
            of the group DM that someone joined.

        user:
            The user who joined the group DM.

    """
    print(user, "joined", channel)


@bot.event
async def on_group_remove(channel, user):
    """
    This event is called when someone leaves a group direct channel (DM).

    Group DM cannot be accessed by bot accounts.

    Args:
        channel:
            The PrivateChannel object with PrivateChannel.type is ChannelType.group
            of the group DM that someone left.

        user:
            The user who left the group DM.

    """
    print(user, "left", channel)


@bot.event
async def on_relationship_add(relationship):
    """
    This event is called when a relationship (friend) has added with the bot.

    Relationships does not apply to bot accounts.

    Args:
        relationship:
            A Relationship Object that was added.

    """
    print(relationship, "was initiated")


@bot.event
async def on_relationship_remove(relationship):
    """
    This event is called when a relationship (friend) was removed with the bot.

    Relationships does not apply to bot accounts.

    Args:
        relationship:
            A Relationship Object that was removed.

    """
    print(relationship, "was terminated")


@bot.event
async def on_relationship_update(before, after):
    """
    This event is called when a relationship is updated.

    This can be:

     * Blocking a friend.
     * a friendship is accepted.
     * etc.

    Relationships does not apply to bot accounts.

    Args:
        before:
            The original Relationship object before the update.

        after:
            The new Relationship object after the update.

    """
    print(before, "was changed into", after)

bot.run(TOKEN)
