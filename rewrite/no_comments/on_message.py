import discord

client = discord.Client()

TOKEN = "TOKEN"


@client.event
async def on_message(message):
    content = message.content
    user = message.author
    channel = message.channel

    if user == client.user:
        return

    print("Received a message:", content)

    if content.strip() == "hello":
        await channel.send("Hi!")

    if content.strip() == "die":
        await channel.send("Bye... :(")
        client.close()


client.run(TOKEN)
