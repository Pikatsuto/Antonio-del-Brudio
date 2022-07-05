from dotenv import dotenv_values
from nextcord import Intents
from nextcord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=",", intents=Intents.all())
        self.config = dotenv_values(".env")

    def run(self):
        super().run(self.config.pop("TOKEN"))
