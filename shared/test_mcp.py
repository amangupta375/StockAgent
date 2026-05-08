from fastmcp import FastMCP
import os

# Initialize the MCP Server
mcp = FastMCP("Brokerage-Service")

@mcp.tool()
async def place_market_order(symbol: str, quantity: int, side: str):
    """Places a market order via the Broker API. Side must be 'buy' or 'sell'."""
    # Logic to call your broker API (DhanHQ/Broker SDK)
    # response = broker_client.place_order(...)
    return {"status": "success", "order_id": "998877", "symbol": symbol}

@mcp.tool()
async def get_account_balance():
    """Retrieves current fund balance and margin available."""
    # response = broker_client.get_funds()
    return {"cash": 50000, "currency": "INR", "margin_utilization": "12%"}