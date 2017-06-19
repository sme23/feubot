import discord
from discord.ext import commands
import asyncio
import re
import random
import urllib
import urllib.request
import urllib.error
import os
import json

bot = commands.Bot(command_prefix=['>>', 'feubot '], description='this is feubot.')

def trunc_to(ln, s):
    if len(s) >= ln: return s
    else: return s[:ln-3] + "..."

def create_embed(posts, threads, term):
    feu_search_base = "http://feuniverse.us/search?q=%s"
    feu_post_base = "http://feuniverse.us/t/{}/{}"
    numresults = 3

    result = discord.Embed(
            title='Search results for "%s"' % urllib.parse.unquote(term),
            url=feu_search_base % term,
            description="Found %d results" % len(posts),
            color=0xde272c)
    for i,post in enumerate(posts[:numresults]):
        result.add_field(
                name='Post in "%s" by %s' % (threads[i]["title"], post["name"]),
                value="[%s](%s)" %
                    (trunc_to(50, post["blurb"]),
                     feu_post_base.format(post["topic_id"], post["post_number"])),
                inline=False)
    if len(posts) > numresults:
        result.set_footer(text="Truncated %d result(s)." % (len(posts)-numresults))
    return result

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Reading the doc!"))

@bot.command()
async def search(*, term):
    """search feu"""
    root = "http://feuniverse.us/search.json?q=%s"
    payload = urllib.parse.quote(term)
    with urllib.request.urlopen(root % payload) as query:
        try:
            data = json.loads(query.read().decode())
            posts = data["posts"]
            threads = data["topics"]
            await bot.say(embed=create_embed(posts, threads, payload))
        except urllib.error.URLError:
            await bot.say("Error accessing FEU server, please try again later.")

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
    flip = random.randint(0,1)
    if flip ==1:
        await bot.say("""<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> <:doot:324593825815461889> <:doot:324593825815461889>
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:""")
    else:
        await bot.upload("./DOOT.png")

token = os.environ.get('TOKEN', default=None)
if token is None:
    token = open('./token').read().replace('\n','')
bot.run(token)
