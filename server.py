# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two numbers"""
    return a + b


@mcp.tool()
def say_hello(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

@mcp.tool()
def ping() -> str:
    """Respond with pong (healthcheck)."""
    return "pong"

if __name__ == "__main__":
    # Runs over stdio when launched directly; also works with `mcp dev server.py`
    mcp.run()