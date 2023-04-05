from decouple import config
import logging


def Logger(name: str):
  level = logging.DEBUG  if config('DEBUG') == 'True' else logging.INFO
  logging.basicConfig(level=level)
  logger = logging.getLogger(name)
  return logger
