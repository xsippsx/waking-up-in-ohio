import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Lets go'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ohio'):
        await message.channel.send('@everyone' , file=discord.File('wake_up.jpg'))

client.run('ODIyNjk5NTgzMjc2NTgwODY0.YFWEsQ.MdAddj-236AIX68AXH0eL18y6Qo')
