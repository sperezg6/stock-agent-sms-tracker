from agents import Agent
from lib.agent_tools import fetch_stock_price, send_stock_sms, get_tracker_list_tool
from resources.prompts import AGENT_STOCK_RESEARCHER_PROMPT
from agents import Agent, WebSearchTool


stock_research_agent = Agent(
  name="Stock Research Agent",
  instructions=AGENT_STOCK_RESEARCHER_PROMPT,
  tools=[
    fetch_stock_price,
    WebSearchTool(),
    send_stock_sms,
    get_tracker_list_tool
  ],
  model="gpt-4.1"
)

