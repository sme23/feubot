import discord
from discord.ext import commands
import asyncio
import re
import random
import urllib
import os

bot = commands.Bot(command_prefix=['>>', 'feubot '], description='this is feubot.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="feubot.py"))

@bot.command()
async def search(*, stuff_to_search_for):
    """search feu"""
    searchpage = "http://feuniverse.us/search?q="+urllib.parse.quote(stuff_to_search_for)
    embed_thing=discord.Embed(title="FEUniverse Search Results", url=searchpage)
    embed_thing.add_field(name=stuff_to_search_for, value="Click me", inline=False)
    await bot.say(embed=embed_thing)
    # await bot.say(searchpage)

@bot.command()
async def donate():
    """you know it"""
    await bot.say("https://donorbox.org/donate-to-circles")

@bot.command()
async def UT2():
    """links ultimate tutorial v2"""
    await bot.say("https://stackedit.io/viewer#!provider=gist&gistId=084645b0690253600f4aa2a57b76a105&filename=feutv2")

@bot.command()
async def reply():
    """r e p l y s o o n"""
    await bot.say("reply :soon: :smile:")

@bot.command()
async def fuckingincredible():
    """fuckingincredible.png"""
    await bot.say("http://i.imgur.com/yt4hXhJ.png")

@bot.command()
async def arch():
    """do something with arch"""
    direction = random.choice([":arrow_down:", ":arrow_up:"])
    await bot.say(direction+" with <:arch_mini:230160993299202068>")

@bot.command()
async def goofs():
    """list goofs"""
    await bot.say("```"+"\n".join(map(str, os.listdir("./goofs")))+"```")

@bot.command()
async def goof(*args):
    """show goof"""
    requested = args
    gooflist = os.listdir("./goofs")
    if len(requested) != 0:
        for request in requested:
            if request in gooflist:
                await bot.upload("./goofs/"+request)
            else:    
                await bot.say("Use >>goofs to see a list of accepted goofs.")
    else:
        await bot.upload("./goofs/"+random.choice(gooflist))

@bot.command()
async def doot():
    """doot doot"""
    await bot.say("""<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> <:doot:324593825815461889> <:doot:324593825815461889>
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:""")


bot.run(open('./token','r').read().replace('\n', ''))