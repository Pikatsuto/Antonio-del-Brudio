import logging
from bothoveen import Bot

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    bot = Bot()
    bot.run()
