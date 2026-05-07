"""
Market data subscription example.

Demonstrates:
- Subscribing to trade extra updates

This example shows how to receive real-time market data for multiple symbols.
"""

import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv
from trading_websocket import TradingClient
import trading_websocket.models

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".env"))

async def main():
    encoding = "json"
    client = TradingClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        base_url="wss://ws-openapi.dnse.com.vn",
        encoding=encoding,
    )

    def handle_trade_extra(trade: trading_websocket.models.TradeExtra):
        received_at = datetime.fromtimestamp(trade.receivedAt).strftime("%H:%M:%S.%f")[:-3] if trade.receivedAt else "N/A"
        print(f"[{received_at}] TRADE EXTRA: {trade}")

    print("Connecting to WebSocket gateway...")
    await client.connect()
    print(f"Connected! Session ID: {client._session_id}\n")

    symbols = ["FPT", "VIC", "SSI", "HPG", "MWG"]
    print(f"Subscribing to trade extra for {symbols}...")
    await client.subscribe_trade_extra(symbols, on_trade_extra=handle_trade_extra, encoding=encoding, board_id="G1")

    print("\nReceiving market data...\n")

    try:
        await asyncio.sleep(8 * 60 * 60)
    except KeyboardInterrupt:
        pass

    print("\n\nDisconnecting...")
    await client.disconnect()
    print("Disconnected!")


if __name__ == "__main__":
    asyncio.run(main())
