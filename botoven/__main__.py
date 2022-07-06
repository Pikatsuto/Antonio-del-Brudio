import logging
from botoven import Bot
from botoven.cogs import Music, Dev, Info

#logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    bot = Bot()
    bot.add_cog(Music(bot))
    bot.add_cog(Dev(bot))
    bot.add_cog(Info(bot))
    bot.run()
