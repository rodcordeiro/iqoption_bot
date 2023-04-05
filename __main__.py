from utils import Logger
from bot import Bot
from decouple import config

logger = Logger(__name__)

if __name__ == '__main__':
  bot = Bot()
  logger.debug('Starting application')
