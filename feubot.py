import discord
from discord.ext import commands
import asyncio
import re
import random
import urllib

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
    """says stuff"""
    await bot.say("http://feuniverse.us/search?q="+urllib.parse.quote(stuff_to_search_for))

bot.run(open('./token','r').read().replace('\n', ''))