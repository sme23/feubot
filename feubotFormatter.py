from discord.ext.commands import DefaultHelpCommand

class FeubotFormatter(DefaultHelpCommand):
    def filter_command_list(self):
        return sorted(super().filter_command_list(), key=lambda e: str.lower(e[0]))

