from discord.ext import commands
import os
from pickle import dump, load

class Other:
    """Commands added for convienience."""
    def __init__(self, bot):
        self.bot = bot
        if os.path.exists("commands.pickle"):
            with open('data.pickle', 'rb') as f:
                try:
                    self.dynamicCommands = pickle.load(f)
                    if type(self.dynamicCommands) != dict():
                        raise Exception
                    for command in self.dynamicCommands:
                        @self.bot.command(name = command, cog_name = "Other")
                        async def local():
                            await self.bot.say(self.dynamicCommands[command])
                except Exception:
                    print("Corrupted command pickle file! Loading nothing.")
                    self.dynamicCommands = dict()
        else:
            self.dynamicCommands = dict()

    @commands.command(ignore_extra = False)
    @commands.has_permissions(administrator = True)
    async def addCommand(self, command_name, command_content):
        """Admins only. Adds a new simple response command."""
        if command_name.casefold() in map(lambda x: x.casefold(), self.bot.commands):
            await self.bot.say("Command name conflicts with existing command.")
            return

        self.dynamicCommands[command_name] = command_content
        @self.bot.command(name = command_name, cog_name = "Other")
        async def local():
            await self.bot.say(command_content)
        await self.bot.say("Added command \"%s\"." % command_name)

    @commands.command(ignore_extra = False)
    @commands.has_permissions(administrator = True)
    async def removeCommand(self, command_name):
        """Admins only. Removes a previously defined simple response command."""
        if command_name not in self.dynamicCommands:
            await self.bot.say("Custom command does not exist.")
            return
        del self.dynamicCommands[command_name]
        self.bot.removeCommand(command_name)
        await self.bot.say("Command \"%s\" successfully deleted." % command_name)

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def save(self):
        """Admins only. Saves all of the current custom commands to be loaded when FEUbot is booted."""
        try:
            with open('commands.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        except Exception:
            await self.bot.say("Error saving commands.")
            return
        await self.bot.say("Commands successfully saved.")


def setup(bot):
    bot.add_cog(Other(bot))
