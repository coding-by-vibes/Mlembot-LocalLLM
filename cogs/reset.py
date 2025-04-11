from discord.ext import commands
from discord import app_commands, Interaction

class Reset(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="botreset", description="Reset the conversation history")
    async def botreset(self, interaction: Interaction):
        await interaction.response.send_message("Conversation history has been reset.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Reset(bot))
