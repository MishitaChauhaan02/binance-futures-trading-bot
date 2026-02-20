# Binance Futures Testnet Trading Bot

A modular cryptocurrency trading bot built in Python that integrates with Binance Futures Testnet (USDT-M).

The bot supports placing MARKET and LIMIT orders via both CLI and a simple Streamlit Web UI.

---

## Features

- Binance Futures Testnet integration
- Secure API key management using `.env`
- MARKET & LIMIT order support
- Input validation (symbol, quantity, side, order type)
- Logging system
- CLI + Web UI interface

---

## Project Structure

trading_bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
├── cli.py
├── ui.py
├── requirements.txt
└── README.md
