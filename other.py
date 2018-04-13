from discord.ext import commands
import os
from pickle import dump, load
import pickle
from functools import reduce

developerIDs = ['91393737950777344', '171863408822452224', '146075481534365697']
developerCheck = commands.check(lambda x: x in developerIDs)

class Other:
    """Commands added for convienience."""
    def __init__(self, bot):
        self.bot = bot
        try:
            if os.path.exists("commands.pickle"):
                with open('commands.pickle', 'rb') as f:
                    self.dynamicCommands = load(f)
                    if type(self.dynamicCommands) != dict:
                        raise Exception
            else:
                self.dynamicCommands = dict()
        except Exception as e:
            try:
                if os.path.exists("commands_backup.pickle"):
                    with open('commands_backup.pickle', 'rb') as f:
                        self.dynamicCommands = load(f)
                        if type(self.dynamicCommands) != dict:
                            raise Exception
                else:
                    print("Corrupted command pickle file! Loading nothing.\nException: %s" % e)
            except Exception as e2:
                print("Corrupted command pickle file and backup! Loading nothing.\nException: %s\n%s" % (e, e2))
            self.dynamicCommands = dict()

        for command in self.dynamicCommands:
            @self.bot.command(name = command, cog_name = "Other")
            async def local():
                await self.bot.say(self.dynamicCommands[command])

    @commands.command(ignore_extra = False)
    @developerCheck
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
    @developerCheck
    async def removeCommand(self, command_name):
        """Admins only. Removes a previously defined simple response command."""
        if command_name not in self.dynamicCommands:
            await self.bot.say("Custom command does not exist.")
            return
        del self.dynamicCommands[command_name]
        self.bot.removeCommand(command_name)
        await self.bot.say("Command \"%s\" successfully deleted." % command_name)

    @commands.command()
    @developerCheck
    async def save(self):
        """Admins only. Saves all of the current custom commands to be loaded when FEUbot is booted."""
        try:
            with open('commands.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                dump(self.dynamicCommands, f, pickle.HIGHEST_PROTOCOL)

            with open('commands_backup.pickle', 'wb') as f:
                dump(self.dynamicCommands, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            await self.bot.say("Error saving commands.\nException: %s" % e)
            return
        await self.bot.say("Commands successfully saved.")

    @commands.command(name = 'eval')
    @developerCheck
    async def botEval(self, *, arg):
        """Admins only. Evaluate a Python code segment. UNSAFE!!!"""
        fix = lambda f: (lambda x: x(x))(lambda y: f(lambda args: y(y)(args)))
        res = eval(arg, __builtins__, { "fix" : fix , "reduce" : reduce })
        await self.bot.say(str(res))


def setup(bot):
    bot.add_cog(Other(bot))
