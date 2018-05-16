# import necessary modules
import discord

client = discord.Client()


TOKEN = "TOKEN"
#       ^^^^^^^ FILL IN THIS! This is the generated token for your bot from the Discord Developer Page


@client.event
async def on_message(message):  # this event is called when a message is sent by anyone
    # this is the string text message of the Message
    content = message.content
    # this is the sender of the Message
    user = message.author
    # this is the channel of there the message is sent
    channel = message.channel

    # if the user is the client user itself, ignore the message
    if user == client.user:
        return

    print("Received a message:", content)

    if content.strip() == "hello":  # if the message is 'hello', the bot responds with 'Hi!'
        await channel.send("Hi!")

    if content.strip() == "die":  # is the message is 'die', the client shuts off
        await channel.send("Bye... :(")
        client.close()


# starts the bot with the corresponding token
client.run(TOKEN)
