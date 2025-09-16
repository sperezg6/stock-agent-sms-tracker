from lib.agent import stock_research_agent
from agents import Runner
import asyncio


async def main():
    result = await Runner.run(stock_research_agent, "Research the stocks in the tracker list and send an SMS with your findings")
    print(result.final_output)


def handler(event, context):
    asyncio.run(main())