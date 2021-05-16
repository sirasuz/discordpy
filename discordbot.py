import discord
import Uma_rise2
client = discord.Client()
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
   if message.author == client.user:
       return
   if message.content.startswith('開始'):
       #await message.channel.send('Hello!')
       await message.channel.send('リセマラ開始します。')
       Uma_rise2.test()
       await message.channel.send('リセマラ完了。続行しますか？')
client.run('ODQzNDkwODQ5OTQ1ODEzMDEy.YKEoEQ.ozvUuuJbg43AmYoxsjM2F-cfTRc')
