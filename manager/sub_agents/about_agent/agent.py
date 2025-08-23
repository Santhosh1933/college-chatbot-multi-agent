from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from google.adk.agents import Agent

# Get the directory of this file
BASE_DIR = Path(__file__).parent

# Open instructions.yaml relative to this file
with open(BASE_DIR / "instructions.yaml", "r") as file:
    config = yaml.safe_load(file)

username = "santhosh"
instruction_with_username = config["instruction"]
if username:
    instruction_with_username += f"\nThe user's name is {username}."


# -------------------------
# Tool: Extract college details from URL
# -------------------------
def extract_college_details():
    """
    Fetches and extracts all meaningful textual content from the college's About page.

    This function:
    - Reads the college URL from the YAML configuration.
    - Fetches the webpage content.
    - Removes scripts, styles, and irrelevant tags.
    - Extracts visible text from headings (h1-h6), paragraphs (p),
        list items (li), and divs.
    - Joins the extracted text into a single string to provide
        complete information about the college.

    Returns:
        str: All extracted textual content from the page, ready for the agent to use.
             If the URL is missing or fetching fails, returns an error message.
    """
    url = config.get("url")
    if not url:
        return "No URL found in configuration."

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts, styles, and noscript tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract all visible text from headings, paragraphs, list items, and divs
        text_elements = []
        for tag in soup.find_all(
            ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div"]
        ):
            text = tag.get_text(strip=True)
            if text:
                text_elements.append(text)

        return "\n".join(text_elements)

    except Exception as e:
        return f"Failed to fetch details: {e}"


# Root Agent with tool
root_agent = Agent(
    name=config["name"],
    model="gemini-2.0-flash-001",
    description=config["description"],
    instruction=instruction_with_username,
    tools=[extract_college_details],
)
