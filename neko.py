import discord # Needs version 0.16.12
import random
import os

path = os.path.dirname(os.path.realpath(__file__)) + '\\images\\'
print(path)
client = discord.Client()

@client.event
async def on_ready():
    print("Server entered.")
    print(client.user)

@client.event
async def on_message(message):
    """ do not interact with our own messages """
    if message.author.id == client.user.id or message.author.bot == True:
        return

    if message.content.lower().startswith("!neko"):
        cat = str(random.randint(1,101))+'.png'
        await client.send_file(message.channel, path+cat)

token = '' # Put yours here!
client.run(token)