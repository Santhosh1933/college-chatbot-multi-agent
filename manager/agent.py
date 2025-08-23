from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
import yaml
from pathlib import Path


# Import sub-agents
from .sub_agents.greeting_agent.agent import root_agent as greeting_agent

# Import tools
from .tools.utils_tools import get_current_time

# Get the directory of this file
BASE_DIR = Path(__file__).parent

# Open instructions.yaml relative to this file
with open(BASE_DIR / "instructions.yaml", "r") as file:
    config = yaml.safe_load(file)

root_agent = Agent(
    name=config["name"],
    model="gemini-2.0-flash-001",
    description=config["description"],
    instruction=config["instruction"],
    sub_agents=[greeting_agent],  # Add more sub-agents as created
    tools=[get_current_time],  # Add more tools if needed
)
