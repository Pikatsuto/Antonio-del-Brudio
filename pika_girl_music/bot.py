from nextcord.ext import commands
from dotenv import dotenv_values


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=",")
        self.config = dotenv_values(".env")

    def run(self):
        super().run(self.config.pop("TOKEN"))