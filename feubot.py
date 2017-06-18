import discord
from discord.ext import commands
import asyncio
import re
import random
import urllib
import urllib.request
import os
import json

bot = commands.Bot(command_prefix=['>>', 'feubot '], description='this is feubot.')

def trunc_to(ln, s):
    if len(s) <= ln: return s
    else: return s[:ln-3]+"..."

def embed_link(thread):
    feu_thread_base = "http://feuniverse.us/t/%d"
    result = discord.Embed(title=thread["title"],url=feu_thread_base % thread["id"])
    thread_data = (feu_thread_base % thread["id"]) + ".json"
    with urllib.request.urlopen(thread_data) as query:
        data = json.loads(query.read().decode())
        op = data["post_stream"]["posts"][0]
        author = op["name"]
        text = trunc_to(200, op["cooked"])
    result.add_field(name="thread by %s" % author, value=text, inline=False)
    return result

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="feubot.py"))

@bot.command()
async def search(*, term):
    """search feu"""
    root = "http://feuniverse.us/search.json?q=%s"
    payload = urllib.parse.quote(term)
    output = ""
    with urllib.request.urlopen(root % payload) as query:
        try:
            data = json.loads(query.read().decode())
            threads = data["topics"]
            response = "Found %d topics with search term '%s'" % (len(threads), term)
            displayed = map(embed_link, threads[5:])
            output = [response, *displayed]
            if len(threads) > 5:
                output.append("(Truncated %d further responses)" % (len(threads)-5))
        except URLError:
            output = ["Error accessing FEU server, please try again later."]
        except KeyError:
            output = ["Found 0 topics with search term '%s'." % term]
    await bot.say(*output)

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
async def erin():
    """ERIN INTENSIFIES"""
    await bot.upload("./erinyous.gif")

@bot.command()
async def fury():
    """2 FAST 2 FURYOUS"""
    await bot.say("Don't you mean `>>erin`?")

@bot.command()
async def doot():
    """doot doot"""
    doot = "trumpet"
    dyute = "<:doot:324593825815461889>"
    await bot.say("\n".join(" ".join(random.choices([doot, dyute], k=15)) for _ in range(5)))

bot.run(open('./token','r').read().replace('\n', ''))
