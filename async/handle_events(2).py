from discord.ext import commands

bot = commands.Bot("$")

TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


@bot.event
async def on_member_join(member):
    """
    This event is called when a member joins a server.

    The Server object can be access by ``member.server``.

    Args:
        member:
            The Member object of the member that joined the server.

    """
    print(member, "joined", member.server)


@bot.event
async def on_member_remove(member):
    """
    This event is called when a member leaves a server.

    The Server object can be access by ``member.server``.

    Args:
        member:
            The Member object of the member that left the server.

    """
    print(member, "left", member.server)


@bot.event
async def on_member_update(before, after):
    """
    This event is called when a member updates its profile.

    Such as when the status, game playing, avatar, nickname, roles, etc. is changed.

    The Server object can be access by ``before.server`` or ``after.server``.

    Args:
        before:
            The original Member object of the member that got updated.

        after:
            The new Member object of the member that got updated.

    """
    print(before, "got changed into", after, "in", before.server)


@bot.event
async def on_server_join(server):
    """
    This event is called when a server is either created by the bot
     or when the bot joins a server.

    Args:
        server:
            The Server object of the joined server.

    """
    print(server, "was created/joined by the bot")


@bot.event
async def on_server_remove(server):
    """
    This event is called when the bot is no longer in a server.

    This can be either be:

     * The bot got kicked.
     * The bot got banned.
     * The bot left the server.
     * The server get deleted.

    Args:
        server:
            The Server object that's left by the bot.

    """
    print("The bot left", server)


@bot.event
async def on_server_update(before, after):
    """
    This event is called the server got updated.

    This can be either be:

     * Name changes.
     * AFK channel changes.
     * AFK timeout.
     * etc.

    Args:
        before:
            The Server object prior to the update.

        after:
            The Server object after the update.

    """
    print(before, "got changed into", after)


@bot.event
async def on_server_role_create(role):
    """
    This event is called when a new role is created in a server.

    The Server object can be retrieved by ``role.server``.

    Args:
        role:
            The Role object of the created role.

    """
    print(role, "was created in", role.server)


@bot.event
async def on_server_role_delete(role):
    """
    This event is called when a new role is deleted in a server.

    The Server object can be retrieved by ``role.server``.
    Args:
        role:
            The Role object of the deleted role.

    """
    print(role, "was deleted in", role.server)


@bot.event
async def on_server_role_update(before, after):
    """
    This event is called when a role is updated in a server.

    The Server object can be retrieved by ``before.server`` or ``after.server``.

    Args:
        before:
            The Role object of the original role.

        after:
            The Role object of the updated role.

    """
    print(before, "was changed to", after, "in", before.server)


@bot.event
async def on_server_emojis_update(server, before, after):
    """
    This event is called when the server adds or removes emojis.

    Args:
        server:
            The Server object that hosts the updated emojis.

        before:
            A list of Emoji objects before being updated.

        after:
            A list of Emoji objects after being updated.

    """
    print(before, "was changed into", after, "in", server)


@bot.event
async def on_voice_state_update(before, after):
    """
    This event is called when a member changed their voice state.

    This can be:

     * A member joins a voice channel.
     * A member leaves a voice channel.
     * A member becomes muted or deafened a voice channel.

    Args:
        before:
            The original Member object before getting changed.

        after:
            The new Member object after getting changed.

    """
    print(before, "changed their voice state into", after)


@bot.event
async def on_member_ban(server, user):
    """
    This event is called when a member is banned from a server.

    Args:
        server:
            The Server object of where the user got banned from.

        user:
            The User object of the one who got banned.

    """
    print(user, "was banned from", server)


@bot.event
async def on_member_unban(server, user):
    """
    This event is called when a member is unbanned from a server.

    Args:
        server:
            The Server object of where the user got unbanned from.

        user:
            The User object of the one who got unbanned.

    """
    print(user, "was unbanned from", server)


async def on_group_join(channel, user):
    """
    This event is called when someone joins a group direct channel (DM).

    Group DM cannot be accessed by bot accounts.

    Args:
        channel:
            The Channel object with Channel.type is ChannelType.group
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
            The Channel object with Channel.type is ChannelType.group
            of the group DM that someone left.

        user:
            The user who left the group DM.

    """
    print(user, "left", channel)


bot.run(TOKEN)
