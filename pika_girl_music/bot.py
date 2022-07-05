from nextcord.ext import commands

class Bot(commands.bot):
    def __init__(self):
        super().__init__(command_prefix=",")