import streamlit as st
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_quantity,
    validate_side,
    validate_order_type,
)

st.set_page_config(page_title="Crypto Trading Bot", layout="centered")

st.title("Binance Futures Testnet Trading Bot")

# Input Fields
symbol = st.text_input("Symbol (e.g., BTCUSDT)")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0, step=0.001)
price = None

if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=0.0, step=0.1)

# Place Order Button
if st.button("Place Order"):

    if not validate_symbol(symbol):
        st.error("Invalid Symbol")
    elif not validate_quantity(quantity):
        st.error("Invalid Quantity")
    elif not validate_side(side):
        st.error("Invalid Side")
    elif not validate_order_type(order_type):
        st.error("Invalid Order Type")
    else:
        try:
            client = get_client()
            response = place_order(
                client=client,
                symbol=symbol.upper(),
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price,
            )

            st.success("Order Placed Successfully 🎉")
            st.write("Order ID:", response.get("orderId"))
            st.write("Status:", response.get("status"))

        except Exception as e:
            st.error(f"Order Failed: {e}")