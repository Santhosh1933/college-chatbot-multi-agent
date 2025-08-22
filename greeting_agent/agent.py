from google.adk.agents import Agent
import yaml

# Simulate username variable
username = "Santhosh"  # leave empty string if not logged in

with open("instructions.yaml", "r") as file:
    config = yaml.safe_load(file)

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
