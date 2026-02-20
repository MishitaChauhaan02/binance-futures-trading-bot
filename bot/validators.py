from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def validate_symbol(symbol: str) -> bool:
    """
    Check if the trading symbol exists on Binance Futures
    """
    try:
        exchange_info = client.futures_exchange_info()
        available_symbols = [s["symbol"] for s in exchange_info["symbols"]]

        if symbol.upper() in available_symbols:
            logger.info(f"Symbol {symbol} is valid.")
            return True
        else:
            logger.warning(f"Symbol {symbol} is NOT valid.")
            return False

    except Exception as e:
        logger.error(f"Error validating symbol: {e}")
        return False


def validate_quantity(quantity: float) -> bool:
    if quantity > 0:
        logger.info(f"Quantity {quantity} is valid.")
        return True
    else:
        logger.warning("Quantity must be greater than 0.")
        return False


def validate_side(side: str) -> bool:
    if side.upper() in ["BUY", "SELL"]:
        logger.info(f"Side {side} is valid.")
        return True
    else:
        logger.warning("Side must be BUY or SELL.")
        return False


def validate_order_type(order_type: str) -> bool:
    if order_type.upper() in ["MARKET", "LIMIT"]:
        logger.info(f"Order type {order_type} is valid.")
        return True
    else:
        logger.warning("Order type must be MARKET or LIMIT.")
        return False