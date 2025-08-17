# test_client.py
import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.session import StdioServerParameters


async def main():
    # Launch local server.py via stdio
    server_params = StdioServerParameters(command="python", args=["server.py"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize handshake
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])

            # Call add
            res_add = await session.call_tool("add", {"a": 4, "b": 5})
            print("add(4, 5) =>", res_add.content or res_add.data)

            # Call say_hello
            res_hello = await session.call_tool("say_hello", {"name": "Durga"})
            print("say_hello =>", res_hello.content or res_hello.data)

            # Call ping
            res_ping = await session.call_tool("ping", {})
            print("ping =>", res_ping.content or res_ping.data)


if __name__ == "__main__":
    asyncio.run(main())
