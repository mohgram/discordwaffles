import discord
import asyncio
import random
import time
import dbl
import logging
from discord import Client
from discord.ext import commands

bot = commands.Bot(command_prefix='sb')
bot.remove_command('help')
@bot.event
async def on_ready():
    print('bot is up')
    activity = discord.Activity(name='pokemon|sbhelp for help!', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Help", description="Help has been delivered!", color=0x00ff00)
        embed.add_field(name="sbhelp", value="This menu is brought up", inline=False)
        embed.add_field(name="sbcalmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="sbhug", value="Sobble hugs you!", inline=False)
        embed.add_field(name="sbslap", value="Sobble slaps you!", inline=False)
        embed.add_field(name="sbdab", value="?????", inline=False)
        embed.add_field(name="sbwisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="sbeightball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name='sbdice [number]', value="A guessing game where you guess the dice number!", inline=False)
        embed.add_field(name='sborder [order info] [waffle]', value="Use this command to order waffles! Remember:Workers are real people too.", inline=False)
        embed.add_field(name='sbfacts', value="Tells you the facts in a debate!", inline=False)
        embed.add_field(name='sbcoinflip', value="It flips a coin.", inline=False)
        embed.add_field(name="sbjoke", value="Tells you a funny joke.", inline=False)
        embed.add_field(name="sbwater", value="I give you some water.", inline=False)
        embed.add_field(name="sbhighfive", value="High five!", inline=False)
        embed.add_field(name="sbvanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="sbdance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="sbmeme", value="Gives you a meme", inline=False)
        embed.add_field(name="sbdrift", value="kansei dorifto!", inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def calmingmusic(ctx):
    await ctx.send("***https://www.youtube.com/watch?v=j5a0jTc9S10***")
@bot.command()
async def hug(ctx):
    await ctx.send("https://tenor.com/view/hug-anime-gif-11074788")
@bot.command()
async def slap(ctx):
    await ctx.send("https://tenor.com/view/slap-bears-gif-10422113")
@bot.command()
async def wisdom(ctx):
    wisdom = ["You can't get banned from a server if you follow the rules.","A sort of life is better than no life.","Some servers aren't worth going to.","Don't obsess over everything."]
    wisdomc = random.choice(wisdom)
    await ctx.send(wisdomc)
@bot.command()
async def eightball(ctx): 
        messag = ["Yes.", "It is certain", "Probably", "50/50", "There is a low probability.", "No."]
        message = random.choice(messag)
        await ctx.send(message)

@bot.command()
async def dice(ctx):
        botdice =["sbdice 1","sbdice 2","sbdice 3","sbdice 4","sbdice 5","sbdice 6"]
        botdi = random.choice(botdice)
        if message.content == botdi:
            await ctx.send("You were right! :partying_face: ")
        else:
            await ctx.send("you were wrong. :pensive:")
@bot.command()
async def joke(ctx):
        await ctx.send("Why did the chicken cross the road? It was getting to the idiot's house.")
        time.sleep(5)
        await ctx.send("Knock knock.")
        time.sleep(3)
        await ctx.send("It's the chicken.")
@bot.command()
async def facts(ctx):
    await ctx.send("https://imgur.com/a/H63R8hG")
@bot.command()
async def water(ctx):
    await ctx.send("https://tenor.com/view/sobble-water-pokemon-sword-and-shield-spit-pokemon-gif-13655946")
@bot.command()
async def highfive(ctx):
   await ctx.send("https://tenor.com/view/pokemon-sobble-high-five-hi-five-cute-gif-15450470")
@bot.command
async def coinflip():
        coin = ["Heads", "Tails"]
        coinf = random.choice(coin)
        await ctx.send(coinf)
@bot.command()
async def vanish(ctx):
    await ctx.send("https://tenor.com/view/sobble-whatever-bye-pokemon-pokemon-sword-and-shield-sword-and-shield-gif-13656059")
@bot.command()
async def dance(ctx):
    await ctx.send("https://tenor.com/view/thanos-dancing-fortnite-orange-gif-11793362")
@bot.command
async def dab(ctx):
    await ctx.send("You asked.")
    time.sleep(1)
    await ctx.send("https://cdn.discordapp.com/attachments/385837258768515083/645685851698888704/165ouZ0gVczfHuvwCma1S96R7I0wAAAABJRU5ErkJggg.png")
@bot.command
async def dab(ctx):
        meme = ["https://cdn.discordapp.com/attachments/645695800352964618/646018286504509440/ae6f07ce-085e-11ea-8da7-95ed4a38ab68.png","https://cdn.discordapp.com/attachments/645695800352964618/646018152743829514/EU-internet-meme_trans_NvBQzQNjv4BqpJliwavx4coWFCaEkEsb3pVDAZXwknrCGX2X3jMDFdw.png","https://cdn.discordapp.com/attachments/645695800352964618/646018080878624788/label-face-crowd-text-homedecor-person-human.png","https://cdn.discordapp.com/attachments/645695800352964618/646017964226904094/e0uhelxpmkm31.png"]
        memes = random.choice(meme)
        await ctx.send(memes)
@bot.command()
async def drift(ctx):
        await ctx.send("...k..kansei dorifto!?!?")
        await ctx.send("https://gfycat.com/zigzagbasicblackpanther")
#Moderation
@bot.command() 
async def kick(ctx, member : discord.Member, * , reason=None): 
 await member.kick(reason=reason)
 await ctx.send("GAME! That user's been kicked.")
@bot.command() 
async def mute(ctx, member : discord.Member, * , reason=None): 
 await member.mute(reason=reason)
 await ctx.send("zip! That user's been muted.")
@bot.command() 
async def unban(ctx, member : discord.Member, * , reason=None): 
 await member.unban(reason=reason)
 await ctx.send("*door opens* That user has been unbanned,")
@bot.command() 
async def ban(ctx, member : discord.Member, * , reason=None): 
 await member.mute(reason=reason)
 await ctx.send("That user's been hit with a ban hammer..")
@bot.command() 
async def unmute(ctx, member : discord.Member, * , reason=None): 
 await member.unmute(reason=reason)
 await ctx.send("unzip! That user's been unmuted")

#dbl
class DiscordBotsOrgAPI(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = 'dbl_token' # set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.updating = self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        while not self.bot.is_closed():
            logger.info('Attempting to post server count')
            try:
                await self.dblpy.post_guild_count()
                logger.info('Posted server count ({})'.format(self.dblpy.guild_count()))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
bot.run('NjQ1MDA5Njc4MjI0NDU3NzQw.XdRAoQ.m2WxInCAssliDtGXt9akAp8766A')

