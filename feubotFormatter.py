from discord.ext.commands import HelpFormatter

class FeubotFormatter(HelpFormatter):
    def _add_subcommands_to_page(self, max_width, commands):
        sortedCommands = sorted(commands, key = lambda c: c.name);
        for name, command in commands:
            if name in command.aliases:
                # skip aliases
                continue

            entry = '  {0:<{width}} {1}'.format(name, command.short_doc, width=max_width)
            shortened = self.shorten(entry)
            self._paginator.add_line(shortened)
