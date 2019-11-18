import discord
import asyncio
import random
import time
from discord import Client
from discord.ext import commands
Client: Client = discord.Client()
bot = commands.Bot(command_prefix='dw')
@Client.event
async def on_ready():
    print('bot is up')
    await Client.change_presence(activity=discord.Game(name='dwhelp|Making waffles!'))

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    if message.content.startswith("dwhello"):
        await message.channel.send("Hi :wave:")
    if message.content.startswith("dwhelp"):
        embed = discord.Embed(title="Help", description="Help has been delivered!", color=0x00ff00)
        embed.add_field(name="dwhelp", value="This menu is brought up", inline=False)
        embed.add_field(name="dworder [info]waffle", value="Orders a waffle!")
        await message.channel.send(embed=embed)
    if message.content.startswith('dworder'):
        if "waffle" in message.content.lower():
          query = message.content
          stopwords = ['sborder']
          querywords = query.split()
          resultwords = [word for word in querywords if word.lower() not in stopwords]
          info= ' '.join(resultwords)      
          InviteLink = await message.channel.create_invite(max_age=0, max_uses=0, reason=None, unique=True, temporary=True)
          embed = discord.Embed(title="New Order!", description=info, colour=0x00ff00)
          embed.add_field(name="Orderer", value=message.author, inline=False)
          embed.add_field(name="Invite", value=InviteLink, inline=False)
          channel = Client.get_channel(645259977304571935)
          await channel.send(embed=embed)
          embed = discord.Embed(title="Order Sent!", description="Your order has been sent to the kitchen.", inline=False, colour=0x206694)
          embed.add_field(name="Order Information", value=info, inline=False)
          embed.add_field(name="Orderer", value=message.author, inline=False)
          await message.channel.send(embed=embed)
        else:
            await message.channel.send("There's no waffle to make!")
Client.run('NjQ1MjcwMDAxNzQxMjAxNDE5.XdLv2Q.dZDKcAUuSHfUg5G9G-ipMagqgFs')            


