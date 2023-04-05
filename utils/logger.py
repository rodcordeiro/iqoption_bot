from decouple import config
import logging


def Logger(name: str):
  debug_level = "config('DEBUG')"
  print(debug_level)
  level = logging.DEBUG  # if config('DEBUG') else logging.INFO
  logging.basicConfig(level=level)
  logger = logging.getLogger(name)
  return logger
