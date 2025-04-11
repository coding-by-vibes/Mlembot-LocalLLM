"""
Main entry point for the Mlembot Discord bot.
- Loads environment variables
- Launches the bot and its extension cogs
- Initializes command tree and starts async loop
"""

import os
from dotenv import load_dotenv
from bot import MlemBot

def main():
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise ValueError("DISCORD_BOT_TOKEN is missing from .env")

    bot = MlemBot()
    bot.run(token)

if __name__ == "__main__":
    main()
