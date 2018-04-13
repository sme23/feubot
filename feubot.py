import discord
from discord.ext import commands
import asyncio
import re
import random
import os
from sys import argv

import helpful, memes, reactions, undelete, other
from feubotFormatter import FeubotFormatter

if __name__ == "__main__":
    if "--debug" in argv:
        bot = commands.Bot(command_prefix=['##', 'feubeta '], description='this is feubot beta.', formatter = FeubotFormatter())
    else:
        bot = commands.Bot(command_prefix=['!', '>>', 'feubot '], description='this is feubot.', formatter = FeubotFormatter())

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        await bot.change_presence(game=discord.Game(name="Reading the doc!"))

    @bot.event
    async def on_message_delete(msg):
        undelete.cache(msg)

    @bot.add_listener
    async def on_command_error(error, ctx):
        if type(error) == commands.CheckFailure:
            pass
        else:
            await self.bot.send_message(ctx.message.channel, error)

    @bot.command()
    async def donate():
        """you know it"""
        await bot.say("https://www.patreon.com/theFEUfund")
        await bot.say("https://donorbox.org/donate-to-circles")

    token = os.environ.get('TOKEN', default=None)
    if token is None:
        token = open('./token').read().replace('\n','')

    reactions.setup(bot)
    memes.setup(bot)
    helpful.setup(bot)
    undelete.setup(bot)
    other.setup(bot)

    bot.run(token)
