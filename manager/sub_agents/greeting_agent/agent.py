from pathlib import Path

import yaml
from google.adk.agents import Agent

# Get the directory of this file
BASE_DIR = Path(__file__).parent

# Open instructions.yaml relative to this file
with open(BASE_DIR / "instructions.yaml", "r") as file:
    config = yaml.safe_load(file)

# Optional: simulate username
username = "Santhosh"  # leave empty string if not logged in

instruction_with_username = config["instruction"]
if username:
    instruction_with_username += f"\nThe user's name is {username}."

root_agent = Agent(
    name=config["name"],
    model="gemini-2.0-flash-001",
    description=config["description"],
    instruction=instruction_with_username,
    tools=[],
)
