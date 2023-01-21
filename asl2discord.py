import discord
from iax import IAXClient

client = discord.Client()
iax = IAXClient('username', 'password', 'server')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel is not None:
            # User has joined a voice channel
            iax.call('channel_name')
        else:
            # User has left a voice channel
            iax.hangup()

client.run('TOKEN')
