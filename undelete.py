
from time import time

import discord
from discord.ext import commands as bot

_TIMEOUT = 60
_PERMITTED_ROLES = ['Paladins', 'Lords', 'Mage Knights']

_cache = None

class DeletedCache(object):
    __slots__ = ['channels']

    def insert(self, msg):
        reqt = time()
        key = msg.channel.id
        if key not in self.channels:
            self.channels[key] = [(msg, reqt)]
        else:
            self.channels[key].append((msg, reqt))
            self._prune(key, reqt)

    def last(self, chn, n, name=None):
        reqt = time()
        self._prune(chn.id, reqt)
        if chn.id not in self.channels: return None
        s = [msg for msg, ts in self.channels[chn.id]
                if name is None or msg.author.name == name][-n:]
        if not s: return None
        n = len(s)
        result = (("%s deleted %d message(s) within the last minute:\n"
                    % (name,n))
                if name is not None
                else ("%d deleted message(s) within the last minute:\n" % n))
        return result + '```' + '\n'.join(m.content for m in s) + '```'

    def __init__(self):
        self.channels = dict()

    def _prune(self, key, reqt):
        if key not in self.channels: return
        self.channels[key] = [
            (msg, ts) for msg, ts in self.channels[key] if reqt-ts <= _TIMEOUT
        ]
        super().__init__()

class UndeleteCog(object):
    FORMAT = '{0.author} said:\n```{0.content}```'
    __slots__ = ['bot']

    @bot.command(pass_context=True, hidden=True)
    async def undelete(self, ctx, n=1, name=None):
        msg = ctx.message
        if (type(msg.author) is discord.Member
            and not [r for r in msg.author.roles
                           if str(r) in _PERMITTED_ROLES]
        ):
            await self.bot.say('You do not have undelete permissions.')
            return
        if n < 1: return
        result = _cache.last(ctx.message.channel, n, name)
        if _cache.last(ctx.message.channel, n, name) is not None:
            await self.bot.say(result)
        else:
            await self.bot.say(
                'No messages deleted ' +
                ('by %s ' % name if name is not None else '') +
                'within the last minute')

    def __init__(self, bot):
        global _cache
        _cache = DeletedCache()
        self.bot = bot

def cache(msg):
    _cache.insert(msg)

def setup(bot):
    bot.add_cog(UndeleteCog(bot))

