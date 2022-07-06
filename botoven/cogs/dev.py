import re

from nextcord.ext import commands
from nextcord.ext.commands import Context
from ..utils.embed import Embed

OWNER_IDS = (261886769077813249, 812699388815605791)


class Dev(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx: Context, *, message):
        """Evaluates a Python expression"""
        if ctx.author.id not in OWNER_IDS:
            return

        code = re.match(r"```py\n(.*)\n```", message, flags=re.S)[1]

        try:
            await ctx.send(f"```\n{eval(code)}\n```")
        except Exception as e:
            await ctx.send(f"```\n{e}\n```")
