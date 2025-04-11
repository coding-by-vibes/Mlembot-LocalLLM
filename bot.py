"""
MlemBot class definition.
- Subclasses discord.ext.commands.Bot
- Automatically loads all cogs in the cogs/ directory
- Syncs slash commands on bot ready
"""

import os
import discord
from discord.ext import commands

class MlemBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.guilds = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                cog_name = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(cog_name)
                except Exception as e:
                    print(f"[ERROR] Failed to load {cog_name}: {e}")