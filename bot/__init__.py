import time
from iqoptionapi.stable_api import IQ_Option
from decouple import config
from utils import Logger
import locale

logger = Logger(__name__)

locale.setlocale(locale.LC_ALL, "pt_BR")


class Bot:
    def __init__(self):
        logger.debug("instantiating bot")
        self.__init__ = self
        self.client: IQ_Option = IQ_Option(config("USER"), config("PASSWORD"))
        self.connect()
        self.ACTIVE = "EURUSD"
        self.orders = []

    def connect(self):
        status, reason = self.client.connect()
        if reason == "2FA":
            logger.info("2FA enable, an sms was sent with auth code to your number!")
            code_sms = input("Enter 2FA code: ")
            status, reason = self.client.connect_2fa(code_sms)
            if status == False:
                logger.info("Failed to connect to API")
                logger.error(reason)
                exit(1)
        if status == False:
            logger.info("Failed to connect to API")
            logger.error(reason)
            exit(1)
        self.profile = self.client.get_profile_ansyc()
        logger.info("Connected to API")
        logger.debug(f"Logged as {self.client.email}")
        logger.debug(
            f"Starting with balance {locale.currency(self.client.get_balance(),grouping=True)}"
        )
