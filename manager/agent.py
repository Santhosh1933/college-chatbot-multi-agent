from pathlib import Path

import yaml
from google.adk.agents import Agent

from .sub_agents.about_agent.agent import root_agent as about_agent

# Import sub-agents
from .sub_agents.greeting_agent.agent import root_agent as greeting_agent

# Import tools
from .tools.utils_tools import get_current_time

# Get the directory of this file
BASE_DIR = Path(__file__).parent

# Open instructions.yaml relative to this file
with open(BASE_DIR / "instructions.yaml", "r") as file:
    config = yaml.safe_load(file)

# Optional: simulate username
username = "Santhosh"  # leave empty string if no username is available

# Add username context to instructions if available
instruction_with_username = config["instruction"]
if username:
    instruction_with_username += f"\nThe user's name is {username}."

root_agent = Agent(
    name=config["name"],
    model="gemini-2.0-flash-001",
    description=config["description"],
    instruction=instruction_with_username,
    sub_agents=[greeting_agent, about_agent],  # Add more sub-agents as created
    tools=[get_current_time],  # Add more tools if needed
)
