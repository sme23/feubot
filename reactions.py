import discord
from discord.ext import commands as bot
import os, random, re, asyncio

class Reactions:
    """memes but not"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def ews(self):
        """disgusting list"""
        filenameslist = [os.path.splitext(f)[0] for f in os.listdir("./disgusting")]
        await self.bot.say("```"+"\n".join(map(str, filenameslist))+"```")

    @bot.command()
    async def ew(self,*args):
        """disgusting"""
        requested = args
        ewlist = {a.lower(): a for a in os.listdir("./disgusting")}
        if len(requested) != 0:
            maxews = 5
            for request in requested:
                if maxews == 0: return
                else: maxews -= 1
                file_extension_or_not_pattern = re.compile('(\.[a-z]+)?$', re.I | re.M)
                found = False
                for extension in ['.png', '.jpg', '.gif', '.jpeg']:
                    request_file = file_extension_or_not_pattern.sub(extension, request).lower()
                    if request_file in ewlist:
                        found = True
                        await self.bot.upload("./disgusting/"+ewlist[request_file])
                if not found:
                    await self.bot.say("Use >>ews to see a list of accepted names.")
        else:
            await self.bot.upload("./disgusting/"+random.choice([a for a in ewlist.values()]))

    @bot.command(aliases=["incredible"])
    async def fuckingincredible(self):
        """fuckingincredible.png"""
        await self.bot.say("http://i.imgur.com/yt4hXhJ.png")

    @bot.command()
    async def crackers(self):
        """jumping boat monkeys!"""
        await self.bot.upload("./Holy_crackers.png")

    @bot.command()
    async def hector(self):
        """judges you"""
        await self.bot.upload("./hectorpc.png")

    @bot.command()
    async def eliwood(self):
        """:("""
        await self.bot.upload("./eliwoodpc.jpg")

    @bot.command()
    async def lyn(self):
        """>:("""
        await self.bot.upload("./lynpc.png")

    @bot.command()
    async def spritans(self):
        """REEE"""
        await self.bot.say("muh")
        await asyncio.sleep(1)
        await self.bot.say("SPRITANS")
        await asyncio.sleep(2)
        await self.bot.say("***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***")

    @bot.command()
    async def reee(self):
        """REEEEEEEEEEEEEEEEEEE"""
        msg = await self.bot.say("*REEE*")
        await asyncio.sleep(0.5)
        for i in range(1, random.randint(5,10)):
            await asyncio.sleep(0.25)
            await self.bot.edit_message(msg, "**REEE" + "E"*i + "**")
        await asyncio.sleep(0.25)
        await self.bot.edit_message(msg, "***REEE" + "E"*(i+1) + "***")

    @bot.command(aliases=["f", 'respects'])
    async def F(self):
        """Press F to pay respects."""
        await self.bot.upload("./respects.jpeg")

    @bot.command()
    async def enough(self):
        """you wouldn't like me when i'm angry"""
        await self.bot.upload("./enough.png")

    @bot.command()
    async def tethys(self):
        """dancer think"""
        await self.bot.upload("./tethys.png")

    @bot.command()
    async def marisa(self):
        """u srs"""
        await self.bot.upload("./marisa.png")

    @bot.command()
    async def lel(self):
        """lel"""
        img=random.choice(["./lel.png","./lel2.png"])
        await self.bot.upload(img)

    @bot.command(pass_context=True, hidden=True)
    async def approve(self, ctx):
        msg = ctx.message
        if str(ctx.message.author.id) == "171863408822452224":
            await self.bot.upload('./approved.png')
            return
        else:
            await self.bot.say(
                "You don't get to approve things!")

    @bot.command(aliases=["OK"])
    async def ok(self):
        """ok"""
        await self.bot.upload("./ok.png")

    @bot.command()
    async def uberthink(self):
        """🤔"""
        await self.bot.upload("./uberthink.gif")

def setup(bot):
    bot.add_cog(Reactions(bot))
