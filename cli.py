import argparse
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_quantity,
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logger

# initialize logger
logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    # =========================
    # VALIDATIONS
    # =========================

    if not validate_symbol(symbol):
        print("Invalid symbol")
        return

    if not validate_side(side):
        print("Invalid side (must be BUY or SELL)")
        return

    if not validate_order_type(order_type):
        print("Invalid order type (must be MARKET or LIMIT)")
        return

    if not validate_quantity(quantity):
        print("Quantity must be greater than 0")
        return

    if order_type == "LIMIT" and price is None:
        print("Price is required for LIMIT orders")
        return

    # =========================
    # PLACE ORDER
    # =========================

    print("\n Order Request Summary")
    print("---------------------------")
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Type       : {order_type}")
    print(f"Quantity   : {quantity}")
    if order_type == "LIMIT":
        print(f"Price      : {price}")
    print("---------------------------\n")

    result = place_order(symbol, side, order_type, quantity, price)

    if "error" in result:
        print("Order Failed")
        print("Error:", result["error"])
    else:
        print("Order Placed Successfully")
        print("Order ID   :", result["orderId"])
        print("Status     :", result["status"])
        print("ExecutedQty:", result["executedQty"])
        print("Avg Price  :", result["avgPrice"])


if __name__ == "__main__":
    main()