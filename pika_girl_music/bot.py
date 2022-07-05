from nextcord.ext import commands
from dotenv import dotenv_values


class Bot(commands.bot):
    def __init__(self):
        self.config = dotenv_values(".env")
        super().__init__(command_prefix=",")

    def run(self):
        super().run(self.config.pop("TOKEN"))