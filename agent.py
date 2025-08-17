# agent.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Launch the local server via stdio
    server = StdioServerParameters(command="python", args=["server.py"])

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            # Handshake
            await session.initialize()

            # List tools
            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            # Call add
            add_res = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print("add(2,3):", add_res.content or add_res.data)

            # Call say_hello
            hello_res = await session.call_tool("say_hello", arguments={"name": "Durga"})
            print("say_hello:", hello_res.content or hello_res.data)

            # Call ping
            ping_res = await session.call_tool("ping", arguments={})
            print("ping:", ping_res.content or ping_res.data)

if __name__ == "__main__":
    asyncio.run(main())
