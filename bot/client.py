import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        raise ValueError("API keys not found. Please set them in .env file")

    client = Client(api_key, api_secret, testnet=True)

    # Set Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    logger.info("Binance Futures Testnet client initialized")

    return client