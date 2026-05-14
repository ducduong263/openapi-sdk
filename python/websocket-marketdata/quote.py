"""
Demonstrates:
- Subscribing to quote (BBO) updates

This example shows how to receive real-time quote data for multiple symbols.
"""

import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv
from trading_websocket import TradingClient
from trading_websocket.models import Quote

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".env"))

async def main():
    encoding = "msgpack"
    client = TradingClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        base_url="wss://ws-openapi.dnse.com.vn",
        encoding=encoding,
    )

    def handle_quote(quote: Quote):
        received_at = datetime.fromtimestamp(quote.receivedAt).strftime("%H:%M:%S.%f")[:-3] if quote.receivedAt else "N/A"
        print(f"[{received_at}] QUOTE: {quote}")

    print("Connecting to WebSocket gateway...")
    await client.connect()
    print(f"Connected! Session ID: {client._session_id}\n")

    symbols = ["FPT", "VIC", "SSI", "HPG", "MWG"]
    print(f"Subscribing to quotes for {symbols}...")
    await client.subscribe_quotes(symbols, on_quote=handle_quote, encoding=encoding, board_id="")

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
