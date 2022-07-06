from dotenv import dotenv_values
from embed_templator import Embed
from nextcord import Intents
from nextcord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=",", intents=Intents.all(), help_command=None)
        self.config = dotenv_values(".env")
        Embed.load(self)

    def run(self):
        super().run(self.config.pop("TOKEN"))

    async def on_message(self, message):
        print("Received message:", message)
        await self.process_commands(message)