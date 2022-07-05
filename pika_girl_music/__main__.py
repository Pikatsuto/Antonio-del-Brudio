import logging
from pika_girl_music import Bot

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    bot = Bot()
    bot.run()
