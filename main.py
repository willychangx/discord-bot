import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(os.getenv('USERID'))
    if message.author.id == os.getenv('USERID'):
        await discord.Message.delete(message)
        await message.channel.send("I'm Frendy's mortal enemy!")
    # if message.content.startswith('$hello'):
    #     await message.channel.send(message.author)

client.run(os.getenv('TOKEN'))
