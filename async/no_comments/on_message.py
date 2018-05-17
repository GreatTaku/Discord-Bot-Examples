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
        await client.send_message(channel, "Hi!")

    if content.strip() == "die":
        await client.send_message(channel, "Bye... :(")
        client.close()


client.run(TOKEN)
