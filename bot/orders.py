from bot.logging_config import setup_logger

logger = setup_logger()


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order placed successfully: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {e}")
        raise e